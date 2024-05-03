#!/usr/bin/python3

import requests
import re

rss = requests.get("https://tube.clifford.lol/feeds/videos.xml?videoChannelId=2").text

rss = re.sub("<link>.*?</link>", "<link>https://ellie.clifford.lol/music/</link>", rss, count=1, flags=re.DOTALL)
rss = re.sub("<description>.*?</description>", "<description>Ellie makes music :]</description>", rss, count=1, flags=re.DOTALL)
rss = re.sub("<image>.*?</image>", "", rss, count=1, flags=re.DOTALL)
rss = re.sub("<copyright>.*?</copyright>", "<copyright>CC BY-SA 4.0</copyright>", rss, flags=re.DOTALL)

print("Content-Type: application/xml; charset=utf-8")
print()
print(rss)
