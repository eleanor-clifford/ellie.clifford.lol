#!/bin/dash

cd $(dirname $0)/..

rsync -a --delete --mkpath pip:/public/home/ecc73/public_html/ellie.clifford.lol/ real_out/http/
rsync -a --delete --mkpath pip:python-lib/ real_out/python-lib/

diff -ur --color out/http real_out/http
diff -ur --color python-lib real_out/python-lib

cd - >/dev/null
