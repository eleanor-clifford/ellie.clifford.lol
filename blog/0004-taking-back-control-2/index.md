---
title: "Taking back control (part 2): futility and obscurity"
excerpt: "My manifesto currently implies I would have to consider every message I send to absolutely anyone public. Is this reasonable?"
createdAt: "2022-03-30"
tags:
  - tech
  - projects
---

::: series-links
[← Part 1](/blog/0003-taking-back-control-1/){.prev}
[Part 3 →](/blog/0007-taking-back-control-3/){.next}
:::

Currently in my manifesto it says:

> 4.2) When transferring data to a person who does not comply with this
> manifesto or a similar one, I will assume it is public and compromised.

This is a bit extreme, and at the moment basically means I would have to
consider every message I send to absolutely anyone public. Does that make the
whole thing futile? Is it even fair when messaging people through E2EE FOSS
systems?

## The problem of notification services

Let's say I send a message to someone on Matrix. Chances are, that person has
some way of accessing Matrix on their smartphone, and has notifications
enabled. Chances are, too, that the notification service on their phone is
proprietary (e.g. Google Play Services). [Here's what Drew DeVault has to say
about Google Play Services](https://drewdevault.com/2018/08/08/Signal.html):

> Here’s what Google Play Services actually is: a rootkit. Google Play Services
> lets Google do silent background updates on apps on your phone and give them
> any permission they want. Having Google Play Services on your phone means
> your phone is not secure.

The same definitely goes for whatever the Apple equivalent is.

So... any message I send to, well, anyone, is automatically insecure, right?
Well... yes. Google (and Apple) almost certainly harvest all the text that goes
through their notification services.

The maybe good news is that it's probably not that easy for these companies to
link that data back to me, if they're only getting it fragmented between the
people I choose to message, and only in notification form. That's not very
comforting though, because one of the core parts of my manifesto is _trust_,
and I can't put any trust in what Apple and Google can or can't do.

## In for a penny, in for a pound

I suppose the question, really, is "Is it worthwhile to secure some parts of a
system if other parts have glaring holes in them?"

Well, information security theory says yes. [If you look at the wikipedia page
on attack surfaces](https://en.wikipedia.org/wiki/Attack_surface), it says:

> The attack surface of a software environment is the sum of the different
> points (for "attack vectors") where an unauthorized user (the "attacker") can
> try to enter data to or extract data from an environment. Keeping the attack
> surface as small as possible is a basic security measure.

So basically, minimising the number of ways in which people and companies can
access your data (the "attack surface") is a worthwhile exercise. Then again,
if one company has unfettered access to your data and sells it to everyone
else, you're pretty screwed regardless. Even so, the more you strive for
privacy, the lower the risk of this happening.

## A third category: obscure information

A thought I keep thinking is "If the ways of getting my private information
are sufficiently obscure, only a targeted attack can affect me, not mass data
gathering".

I think this is a worthwhile protection if it's infeasible to be totally
secure, so I'll probably rework the manifesto a bit to introduce a third
privacy/security tier. As well as the original "secure" and "public", it'll be
something like "obscure", and would be information which is technically
insecure and could be exposed, but probably only by someone who is specifically
targeting me rather than just doing mass data gathering.

Of course, if someone targets me personally, I'll have bigger things to worry
about.

## Some meta things about this blog

I'll keep this bit short, I just wanted to say: please let me know your
opinions! I wholeheartedly think that having your views challenged is the best
way to formulate good ones. Even if what you're gonna say is "you're stupid, I
love Apple and Facebook, please violate my personal data, Daddy Zuck.", I wanna
hear it. I don't kink-shame.

::: series-links
[← Part 1](/blog/0003-taking-back-control-1/){.prev}
[Part 3 →](/blog/0007-taking-back-control-3/){.next}
:::
