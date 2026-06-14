---
title: "Don't Make the Model Do a Build Step"
subtitle: "An agent spends the first minutes of every session rebuilding a map of your codebase. A script already has that map. The model should read the facts, not re-derive them."
date: 2026-06-13
description: "The context an agent needs splits into facts and judgment. A code graph, API surface, and dependency map can be generated from source and kept fresh on every commit. Asking an LLM to produce or maintain them is slower, costs tokens, and rots. Let the build step own the facts and save the model for judgment."
cover: /assets/img/2026-06-13-tools-own-the-facts.png
coverAlt: "A deep charcoal scene where a glowing amber wiring diagram of a structure draws itself along precise lines of teal light, no human hand in frame, brushstroke texture and soft bloom."
---

Watch an agent start a task in a codebase it has seen before. It greps for a function. It opens three files to learn what calls that function. It reads an import to find where a type is defined, then opens that file too. Five minutes in, it has rebuilt a map of your code in its head. The same map it rebuilt yesterday. The same map a script could have handed it in two seconds.

You are paying for that. Tokens for every file it reads to orient. Latency while it wanders. And worse than the cost, you are trusting a guess where you could have had a fact. The agent's mental model of your code is an inference. The code itself is the truth.

This is the mistake I want to name. We reach for the model to do work a build step does better.

## Facts and judgment

The context an agent needs comes in two kinds.

One kind is facts about the code. Where is this defined. What calls it. What does this API accept and return. Which modules depend on which. What is deprecated. These answers live in the source. They are not opinions. A tool reads them.

The other kind is judgment. Given those facts, and given what we are trying to build, what change makes sense. That is the model's job, and the model is good at it.

The line between them is sharp, and most setups smudge it. They make the model gather the facts before it gets to think. The model is slower at gathering than a parser, more expensive, and it forgets everything the moment the session ends. Then it does it all again next time.

## The deterministic three

Three maps cover most of what an agent reorients on, and all three come from source with no model in the loop.

A **code graph**. Who defines each symbol, who calls it, what imports what. A parser walks the syntax tree and writes it down. This is the map the agent rebuilds by hand every session. Build it once per commit instead.

An **API surface**. The public types, the function signatures, the routes, the database schema. The contract your code exposes. You do not narrate a contract to an agent and hope it stays current. You derive it from the types that already exist and regenerate it when they change.

A **dependency and architecture map**. Module boundaries, which way the dependencies point, what is on its way out. This one catches the agent's most confident mistakes, the change that looks right in one file and breaks the layering of the whole system. Generated from the imports and the config, it is a fact the agent reads instead of a rule it stumbles over.

None of these need a language model to produce. They need a parser and a commit hook. The output is a file the agent reads first, fresh every time, because a build step rewrote it when the code last changed.

## The one map a tool cannot build

There is a boundary, and it proves the rule.

A tool can read your code. It cannot read your intent. Why this feature exists, what counts as done, what you decided not to build and why. That lives in heads, not in source, and no parser will ever find it. I have [written](/posts/2026-05-24-context-is-not-a-dev-job/) about [this half](/posts/2026-05-22-your-ai-context-belongs-to-the-team/) before. A human writes the product view, once, by hand.

So the agent gets two inputs. The facts, derived from source by a tool. The intent, written by a person. Both arrive fresh, neither is the model's to invent. The model sits in the middle and does the one thing only it can do. It reasons.

Notice what the model never does in this picture. It never produces the facts. It never produces the intent. It consumes both and writes the change.

## Why the build step wins

Three reasons, and they stack.

Cost. A generated map is a few seconds of CPU. The agent reading the same map by hand is dozens of file reads, every session, paid in tokens every time.

Speed. The map is already on disk when the agent starts. No orientation phase. It opens one file and knows the shape of the system.

Trust, and this is the one that matters most. A generated map cannot be out of date, because a commit hook rewrites it whenever the code changes. An LLM's mental model goes stale the instant a teammate merges. A doc a person wrote last quarter is already lying. The only documentation you can trust is the documentation a pipeline regenerates, the same reason I built [Conduit](/posts/2026-06-12-conduit-launch/) to keep retrieval data fresh instead of trusting a snapshot. Freshness comes from a pipeline, not from an author.

## What this is not

- Not a tools tutorial. Tree-sitter, ctags, language servers, OpenAPI generators, the category is full of good options and they are not the point. Pick one.
- Not anti-LLM. The model is the whole reason to do this. You are clearing its desk so it can think.
- Not the human-context argument again. That was about writing down intent. This is about not writing down facts a tool already knows.

## Close

Stop asking the model to be a worse version of a build step. It is slow at gathering, it forgets between sessions, and it guesses where a parser would know.

Give it a map the build step keeps fresh and an intent a person wrote down. Then let it do the part you actually hired it for.
