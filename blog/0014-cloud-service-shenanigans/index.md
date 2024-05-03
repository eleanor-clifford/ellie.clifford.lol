---
title: "Cloud Service Shenanigans"
excerpt: "Free (as in beer), but at what cost?"
createdAt: "2024-05-03"
css: |
  img {
    width: 100%;
  }
  button {
    transition: all .3s ease-in-out;
    margin-left: 5px;
    margin-right: 5px;
    display: inline-block;
    border-radius: 4px;
    text-align: center;
    background: #50fa7b;
    color: #000;
    font-weight: 400;
    padding: 10px 18px;
    font-size: 18px;
    border: 0;
  }
  button:focus, button:hover {
    background: rgba(80, 250, 123, .8);
    cursor: pointer;
  }
---

A month or two ago a [friend of mine](https://skye.purchasethe.uk) ran a silly
little event with a bunch of people where we each drank about six or seven
shots of alcohol, and then tried to deliver a presentation using slides we had
never seen before, which one of the other attendees had made beforehand.

At the time I had just been dealing with a major outage of my main server,
which contained a lot of quite important data that wasn't properly backed up
anywhere (I *did* have a backup system, but I turned it off in 2022 when I ran
out of storage, and then forgot to actually deal with the problem, thanks
ADHD)[^1].

[^1]: In fairness, the threat model of "Oracle locks you out of your server
without giving you any warning whatsoever" had not even entered my mind. I
assumed that a vaguely reputable company would at least give a *warning*
first...

Anyway, I had fun making this silly little presentation, and I figure you might
have fun reading it:

<script>
  // JAAAAAVASCRIPT?? What have I become???
  const slides = ["1.0", "1.1", "2.0", "3.0", "3.1"]
  function toSlide(displayed_slide) {
    for (slide of slides) {
      if (slide === displayed_slide) {
        document.getElementById("slide_"+slide).style.display = "";
      } else {
        document.getElementById("slide_"+slide).style.display = "none";
      }
    }
  }
  function prev() {
    let current_idx = +document.getElementById("slides").dataset.current;
    let prev_idx = Math.max(current_idx - 1, 0);
    toSlide(slides[prev_idx]);
    document.getElementById("slides").dataset.current = prev_idx;
  }
  function next() {
    let current_idx = +document.getElementById("slides").dataset.current;
    let next_idx = Math.min(current_idx + 1, 4);
    toSlide(slides[next_idx]);
    document.getElementById("slides").dataset.current = next_idx;
  }
</script>

<div id="slides" data-current="0" onload="toslide('1.0')">
  <img id="slide_1.0" src="./slides/1.0.svg">
  <img id="slide_1.1" src="./slides/1.1.svg" style="display: none">
  <img id="slide_2.0" src="./slides/2.0.svg" style="display: none">
  <img id="slide_3.0" src="./slides/3.0.svg" style="display: none">
  <img id="slide_3.1" src="./slides/3.1.svg" style="display: none">
</div>

<p>
  <button onclick="prev()">Previous Slide</button>
  <span style="float:right">
    <button onclick="next()">Next Slide</button>
  </span>
  <span style="float:center"><a href="./original.odp">Original .odp presentation (no JS required)</a></span>
</p>

I did end up getting the data back, thanks to my insane luck in getting in
contact with Greg. Had I not been so lucky, all the data would be gone, without
even an explanation. The moral of the presentation isn't really about how great
Greg is, though. Greg's not even their real name.

What is the moral? Idk, there's a lot more to say about economies and
diseconomies of scale, about the ossification of corporate structures into
monstrosities where "computer says no" is a valid response; where even the
people at the top can't apply discretion to bend their self-imposed rules even
when they obviously should. But I'll leave that for another post.

For now, the moral is: check your backups! Mine are solid now, don't worry \^w\^
