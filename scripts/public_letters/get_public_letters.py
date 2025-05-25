import yaml
import email.policy
import email.parser
import re
from datetime import datetime, timedelta, timezone
from string import Template

from notmuch2 import Database, Message

config = yaml.safe_load(open("scripts/public_letters/config.yaml").read())

db = Database()
email_parser = email.parser.BytesParser(policy=email.policy.default)


def filter_string(string, filters, flags=0, sub={}):
	for k, v in filters.items():
		string = re.sub(
			Template(k).safe_substitute(sub),
			Template(v).safe_substitute(sub),
			string,
			flags=flags
		)
	return string


def subject_filter(s):
	return filter_string(s, config["rules"]["subject_filters"], flags=re.I).strip()


def get_wrapped_body(message, filter_sub={}, msgid=None):
	if not isinstance(message, email.message.EmailMessage):
		msgid = msgid or message.messageid
		message = email_parser.parsebytes(message.path.open('rb').read())

	t = message.get_content_type()
	if t.startswith("multipart/"):
		return get_wrapped_body(message.get_body(), filter_sub=filter_sub, msgid=msgid)
	elif t == "text/plain":
		return Template(config["format"]["plain_body"]).substitute(
			CONTENT=filter_string(
				message.get_content(),
				config["format"]["filters"]["plain_body"] | config["format"]["filters"]["per_message"].get(msgid, {}),
				flags=re.M | re.S,
				sub=filter_sub,
			).strip(),
		)
	elif t == "text/html":
		return Template(config["format"]["html_body"]).substitute(
			CONTENT=filter_string(
				message.get_content(),
				config["format"]["filters"]["html_body"] | config["format"]["filters"]["per_message"].get(msgid, {}),
				flags=re.M | re.S,
				sub=filter_sub,
			).strip(),
		)
	else:
		print(f"??? {t}")
		exit(1)


def ignore_thread(thread):
	return False


def ignore_message(message: Message):
	return any(
		re.search(pattern, subject(message), flags=re.I)
		for pattern in config["rules"]["ignore_messages_with_patterns"]
	)


def time_close_enough(t1, t2):
	first1 = datetime.fromtimestamp(t1.first, timezone.utc)
	first2 = datetime.fromtimestamp(t2.first, timezone.utc)
	last1 = datetime.fromtimestamp(t1.last, timezone.utc)
	last2 = datetime.fromtimestamp(t2.last, timezone.utc)
	delta = timedelta(days=config["rules"]["days_assume_related"])

	return abs(first1 - last2) < delta or abs(first2 - last1) < delta


def subject(m_or_t):
	try:
		return getattr(m_or_t, "subject", None) or m_or_t.header("subject")
	except (LookupError, AttributeError):
		return ""


def subject_close_enough(t1, t2):
	s1 = subject_filter(subject(t1))
	s2 = subject_filter(subject(t2))

	return s1 == s2 and s1.lower() not in config["rules"]["dont_subject_combine"]


for person in config["people"]:
	threads = set()
	for e in person["emails"]:
		threads |= set(x for x in db.threads(f"to:{e} or from:{e}") if not ignore_thread(x))

	thread_pools = []
	for thread in sorted(threads, key = lambda t: t.first):
		for i, other_threads in enumerate(thread_pools):
			for other_thread in other_threads:
				if (
					time_close_enough(thread, other_thread) or
					subject_close_enough(thread, other_thread)
				):
					thread_pools[i].append(thread)
					break
			else:
				continue
			break
		else:
			thread_pools.append([thread])

	msgss = [
		[m for t in pool for m in t if not ignore_message(m)]
		for pool in thread_pools
	]
	msgss = [m for m in msgss if len(m) > 0]

	for i, msgs in enumerate(msgss):
		with open(f'http/md/documents/letters/{person["id"]}-{i:02d}.md', "w") as fp:
			fp.write('```{=html}\n')
			for i, m in enumerate(msgs):
				def _name(h):
					return (
						person["name"] if any([x.lower() in m.header(h).lower() for x in person["emails"]])
						else config["me"]["name"]
					)

				From = _name("from")
				To = _name("to")
				assert sum(int(x == config["me"]["name"]) for x in (From, To)) == 1

				from_me = From == config["me"]["name"]
				name_regex = config["me"]["name_regex"] if from_me else person["name_regex"]

				would_be_subject = subject_filter(subject(m))
				MaybeSubject = (
					f"\nSubject: {subject_filter(subject(m))}"
					if would_be_subject and (i == 0 or not subject_close_enough(m, msgs[0]))
					else ""
				)

				note = config["notes"].get(m.messageid)
				MaybeNote = (
					Template(config["format"]["note"]).substitute(
						CONTENT=note,
					) if note else ""
				)

				fp.write(
					Template(config["format"]["format"]).substitute(
						NOTE=MaybeNote,
						Date=m.header("date"),
						From=From,
						To=To,
						MaybeSubject=MaybeSubject,
						Body=get_wrapped_body(m, filter_sub={"name": name_regex}),
					)
				)
				if i < len(msgs) - 1:
					fp.write(config["format"]["between"])
			fp.write('```\n')
