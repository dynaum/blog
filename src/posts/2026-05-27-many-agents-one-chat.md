---
title: "Many Agents, One Chat"
subtitle: "Once you run more than one agent locally, you become the bottleneck. A chat interface plus a vault is the upgrade. Why agentchattr and Obsidian pair so well for the personal scaling problem."
date: 2026-05-27
description: "Scaling the local developer setup with agentchattr (a chat interface for multi-agent work, each agent in its own tmux session and worktree) and Obsidian as the day's plan and decision log. The two-surface daily loop, why the chat metaphor pays off, and what the chat does not solve."
cover: /assets/img/2026-05-27-many-agents-one-chat.png
coverAlt: "A cozy dark desk at night, an open notebook in the center beside a warm amber lantern, with several small glowing terminal panes floating in the dark around them. One watcher, one notebook, many agents."
---

Once you are running more than one agent at a time, the bottleneck stops being the agent and starts being you, the orchestrator. Switching between four terminal panes, four worktrees, and four mental contexts is the new tax. This post is about the tooling that pays it off, and the daily loop the tooling makes possible.

I started this series writing in one Claude Code window at a time. Eight posts later I was running three or four in parallel through [git worktrees](/posts/2026-05-25-pick-a-framework-any-framework/), and the win was real. The orchestration overhead was real too. The next move was a chat interface.

## The chat metaphor

The chat metaphor is the right UI for managing multiple agents locally, because developers already know how to use chat with humans. `@mention` them, see their messages, ignore them when you are deep in something else, let them ping you when they get stuck or finish. The cognitive interface is already wired.

[agentchattr](https://github.com/bcurts/agentchattr) delivers this metaphor cleanly. Free, local, a chat server plus a web UI. Each agent auto-registers with its own identity, color, status pill, and `@mention` routing. Each agent runs inside its own tmux session, so the agent survives a closed laptop. You reattach with `tmux attach -t agentchattr-claude` when you want the full terminal view. Multiple providers can run in parallel, so the right tool fits the right task.

Honest mention of the neighbors. [multiagent-chat](https://github.com/estrada0521/multiagent-chat), [tmux-agents](https://github.com/super-agent-ai/tmux-agents), [agentic-tmux](https://github.com/negaga53/agentic-tmux), and [TMAI](https://github.com/trust-delta/tmai) all live in this space. agentchattr is the one this post is built around because the chat plus tmux plus web UI combination is the cleanest local fit today.

## The two-surface day

The chat is one surface. The vault is the other. Together they form the personal team room.

The blog already made the case for [Obsidian as shared context](/posts/2026-05-22-your-ai-context-belongs-to-the-team/). For the personal workflow, the vault carries a second role: the day's planning and decision log. A `daily/` folder, one note per day, named by date. The morning note holds the plan: today's intents, what each agent will work on, what success looks like. Decisions made in the chat get written back to the daily note as one-liners. The principles folder absorbs anything durable. The next morning's note starts by reading yesterday's.

The chat is volatile. The vault is durable. Without the vault, the agents do today's work and nothing about it survives to tomorrow.

## The daily loop

Concretely, what a day looks like with this setup.

1. **Morning, in the vault.** Open today's daily note. Write the day's intents in one paragraph. Decompose each into a spec or a clear ask. Decide which agent gets which.
2. **Open the chat.** Spawn one agent per ask. Each lands in its own tmux session and its own worktree. Brief them with the spec text from the vault.
3. **During the day.** Move between deep work and orchestration. The chat is where the agents talk to you and to each other. `@mention` to redirect. Let the others run.
4. **When an agent is stuck.** Pull up its tmux session for the full terminal context. Decide, type a one-line redirect, detach, move on.
5. **End of day, back in the vault.** Update the daily note with what shipped, what did not, the decisions that matter, the gotchas worth keeping.
6. **Tomorrow.** The next daily note reads from this one, the vault holds the principles updated mid-day, and the agents wake up to a context base that grew overnight.

This is the [spec-driven loop](/posts/2026-05-19-the-spec-driven-loop/) running in parallel, with the chat as the orchestration layer and the vault as the memory.

A decision written back to the daily note looks like one line: *"agent investigated the rate-limit issue, root cause was the missing TTL on the redis key, fix in PR #234, ship after the migration. See `principles/rate-limits.md` for the rule that came out of it."* That sentence is the day's memory. It is short, it is durable, the next morning's note reads it, and the principles folder grew by one.

There is a friction cost to this setup. Spawning four agents instead of one means four chances for one to wander. The vault is what catches the wandering, because the spec is in writing, but the cost is real. Two or three agents is the sweet spot until you trust the loop. Four is the limit before the orchestration overhead starts to bite again.

## Why the chat metaphor matters

Three reasons.

**Cognitive familiarity.** A developer with four agents in four terminal tabs is mentally tracking four threads. A developer with four agents in a chat is reading one stream. The chat collapses N contexts into one inbox. Same workload, less switching tax.

**Mention routing.** `@claude do X` is a verb developers already use. The tooling that makes that work is one of those small UI choices that disappears once you have it. The agent answers in line. The thread is the record.

**Status visibility.** Color, status pill, last-message timestamp tell you in one glance which agent is running, which is stuck, which is waiting on you. That is the dashboard you wanted instead of "ten tmux windows, which one was the one with the failure."

## What the chat does not do

Honest section. The chat is not a replacement for any of the work this blog has been arguing for.

- The chat is not a spec. You still write the brief in the vault first. The chat is where you hand it over.
- The chat is not memory. Conversations age out, agents reset. The vault is where things survive.
- The chat is not validation. Agents still produce drafts. You still review and decide. Same rule as every other post.
- The chat is not autonomy. Same operator-in-the-loop principle from [the ops post](/posts/2026-05-26-save-the-boring-time/). Agents propose, you decide.
- The chat is not a magic team. Four agents are four reports, not four teammates. Reports do not have the shared understanding teammates build over years. The vault closes some of that gap; nothing closes all of it.

The chat solves the orchestration problem. It does not solve the discipline problem.

## The role shift

A developer with one editor and one IDE is a solo coder. A developer with four agents in a chat is closer to a team lead with four reports. The tools should match that role. A chat-style inbox matches it. A daily note in a vault matches it. The terminal still exists for the deep work, but the day's center of gravity moves to "orchestrate and validate" rather than "type the next character."

That is the upgrade. The series has been building toward the developer doing more thinking and less typing. agentchattr plus Obsidian is what that day looks like at the local scale.

## Close

The framework picks the path. The foundation makes the path walkable. Worktrees let you walk many at once. The chat coordinates the walkers. The vault keeps each walk from starting from zero.

The cost of this setup is one afternoon. The cost of not having it shows up the third time you forget which tmux window had the failing test.
