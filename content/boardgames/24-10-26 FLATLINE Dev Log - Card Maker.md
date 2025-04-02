---
title: "FLATLINE Dev Log: Card Maker"
date: 2024-10-26
rank: 0
summary: Coded a card maker from HTML template.
description: 
toc: true
readTime: true
autonumber: true
math: true
tags:
  - board-game
  - FLATLINE
showTags: true
hideBackToTop: false
---
# The Card Maker

So there are problems with hand-drawn cards.
* They can't fit as much detail
* They are hard to adjust the values
* They don't look as cool / immersive

I need to make something that can generate these cards with my stats. But existing card makers just don't fit my needs.

The solution? make a **Card Maker!**

1. import CSV data file
2. put those data file into HTML template
3. export as .png or .pdf or whatever

GitHub repo: https://github.com/iambaangkok/Card-Maker

## How it works
1. use html/template lib to parse a html template
2. fill the template with variables from a struct
3. render with headless browser via chromedp lib

## The making of Card Maker

![FLATLINE 24-09-21.png](</image/boardgames/FLATLINE/FLATLINE 24-09-21.png>)
https://x.com/meisbk/status/1837197359358562625

![FLATLINE 24-09-22.png](</image/boardgames/FLATLINE/FLATLINE 24-09-22.png>)
https://x.com/meisbk/status/1837781078901137807

## Print-outs!

![FLATLINE 24-10-23 - 1.png](</image/boardgames/FLATLINE/FLATLINE 24-10-23 - 1.png>)
* VEND smg : 🤓
* VEND : 😎

https://x.com/meisbk/status/1848980292683653594

![FLATLINE 24-10-23 - 2.png](</image/boardgames/FLATLINE/FLATLINE 24-10-23 - 2.png>)

![FLATLINE 24-10-23 - 3.png](</image/boardgames/FLATLINE/FLATLINE 24-10-23 - 3.png>)

![FLATLINE 24-10-23 - 4.png](</image/boardgames/FLATLINE/FLATLINE 24-10-23 - 4.png>)

![FLATLINE 24-10-23 - 5.png](</image/boardgames/FLATLINE/FLATLINE 24-10-23 - 5.png>)
https://x.com/meisbk/status/1849086191041495490


# Gallery

{{< image-gallery gallery_dir="/image/boardgames/FLATLINE" show_image_title="false" >}}
