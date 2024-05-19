#!/usr/bin/env python3
# vi: set noet
import requests
from urllib.parse import unquote

from os import environ

print("Content-Type: text/html")

q = environ.get("QUERY_STRING", "")

try:
	q = {x.split("=")[0]: unquote("=".join(x.split("=")[1:])) for x in q.split("&")}
except Exception:
	print("Status: 400 Bad Request")
	print()
	print("Failed to load webring")

left = q.get("left", "left")
right = q.get("right", "right")
site = q.get("site", "https://ellie.clifford.lol/")

try:
	r = requests.get("https://artemislena.eu/services/downloads/beCrimeDoGay.json")
	r.raise_for_status
	ring = r.json()

	try:
		position = ring.index(site)

		next_site = ring[(position + 1) % len(ring)]
		prev_site = ring[(position - 1) % len(ring)]

		print("Status: 200 OK")
		print()
		print(f"<a href=\"{prev_site}\">{left}</a>")
		print(f"<a href=\"{next_site}\">{right}</a>")
	except ValueError:
		print("Status: 400 Site not in webring")
		print()
		print("This site is not (yet?) in the webring")
		exit(0)

except Exception:
	print("Status: 500 Internal Error")
	print()
	print("Failed to load webring")
