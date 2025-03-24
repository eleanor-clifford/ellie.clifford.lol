import json
import yaml

from os import listdir, chdir
from os.path import dirname, abspath, isdir, isfile

chdir(dirname(dirname(abspath(__file__))) + "/blog/")
posts = [x for x in reversed(sorted(listdir())) if isdir(x) and isfile(x + "/index.md")]

if isdir("staging"):
	posts += ["staging/" + x for x in reversed(sorted(listdir("staging"))) if isdir("staging/" + x) and isfile(f"staging/{x}/index.md")]

tag_data = yaml.safe_load(open("tags.yaml").read())

for p in posts:
	y = yaml.safe_load(open(p + "/index.md").read().split("---\n")[1])

	if 'tags' not in y:
		print(f"WARNING: {p} does not have tags")

	post_data = {
		"title": y.get("title"),
		"date": y.get("createdAt"),
		"excerpt": y.get("excerpt"),
	}

	for t in y.get('tags', []) + ["all"]:
		tag_data["tags"][t] = tag_data["tags"].get(t) or {}
		tag_data["tags"][t]["posts"] = (
			(tag_data["tags"][t].get("posts") or {}) | {p: post_data}
		)

open("../out/http/blog/tag_data.json", "w").write(json.dumps(tag_data))
