from sys import path, argv
path.append("/home/ecc73/python-lib")

import srcf_tweaked.mail as mail


def strip_end(s, strip):
	return s[:-len(strip)] if s.endswith(strip) else s


def send_mail(blog_comment_dir):
	blog_comments_dir = "/".join([x for x in strip_end(blog_comment_dir, "/").split("/")][:-1])

	post_data = dict()
	post_data['name'] = open(f"{blog_comment_dir}/name").read()
	post_data['comment'] = open(f"{blog_comment_dir}/comment").read()
	post_data['post'] = open(f"{blog_comment_dir}/post").read()

	try:
		subscribers = set([
			tuple(x.split("\t"))
			for x in open(f"{blog_comments_dir}/subscribers.tsv").read().split("\n")[:-1]
		])
	except FileNotFoundError:
		subscribers = set()

	subscribers.add(
		("Ellie Clifford", "blog-comments@clifford.lol")
	)

	mail_body = f"""\
{post_data['name']} wrote:

  {post_data['comment']}

--

You can reply by navigating to https://ellie.clifford.lol/blog/{post_data['post']}/
Please don't reply to this email."""

	for subscriber in subscribers:
		mail.send_mail(
			subscriber,
			f"Blog | New comment on {post_data['post']}",
			mail_body,
			sender=("Ellie's blog comment system", "blog-comments@clifford.lol")
		)


if __name__ == "__main__":
	if len(argv) < 2:
		print(f"{argv[0]}: Needs arg")
		exit(1)

	send_mail(argv[1])
