---
title: "tmux Still Works. I Switched Anyway."
subtitle: "Nothing broke. My work changed shape, the tool did not, and after years of the same setup I wanted to find out if I was still able to move."
date: 2026-07-11
description: "I used tmux for years and it never failed me. Then my terminal filled with coding agents I had to supervise instead of commands I typed, and a tool built for that from day one beat a tool adapting to it. The switch was small. The habit behind it is not."
cover: /assets/img/2026-07-11-tmux-still-works.png
coverAlt: "A worn wooden-handled hand tool lying on a dark workbench, still clean and usable, while a hand reaches past it to pick up a newer precision instrument, a warm amber glow between them and a muted teal rim light, brushstroke texture and soft bloom."
---

tmux never failed me. Not once, in years. No crash, no data loss, no morning where my sessions were gone. Which is exactly what made leaving hard.

A broken tool asks you to replace it. A working tool asks nothing. You keep the muscle memory, you keep the config you tuned in 2019, and you never find out what else exists. I stayed there a long time, comfortable, and comfort is a bad reason to stop looking.

Last week I installed [herdr](https://herdr.dev/) and moved my daily work into it.

## The tool did not change. The work did.

My terminal used to be a place where I typed. Commands, tests, a server on the left, logs on the right. Panes were containers for things I started and watched with my own eyes.

That is no longer what I do all day. Now I run coding agents. Several at once, on different repos, on different branches. One is running a test suite. One is halfway through a refactor. One stopped four minutes ago and is waiting for me to answer a question, and I have no idea, because a pane looks the same whether an agent is grinding through work or sitting idle asking for permission.

The bottleneck moved. I am not slow at typing. I am slow at knowing which of my agents needs me right now.

tmux has no opinion about any of this, and it should not. It is a terminal multiplexer, and a good one. It gives me panes and sessions and gets out of the way. The state inside those panes is none of its business, by design.

## Built for it beats adapting to it

herdr starts from a different premise. It is a multiplexer where the workspace knows agents are running inside it.

Each pane carries a state: idle, working, blocked, done. A sidebar shows all of them at once. I glance at one column and I see the shape of my whole herd. The agent waiting on a decision is marked as waiting on a decision. I stop discovering blocked sessions three minutes late by cycling through panes.

That is the entire benefit, and it sounds small written down. In practice it changes how the day feels. My attention goes to the agent asking for it instead of to a round-robin scan of six panes hoping to catch someone stuck.

The ecosystem around tmux is adapting. Status line hacks, wrapper scripts, plugins to surface agent state. People are building the same idea on top of a tool never designed for it, and some of those setups are clever. But there is a difference between a tool bending toward your work and a tool starting where your work already is. The first one asks you to assemble the answer. The second one ships with it.

## The part nobody enjoys

The first two days were worse. Obviously they were worse.

My hands know tmux. The prefix key fires before the thought does. I hit it constantly in herdr and nothing happened, the way you reach for a light switch in a house you moved out of. Some corner of my old config, tuned over years, is not reproduced anywhere yet. I felt slow, and being slow at something you were fast at is a small, specific humiliation.

Then it passed. Two days. That was the whole price.

Compare it against what the years of not looking cost me. I ran an agent-heavy workflow inside a tool with no idea agents existed, and I called the friction normal, because I had nothing to compare it against. The cost of switching is loud, visible, and over in a week. The cost of never switching is silent and compounds. You do not feel it. You quietly become someone whose setup was designed for the work they were doing in 2019.

## The habit is not about the multiplexer

I am not telling you to install herdr. Perhaps tmux plus a good plugin is the right answer for you. Perhaps you tried herdr and hated it.

I am telling you the switch was never about a multiplexer. It was a test of whether I am still someone who moves. Doing the same thing for years does not have to mean you stopped learning, but it slides there quietly, and nobody sends you a notification when it happens. You find out later, when a whole category of tool went past you and you did not look up.

So look up on purpose. Once in a while, pick up the thing built for the work you are doing now, and see if the ground has moved.

Then look at the room you are sitting in. If your team is doing the same work in the same way as three years ago, and everything new is met with "what we have works," ask yourself honestly what you are learning there. A working tool asks nothing of you. Neither does a comfortable company. Both let you stand still while the field moves, and one of them is costing you a career, not a config file.

I know which one I would leave.

I might go back to tmux next month. If I do, it will be because I know, not because I never checked.
