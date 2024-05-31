#!/usr/bin/python3

import traceback

from sys import stdin
from urllib.parse import unquote as url_unquote
from datetime import datetime
from email_validator import validate_email, EmailNotValidError

from subprocess import check_output, CalledProcessError

logfile = "/home/ecc73/logs/blog_subscribe_POST"
now = datetime.now()


def error(text):
    return f'<div style="color: #ff5555;">{text}</div>'


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
