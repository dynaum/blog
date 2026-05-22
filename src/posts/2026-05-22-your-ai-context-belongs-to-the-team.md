---
title: "Your AI Context Belongs to the Team"
subtitle: "Every session with an AI is a teaching session. Most teams throw the teaching away. Here is how to keep it, share it, and let it compound."
date: 2026-05-22
description: "The context you build with AI in private sessions is a team asset. How to keep it in a shared knowledge base with Obsidian, manage the in-repo CLAUDE.md layer, and make AI-DLC easier."
cover: /assets/img/2026-05-22-your-ai-context-belongs-to-the-team.png
coverAlt: "A constellation of small glowing amber notes connected by fine threads of teal light, like a knowledge graph seen in the dark."
---

Every time you open a session with an AI, you teach it. You explain the shape of the codebase, the conventions, the domain rules, the gotcha from last month, the reason a strange piece of code is strange. That explaining is real work. It is also one of the most valuable things you produce all day, and most teams throw it in the bin the moment the session closes.

Here is the pattern I keep seeing. One developer spends twenty minutes getting the model up to speed on a service. They do good work, the session ends, and the context leaves with it. The next day a teammate opens a fresh session and explains the same service from zero. Same twenty minutes. Same explanation. Nobody is lazy and nobody is wrong, and the team still pays the tax every day. The meter is running and no one sees it.

The fix starts with a reframe. AI context is not a personal artifact. It is infrastructure. The knowledge base you build for your own model is, almost line for line, the knowledge base the developer next to you needs. Treat it the way you treat code. Write it down once, put it somewhere shared, version it, and let everyone draw on it.

The tool I reach for is [Obsidian](https://obsidian.md/). The reason is narrow and it matters. An Obsidian vault is a plain folder of Markdown files. You read it through a clean interface with links and a graph view. An AI agent reads the same files directly, with no export and no conversion. The knowledge base your team maintains and the knowledge base the model consumes are one thing, not two copies drifting apart.

The rest is supporting cast. Notes link to each other, so a note about a system points at the principle behind it. The vault is a git folder, so the knowledge base versions alongside the work. And none of this is locked to Obsidian. Any folder of Markdown does the job. Obsidian is a good default, not the only door.

A structure I trust: a principles folder for the durable rules, the how-we-think notes, and a folder per system or domain for the specifics. Keep each note small and about one thing. Link them.

I run this for my games. I keep a vault where the design lessons from one game live in a principles folder, kept separate from the folder for the game itself. When I start the next game, I do not start from nothing. The model and I both open the same vault, and the hard-won lessons from the last project are already on the table. The first game pays the tuition. Every game after it reads the notes. The idea works at the scale of one person across projects the same way it works for a team across people.

What goes in it? The gotchas, the why behind decisions, the domain vocabulary, the non-obvious constraints, the dead ends you already walked down. A simple test: if you would explain it to a new hire in their first week, and you would also explain it to a fresh AI session, it belongs in the shared base. New hires and fresh sessions need the same things.

There is a second layer, closer to the code. A `CLAUDE.md` or `AGENTS.md` file sits in the repo and carries the context specific to that project. The vault holds the durable, cross-project knowledge. The repo file holds what only this codebase needs.

Managing both is one habit, not a process. When you catch yourself explaining something to the model you have explained before, stop and write it down. If it is specific to the project, it goes in the repo file. If it is a durable principle, it goes in the vault. Re-explaining the same thing is the signal. The second time is a bug, and the fix is a paragraph. Prune the same way. A stale context file costs more than an empty one, so delete what is no longer true.

This pays off directly if your team is moving toward AI-DLC. AI-DLC runs on steering files, shared rule files that constrain the agent. A team with a real shared context base already owns the raw material. The steering files become a curation job, not a blank page. The [last post](/posts/2026-05-21-you-cannot-push-a-developer/) on this blog argued that friction is what stalls adoption. A thin or missing context base is friction. A good one removes it.

The [spec-driven loop](/posts/2026-05-19-the-spec-driven-loop/) keeps one model on track by writing context down. This is the same move, made plural. The context you write today is the twenty minutes a teammate does not lose tomorrow, and the head start your next project gets for free. Stop hoarding it. Put it somewhere everyone, and every session, will find it.
