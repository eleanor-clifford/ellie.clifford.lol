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
        continue

    for t in y['tags']:
        tag_data[t] = tag_data.get(t) or {}
        tag_data[t]["posts"] = (tag_data[t].get("posts") or {}) | {p: {
            "title": y.get("title"),
            "date": y.get("createdAt"),
            "excerpt": y.get("excerpt"),
        }}

open("../out/http/blog/tag_data.json", "w").write(json.dumps(tag_data))
