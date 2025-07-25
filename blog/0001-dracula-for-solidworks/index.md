---
title: "Dracula for SolidWorks?!?!?"
excerpt: "Hah! Who says proprietary programs can't be themed?? SolidWorks never stood a chance. I even edited a DLL with vim."
createdAt: "2021-04-12"
tags:
  - favourites
  - projects
  - tech
---

Hah! Who says proprietary programs can't be themed?? SolidWorks never stood a
chance. I even edited a DLL with vim.

![Dracula for SolidWorks](./screenshot.png)

*You can find the theme with full install instructions
[here](https://draculatheme.com/solidworks).*

## Why?

Despite my comments in [this blog post](/blog/0000-why-foss), there are a few
proprietary programs which I am tied to, with no hope of escape. One of these
is SolidWorks, a 3D Computer Aided Design program used extensively in many
engineering teams.

I have spent many hours late at night using SolidWorks, and having a dark theme
really does help prevent eye strain. As for why Dracula, that much is obvious.

## How?!?

SolidWorks doesn't expose a theming mechanism for many of the important colors
in the UI, and it's not open source so I can't just fork it, but obfuscated or
not, a color code is a color code, and I figured I should be able to find it
with grep. A bit of regex fu latex and I was staring at this line...

```
grep: swStyleBlueu.dll: binary file matches
```

Now, the appropriate response here is probably to think "Ok, let me find a
program designed for dealing with DLLs" (or, alternatively, to give up). But
naturally the only thing I was thinking was "Can I open it in vim".  And what I
found was a veritable goldmine...

![Some color codes I found embedded in a DLL](./vim-dll-comments.png)

Yep, that's some sort of style description *embedded in plaintext in a DLL*.
And even better, there are comments! Comments which they thought nobody would
see...

*As a side note, I couldn't figure out for the life of me what tabstop they
were using. Literally nothing would get the comments aligned. Were they just...
incompetent?*

Here are my favourite comments, reformatted for my sanity:

```
// Debug testing colors. Use this to show a custom area with very bright and obnoxious color so it can stand out during debugging.
// jps... I MADE THIS UP. NOT CLEAR FROM IMAGES WHAT IS "PRESSED" VS. "SELECTED"
// thx nvidia for the bug.. :(
// consequently this is no good to do something here !!
// !! magic
// what for ???
// WARNING: setView(-1) CRASHES !!
// TOTEST !!!
// ERROR TO BE HERE!!
// This one is broken
```

Needless to say, I have some questions about the development practices at
Dassault Systèmes...

*As an aside, here's the script I used to find all the comments. Beautiful, I
know.*
```
#!/bin/sh
for i in $(find . -name '*.dll'); do
	vim \
		+"set lazyredraw" \
		+"g/^[[:print:]\r]*\(https\?:\)\@<\!\/\/[[:print:]\r]*$/.,.w! \
			>>//10.0.2.4/qemu/swout.txt" \
		+'q!' $i
done
```

Anyway, naturally, I then wrote a script to change the colors and voilà,
Dracula for Solidworks. But the story's not over. Have you been wondering why
there are still ugly grey bits in the screenshot? Yeah. I found the variables
for that, and tried to change them. SolidWorks refused to start.
