---
title: "Build Your Own Tools"
subtitle: "A tool that used to cost a sprint now costs an afternoon. The decision of what to build is the bottleneck. A direct challenge: pick one task you did twice this week and have a custom tool for it by tomorrow night."
date: 2026-05-28
description: "The cost curve for building custom internal tools flipped: sprint to afternoon. The bottleneck is now the decision of what to build, not the build itself. Three categories of tools you can build today (CLIs, tiny web tools, quick-launcher extensions), and a 24-hour challenge to act."
cover: /assets/img/2026-05-28-build-your-own-tools.png
coverAlt: "A dark craftsman's workshop at night. Several small handcrafted tools sit on a heavy wooden workbench, each one slightly different. A warm amber lantern at the center is the dominant light source."
---

I have been building small tools for myself for years. The blog you are reading runs on a custom Eleventy setup. My notes live in a custom Obsidian vault structure. The games I make at night come with their own internal scripts. Building bespoke tools is not new.

The difference now is that an afternoon is enough.

A tool that used to cost a sprint costs an afternoon, because the model writes the code while the developer decides what the code is for. The cost of an experiment dropped to one good prompt and a review session. Most developers I work with have not internalized this yet. They still file the ticket and hope someone else builds it. The cost curve flipped underneath that habit, and the habit has not noticed.

The bottleneck moved. It is not "can I build this?" anymore. It is "should I?" The answer is simple: anything you do more than twice this month is a candidate.

Most developers I know are sitting on five of those candidates today and do not see them, because the old math (a tool costs a sprint, my time is the company's, no one approves it) is still running in the background. Run the new math instead: the tool costs an afternoon, the payoff is every week for the rest of the project. The decision pencils out the first time.

The candidates hide in plain sight. The morning standup digest you write by hand. The pull-request triage you do every Monday. The data-fetch-and-format you do whenever someone asks for a status. The "find that bug across three repos" search. The repeated translation between your tool's vocabulary and the deployed system's. These all look small because each one is small. The size that matters is the year you keep paying for them.

## Three categories

**Internal CLIs.**

A `bin/` script that takes the boring repeating thing and turns it into one command. Example: `bin/standup` reads yesterday's git log, calls a model to summarize what shipped (commit messages do not lie, but they read like noise), and writes the summary to today's daily note in your vault. Built in an evening with [Bun](https://bun.sh) and a single Anthropic SDK call. The agent does the summarize-from-diff. The CLI gives you `bin/standup` as the verb. Daily, runs in five seconds, output ready when you open your laptop.

**Tiny web tools.**

A single-page app that lives on `localhost:3000` and replaces a workflow you currently do across five tabs. Example: a triage board that reads your inbox and your repo issues, asks a model to rank them by urgency and group them by topic, and lets you drag the top five into "today" while the rest go to "next week." [Bun](https://bun.sh) plus [Hono](https://hono.dev) on the backend, Vite plus Tailwind on the frontend, all sitting on your machine. Afternoon, not a sprint. [Tauri](https://tauri.app) wraps it as a desktop app if you want one without a browser tab.

**Quick-launcher extensions or bots.**

A [Raycast](https://developers.raycast.com) extension on macOS or a small Slack or Discord bot that turns "context-switch, run a command, come back" into a single hotkey or a single message. Example: a Raycast command that takes a selected paragraph and rewrites it in the blog's voice, with the right style rules already attached to the prompt. Two hours, including the part where I argued with the model about whether "just" was a banned word. Now it ships with the rules built in.

The pattern repeats across all three. The tool gives you the right surface, a CLI verb, a localhost UI, a hotkey, a Slack message. The agent does the gather-and-correlate inside the tool. You stay the one who decides. Same divide of labor as every other post. Smaller scope, faster loop.

## What this is not

Honest section, three bullets.

- This is not "AI builds the tool while you sit." You still write the spec for the tool, decide what it is for, and review the code. Same divide of labor as every other post.
- This is not a replacement for the platform team's tools. Use those when they exist. Build your own when the friction is yours and the platform team is six months out.
- This is not a vibe-coding pitch. The same [spec-driven loop](/posts/2026-05-19-the-spec-driven-loop/) applies: brainstorm, spec, plan, implement. The tool that took an afternoon to build is the tool that survives because you specced it.

## The challenge

Pick one task you did at least twice this past week. Write it on a sticky note. The morning standup digest. The pull-request triage. The recurring report. The Jira-ticket-to-PR translation. The "where did that bug land" hunt across repos. Whichever one you remember without thinking about it.

Now ask one question: if a custom tool ran that task for me, would the result land in under a minute and let me move on?

If yes, the answer to "should I build it?" is yes. The cost is one afternoon. The payoff is every week you keep working in that codebase.

Twenty-four hours. By tomorrow night you have either built it, or you have decided it is not worth building. Either answer is fine. The one this post is challenging is the default of "I will get to it later."

## Close

The blog has spent ten posts on AI as a collaborator in the work you already do. This post is the one that says: the work you do is not fixed. The set of tools you have access to is not fixed. Build the ones that match the work you actually do, not the ones a generic product caters to.

Tools you build are the friction you stop paying.
