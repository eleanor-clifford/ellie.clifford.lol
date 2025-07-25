---
title: "Taking back control (part 3): the PinePhone Pro"
excerpt: "I can't go on having a spyware device in my pocket, can I?? (I use arch btw)"
createdAt: "2022-10-22"
tags:
  - tech
  - projects
---

::: series-links
[← Part 2](/blog/0004-taking-back-control-2/){.prev}
[Part 4 →](/blog/0008-taking-back-control-4/){.next}
:::

PS: this blog is now also accessible over RSS [here](https://ellie.clifford.lol/blog/rss.xml).

From my [manifesto](/documents/technology-usage-manifesto.html):

> 2.0) I will not depend on any proprietary software.

> 2.1) Proprietary software must be run in an [untrusted sandbox].

Clearly, continuing to use a proprietary Samsung device with a proprietary
software additions to Android (as well as some unremovable proprietary apps) is
unacceptable. I could have perhaps installed LineageOS (a fully FOSS build of
Android) on my old phone, but I figured I'd go the whole mile and buy a
PinePhone Pro, which is FOSS all the way down to the PCB design (some of the
chips e.g. the GSM module are proprietary, sadly, though they are sandboxed).
Naturally I've got it running Arch Linux, for the memes but also because it
works really well lol.

## Introducing "flumph"

Having silly naming schemes for things is fun, so I've decided to call my new
PinePhone Pro "flumph", after the creature from Dungeons and Dragons.
Canonically, flumphs are very intelligent creatures, and are immune to
telepathy, just like how this flumph is (hopefully) resistant to surveillance
:D

(Fitting with the DnD creature theme, I've now named my outgoing Samsung "Mind
Flayer", since it has been trying to enslave my brain.)

## Ricing (of course)

Naturally, on buying any new device, one must spend least 15 hours "ricing" it
(aka making it look good without improving usability). I focused my ricing on
the bootloader, since it's the perfect place to put flumph-themed artwork etc
etc. Here are some pictures of the final result:

<table class="noborder" style="border: none">
  <tr>
    <td style="width: 50%">
      <video style="width:100%" controls loop>
        <source src="./flumph-anim.mp4" type="video/mp4">
      </video>
    </td>
    <td style="width: 50%"><img style="width:100%" src="./flumph-unlock.png"
          alt="flumph's full disk encryption unlock screen">
    </td>
  <tr>
    <td style="width: 50%"><img style="width:100%" src="./flumph-incorrect.png"
             alt="flumph after a failed password">
    </td>
    <td style="width: 50%"><img style="width:100%" src="./flumph-unlocking.png"
            alt="flumph during encryption unlock">
    </td>
  </tr>
</table>

<br>
I haven't yet riced sxmo, the desktop environment I'm using, but it's basically
sway, which is basically i3, which I've riced a ton on on my desktop, so it
shouldn't be too much work...

## Mobile data restrictions

Since, while I'm out and about, I plan to use flumph pretty much only for
instant messaging, I bought a super cheap SIM card with very little data
(750MB/mo), and I've tweaked both my matrix client and the network traffic
rules in Arch so that I can't accidentally use it all up at once. I was going
to give a boring technical description of how I did that, but I reckon nobody
cares lol, so I wont (:

## Is it actually usable?

So I'll admit it took me a while to get everything set up, and there are are
still a few niggling annoyances, e.g., I can't get messages over matrix while
the screen is locked because the network devices get turned off when it goes to
sleep >:, but overall yes, it's very usable, and I barely ever have to go back
to Mind Flayer! So that's put me one step closer to fully following my
manifesto...

::: series-links
[← Part 2](/blog/0004-taking-back-control-2/){.prev}
[Part 4 →](/blog/0008-taking-back-control-4/){.next}
:::
