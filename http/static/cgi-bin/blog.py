#!/usr/bin/env python3

import json
import traceback

from itertools import cycle
from os import environ
from urllib.parse import parse_qs
from string import Template


webroot = "/public/home/ecc73/public_html/ellie.clifford.lol"
color_order = ["cyan", "purple", "pink", "yellow", "green"]

try:
    tag_data = json.loads(open(webroot + "/blog/tag_data.json").read())
    query = parse_qs(environ.get("QUERY_STRING") or "")
    tags = ",".join(query.get("tags", []))
    tags = [x.strip() for x in tags.split(",")]

    posts = {}
    if tags == [""]:
        for ps in tag_data.values():
            posts.update(ps.get("posts") or {})
    else:
        for tag in tags:
            posts.update(tag_data.get(tag, {}).get("posts") or {})

    posts = sorted(posts.items())
    p_col = reversed(list(zip(posts, cycle(color_order))))

    template = Template(open(webroot + "/_templates/blog-item.html").read())

    print("Status: 200 OK")
    print("Content-Type: text/plain")
    print()
    for (p_id, p), col in p_col:
        print(template.substitute(dict(
            REF = f"/blog/{p_id}/",
            TITLE = p["title"],
            DATE = p["date"],
            EXCERPT = p["excerpt"],
            COLOR = col,
        )))

except Exception:
    print("Status: 500 Internal Server Error")
    print("Content-Type: text/plain")
    print()
    print(traceback.format_exc())



