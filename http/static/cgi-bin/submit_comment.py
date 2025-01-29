#!/usr/bin/python3

import traceback

from collections import defaultdict
from datetime import datetime
from email_validator import validate_email, EmailNotValidError
from os import makedirs, environ
from os.path import isdir
from string import Template
from sys import stdin, path
from urllib.parse import unquote as url_unquote

path.append("/home/ecc73/python-lib")

import blog_gen_comments
import blog_send_mail

webroot = "/public/home/ecc73/public_html/ellie.clifford.lol"
blog_comments_upper_dir = "/home/ecc73/blog_comments"
logfile = "/home/ecc73/logs/blog_comment_POST"

now = datetime.now()


def tryfloat(s, default=0):
	try:
		return float(s)
	except ValueError:
		return default


def error(text):
    return f'<div class="red-override">{text}</div>'


def get_inner_html():  # side effects!
	ip_address = environ["REMOTE_ADDR"]
	# we don't have a lock but it doesn't matter that much
	rate_limits = [
		x.split("\t")
		for x in open(f"{blog_comments_upper_dir}/rate_limit").read().split("\n")
	]
	for i, r in enumerate(rate_limits):
		if r[0] == ip_address:
			timestamps = [x for x in r[1:] if tryfloat(x) > now.timestamp() - 10 * 60]
			if len(timestamps) > 5:
				return (429, error("Sorry, you've been ratelimited. Try again later."))
			else:
				rate_limits[i] = [rate_limits[i][0]] + timestamps + [str(now.timestamp())]
			break
	else:
		rate_limits.append([ip_address, str(now.timestamp())])

	open(f"{blog_comments_upper_dir}/rate_limit", "w").write(
		"\n".join(("\t".join(x) for x in rate_limits)) + "\n"
	)

	raw_data = stdin.read()

	open(logfile, "a").write(f"[{now.isoformat()}] " + raw_data + "\n")

	post_data = {}

	for x in raw_data.split("&"):
		s = x.split("=")
		if len(s) != 2:
			return (400, error("Invalid input (0)</div>"))

		post_data[s[0]] = url_unquote(s[1].replace("+", " "))  # why

	if not sorted(post_data.keys()) == ['antispam', 'comment', 'email', 'name', 'post']:
		return (400, error("Invalid input (1)"))

	if post_data["antispam"] == open(f"{blog_comments_upper_dir}/secret_antispam").read():
		is_me = True
	else:
		is_me = False
		if post_data["antispam"] != "lethologica":
			return (401, error('Possible spam detected. Did you type the antispam word wrong?'))

	if "." in post_data['post'] or "/" in post_data['post']:
		return (403, error("Invalid input (2). Stop pentesting, you do not have consent."))

	blog_dir = f"{webroot}/blog/{post_data['post']}"

	post_comments_dir = f"{blog_comments_upper_dir}/{post_data['post']}"

	if not isdir(blog_dir):
		return (400, error("Invalid input (3)"))

	# now we should be happy {post_data['post']} is safe

	if "\n" in post_data['name'] or "\t" in post_data['name']:
		return (400, error("Invalid name (4)"))

	if post_data["name"] == "":
		post_data["name"] = "Anonymous"

	if not is_me and (
		post_data["name"].lower() == "ellie" or
		post_data["name"].lower() == "el" or
		post_data["name"].lower() == "eleanor" or
		(
			"el" in post_data["name"].lower() and
			"clifford" in post_data["name"].lower()
		)
	):
		return (401, error("Please don\'t impersonate me"))

	if post_data["comment"] == "":
		return (400, error("Comment cannot be blank"))

	if post_data['email'] != "":
		try:
			v = validate_email(post_data['email'], check_deliverability=False)
			post_data['email'] = v['email']
		except EmailNotValidError:
			return (400, error("Invalid input (5)"))

	post_comment_dir = f"{post_comments_dir}/{now.timestamp()}"

	makedirs(post_comment_dir)

	open(f"{post_comment_dir}/post", "w").write(post_data["post"])
	open(f"{post_comment_dir}/name", "w").write(post_data["name"])
	open(f"{post_comment_dir}/comment", "w").write(post_data["comment"])

	# now regenerate comments for that post

	blog_gen_comments.http_update(post_data["post"])
	blog_gen_comments.gem_update(post_data["post"])

	# and email

	blog_send_mail.send_mail(post_comment_dir)

	if post_data['email'] != "":
		open(f"{post_comments_dir}/subscribers.tsv", "a").write(
			f"{post_data['name']}\t{post_data['email']}\n"
		)

	return (200, "Successfully added your comment")


try:
	inner = get_inner_html()
except Exception:
	inner = (500, f"An internal error occured\n{traceback.format_exc()}")


print("Content-Type: text/html")
print(f"Status: {inner[0]}")
print()

template = Template(open(webroot + "/_templates/outer.html").read())
print(template.substitute(defaultdict(str, dict(
    CONTENT=f"""<div class="wrap"><div class="page">{inner[1]}</div></div>""",
    COLOR="purple",
    TITLE="Comment submission",
))))
