# Many Agents, One Chat — Design Spec

**Date:** 2026-05-27
**Status:** Draft, awaiting Elber's review.
**Author:** Session co-design (Elber Ribeiro + Claude).

## One-sentence pitch

A field-note post about scaling the local developer setup with [agentchattr](https://github.com/bcurts/agentchattr), a chat interface where multiple AI agents (each in its own tmux session and worktree) become @mentionable teammates, paired with Obsidian as the day's planning and decision log so the chat is the in-the-moment work and the vault is the persistent memory.

## Framing decision

Personal-developer focus, not org-level. No team or colleague named. Light self-cast: "I started with one Claude Code window. The local scaling problem (multiple agents, multiple branches, mental overhead) led me here." The "regulated domain" line is dropped this post; this is a tooling-and-workflow piece, not an ops or adoption argument.

## Goals

- Show that the **chat metaphor is the right UI** for managing multiple agents locally, because developers already know how to use chat with humans.
- Recommend [agentchattr](https://github.com/bcurts/agentchattr) by name as the concrete tool the post is built around. Honest mentions of the alternatives.
- Show the **two-surface daily loop**: chat for the in-the-moment work, Obsidian for the day's plan and the decisions worth keeping.
- Tie back to the series: same foundation (specs, shared context), same divide of labor, same parallelization (worktrees, per-agent isolation), same honest "validate the plan" rule.
- Close on the role shift: a developer with multiple agents is closer to a team lead than to a solo coder, and the tools should match that role.

## Non-goals (YAGNI)

- An agentchattr installation tutorial. Pointers, not configs.
- An Obsidian onboarding guide. Reference post 5.
- A multi-agent-orchestrator shootout. agentchattr is the local-developer flavor; the team flavor (Claude Code Agent Teams, Conductor, Claude Squad) was post 8.
- Naming the employer, a team, or a colleague.
- "AI replaces the developer" arguments. The opposite is the point.
- Affiliate links.

## The thesis

Once you are running more than one agent at a time, the bottleneck stops being the agent and starts being **you**, the orchestrator. Switching between four terminal panes, four worktrees, and four mental contexts is the new tax. The chat metaphor pays it off, because the cognitive interface developers already have for "people in a chat" maps onto agents naturally. @mention them, see their messages, see their status, ignore them when you are deep in something else, let them ping you when they are stuck or done.

[agentchattr](https://github.com/bcurts/agentchattr) is the concrete tool that delivers this metaphor cleanly: free, local, a chat server plus a web UI, each agent auto-registering with its own identity, color, status pill, and @mention routing. Each agent runs inside its own tmux session, so it survives a closed laptop; you reattach with `tmux attach -t agentchattr-claude` when you want the terminal view. Multiple providers (Claude, Gemini, others) can run in parallel, so the right tool fits the right task.

Honest mention of the neighbors: [multiagent-chat](https://github.com/estrada0521/multiagent-chat), [tmux-agents](https://github.com/super-agent-ai/tmux-agents), and [agentic-tmux](https://github.com/negaga53/agentic-tmux) all live in this space. agentchattr is the one this post is built around because the chat + tmux + web UI combination is the cleanest local fit today.

## The two-surface day

The chat is one surface. The vault is the other. Together they form the personal team room.

### Obsidian as the day's planning and decision log

The blog already made the case for [Obsidian as shared context](/posts/2026-05-22-your-ai-context-belongs-to-the-team/). For the personal workflow, the vault carries a second role: **the day's planning and decision log**. The shape that works:

- A `daily/` folder, one note per day, named by date.
- The morning note holds the plan: today's intents, what each agent will work on, what success looks like.
- During the day, the chat happens in agentchattr. Decisions made there get written back to the daily note as one-liners.
- The principles folder absorbs anything durable. The per-project folders absorb anything project-specific.
- The next morning's note starts by reading yesterday's.

The chat is volatile. The vault is durable. Without the vault the agents do today's work and nothing about it survives to tomorrow.

## The daily loop

Concretely, what a day looks like with this setup:

1. **Morning, in the vault.** Open today's daily note. Write the day's intents in one paragraph. Decompose each into a spec or a clear ask. Decide which agent gets which.
2. **Open the chat.** Spawn one agent per ask. Each lands in its own tmux session and its own worktree. Brief them with the spec text from the vault (paste or link to the vault file the agent can read).
3. **During the day.** Move between deep work and orchestration. The chat is where the agents talk to you and to each other. @mention to redirect. Let the others run.
4. **When an agent is stuck.** Pull up its tmux session for the full terminal context. Decide, type a one-line redirect, detach, move on.
5. **End of day, back in the vault.** Update the daily note with what shipped, what did not, the decisions that matter, the gotchas worth keeping.
6. **Tomorrow.** The next daily note reads from this one, the vault holds the principles updated mid-day, and the agents wake up to a context base that grew overnight.

This is the [spec-driven loop](/posts/2026-05-19-the-spec-driven-loop/) running in parallel, with the chat as the orchestration layer and the vault as the memory.

## Why the chat metaphor matters

Three reasons.

**Cognitive familiarity.** A developer with four agents in four terminal tabs is mentally tracking four threads. A developer with four agents in a chat is reading one stream. The chat collapses N contexts into one inbox. Same workload, less switching tax.

**Mention routing.** `@claude do X` is a verb developers already use. The tooling that makes that work is one of those small UI choices that disappears once you have it. The agent answers in line. The thread is the record.

**Status visibility.** Color + status pill + last-message timestamp tells you in one glance which agent is running, which is stuck, which is waiting on you. That is the dashboard you actually wanted instead of "ten tmux windows, which one was the one with the failure."

## What the chat does not do

Honest section. The chat is not a replacement for any of the work this blog has been arguing for.

- The chat is not a spec. You still write the brief in the vault first; the chat is where you hand it over.
- The chat is not memory. Conversations age out, agents reset. The vault is where things survive.
- The chat is not validation. Agents still produce drafts; you still review and decide. Same rule as every other post.
- The chat is not autonomy. Same operator-in-the-loop principle from [the ops post](/posts/2026-05-26-save-the-boring-time/). Agents propose, you decide.

The chat solves the orchestration problem. It does not solve the discipline problem.

## The role shift

A developer with one editor and one IDE is a solo coder. A developer with four agents in a chat is closer to a team lead with four reports. The tools should match that role. A chat-style inbox matches it. A daily note in a vault matches it. The terminal still exists for the deep work, but the day's center of gravity moves to "orchestrate and validate" rather than "type the next character."

That is the upgrade. The series has been building toward the developer doing more thinking and less typing. agentchattr plus Obsidian is what that day looks like at the local scale.

## Proposed structure

1. **Hook.** Once you are running more than one agent, the bottleneck stops being the agent and starts being you.
2. **Thesis.** The chat metaphor pays off the orchestration tax. agentchattr is the cleanest local fit today.
3. **The two-surface day.** Chat for in-the-moment work, Obsidian for the day's plan and decisions.
4. **The daily loop.** Six concrete steps, morning to morning.
5. **Why the chat metaphor matters.** Cognitive familiarity, mention routing, status visibility.
6. **What the chat does not do.** Honest section. Not a spec, not memory, not validation, not autonomy.
7. **The role shift.** Solo coder to team lead, locally.
8. **Close.** Series tie-back: same foundation, same divide of labor, new orchestration layer.

Target length: 900 to 1100 words.

## Working title

**"Many Agents, One Chat"**

Subtitle: *Once you run more than one agent locally, you become the bottleneck. A chat interface plus a vault is the upgrade. Why agentchattr and Obsidian pair so well for the personal scaling problem.*

Alternative titles:
- "A Chat Room for Your Agents"
- "Scaling the Local Setup"
- "Your Personal Agent Team Room"
- "The Day in Two Surfaces"

## Links

- [agentchattr](https://github.com/bcurts/agentchattr)
- Honorable mentions: [multiagent-chat](https://github.com/estrada0521/multiagent-chat), [tmux-agents](https://github.com/super-agent-ai/tmux-agents), [agentic-tmux](https://github.com/negaga53/agentic-tmux), [TMAI](https://github.com/trust-delta/tmai)
- [Obsidian](https://obsidian.md/)
- Internal: spec-driven loop, `/posts/2026-05-19-the-spec-driven-loop/`
- Internal: shared context, `/posts/2026-05-22-your-ai-context-belongs-to-the-team/`
- Internal: pick a framework + worktrees scaling, `/posts/2026-05-25-pick-a-framework-any-framework/`
- Internal: save the boring time, `/posts/2026-05-26-save-the-boring-time/`

## Cover image plan

Same FLUX pipeline and dark amber-and-teal palette as posts two through nine. Concept: a dark desk at night, a single open notebook in the foreground (the vault), and around it several small glowing terminal panes arranged like floating windows, each showing a different colored status pill (the agents in the chat). A warm amber lantern beside the notebook ties the scene together: one watcher, one notebook, many agents. Painterly. No text in the image.

## Open questions for Elber

- Self-cast as "the developer who graduated from one Claude Code window to a multi-agent chat" — accurate? Recommendation: yes.
- Honorable mention list for the neighbors (multiagent-chat, tmux-agents, agentic-tmux, TMAI) — keep all four named, or just two? Recommendation: keep all four; they are real and credible alternatives.
- The "daily loop" six-step section — keep at six steps or compress to four? Recommendation: keep at six, each step is short and the morning-to-morning loop reads better complete.
- Any specific Obsidian plugin (Periodic Notes, Dataview) worth naming, or stay tool-pure? Recommendation: stay tool-pure. Obsidian works without plugins for this; the plugins are an upgrade, not a requirement.

## Decisions

- **Personal-developer focus.** No employer angle.
- **agentchattr named as the primary tool**, with four honorable mentions.
- **Obsidian named** as the vault tool, consistent with post 5.
- **The chat is for orchestration, the vault is for memory.** Both required.
- **The role shift is the close.** Solo coder to team lead is the thesis underneath the tooling.
- **No affiliate links.**
- **Cover generated, not commissioned.** Consistent with the series.

## Sequencing

Post ten in the build-with-AI arc. Publish after Elber reviews this spec and answers the open questions. Same flow as before: spec, draft to iCloud, review, cover, publish EN + PT-BR together per the playbook, then LinkedIn.
