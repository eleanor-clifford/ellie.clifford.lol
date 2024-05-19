#!/bin/dash

cd $(dirname $0)/..

if [ $# -eq 0 ] || [ "$1" = "--all" ] || [ "$1" = "--bliz" ]; then
	rsync -a --delete out/bliz/ pip:bliz/serve
	rsync -a --delete --exclude=hits.db bliz_config/ pip:bliz/personal
fi

if [ $# -eq 0 ] || [ "$1" = "--all" ] || [ "$1" = "--http" ]; then
	rsync -a --delete out/http/ ecc73@pip:/public/home/ecc73/public_html/ellie.clifford.lol/
fi

if [ "$1" = "--test" ]; then
	rsync -a --delete out/http/index.shtml ecc73@pip:/public/home/ecc73/public_html/testing/
	rsync -a --delete out/http/blog ecc73@pip:/public/home/ecc73/public_html/testing/
	rsync -a --delete out/http/cgi-bin ecc73@pip:/public/home/ecc73/public_html/testing/
	rsync -a --delete out/http/main.css ecc73@pip:/public/home/ecc73/public_html/testing/
else
	rsync -a --delete python-lib/ ecc73@pip:python-lib/
	ssh ecc73@pip python3 python-lib/blog_gen_comments.py
fi


cd - >/dev/null
