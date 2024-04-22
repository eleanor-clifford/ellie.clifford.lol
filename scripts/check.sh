#!/bin/dash

cd $(dirname $0)/..

rsync -a --delete --mkpath pip:/public/home/tc565/public_html/ellie.clifford.lol/ real_out/http/

diff -ur real_out/http out/http

cd - >/dev/null
