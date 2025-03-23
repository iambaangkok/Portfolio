---
title: "RootAI"
date: "2024-03-01"
rank: 4
summary: "A non-neural network artificial intelligence ( AI ) system that is capable of playing the boardgame 'Root.'"
description: "An arena shooter game where you must keep the reactor alive by collecting coolants around the arena while surviving the invasion of lava slimes."
toc: true
readTime: true
autonumber: true
math: true
tags: ["video-game", "board-game", "research", "Pygame", "Python"]
showTags: true
hideBackToTop: false
---


![1742401112578.png](/image/my-games/RootAI/1742401112578.png)

## About

**RootAI** is a non-neural network artificial intelligence ( AI ) system that is capable of playing the boardgame "Root." It is the final project of my bachelor's degree. We experimentd by creating various different agents, then **running multiple battles** between them. One *best* AI agent for each faction were found. They were able to play **as good as an experienced human*** (according to Reddit and our own experience), while using **reasonable*** thinking time.

RootAI is set in the scenario of a 2 faction game — **Marquise de Cat** vs **Eyrie Dynasties**.

![1742403391551](/image/my-games/RootAI/1742403391551.png)

* **See** RootAI's source code on [GitHub](https://github.com/iambaangkok/RootAI)

## Running the game

### Prerequisite

* knowledge of Root boardgame's rules ([official Law of Root pdf](https://ledergames.com/pages/resources))

### Download

* download `RootAI.zip` from [GitHub releases](https://github.com/iambaangkok/RootAI/releases)
* extract the zip file

### Run

* double click `RootAI.exe`

### Config

config file is in `/config/config.yml`, change to match your needs.

* Eyrie is set to be the MCTS AI agent
* Marquise is the player
* Eyrie starts first

## Controls

- Press UP/DOWN --- change selected action
- Press R --- random action
- Press RETURN/SPACE --- execute selected action
- Hold F --- continuously run player
- Hold A --- continuously run agent
- Press N in game-end state --- new game
- Press Q in game-end state --- quit game
- Press O --- print_game_state
- Press C --- new_game_from_current_game_state
## Development

* Graphics Engine - **Pygame**
* Programming Language - **Python**

### Breakdown of the program

![1742403506905](/image/my-games/RootAI/1742403506905.png)

#### RootMinimal

**RootMinimal** is the game environment with the following features:

* **Simulate** the current state of the game
* **Generate** all possible actions (“legal actions”)
  for the current player
  at the current state of the game
* **Change** state according to the selected action
  Certain mechanics that are not stated in the rulebook are intepreted according to the Root digital game.

#### RootTrainer

**RootTrainer** is a framework allows humans and AI agents to interact with RootMinimal’s environment.

The AI agents are implemented using these methods:

* Random decision
* Monte Carlo Tree Search (MCTS) algorithm with multiple variants
  * One Depth MCTS
  * General MCTS with various settings

##### Agent: Random decision

It just picks a random action.

##### Agent: Monte Carlo Tree Search (MCTS)

![1742403826862](/image/my-games/RootAI/1742403826862.png)

The MCTS algorithm **maximize the probability of winning** by **simulating rollouts**. Basically, it branch out to each action, simulate randomly (multiple times) until a set condition, and propagates the *"goodness"* of the game state that it reached back to the root node.

Then it picks the best action by looking at the results.

Read more at [Wikipedia: Monte Carlo tree search](https://en.wikipedia.org/wiki/Monte_Carlo_tree_search).

## Gallery
{{< image-gallery gallery_dir="/image/my-games/RootAI" show_image_title="false" >}}