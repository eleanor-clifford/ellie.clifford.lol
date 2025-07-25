#!/bin/dash

cd $(dirname $0)/..

. ./scripts/convert.sh
. ./scripts/html.sh
. ./scripts/template.sh

html_escape() {
	# stack overflow told me this is "elegant", hahahaa
	sed 's/&/\&amp;/g; s/</\&lt;/g; s/>/\&gt;/g; s/"/\&quot;/g; s/'"'"'/\&#39;/g'
}

build_rss() {
	posts="$(find blog/ -mindepth 2 -type f -name 'index.md' | while read post
		do
			echo "$(md_get_metadata "$post" .createdAt)	$post"
		done | sort | cut -f2)"

	export DATE="$(date --rfc-email)"
	{
		envsubst <http/templates/rss-outer-start.xml
		echo "$posts" | while read -r post; do # too big to use variables
			md_extensions="$(md_get_metadata "$post" '(.md_extensions // []) | join("")')"
			export TITLE="$(md_get_metadata "$post" .title)"
			export TITLE="$(md_get_metadata "$post" .title)"
			export URL="https://ellie.clifford.lol/$(echo "$post" | sed -E 's/\.md$/.html/;s/index.html$//')"
			export DESCRIPTION="$(md_strip_yaml <$post | md_strip_venus_hidden | pandoc -f markdown${md_extensions} -t html \
				| perl -pe "$(cat << 'EOF'
BEGIN{undef $/;}

sub get_title {
	$title = $_[0];
	return $title if $title =~ s/.*?title="(.*?)".*/$1/smg;
}

sub get_link {
	$link = $_[0];
	return $link if $link =~ s/.*?src="(.*?)".*/$1/smg;
}

sub get_a {
	$iframe = $_[0];
	return '<a href="' . get_link($iframe) . '">' . get_title($iframe) . "</a>\n";
}

s/(<iframe.*?(\/>|<\/iframe>))/get_a($1)/smge;
EOF
			)" | html_escape)"
			export DATE="$(date --rfc-email --date="$(md_get_metadata "$post" .createdAt)")"
			envsubst <http/templates/rss-item.xml
		done
		envsubst <http/templates/rss-outer-end.xml
	} > out/http/blog/rss.xml
}

build_blog_alts() {
	find blog/ -mindepth 2 -type f -name index.md | while read post; do
		# xargs doesn't work for some reason
		convert_blog_to_bliz_txt_eml $post
	done
}

build_http() {
	echo "Compiling python..." >/dev/stderr
	find http/ssg secrets/http/ssg -type f -name '*.py' | while read file; do
		html_compile_python "$file"
	done

	echo "Building main pages..." >/dev/stderr
	find http/ssg secrets/http/ssg build/ssg -type f -name '*.md' | while read file; do
		html_build_md_page "$file"
	done

	echo "Building blog pages..." >/dev/stderr
	mkdir -p out/http

	blog_sort_color | while read line; do
		echo "$line" | html_build_blog_post
	done

	html_build_blog_indices

	echo "Building RSS..." >/dev/stderr
	build_rss

	echo "Building tagdata..." >/dev/stderr
	python3 scripts/build_tagdata.py

	echo "Copying static files..." >/dev/stderr

	cp -r static/* out/http/
	cp -r http/static/* out/http/
	cp -r secrets/static/* out/http/
	cp -r secrets/http/static/* out/http/

	# dotfiles too
	cp -r static/.[!.]* out/http/
	cp -r http/static/.[!.]* out/http/
	cp -r secrets/static/.[!.]* out/http/
	cp -r secrets/http/static/.[!.]* out/http/

	echo "Handling joemode..." >/dev/stderr
	./scripts/joemode.sh
}

build_bliz() {
	mkdir -p out/bliz

	cp -r bliz/* out/bliz/
	cp -r static/* out/bliz/

	ls out/bliz/blog/*/index.bliz | while read -r file; do
		cat >> "$file" << 'EOF'

%%%
cat (dirname "$blizfile")/comments.gmi
%%%

=> ./submit/ Add a comment!
EOF

		mkdir -p "$(dirname "$file")/submit"
		cp bliz_config/submit_start.bliz "$(dirname "$file")/submit/index.bliz"
	done

	cp -r bliz/.[!.]* out/bliz/
	cp -r static/.[!.]* out/bliz/
}

rm -rf blog/staging
if [ $# -eq 0 ] || [ "$1" = "--all" ]; then
	build_blog_alts
	build_http
	build_bliz
elif [ "$1" = "--blog" ]; then
	build_blog_alts
elif [ "$1" = "--bliz" ]; then
	build_bliz
elif [ "$1" = "--http" ]; then
	build_http
elif [ "$1" = "--test" ]; then
	rsync -a secrets/blog/staging/ blog/staging/
	build_http
	rm -rf blog/staging
fi
rm -rf blog/staging

cd - >/dev/null
