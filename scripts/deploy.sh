#!/bin/dash

cd $(dirname $0)/..

if [ $# -eq 0 ] || [ "$1" = "--all" ] || [ "$1" = "--bliz" ]; then
	rsync -a --delete out/bliz/ pip:bliz/serve
	rsync -a --delete --exclude=hits.db bliz_config/ pip:bliz/personal
fi

if [ $# -eq 0 ] || [ "$1" = "--all" ] || [ "$1" = "--http" ]; then
	rsync -a --delete out/http/ ecc73@pip:/public/home/ecc73/public_html/ellie.clifford.lol/ --exclude blog/staging
fi

if [ "$1" = "--test" ]; then
	rsync -a --delete out/http/ ecc73@pip:/public/home/ecc73/public_html/testing/ --exclude music --exclude '.htaccess'
	rsync http/.htaccess.testing ecc73@pip:/public/home/ecc73/public_html/testing/.htaccess
else
	rsync -a --delete python-lib/ ecc73@pip:python-lib/
	ssh ecc73@pip python3 python-lib/blog_gen_comments.py
fi


cd - >/dev/null
