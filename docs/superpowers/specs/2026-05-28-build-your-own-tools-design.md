# Build Your Own Tools — Design Spec

**Date:** 2026-05-28
**Status:** Draft, awaiting Elber's review.
**Author:** Session co-design (Elber Ribeiro + Claude).

## One-sentence pitch

A field-note post arguing that the cost curve for building custom internal tools has flipped (afternoon instead of sprint), that the bottleneck is now the **decision** of what to build rather than the build itself, and that any task a developer does more than twice this month deserves its own purpose-built tool with an AI agent inside it.

## Framing decision

Personal-developer focus, challenging in tone. No employer angle, no team naming. Light self-cast: "I have been building small tools for myself for years. The difference now is that an afternoon is enough, and most developers have not noticed the cost curve flipped." The "regulated domain" line is dropped this post; this is a craft argument, not an ops or adoption one.

## Goals

- Land the thesis: **the decision is the bottleneck.** Building the tool is cheap. Knowing what to build is the work.
- Make the cost curve concrete. A tool that used to cost a sprint costs an afternoon. Quantified, not handwaved.
- Show **three categories of bespoke tools** developers can build today: CLIs, tiny web tools, and quick-launcher extensions or chat-bots. With one concrete example per category.
- Name **AI as the accelerator inside the tool**, not the tool itself. The tool gives the human fast feedback and decision power; the agent does the gather-and-correlate.
- **Challenge the reader directly.** End with a specific question and a 24-hour challenge: pick one repeating task this week, build the tool, ship to yourself.
- Tie to the series: every previous post has been about removing friction or scaling output. This is the post that says: turn the friction you keep paying into a tool that pays it off forever.

## Non-goals (YAGNI)

- A framework shootout (Bun vs Node, Tauri vs Electron, Raycast vs Alfred). Name them in passing, do not rank them.
- A coding tutorial. The post says "an afternoon," it does not walk through the afternoon.
- Naming the employer, a team, or a colleague.
- "AI builds the whole tool for you" hype. The model writes the code; the developer decides what the tool is for.
- A tool catalog. Examples are illustrations, not a list of every option.
- Affiliate links.

## The thesis

For most of a developer's career, building a custom tool was a deliberate cost. A small workflow improvement competed with shipping features. The honest math said: file a ticket, hope someone else builds it, accept the current pain.

The math changed. A tool that needs a small backend, a small UI, and a single integration used to take a week. It now takes an afternoon, because the model writes the code while the developer decides what the code is for. The cost of an experiment dropped to the cost of one good prompt and a review session.

The bottleneck moved. It is not "can I build this?" anymore. It is "should I?" The answer is: anything you do more than twice this month is a candidate.

This post is the challenge to act on that.

## Three categories of bespoke tools

Each gets one short paragraph, with a concrete example.

**Internal CLIs.** A `bin/` script that takes the boring repeating thing and turns it into one command. Example: a `bin/standup` that reads yesterday's git log, calls a model to summarize what you actually shipped, and writes the summary to today's daily note. Built in an evening with Bun or Node, plus an Anthropic SDK call. The agent does the summarize-from-diff; the CLI gives you `bin/standup` as the verb.

**Tiny web tools.** A single-page app that lives on `localhost:3000` and replaces a workflow you currently do across five tabs. Example: a small triage board that reads your inbox or your repo issues, asks a model to rank them by urgency and group by topic, and lets you drag the top five into "today" and the rest into "next week." Frameworks like Bun + Hono on the backend and Vite + Tailwind on the frontend put this within reach in an afternoon. Tauri wraps it as a desktop app if you want one.

**Quick-launcher extensions or chat-bots.** A Raycast extension on macOS or a small Slack/Discord bot that turns "context-switch into a tool, run a command, come back" into a single hotkey or a single message. Example: a Raycast command that takes a selected paragraph and rewrites it in the blog's voice, hitting the model with the right style rules attached. Two hours.

The pattern repeats: the tool gives you the right surface (a CLI verb, a localhost UI, a hotkey), and the agent does the gather-and-correlate inside. You stay the one who decides.

## What this is not

Honest section, three short bullets.

- This is not "AI builds the tool while you sit." You still write the spec for the tool, decide what it is for, and review the code. Same divide of labor as every other post.
- This is not a replacement for the platform team's tools. Use those when they exist. Build your own when the friction is yours and the platform team is six months out.
- This is not a vibe-coding pitch. The same [spec-driven loop](/posts/2026-05-19-the-spec-driven-loop/) applies: brainstorm, spec, plan, implement. The tool that took an afternoon to build is the tool that survives because you specced it.

## The challenge

The post ends with a direct, concrete challenge to the reader.

Pick **one task you did at least twice this past week.** Write it on a sticky note. The morning standup digest. The pull-request triage. The recurring report. The Jira-ticket-to-PR translation. The "where did that bug land" hunt across repos. Whichever one you remember without thinking.

Now ask one question: if a custom tool ran that task for me, would the result land in under a minute and let me move on?

If yes, the answer to "should I build it?" is yes. The cost is one afternoon. The payoff is every week you keep working in that codebase.

The post will name a 24-hour version: by tomorrow night, you have either built it, or you have decided it is not worth building. Either answer is fine. The default of "I will get to it later" is the one this post is challenging.

## Series callbacks

- **Post 10, many agents one chat.** That post said your local setup is the personal team room. This post says the same room can contain the tools you built to do the thinking faster.
- **Post 9, save the boring time.** Same boring time, smaller scope. Post 9 was about ops automations on cluster-sized problems. This post is about hour-sized problems that compound across the year.
- **Post 8, pick a framework, any framework.** Same scaling argument applied to your tools: build the foundation once, parallelize the build with worktrees, accept that the framework matters less than picking up the saw.
- **Post 2, the spec-driven loop.** The tool gets a spec too. An afternoon does not mean skip the spec; it means the spec is short and the implementation is fast.

## Proposed structure

1. **Hook.** I have been building small tools for myself for years. The difference now is that an afternoon is enough, and most developers have not noticed.
2. **The cost curve.** Used to be a sprint, now is an afternoon, because the model writes the code while you decide what the code is for.
3. **The decision is the bottleneck.** Anything you do more than twice this month is a candidate. Hard part is choosing.
4. **Three categories.** Internal CLIs, tiny web tools, quick-launcher extensions or bots. One concrete example each.
5. **What this is not.** Three honest bullets.
6. **The challenge.** Direct, specific, 24-hour version.
7. **Close.** Tools you build are the friction you stop paying.

Target length: 900 to 1100 words.

## Working title

**"Build Your Own Tools"**

Subtitle: *A tool that used to cost a sprint now costs an afternoon. The decision of what to build is the bottleneck. A direct challenge: pick one task you did twice this week and have a custom tool for it by tomorrow night.*

Alternative titles:
- "Build Tools, Not Tickets"
- "An Afternoon to a Tool"
- "The Decision Is the Bottleneck"
- "Stop Asking, Build It"

## Links

- [Anthropic Claude API / Agent SDK](https://docs.claude.com/api) (for the agent-inside-the-tool pattern)
- [Bun](https://bun.sh/) (the fast TypeScript runtime example)
- [Hono](https://hono.dev/) (the tiny backend framework)
- [Tauri](https://tauri.app/) (the desktop wrapper)
- [Raycast extensions](https://developers.raycast.com/) (the quick-launcher example)
- Internal: spec-driven loop, `/posts/2026-05-19-the-spec-driven-loop/`
- Internal: shared context, `/posts/2026-05-22-your-ai-context-belongs-to-the-team/`
- Internal: save the boring time, `/posts/2026-05-26-save-the-boring-time/`
- Internal: many agents one chat, `/posts/2026-05-27-many-agents-one-chat/`

## Cover image plan

Same FLUX pipeline and dark amber-and-teal palette as posts two through ten. Concept: a craftsman's dark workshop at night. Several small handcrafted tools, each one slightly different in shape, sit on a wooden workbench. A warm amber lantern in the foreground is the strongest light source, with cooler teal-cyan rim light tracing the tool edges. Painterly. No text. Conveys "your own tools" as bespoke craft.

## Open questions for Elber

- Self-cast as "I have been building small tools for myself for years" — accurate? Recommendation: yes, the blog itself, the gstack skills, Lanterns tooling, and your daily-note vault all qualify as evidence.
- Three categories (CLI, web tool, quick-launcher / bot) or two? Recommendation: three. They map to three different surfaces and the post is shorter without one of them missing.
- The 24-hour challenge as a closer — too aggressive, or land it? Recommendation: land it. The post needs the bite to do the work the user asked for ("challenge the reader to think about automation").
- Name specific stacks (Bun, Hono, Tauri, Raycast)? Recommendation: yes, brief inline links, the way post 8 named Conductor and Claude Squad. Concrete is better than abstract.

## Decisions

- **Personal-developer focus.** No employer angle.
- **Thesis first.** The cost curve flipped; the decision is the bottleneck.
- **Three categories with one concrete example each.** Not a catalog, not a tutorial.
- **24-hour challenge as the closer.** The post earns its argument by asking the reader to act.
- **Honest about what AI does and does not do.** Same divide of labor.
- **No affiliate links.**
- **Cover generated, not commissioned.** Consistent with the series.

## Sequencing

Post eleven in the build-with-AI arc, after the multi-agent chat post. Publish after Elber reviews this spec and answers the open questions. Same flow as before: spec, draft to iCloud, review, cover, publish EN + PT-BR together per the playbook, then LinkedIn.
