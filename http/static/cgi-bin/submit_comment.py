#!/usr/bin/python3

import traceback

from sys import stdin, path
from urllib.parse import unquote as url_unquote
from datetime import datetime
from os import makedirs, environ
from os.path import isdir
from email_validator import validate_email, EmailNotValidError

path.append("/home/tc565/python-lib")

import blog_gen_comments
import blog_send_mail

http_blog_upper_dir = "/public/home/tc565/public_html/ellie.clifford.lol/blog"
blog_comments_upper_dir = "/home/tc565/blog_comments"
logfile = "/home/tc565/logs/blog_comment_POST"

now = datetime.now()


def tryfloat(s, default=0):
	try:
		return float(s)
	except ValueError:
		return default


def get_inner_html():  # side effects!
	def error(text):
		return f'<div style="color: #ff5555;">{text}</div>'

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

	blog_dir = f"{http_blog_upper_dir}/{post_data['post']}"

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

print(r"""
<html lang="en">
  <head>
    <title>Email subscription</title>
    <link rel="icon" type="image/jpeg" href="/avatar_48.jpg"/>
    <meta charSet="utf-8"/>
    <meta content="width=device-width, initial-scale=1" name="viewport"/>
    <link rel="stylesheet" type="text/css" href="/main.css?v4"/>
  </head>
  <body>
    <div class="purple">
      <div class="topbar">
        <nav>
          <a class="topbar-title" href="/">
            <img src="/avatar_transparent_256.png"/>
          </a>
          <a class="topbar-toggle" href="https://eleanor.clifford.lol">
            <img src="/toggle.svg"/>
            <p>Toggle silliness</p>
          </a>
          <ul>
            <li>
              <a href="/about/" class="topbar-button left">About</a>
            </li>
            <li>
              <a href="/music/" class="topbar-button middle">Music</a>
            </li>
            <li>
              <a href="/blog/" class="topbar-button right">Blog</a>
            </li>
          </ul>
        </nav>
      </div>
      <div class="single">
        <div class="wrap"><div class="page">
""")

print(inner[1])

print(r"""
        </div></div>
      </div>
      <div class="footer">
        <table class="noborder" style="border: 0px solid; width: 100%"><tr>
          <td><a href="https://www.srcf.net" class="nounderline">
            <img style="min-height: 48pt; padding-right:10pt"
                 src="/srcf.svg" alt="The logo of the SRCF"></img>
          </a></td>
          <td style="text-align: center"><i>
            This site is hosted by the Student Run Computing Facility, and
            uses a Dracula theme
          </i></td>
          <td><a href="https://draculatheme.com" class="nounderline">
            <img style="min-height: 48pt; padding-left:10pt"
                 src="/dracula.svg" alt="The logo of the Dracula theme">
            </img>
          </a></td>
        </tr></table>
      </div>
    </div>
  </body>
</html>
""")
