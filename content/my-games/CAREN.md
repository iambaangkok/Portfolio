---
title: C.A.R.E.N.
date: 2022-03-01
rank: 3
summary: A battle simulator between antiviruses and viruses.
description: 
toc: true
readTime: true
autonumber: true
math: true
tags:
  - video-game
  - Java
  - Springboot
  - HTML canvas
  - React.js
showTags: true
hideBackToTop: false
---
![CAREN BANNER](</image/my-games/CAREN/CAREN BANNER.png>)
{{< youtube 0LhSYf7sUOA >}}

## About

**C.A.R.E.N.** is a simulation game of a battle between **viruses** and **antibodies** in your body. Both have their unique genetic codes which determine their behavior.

It is a course project therefore there are some specs that we must follow, like make this a front-end web + back-end server architecture and communicate using REST API... which is not the most suitable for making a game, but we managed to make it work to some degree.

It's like those games where you can ***"code your units"***.


* **See** C.A.R.E.N.'s source code on [GitHub](https://github.com/iambaangkok/CPE200-Project-CAREN)

### The Units

![CAREN UNITS 1](</image/my-games/CAREN/CAREN UNITS 1.png>)
![CAREN UNITS 2](</image/my-games/CAREN/CAREN UNITS 2.png>)
![CAREN UNITS 3](</image/my-games/CAREN/CAREN UNITS 3.png>)

### The Grammar

![CAREN GRAMMAR 1](</image/my-games/CAREN/CAREN GRAMMAR 1.png>)
![CAREN GRAMMAR 2](</image/my-games/CAREN/CAREN GRAMMAR 2.png>)
![CAREN G-CODES 1](</image/my-games/CAREN/CAREN G-CODES 1.png>)

## Running the Game

* clone the GitHub repo above
* the backendserver
  * open `back-end` as the root folder in IntelliJ
  * run `Cpe200ProjectCarenApplication`
* the display (where you play the game)
  * cd to `/front-end/cpe200-project-caren`
  * run `npm install` or do a clean install
  * run `npm start`
  * go to `http://localhost:3000/iambaangkok/CPE200-Project-CAREN` on your browser to play
  * you may need to refresh the page 1 or 2 times

### How to Play

* you only need the mouse
* buy antibodies using the button at the right
* click in one of the three organs to open a scanner
  * click outside the scanner to exit the scanner
* click the button on the right of the scanner to select which antibody to place, click the selected button to unselect
  * click on the scanner screen to place an antibody
  * click on an antibody *on the screen* while **no buttons are selected** to **pickup** that antibody
* you must place at least 1 antibody in each organs for the game to start
* you must clear the viruses in each organs to complete each wave
* there are speed settings in the top left
* to restart the game, restart the backend server, then refresh the game page on your browser

## Development

* Game Engine - **Springboot as backend server**
* Programming Language - **Java**
* Graphics - **HTML canvas**

## Gallery
{{< image-gallery gallery_dir="/image/my-games/CAREN" show_image_title="false" >}}