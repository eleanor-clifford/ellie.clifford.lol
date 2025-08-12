---
title: "Quickies #1: keyboards, least privilege, and linguistic warfare"
excerpt: "My \"I should write a blog post about this\" list is getting far too long..."
createdAt: "2024-05-30"
tags:
  - quickies
  - projects
  - tech
  - phil-pol
---

Ok so my "I should write a blog post about this" list is getting far too long
and I keep ADHDing on actually writing the damn things. I figure I should start
a (hopefully regular) series where I write just a little about a few things
that could have been a longer post. That way I get some closure and you get
some content. Here we go!

## 1\. I built a keyboard

Back in 2020/2021 my COVID and/or distraction-from-recent-breakup project was
to [design and build a custom keyboard](https://git.sr.ht/~ecc/ErgoDash-R)
(well, really just modify an existing design, but anyway).

I ended up with this:

![The ErgoDash-R](./ErgoDash-R.jpg)

It was fun! I made my fair share of mistakes (those thumb wheels are _not_ very
stably mounted), and my next design --- which I think I have a super cool idea
for --- will be much better, if I ever get around to it...

(Yes, this is now a very old thing to post, but it's been on my list all this
time!!)

## 2\. The principle of least privilege

In computer security there is this thing called the "principle of least
privilege". [Wikipedia defines it as](https://en.wikipedia.org/wiki/Principle_of_least_privilege):

> every module must be able to access only the information and resources that
> are necessary for its legitimate purpose.

It's super cool, and can lead to much more secure designs, but we shouldn't
just apply this to computer security, we should apply it to everything! Want to
get on the bus? The driver should receive a few coins, and no other
information. Want to get into a building with restricted access? The door lock
should authenticate _that you have access to the building_, but not be capable
of identifying you. Want to access a publicly available website? It should
receive no information at all except where to send data packets to.

Older technologies (cash, physical keys, physical bulletin boards) often abide
by this principle somewhat by accident, just because it's expensive to add
functionality you don't need. That's not the case with computers, so abiding by
the principle of least privilege has to be an explicit design goal.

## 3\. Linguistic Warfare

Language is not neutral. You may wish that it were neutral, but others will
wage war through language whether you like it or not. There are lots of obvious
examples of this. For instance, the word "queer", first weaponised into a slur,
and then dismantled and rebuilt into something better. Or perhaps, "cisgender",
hated by transphobes for keeping trans people on a level playing field.

But there are much more subtle acts of linguistic warfare, too. I am fascinated
by what seems to be an increasing trend among large companies to choose names
using common words --- TikTok "Sounds", YouTube "Shorts", Facebook "Messenger",
Nintendo "Switch", "Meta", the list goes on.[^1]

[^1]: The bulk of these examples are products of companies, rather than company
names, but that's mostly a consequence of the companies not already being large
when named. "Meta" proves the pattern.

I'm not really sure how new this is, but my hypothesis is that at some point
there was a paradigm shift in corporate naming theory --- from "use
invented/uncommon words or word pairings to maintain trademark rights"
("YouTube", "iPhone", "Wii", etc) to "screw trademarks, let's co-opt an
ordinary word such that wherever that word is, a mental link to our company is
drawn."

The more common the word is, the bigger the product needs to be to successfully
co-opt it. TikTok is gunning for the top by trying to have "Oh, did you hear
that new sound?" unambiguously refer to TikTok --- and among today's teenagers
they're probably already succeeded.

So what do we do? Well, one strategy is to always add the disambiguating prefix
(if it exists) and be annoying about it when other people don't. For example,
my response to "Oh look at this text I just got on Messenger" would be "Which
messenger?" regardless of whether I know they mean Facebook Messenger.

Let's just hope Facebook doesn't get so big they can get away with renaming
themselves "The" so that they can call it "The Messenger"...
