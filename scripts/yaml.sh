#!/bin/dash

cd $(dirname $0)/..

md_strip_yaml() { # stdin -> stdout
	perl -0777 -pe 's/^---\n.*?\n---\n+//s'
}

md_get_metadata() { # $1: file, $2: param
	yaml="$(<$1 sed -n '/^---/{:loop n; /^---/q; p; b loop}')"
	echo "$yaml" | yq -rc "$2"
}

cd - >/dev/null
