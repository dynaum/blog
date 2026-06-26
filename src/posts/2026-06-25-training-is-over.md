---
title: "Training Is Over Before You Arrive"
subtitle: "The model never learns from your chats. It arrived finished. What feels like learning inside a session is context, and it dies when you close the tab."
date: 2026-06-25
description: "Correct the model and it adapts, then forgets by tomorrow. It never learned, it re-read. Weights freeze before the model ships, every session starts from the same frozen object, and in-session learning is context, not training. Fine-tuning vs context in one stroke."
cover: /assets/img/2026-06-25-training-is-over.png
coverAlt: "A deep charcoal gallery where a single finished amber-lit sculpture stands complete on a plinth, faint teal light drifting past without changing it, brushstroke texture and soft bloom."
---

You tell the model it got something wrong. You explain the rule. It agrees, and from then on it follows the rule perfectly. For the rest of the session it holds your name, your preferences, the correction you made an hour ago. It feels like it learned.

Open a fresh chat tomorrow and it is all gone. The name, the rule, the correction. Blank. You did not teach it anything. It re-read what was in front of it, and then the page was cleared.

## The model is already finished

Training happened in the past. Before the model reached you, it went through one long, expensive process. It read a huge amount of text and adjusted billions of internal numbers, its weights, until it got good at predicting the next word. Then the process stopped. The weights froze. The model shipped.

Every conversation you have runs against that frozen set of numbers. So does every conversation everyone else has. You and a stranger on the other side of the world open the same model, in the same state, down to the last decimal. Nothing you do in a chat changes a single weight. The model answering your last message is identical to the one answering your first.

## Then what felt like learning?

Context.

The correction you gave did not update the model. It sat in the context window, the working space the model re-reads from scratch on every turn. While your words are in that window, they shape what comes next. The model looks like it adapted because it is reading your correction every single time it generates a reply. Clear the window, start a new session, and your words are no longer there to read. There is nothing to forget, because nothing was ever stored. I wrote about this in [The Context Window Is a Desk, Not a Memory](/posts/2026-06-10-context-window-desk-not-memory/).

This is the whole trick. In-session learning is not learning. It is reading.

## Two ways to change behavior

There are exactly two ways to make a model behave differently, and they are not the same size.

One is fine-tuning. You take the frozen model and run more training on it, with new examples, until the weights shift. This is real change to the model itself. It is also slow, expensive, done offline by the people who own the weights, and it produces a new frozen model, not a model still able to learn. Fine-tuning is rare, and almost nobody reaches for it to solve a daily problem.

The other is context. You put instructions, examples, and facts into the window, and the existing frozen weights respond to them. Nothing changes inside the model. You are steering a fixed object with the input you hand it. This is cheap, instant, per-session, and it is what you do every time you write a prompt, paste a style guide, or correct a mistake.

Almost everything you think of as getting the model to do X is context, not training. When you are tempted to say you taught the model something, you almost always mean you put something good in the window.

## What this changes

A few things fall out of this once you hold it.

The model is reproducible. Same weights for everyone means the behavior you get is a function of the input, not of some private history the model built up with you. If two people get different answers, the difference is in the context, not the model.

You brief, you do not plead. Your frustration does not train the model, so repeating yourself louder does nothing. What works is putting the right thing in the window. A clear instruction beats a third correction.

Memory features are saved context, not learning. When a tool remembers you across sessions, it is storing text somewhere and quietly pasting it back into the window next time. Useful. Still context. The weights never moved.

Your fix does not stick on its own. Because the correction lives only in the window, it dies with the session. If you want it every time, you have to put it somewhere re-supplied on every run: a system prompt, a project file, a [committed CLAUDE.md](/posts/2026-06-15-commit-the-context/). This is the same reason I argued you should [capture corrections as durable rules](/posts/2026-05-31-fix-the-system-not-the-output/) instead of fixing the same thing twice.

## One question this is not about

People ask a related question: does my conversation get used to train the next version of the model? It is a real question with a real answer, and the answer depends on the provider and your settings. It is also a different question. It is about a future training run you are not in. This post is about the model in front of you right now, which is finished and will not change while you use it.

## Close

The model is not growing alongside you. It arrived done. Every session starts it from the same frozen state, reads whatever you put in front of it, and forgets all of it the moment you close the tab.

So stop trying to teach it. You are not its teacher, you are its briefer. Every session is day one, and the quality of the day depends on how well you brief it.
