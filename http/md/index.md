---
# vi: set et ts=2 sw=2 sts=2 :
ssi: false
css: |
  .columns {
    display: flex;
    flex-wrap: wrap;
    flex-direction: row;
    max-width: 100%;
    margin-bottom: -20px; /* to deal with margins not collapsing */
  }

  .column-left {
    width: 410px;
    max-width: 100%;
    margin-right: 20px;
  }

  .column-right {
    width: 410px;
    max-width: 100%;
  }

  .flex {
    display: flex;
    flex-direction: column;
    justify-content: center;
  }

  .webring h2 {
    display: flex;
  }

  .webring span {
    margin: auto;
    display: block;
    text-align: center;
  }

  .webring {
    display: table;
    margin-top: -20px;
    margin-bottom: 30px;
  }

  .webring-links {
    text-align: center
  }

  .webring-links a {
    margin: 0px 20px;
  }

  div.motd {
    width: fit-content;
    margin-top: 20px;
  }

  .motd figure {
    margin: auto;
  }

  .motd img.main-img {
     width: 300px;
     max-width: 100%;
     margin: 0px;
  }

  .motd figcaption {
    margin: 8px;
  }

  .motd div.thumbs {
    display: flex;
    flex-wrap: wrap;
    max-width: 300px;
    margin: auto auto 20px auto;
  }

  .motd .thumbs a {
    max-width: 25%;
  }

  .motd .thumbs img {
    height: 56px;
    object-fit: contain;
    margin: 0px;
  }

  .webring-disclaimer p {
    font-size: 16px;
    text-align: center;
    margin-bottom: 0px;
  }

  .overlay {
    position: absolute;
    top: 100px;
    right: 20px;
    padding: 10px;
    color: #8be9fd;
    transform: rotate(10deg);
  }

  .overlay p {
    font-size: 30px;
    font-weight: 700;
    margin: 0px;
  }

  @media screen and (max-width: 600px) {
    .overlay {
      top: 90px;
      right: 10px;
    }
    .overlay p {
      font-size: 20px;
    }
  }

  .indent p {
    margin-top: 5px;
    margin-left: 20px;
  }

  p:has(.blog-summary) {
    margin-bottom: 5px;
  }

  img.bsky {
    margin: 0px;
    height: 38px;
  }
---

::: columns
::: column-left

``` {=html}
<h1>Ellie Clifford</h1>

<div class="blog-updates">
 <form method="post" action="/cgi-bin/subscribe.py" class="form">
  <input type="email" name="email" placeholder="Your email"/>
  <input type="text"  name="antispam" placeholder="1+1="/>
  <input type="submit" value="Subscribe"/>
 </form>
 <a class="nounderline" href="/blog/rss.xml">
  <img class="rss" src="/_icons/rss.svg" alt="RSS feed icon"/>
 </a>
 <a class="nounderline" href="https://bsky.app/profile/ellie.clifford.lol">
  <img class="bsky" src="/_icons/bluesky.svg" alt="Bluesky icon"/>
 </a>
</div>
```

Armchair philosopher, musician, cypherpunk.

::: webring

## <span>🏳️‍🌈</span><span style="margin: 0 0.5em">Be crime do gay webring</span><span>🏳️‍⚧️</span>

::: webring-links
<a href="/cgi-bin/webrings/be_crime_do_gay.py?side=left">← Go left</a>
<a href="/cgi-bin/webrings/be_crime_do_gay.py?side=right">Go right →</a>
:::

::: webring-disclaimer
Membership of the webring does not imply my endorsement
:::
:::

Apparently some people who visit this site don't notice that there are buttons
in the top right that take you to other parts of the site. If that's you,
here's your PSA: click them and be taken to cool places!!!

:::
::: {.column-right .flex}
<div class="motd">
<figure>
  <figcaption>Meme of the now:</figcaption>
  <a class="nounderline" href="/memes/07_terf_island.jpg">
    <img class="main-img"
         alt="Meme with cat in the centre and infinite loop between &quot;I wake up&quot; and &quot;there is something wronger with Britain&quot;"
         src="/memes/07_terf_island.jpg">
  </a>
</figure>
<figure>
  <figcaption>Previously:</figcaption>
  <div class="thumbs">
   <a class="nounderline" href="/memes/06_stem.jpg">
     <img alt="YEAH I'm a STEM girl. Stopped friendship with Testosterone, now Estrogen is My best friend!!1!"
          src="/memes/thumbs/06_stem.jpg">
   </a>
   <a class="nounderline" href="/memes/05_sysadmin_cat.jpg">
     <img alt="[picture of a cat inside a server cabinet]. Her ass is NOT sysadmin certified!!"
          src="/memes/thumbs/05_sysadmin_cat.jpg">
   </a>
   <a class="nounderline" href="/memes/04_skellie.jpg">
     <img alt="state of the world? bad. mental health? also bad. but still, we charge forward"
          src="/memes/thumbs/04_skellie.jpg">
   </a>
   <a class="nounderline" href="/memes/03_hrt.jpg">
     <img alt="Get in the tank comrade, we are going to seize the means of hormone production"
          src="/memes/thumbs/03_hrt.jpg">
   </a>
   <a class="nounderline" href="/memes/02_calculations.jpg">
     <img alt="According to my calculations, you're trans"
          src="/memes/thumbs/02_calculations.jpg">
   </a>
   <a class="nounderline" href="/memes/01_cam_girls.jpg">
     <img alt="In a mass surveillance state, we are all cam girls"
          src="/memes/thumbs/01_cam_girls.jpg">
   </a>
   <a class="nounderline" href="/memes/00_him.jpg">
     <img alt="cute kitty with the caption 'put him on your site immediately'"
          title="Do it or die trying"
          src="/memes/thumbs/00_him.jpg">
   </a>
  </div>
</figure>
</div>
:::
:::

::: columns
::: column-left


## A few of my favourite works

[What we leave behind](/blog/0006-what-we-leave-behind/){.blog-summary}

::: indent
On humanity, legacy, and why I write at all
:::

[Chains of Flesh](/blog/0022-chains-of-flesh/){.blog-summary}

::: indent
A trans and transhumanist ballad
:::

[Cloud Service Shenanigans](/blog/0014-cloud-service-shenanigans/){.blog-summary}

::: indent
A silly one about nearly losing all my data
:::

[Taking back control (part 5)](/blog/0021-taking-back-control-5/){.blog-summary}

::: indent
On technology, power, and tentacled monsters
:::

[more...](/blog/)

:::
::: column-right

## Links for tech people

[Services for all at `transgirl.fr`](https://transgirl.fr/){.green-override}

[Services for UniOfCam people at `srcf.net`](https://www.srcf.net/){.cyan-override}

[Dracula theme gallery](/dracula/){.purple-override}

[Miscellaneous projects](https://sr.ht/~ecc/){.pink-override}

[My Technology Usage Manifesto](/documents/technology-usage-manifesto.html){.orange-override}

[A Cypherpunk's Manifesto (by Eric Hughes)](/documents/cypherpunks-manifesto.html){.yellow-override}

:::
:::
