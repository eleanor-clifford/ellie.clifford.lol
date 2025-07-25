#!/bin/dash

cd $(dirname $0)/..

rsync -a --delete --mkpath pip:/public/home/ecc73/public_html/ellie.clifford.lol/ real_out/http/
rsync -a --delete --mkpath pip:python-lib/ real_out/python-lib/

diff -ur --color real_out/http out/http
diff -ur --color real_out/python-lib python-lib

cd - >/dev/null
