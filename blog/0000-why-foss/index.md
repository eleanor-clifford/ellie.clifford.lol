---
title: "Why FOSS?"
excerpt: "Free and Open Source Software is about more than ideology. There are several practical reasons why FOSS software is much better than proprietary alternatives."
createdAt: "2021-04-10"
tags:
  - phil-pol
  - tech
---

Free and Open Source Software is about more than ideology. There are several
*practical* reasons why FOSS software is much better than proprietary
alternatives. Here are the reasons that are the most important to me.

*Note that free refers to freedom, not price*

## 1: Guarantee of future availability

The biggest practical problem with any proprietary software is that there is no
guarantee that you will be able to use it indefinitely. For services that you
depend on, this is a huge issue.

An example that affected me is that of LastPass, a password management system
which I depended on for years. One day they decided that they would lock out
freemium users from using LastPass on desktop and mobile devices at the same
time, rendering it practically useless. This came at a time when I was
particularly busy, and transferring over to another service took a significant
amount of time and energy. This technological ransom is simply not possible
with FOSS services.

So when my friends ask me why I don't want to use PyCharm, this is the second
biggest reason. (The first, of course, is that
[Neovim](https://github.com/neovim/neovim) is clearly superior). "Oh, but it's
free to use with the university! Your future employer will probably give you a
license too!". I expect to use a text editor for decades to come, and I simply
refuse to rely on the whim of a company to do that. Don't even get me
started on operating systems...

## 2: Adaptability and Maintainability

You simply cannot rely on a company to solve your problems for you or implement
the features you want. Why should they? Unless you have a problem that will
affect their public relations, you are relying on the good will of their
employees. Don't forget that the goals of a company are vastly different from
yours.

But even if you aren't a technical person, this is is still a reason to use
FOSS software. Take Microsoft Teams for example. Does it work on Linux? Sort
of, but not well. Are there thousands of developers out there who rely on it
and are capable of fixing it? Certainly, with the source code and some work. Do
Microsoft care? Of course not! The worse it is, the more likely people are to
dual-boot Windows. But they can say "Microsoft ♥ Linux" and get away with it,
because it *sort of* works.

And never mind Microsoft programs that people desperately need, like Word,
instead they have implemented Edge and Powershell on Linux, which I don't think
anybody asked for. At the end of the day, all they care about is the way that
they can present themselves (and in turn, their profits). Not their users.

And what about adaptability? I regularly come across things that I wish were
different in software. I want my drawing program to default to drawing circles
from the centre? [Sure!](https://github.com/eleanor-clifford/xournalpp) Want to use
different keybindings in my terminal?
[Absolutely!](https://github.com/jeffreytse/zsh-vi-mode/pull/89) Want to make
Zoom stop going into fullscreen for no reason when I already have it arranged
perfectly in my window manager? Ah... I guess not. I regularly curse the
developers of proprietary software which I am forced to use, because I have no
way to adapt them to my workflow.

## 3: Usage beyond end of life

Another major gripe I have with many companies is their attitude to
decommissioning proprietary projects, which is generally "I'm not making any
money from this anymore, and nobody else should either, because it's *my* work
so why should I give it away!" This is the corporate equivalent of a toddler
stuffing themselves with cake and then, after they are satisfied, screaming
that it's not fair for anyone else to take a slice. As far as I'm concerned,
when support is dropped for a program, it's common decency to release the
source code and documentation for people to continue to maintain it on their
own. Any claims of copyright infringement in this scenario are bullying at
best.

## 4: Reducing wasted development time

This one is fairly self explanatory. Too much developer time is wasted
reimplementing proprietary software. Take this website for example. Did I
design it? No! The amazing [Zeno Rocha](https://zenorocha.com) did. And he
made it open source, which has meant that I haven't had to learn web
development from scratch, just tweak a few things. The same holds true in
more widespread software. Proprietary software causes massive wastes of
time, when people could be developing truly new software which changes the
world.

## 5: Privacy, security, and transparency

FOSS software is much more trustworthy than proprietary software. There are two
important components to this:

- When the source code is freely available, far more people are able to notice
  security holes.
- You can be sure that the code you are actually running is the same as what
  has been audited.

What's important to note here too is that you simply cannot trust a company not
to have been forced (by governments or otherwise) to distribute software with
backdoors added. You don't have to read and understand the code yourself, but
if several independent auditors across different countries concur that there
are no backdoors, and you can verify that you're running that exact same code,
you can trust it.

That's all from me! More blog posts to come.
