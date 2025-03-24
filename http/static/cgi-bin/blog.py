#!/usr/bin/env python3

import json
import traceback

from itertools import cycle
from os import environ
from urllib.parse import parse_qs
from string import Template

from os.path import dirname, realpath

webroot = dirname(dirname(realpath(__file__)))

color_order = ["cyan", "purple", "pink", "yellow", "green"]  # bad

try:
	tag_data = json.loads(open(webroot + "/blog/tag_data.json").read())
	query = parse_qs(environ.get("QUERY_STRING") or "")
	tags = ",".join(query.get("tags", []))
	tags = [x.strip() for x in tags.split(",") if x != ""]

	out = ""

	if len(tags) == 1:
		color = tag_data["tags"].get(tags[0], {}).get("color")
		title = tag_data["tags"].get(tags[0], {}).get("name")
		if title:
			cls = f"{color}-override" if color else ""
			out += f'<h1 class="{cls}">{title}</h1>\n'

	if len(tags) > 0:
		out += """
<div class="blog-tag-return">
  <h2><a href="/blog">↩︎ Return to all posts</a></h2>
</div>
"""
	else:
		tag_template = Template(open(webroot + "/_templates/tag.html").read())
		out += '<div class="tags all-tags">\n'
		for tag in tag_data["order"]:
			tw = 9 * (len(tag) + 1)
			W = 15 + tw
			Wm1 = W - 1
			mid = 12 + tw / 2
			out += tag_template.substitute(dict(
				TAG=tag,
				COLOR=tag_data["tags"][tag]["color"],
				W=W,
				Wm1=Wm1,
				mid=mid,
			))
		out += '</div>\n'

	posts = {}
	if tags:
		for tag in tags:
			posts.update(tag_data["tags"].get(tag, {}).get("posts") or {})
	else:
		for ps in tag_data["tags"].values():
			posts.update(ps.get("posts") or {})

	posts = sorted(posts.items())
	p_col = reversed(list(zip(posts, cycle(color_order))))

	post_template = Template(open(webroot + "/_templates/blog-item.html").read())

	for (p_id, p), col in p_col:
		out += post_template.substitute(dict(
			REF = f"/blog/{p_id}/",
			TITLE = p["title"],
			DATE = p["date"],
			EXCERPT = p["excerpt"],
			COLOR = col,
		))

	print("Status: 200 OK")
	print("Content-Type: text/plain")
	print()
	print(out)

except Exception:
	print("Status: 500 Internal Server Error")
	print("Content-Type: text/plain")
	print()
	print(traceback.format_exc())
