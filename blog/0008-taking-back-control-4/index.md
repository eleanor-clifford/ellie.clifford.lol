---
title: "Taking back control (part 4): ultimatum games"
excerpt: "This is the hill I have chosen to die on, and I will die on it if necessary."
createdAt: "2022-11-20"
tags:
  - tech
  - projects
---

::: series-links
[← Part 3](/blog/0007-taking-back-control-3/){.prev}
[Part 5 →](/blog/0021-taking-back-control-5/){.next}
:::

*This post was minorly edited for clarity on 2025-01-29*

There are (approximately) two types of people who will read this post: my
regular readers (hi!) and people who I've sent this link to, presumably after
refusing to continue messaging them on their favourite messaging system. This
is on grounds of privacy, security, and freedom.

Usually, I would consider the act of giving such strong ultimatums to be
unreasonable and unfair: surely the other person should be given a say? Surely
I should attempt to reason with them and come to an fair compromise? But I find
myself somewhat backed into a corner. Make no mistake, I don't take this
lightly. I apologise for the inconvenience, but this is the hill I have chosen
to die on, and I will die on it if necessary.

## Adversaries

We should start by talking about our adversaries. Get the idea out of your head
of an FBI agent actively listening into your phone calls, that's not what the
real world is like at all. We have two classes of adversary:

1. Profit-motivated entities: this includes Facebook, Google, etc. They
passively harvest all the data they can slurp up and use it to train a
sophisticated model of you: your likes, your dislikes, your triggers, your
guilty pleasures, your political opinions, and so on. So far, this is mostly
used for advertising, but don't think of this in terms of tailoring ads for
you, or you'll fool yourself into thinking that you're smart enough to resist.
No, the other, more worrying, side of this, is that they try to make you waste
as much time as possible interacting with their services (and hence viewing
*more* ads). They will happily trick your brain into a certain dopamine
response which keeps you watching YouTube videos or browsing TikTok even after
you should rightfully be bored. This is obviously dystopian. Don't let it carry
on. (This is not even to mention political nudging, which certain companies
have also engaged in).

2. Government agencies: entities like the NSA or GCHQ undergo mass
surveillance, slurping up all this information too. Ostensibly, they sift
though all of this traffic to detect terrorism and other security threats, but
do we really trust that this is and will always be the only reason? This is a
[Chekhov's gun](https://en.wikipedia.org/wiki/Chekhov%27s_gun), and it must go
off by Act III. By letting the government see our private messages, we are
enabling a future government to use them as evidence against us. Is that
something you want to risk?

## What makes a good messaging system?

So, what do we need from a messaging system in order to fight our adversaries?

1. Privacy: human beings have a right to privacy. The content of messages
(ordinary data) and information about message timing and who is involved
(metadata) should not be passively revealed.

2. Security: In order for privacy to be possible, security is required. We
shouldn't just take a company's word for it, we should be able to verify that
they *cannot* access our information under reasonable threat models.

3. Freedom: Privacy and Security cannot be practically achieved in a zero-trust
setting, some other parties must occasionally be trusted (e.g. server
operators). Users of a messaging system should have the freedom to decide who
to trust, and should not be locked in to trusting any specific party.
Additionally, [ordinary software
freedoms](https://www.gnu.org/philosophy/free-sw.html) are necessary.

## The classic ultimatum game

A bit of a (relevant) aside: the ultimatum game is a classic
economic/philosophical thought experiment, in which there are two players, the
proposer, and the responder. (And an optional third, the arbiter, who manages
the game).

> The proposer is tasked with proposing a percentage split of a sum of money to
> the responder. The responder can either accept (in which case the money is
> split as proposed) or reject (in which case neither of them get any money).

What is the optimal strategy for both the proposer and the responder? The
(absurdly oversimplified) "Homo economicus" model of humanity suggests that the
responder, who maximises the money they get, should accept any split in which
they receive more than zero. Naturally the proposer knows this, and hence
proposes the most unfair split possible.

This is absurdly silly (and yet the "Homo economicus" model is used widely).
Another potential solution is for the responder to reject anything other than a
50/50 split: knowing that knowledge of this would force the proposer to offer a
50/50 split, since the proposer is also trying to maximise the amount of money
they get. But in reality, the responder would surely also accept 51/49 splits.
What about 52/48? 53/47? Clearly this solution isn't quite stable.[^random]

There are other potential solutions (e.g. involving randomness), but
really the only way to understand real human responses is with real data.
Wikipedia says:

[^random]: 2025-01-29: The solution to this instability is the following
optimal strategy: accept a 50/50 split with 100% probability, and accept with
decreasing probability as the proposal becomes more unfair, such that the
expected value to the proposer is maximised at the fair split.

> When carried out between members of a shared social group [...] people offer
> "fair" (i.e., 50:50) splits, and offers of less than 30% are often rejected.

This fits with my intuition. Yay.

## The messaging system ultimatum game

I have in the past been a critic of the classic ultimatum game as being
completely out of touch with the real world, and yet here I am playing a
modified version, namely:

> Ellie (the proposer) is tasked with proposing a set of acceptable messaging
> systems to the responder. The responder can either accept, in which case the
> pair continue to message, or reject, in which the pair cannot message.

This is pretty much identical to the classical ultimatum game, where I am the
proposer, you are the responder, and "money" is some function of the messaging
system we use. I want it to be secure and private, and you don't want to be
inconvenienced. What should be my strategy? Well, firstly, I should clarify my
objectives in this ultimatum game, which are (in no particular order):

1. Continue to talk to my friends

2. Ensure that leaks of my own private information are as unlikely as
reasonably possible

3. Effect societal change (at least in local societal circles) towards privacy,
security, and freedom

The research suggests I'll do reasonably well with somewhere between 50/50 and
70/30 splits, whatever we define those to be.

Let me rank messaging systems then into a few categories of
privacy/security[^categories]:

[^categories]: 2025-01-29: Arguably, Signal's data security is stronger than
Matrix's (it forgoes some features and is more mature), and whether its
metadata security is better than Matrix's depends heavily on your threat model.
This doesn't change the conclusions of the post, and I still strongly prefer
Matrix.

_[More technical explanation](/documents/chat-systems.html)_

1. Data secure, metadata secure (Matrix, XMPP, IRC; each in ideal circumstances)
2. Data secure, metadata unknown (Matrix in ordinary circumstances, Signal)
3. Data unknown, metadata insecure (Whatsapp, Telegram)
4. Data insecure, metadata insecure (Facebook Messenger, Discord, SMS, Unencrypted email)

This suggests I should draw the line between (2) and (3). But it's still a
massive oversimplification of the real scenario. Is this the right place to
draw the line?

## Complicating factor 1: The perception of fairness

In the classic ultimatum game, there is an objective idea of fairness, namely,
"Equal money = fair". Here there isn't. For example, in your head, messaging
systems might be ordered like this:

1. Things you've never heard of (Matrix, XMPP, IRC)
2. Things you've heard of but don't use (Signal, Telegram)
3. Things you occasionally use but don't like (Whatsapp, Unencrypted email)
4. Things you use quite a lot (Facebook Messenger)
5. Your favourite apps (Discord)

Then again, I could order them like this if I was feeling mean:

1. Very likely to be secure, been around a long time (XMPP, IRC)
2. Younger and more featureful but still reasonably secure (Matrix in ideal situations)
3. Likely to be okay, but metadata is potentially vulnerable (Matrix in ordinary situations)
4. Possibly an NSA metadata honeypot but at least the ordinary data is secure (Signal)
5. Very likely to be at least stealing your metadata (Telegram, Whatsapp, Discord, Facebook Messenger, etc)

Using either of these changes perception of a "fair" ultimatum quite a lot,
and there's no neat resolution. I think my original categorisation is
reasonable, but we can argue about it if you like.

## Complicating factor 2: Social dynamics

Ultimatums don't exist in a vacuum. You might be thinking to yourself "Wow,
this girl's an asshole. Nobody else cares about this and she wants to dictate
how we message?" Not only that, but people don't like caving to ultimatums,
lest other person take advantage and make even more ultimatums.

Honestly, I can relate to that. All I can say is that I'm okay with you being
annoyed at me, because I truly believe that this is a cause worth championing,
whatever the consequences. I don't like making ultimatums either.

## Complicating factor 3: Negotiation and individuals

Why should I apply the same ultimatum to everyone? Some of you might rightly
realise that I really enjoy talking to you, and that you have negotiation power
over me. If you were to refuse to message securely, would I cave and continue
messaging you insecurely? I would have to choose either to compromise the
legitimacy of my ultimatum, or stop talking to you.

That's a tough choice to make. It will be even harder when this becomes
concrete rather than abstract. In general I want to be the type of person that
sticks to their values, and so I'm sorry, but I won't cave. My only hope is
that in showing you how important this is to me, you'll come around.

That said, if it's not "can you break your rules for me", but "I think your
rules could be improved", then please bring it up. I'm not a brick wall.

## Complicating factor 4: Groups

The 1 on 1 ultimatum game is one thing, but to say to an entire group of people
"Let's move to this other system, or I'm leaving" is a whole other beast. I
have succeeded (more gently) with a few small groups, but it's a difficult
task.

For this reason, I will (for now) let myself be part of Whatsapp groups (but
*not* Facebook Messenger groups). However, I will (on the whole) only be a
passive observer, and never send anything remotely sensitive. I will continue
to petition for the group to move to Matrix, since even my presence in the
group is a powerful source of information for Facebook (who own Whatsapp).

An even harder problem is large organisational entities (e.g., companies I work
with). In those, I have zero power whatsoever, and must do what I'm told. To be
honest, this *sucks*, and I'll try not to work for companies that communicate
over Facebook Messenger, Slack, etc. But when I have no choice, I have no
choice. I'll certainly be careful to watch what I say, at least.

## Complicating factor 5: New people

Ok so like, there's no way if someone I don't know tries to message me on
Whatsapp or something I can just reply with "Install this other app and then
I'll reply". They'd just think I'm weird and then ignore me probably. Or it
would at least be awkward. As the [old
adage](https://files.clifford.lol/copypastas/free-virgin.txt) goes:

> I can't ever seem to get girls to come over to my place and I can't text them
> either. Once I get their numbers since I've added customs roms to my phone
> and refuse to use sms since it's a security concern I require all of my
> friends to download a free and open source messaging app and I share with
> them my public gpg key so that we can verify that our conversations are
> secure. None of my friends are willing to do this. And I can't use sites like
> tinder since it's not only proprietary software but a major privacy
> vulnerability. How come it is so hard to find a girl concerned about software
> freedom. I feel like I'm going to be a virgin forever.

I think what I'll do is finish the initial conversation (watching what I say)
and then tell them I don't actually use Whatsapp, and ask them to select from a
list of secure apps. That seems reasonable, but it's subject to change.

## Complicating factor 6: Edge cases

I don't expect this to happen, but what if someone literally can't comply with
my ultimatum? For instance, they only use a Nokia brick and have no other
computer, so they can only use SMS. Honestly I'd be surprised if this happens.
But if it does, then let's work together to figure something out. It won't be
as simple as "Ok, I'll just use SMS then", but I'm not going to just ignore you
if there's nothing you can do about it. That said, don't try to use this as an
excuse to refuse. If you own either a smartphone or a laptop, it's extremely
unlikely you *can't* use a secure messaging system.

Another edge case: what if I meet someone with an ultimatum which directly
contradicts mine? Again, ideally I'd want to work together to figure it out.
But if your ultimatum contradicts mine in such a fundamental way that it can
never be reconciled (e.g. "I want Facebook to have a record of our
conversation"), then maybe I just don't want to be your friend?

## Conclusion

So, there are a lot of complicating factors. On the whole, I don't think they
affect the outcome too much, other than adding nuance, and informing me that I
should apply discretion. I truly am sorry for the inconvenience I am likely
causing you, but I must hold true to my values.

So then, the (possibly incomplete) list:

*(You may find [these diagrams](https://ellie.clifford.lol/documents/chat-systems.html) useful for technical explanations)*

### I will use (please suggest others if appropriate)

Matrix (e.g. the "Element" app), Signal, (and XMPP, IRC, PGP-encrypted email, ...)

### I will use only passively for groups

Whatsapp

### I will not use

Facebook Messenger, Discord, Telegram, SMS, Snapchat, Instagram DMs, ...

::: series-links
[← Part 3](/blog/0007-taking-back-control-3/){.prev}
[Part 5 →](/blog/0021-taking-back-control-5/){.next}
:::
