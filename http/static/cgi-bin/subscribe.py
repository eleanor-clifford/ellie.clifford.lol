#!/usr/bin/python3

import traceback

from collections import defaultdict
from datetime import datetime
from email_validator import validate_email, EmailNotValidError
from string import Template
from subprocess import check_output, CalledProcessError
from sys import stdin
from urllib.parse import unquote as url_unquote

webroot = "/public/home/ecc73/public_html/ellie.clifford.lol"
logfile = "/home/ecc73/logs/blog_subscribe_POST"
now = datetime.now()


def error(text):
    return f'<div class="red-override">{text}</div>'


def get_inner_html():  # side effects!
	raw_data = stdin.read()

	open(logfile, "a").write(f"[{now.isoformat()}] {raw_data}\n")

	post_data = {}

	for x in raw_data.split("&"):
		s = x.split("=")
		if len(s) != 2:
			return (400, error("Invalid input (0)"))

		post_data[s[0]] = url_unquote(s[1].replace("+", " "))  # why

	open(logfile, "a").write(f"[{now.isoformat()}] {post_data}\n")

	if not sorted(post_data.keys()) == ['antispam', 'email']:
		return (400, error("Invalid input (1)"))

	if post_data['email'] == "":
		return (400, error("You have to actually type your email in the box before pressing the button! :3"))

	try:
		v = validate_email(post_data['email'], check_deliverability=False)
		post_data['email'] = v['email']
	except EmailNotValidError:
		return (400, error("Invalid email address. If you're trying to hack me I'll be mad 😠"))

	if post_data["antispam"] != "ataraxia":
		return (401, error('Possible spam detected. Did you type the antispam word wrong?'))

	try:
		email = post_data["email"].replace("'", """'"'"'""")
		out = check_output(
			f"echo {email} | /usr/bin/ssh shell.srcf.net /usr/local/bin/srcf-mailman-add ecc73-blog 2>&1",
			shell=True, text=True)

		open(logfile, "a").write(f"[{now.isoformat()}] {out}\n")

		return (200, out)
	except CalledProcessError:
		return (500, error("Failed to subscribe email. Please email me so i can fix it :3"))


try:
	inner = get_inner_html()
except Exception:
	inner = (500, error(f"An unknown internal error occured. Please email me so i can fix it :3\n<pre>{traceback.format_exc()}</pre>"))

print("Content-Type: text/html")
print(f"Status: {inner[0]}")
print()

template = Template(open(webroot + "/_templates/outer.html").read())
print(template.substitute(defaultdict(str, dict(
    CONTENT=f"""<div class="wrap"><div class="page">{inner[1]}</div></div>""",
    COLOR="purple",
    TITLE="Email subscription",
))))
