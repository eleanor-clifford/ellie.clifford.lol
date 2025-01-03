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
			color_code="$(yq -r .colors.$color_single <config.yaml)"
			echo "<h2 style=\"color: $color_code\">"
			echo "$line" | sed 's|^##[[:space:]]*||'
			echo "</h2>"
		else
			echo "$line"
		fi
	done
}


html_build_md_page() { # $1: filename, writes to out/http/
	file="$1"
	escaped_name="$(
		((echo "$file" | grep -Eq 'index.md$') \
			&& dirname "$file" \
			|| echo "$file" \
		) | perl -pe 's|.*?md/?|/|;s|[/.-]|_|g;')"

	export SSI="$(md_get_metadata "$file" ssi)"
	[ "$SSI" = null ] && SSI=false

	$SSI && ext=shtml || ext=html
	out_file="$(echo "$file" | sed 's|^http/md/|out/http/|; s|.md$|.'$ext'|')"
	mkdir -p "$(dirname "$out_file")"

	h="$(md5sum "$file")"
	if test -e "$out_file" && grep -q "$h" "$out_file"; then
		echo "skipping $file..."
		return
	else
		echo "regenerating $file..."
	fi

	export HASH="$h"
	export COLOR="$(<config.yaml yq -rc ".page_colors.$escaped_name")"
	export TITLE="$(md_get_metadata "$file" title)"

	banner="$(md_get_metadata "$file" banner)"

	vars="$(md_get_metadata "$file" 'vars | to_entries[] | "\(.key)\t\(.value)"' 2>/dev/null)"
	IFS="
"
	for line in $vars; do
		var="$(echo "$line" | cut -f1)"
		value="$(echo "$line" | cut -f2-)"
		export $var="$(eval "$value")"
	done

	if [ "$banner" != "null" ]; then
		src="$(echo "$banner" | cut -d':' -f1)"
		alt="$(echo "$banner" | cut -d':' -f2- | sed 's/^ *//')"
		export BANNER="<div class=\"banner\"><img src=\"$src\" alt=\"$alt\"/></div>"
	fi

	css="$(md_get_metadata "$file" css)"

	if [ "$css" != "null" ]; then
		export CSS="$css"
	fi

	<$file md_color_headings $COLOR | envsubst | pandoc --from markdown --to html \
		| activate_double_template http/templates/default.html >$out_file
}

html_build_blog_all() {
	# put data into templates and output
	blog_sort_color | html_build_blog_from
}

html_build_blog_from() { # stdin is blog_sort_color equivalent
	while read post; do
		test -z "$post" && continue
		color="$(echo "$post" | cut -f 1)"
		date="$(echo "$post" | cut -f 2)"
		file="$(echo "$post" | cut -f 3)"
		basename_noext="$(basename "$(dirname "$file")")"

		export TITLE="$(md_get_metadata $file title)"
		export DATE="$date"
		export EXCERPT="$(md_get_metadata $file excerpt)"
		export REF="/blog/$basename_noext/"
		export COLOR="$color"
		envsubst <http/templates/blog-item.html
	done
}

html_build_blog_indices() {
	categories="$(yq -rc '.[]' <blog/categories.yaml)"
	sorted_colored_blogs="$(blog_sort_color)"

	echo "$categories" | while read -r category; do
		name="$(echo "$category" | yq -r .name)"
		shortname="$(echo "$category" | yq -r .shortname)"
		export COLOR="$(echo "$category" | yq -r .color)"

		mkdir -p out/http/blog/$shortname
		out_file="out/http/blog/$shortname/index.html"

		files="$(echo "$category" | yq -rc '.posts[]' | sed 's|^|blog/|;s|$|/index.md|')" # jank
		export HASH="$(md5sum $files)"

		if test -e "$out_file" && grep -q "$HASH" "$out_file"; then
			echo "skipping $name blog index..." > /dev/stderr
		else
			echo "regenerating $name blog index..." > /dev/stderr
			echo "$files" \
				| blog_apply_color_to \
				| html_build_blog_from \
				| activate_double_template http/templates/blog-listing.html \
					> "$out_file"
		fi
	done

	#mkdir -p out/http/blog/all

	export COLOR="$(yq -r .page_colors._blog <config.yaml)"

	files="$(find blog/ -mindepth 2 -type f -name '*.md' | sort)"
	export HASH="$(md5sum $files)"
	out_file="out/http/blog/index.html"

	if test -e "$out_file" && grep -q "$HASH" "$out_file"; then
		echo "skipping full blog index..." > /dev/stderr
	else
		echo "regenerating full blog index..." > /dev/stderr
	fi
	html_build_blog_all \
		| activate_double_template http/templates/blog-listing.html > "$out_file"
	export HASH=

	mkdir -p out/http/blog/categories
	<blog/categories.md \
		  pandoc --from markdown --to html \
		| activate_double_template http/templates/blog-index.html > out/http/blog/categories/index.html

}

md_strip_venus_hidden() {
	perl -0777 -pe 's/```[ \w]*hidden.*?```//gs'
}

html_build_blog_post() { # reads tsv color, date, file
	read tsv
	test -z "$tsv" && return
	file="$(echo "$tsv" | cut -f 3)"
	basename_noext="$(basename "$(dirname "$file")")"

	mkdir -p out/http/blog/$basename_noext
	out_file="out/http/blog/$basename_noext/index.shtml"

	h="$(md5sum "$file")"
	if test -e "$out_file" && grep -q "$h" "$out_file"; then
		echo "skipping $file..."
		return
	else
		echo "regenerating $file..."
	fi

	export HASH="$h"
	export COLOR="$(echo "$tsv" | cut -f 1)"
	export DATE="$(echo "$tsv" | cut -f 2)"
	export TITLE="$(md_get_metadata $file title)"
	export URL_PART="$basename_noext"

	cw="$(md_get_metadata $file cw)"

	if [ "$cw" != "null" ]; then
		export CW="<div class=\"content_warning\"><p>$cw</p></div>"
	fi

	pandoc_options="$(md_get_metadata $file pandoc_options)"
	[ "$pandoc_options" = null ] && pandoc_options=

	css="$(md_get_metadata "$file" css)"

	if [ "$css" != "null" ]; then
		export CSS="$css"
	fi

	mkdir -p out/http/blog/$basename_noext
	out_file="out/http/blog/$basename_noext/index.shtml"

	if [ "$(md_get_metadata $file nocolor)" = "true" ]; then
		<$file md_strip_yaml | md_strip_venus_hidden \
			| pandoc --from markdown --to html $pandoc_options \
			| activate_double_template http/templates/blog-post.shtml >$out_file
	else
		<$file md_strip_yaml | md_strip_venus_hidden | md_color_headings $COLOR \
			| pandoc --from markdown --to html $pandoc_options \
			| activate_double_template http/templates/blog-post.shtml >$out_file
	fi

	find "$(dirname "$file")" -mindepth 1 ! -name index.md \
		| xargs -I% cp -r % "$(dirname $out_file)"
}

cd - >/dev/null
