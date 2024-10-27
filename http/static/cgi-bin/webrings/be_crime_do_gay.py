#!/usr/bin/env python3
# vi: set noet
import requests
from urllib.parse import unquote

from os import environ

print("Content-Type: text/html")

q = environ.get("QUERY_STRING", "")

try:
	q = {x.split("=")[0]: unquote("=".join(x.split("=")[1:])) for x in q.split("&")}

	site = q.get("site") or "https://ellie.clifford.lol"
	side = q.get("side")

	if not side:
		raise TypeError

	r = requests.get("https://artemislena.eu/services/downloads/beCrimeDoGay.json", timeout=1)
	r.raise_for_status
	ring = r.json()

	position = ring.index(site)

	if side == "right":
		r = ring[(position + 1) % len(ring)]
	else:
		r = ring[(position - 1) % len(ring)]

	print("Status: 302 Found")
	print(f"Location: {r}")
	print()
except TypeError:
	print("Status: 400 Bad Request")
	print()
	print("Query parameters 'side' and 'site' must be given")
except ValueError:
	print("Status: 400 Bad Request")
	print()
	print(f"{site} is not (yet?) in the webring")
except requests.exceptions.Timeout:
	print("Status: 500 Internal Error")
	print()
	print("Webring load timed out")
except Exception:
	print("Status: 500 Internal Error")
	print()
	print("Failed to load webring")
