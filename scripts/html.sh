#!/bin/dash

cd $(dirname $0)/..

. ./scripts/template.sh
. ./scripts/blog.sh

md_color_headings() { # $1: start color
	# h2 specifically
	color_cycle="$(yq -r .color_cycle <config.yaml | tr ' ' '\n' | tac)"
	start_color="$1"
	color_current="$(echo "$color_cycle" | grep -A9999 "$1")"

	while IFS= read -r line; do
		if echo "$line" | grep -Eq '^##[^#]'; then
			color_current="$(echo "$color_current" | tail -n +2)"
			if [ -z "$color_current" ]; then
				color_current="$color_cycle"
			fi
			color_single="$(echo "$color_current" | head -n1)"
			#color_code="$(yq -r .colors.$color_single <config.yaml)"
			echo "<h2 class="$color_single-override">"
			echo "$line" | sed 's|^##[[:space:]]*||'
			echo "</h2>"
		else
			echo "$line"
		fi
	done
}

check_hash_change() {
	file="$1"
	if ! test -e "$file"; then
		echo true
		return
	fi

	while read -r h; do
		if ! grep -q "$h" "$file"; then
			echo true
			return
		fi
	done
	echo false
}

html_build_md_page() { # $1: filename, writes to out/http/
	file="$1"
	escaped_name="$(
		((echo "$file" | grep -Eq 'index.md$') \
			&& dirname "$file" \
			|| echo "$file" \
		) | perl -pe 's|.*?md/?|/|;s|[/.-]|_|g;')"

	export SSI="$(md_get_metadata "$file" .ssi)"
	( test -z "$SSI" || [ "$SSI" = null ] ) && SSI=false || SSI=true

	$SSI && ext=shtml || ext=html
	out_file="$(echo "$file" | sed 's|^http/md/|out/http/|; s|.md$|.'$ext'|')"
	mkdir -p "$(dirname "$out_file")"

	hs="$(md5sum "$file" "http/templates/default.html" "http/templates/outer.html" "scripts/html.sh")"
	regen="$(echo "$hs" | check_hash_change "$out_file")"

	if $regen; then
		echo "regenerating $file..."
	else
		echo "skipping $file..."
		return
	fi

	export HASH="$hs"
	export COLOR="$(<config.yaml yq -rc ".page_colors.$escaped_name")"
	export TITLE="$(md_get_metadata "$file" '.title // ""')"

	if test -n "$TITLE"; then
		export INNERTITLE="<h1>${TITLE}</h1>"
	fi

	banner="$(md_get_metadata "$file" '.banner // ""')"

	vars="$(md_get_metadata "$file" '.vars | to_entries[] | "\(.key)\t\(.value)"' 2>/dev/null)"
	IFS="
"
	for line in $vars; do
		var="$(echo "$line" | cut -f1)"
		value="$(echo "$line" | cut -f2-)"
		export $var="$(eval "$value")"
	done

	if test -n "$banner"; then
		src="$(echo "$banner" | cut -d':' -f1)"
		alt="$(echo "$banner" | cut -d':' -f2- | sed 's/^ *//')"
		export BANNER="<div class=\"banner\"><img src=\"$src\" alt=\"$alt\"/></div>"
	fi

	md_extensions="$(md_get_metadata $file '(.md_extensions // []) | join("")')"
	test -n "$md_extensions" && echo "extensions: $md_extensions" >&2

	css="$(md_get_metadata "$file" .css)"

	if [ "$css" != "null" ]; then
		export CSS="$css"
	fi
	test -n "$CSS" && echo "css: $css" >&2

	<$file md_color_headings $COLOR | envsubst | pandoc --from markdown${md_extensions} --to html \
		| activate_double_template http/templates/default.html >$out_file
}

html_build_blog_indices() {
	export COLOR=green
	cat http/blog.shtml \
		| activate_double_template http/templates/blog-index.html > "out/http/blog/index.shtml"
}

md_strip_venus_hidden() {
	perl -0777 -pe 's/```[ \w]*hidden.*?```//gs'
}

html_build_blog_post() { # reads tsv color, date, file
	read tsv
	test -z "$tsv" && return
	file="$(echo "$tsv" | cut -f 3)"

	basename_noext="$(basename "$(dirname "$file")")"
	out_file="$(echo "$file" | sed 's|^|out/http/|; s|.md$|.shtml|')"
	mkdir -p "$(dirname "$out_file")"

	hs="$(md5sum "$file" "http/templates/blog-post.shtml" "http/templates/tag.html" "http/templates/outer.html" "scripts/html.sh")"
	regen="$(echo "$hs" | check_hash_change "$out_file")"

	if $regen; then
		echo "regenerating $file..."
	else
		echo "skipping $file..."
		return
	fi

	export TAGS="$({
		md_get_metadata $file '.tags[]?' | while read -r tag; do
			export TAG="$tag"
			export COLOR="$(<blog/tags.yaml yq -cr '.tags.["'"$tag"'"].color')"
			tw=$((9*$(echo "$tag" | wc -c)))
			export W=$((15 + $tw))
			export Wm1=$(($W-1))
			export mid="$(echo "scale=1; 12 + $tw/2" | bc -l)"
			<http/templates/tag.html envsubst
		done
	})"
	export HASH="$hs"
	export COLOR="$(echo "$tsv" | cut -f 1)"
	export DATE="$(echo "$tsv" | cut -f 2)"
	export TITLE="$(md_get_metadata $file .title)"
	export URL_PART="$basename_noext"

	cw="$(md_get_metadata $file .cw)"

	if [ "$cw" != "null" ]; then
		export CW="<div class=\"content-warning\"><p>$cw</p></div>"
	fi

	pandoc_options="$(md_get_metadata $file '.pandoc_options // ""')"
	test -n "$pandoc_options" && echo "options: $pandoc_options" >&2

	md_extensions="$(md_get_metadata $file '(.md_extensions // []) | join("")')"
	test -n "$md_extensions" && echo "extensions: $md_extensions" >&2

	css="$(md_get_metadata "$file" .css)"

	if [ "$css" != "null" ]; then
		export CSS="$css"
	fi

	if [ "$(md_get_metadata $file .nocolor)" = "true" ]; then
		colorpipe="cat"
	else
		colorpipe="md_color_headings $COLOR"
	fi

	<$file md_strip_yaml | md_strip_venus_hidden | eval "$colorpipe" \
		| pandoc --from markdown${md_extensions} --to html $pandoc_options \
		| activate_double_template http/templates/blog-post.shtml >$out_file

	find "$(dirname "$file")" -mindepth 1 ! -name index.md \
		| xargs -I% cp -r % "$(dirname $out_file)"
}

cd - >/dev/null
