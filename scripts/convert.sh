#!/bin/dash

cd $(dirname $0)/..

. ./scripts/yaml.sh

convert_md_to_bliz() { # $1: title, $2: date, stdin -> stdout
	echo "\
% gem_header 20 'text/gemini'
% # vi: ft=gemtext

# $1

% gemlog_intro_meta_p $2
"
	# replace single line links
	# md2gemini will footnote http links regardless of whether we manually edit
	# them, so I'm replacing "http" with "fakeurl" and back on either side of
	# the md2gemini call
	sed 's|^!\?\[\([^]]*\)\](http\(s\?://[^)]*\))$|=> fakeurl\2 \1|;
	     s|^!\?\[\([^]]*\)\](\([^)]*\))$|=> \2 \1|' \
		| md2gemini -w -l at-end | tr -d '' | sed 's/^=> fakeurl/=> http/'
	# who decided to make it use CRLF...
}

convert_bliz_to_txt() { # stdin -> stdout
	# note that we are losing title and date info since this will be used for
	# email
	sed '1,/^% gemlog_intro_meta_p/d;
	     s/^=> \([^ ]*\) \(.*\)/\2: \1/'
}

convert_to_email() { # args -> stdout
	recipient="$1"
	subject="$2"
	mdfile="$3"
	txtfile="$4"
	url="$5"
	gemurl="$(echo "$5" | sed 's/^https\?/gemini/')"

	echo "\
From: Ellie's blog <blog@clifford.lol>
To: $recipient
Subject: $subject

View in a browser: $url
Or on Gemini: $gemurl
$(cat "$txtfile")

---

You are recieving this email because you opted in via ellie.clifford.lol.
To unsubscribe, email ecc73-blog-request@srcf.net with subject line
\"unsubscribe\"
"
}

convert_to_html_email() { # args -> stdout
	recipient="$1"
	subject="$2"
	mdfile="$3"
	txtfile="$4"
	url="$5"
	gemurl="$(echo "$5" | sed 's/^https\?/gemini/')"
	md_extensions="$6"

	echo "\
From: Ellie's blog <blog@clifford.lol>
To: $recipient
Subject: $subject
MIME-Version: 1.0
Content-Type: multipart/alternative; boundary=proprietarysoftwareismalware
Content-Transfer-Encoding: 8bit

--proprietarysoftwareismalware
Content-Type: text/html; charset=utf-8

<p>
  <a href=\"$url\">View in a browser</a>
</p>
<p>
  <a href=\"$gemurl\">Or on Gemini</a>
</p>

$(pandoc "$mdfile" --from markdown${md_extensions} --to html)

--proprietarysoftwareismalware
Content-Type: text/plain; charset=utf-8

View in a browser: $url
Or on Gemini: $gemurl
$(cat "$txtfile")

---

You are recieving this email because you opted in via ellie.clifford.lol.
To unsubscribe, email ecc73-blog-request@srcf.net with subject line
\"unsubscribe\"

--proprietarysoftwareismalware--
"
}

convert_blog_to_bliz_txt_eml() { # $1: filename, writes to files

	# get header yaml
	stripped_md="$(<"$1" md_strip_yaml | md_strip_venus_hidden)"

	# yaml vars
	title="$(md_get_metadata "$1" .title)"
	date="$(md_get_metadata "$1" .createdAt)"
	excerpt="$(md_get_metadata "$1" .excerpt)"
	md_extensions="$(md_get_metadata "$1" '(.md_extensions // []) | join("")')"

	# yaml-derived
	name="$(echo "$1" | perl -pe 's|.*/([^/]*)/index.md$|\1|')"
	httpurl="https://ellie.clifford.lol/blog/$name"

	# filenames
	f_bliz="bliz/blog/$name/index.bliz"
	f_txt="eml/txt/$name.txt"
	f_eml="eml/$name.eml"

	if ! test -f $f_bliz; then
		mkdir -p "$(dirname $f_bliz)"
		echo "$stripped_md" | convert_md_to_bliz "$title" "$date" >$f_bliz
		find "$(dirname "$1")" -mindepth 1 ! -name index.md \
			| xargs -I% cp -r % "$(dirname $f_bliz)"
	fi

	if ! test -f $f_txt; then
		mkdir -p "$(dirname $f_txt)"
		<$f_bliz convert_bliz_to_txt >$f_txt
	fi

	if ! test -f $f_eml; then
		mkdir -p "$(dirname $f_eml)"
		echo "$stripped_md" | convert_to_html_email \
			ecc73-blog@srcf.net \
			"Blog | $title" \
			/dev/stdin \
			$f_txt \
			$httpurl \
			"$md_extensions" \
		>$f_eml
	fi
}

cd - >/dev/null
