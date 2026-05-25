---
title: "Pick a Framework, Any Framework"
subtitle: "AI-DLC is one option, not the option. Four methodologies in 2026, the foundation they all share, and the worktrees-and-orchestration upgrade that scales any of them."
date: 2026-05-25
description: "A survey of four AI-development methodologies in 2026 (AI-DLC, Superpowers, Spec-Kit, PRPs), the three foundations they all share, and the git worktrees plus Claude Code Agent Teams plus Beads stack that scales them."
cover: /assets/img/2026-05-25-pick-a-framework-any-framework.png
coverAlt: "A dark stone wall at night with four different archways and doorways in a row, each a different shape, all opening onto warmly lit space beyond. Many paths, same destination."
---

I have been the loud advocate for one framework for a while now. Spending real time with the others taught me two things. The framework matters less than I thought. And the upgrade I was missing was not in the framework at all, it was in parallelizing the work once the foundation was in place.

The four frameworks below differ in vocabulary, surface area, and tooling depth. They converge on the same three moves:

1. **Describe the problem well.** A user, a pain, a why.
2. **Write a spec.** Pitch, non-goals, success criteria, decision log.
3. **Break the work into steps.** Ordered, testable, small enough that a single agent run finishes one.

Teams that do those three things get value from any of the frameworks. Teams that skip them get a faster mess from all of them.

What actually matters is following the process. The frameworks help because they **force** the process. Like [Docker](https://www.docker.com) forces you to use environment variables instead of hardcoded config, these frameworks force you to write specs, name non-goals, and order steps before code. Without one, the discipline is optional. Optional discipline rots. That is why people who say "I do not need a framework" still benefit from picking one, even casually, because the framework holds the line on days you would not.

## The four

**[AWS AI-DLC](https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/).** The institutional version. Inception then Construction then Operations. Sprints become **bolts**. **Steering files** constrain the agent. [Open-source workflows](https://github.com/awslabs/aidlc-workflows) on GitHub. Best fit when the org already lives on AWS, already runs Kubernetes, and is ready to standardize an entire engineering function on one approach. The [AI-DLC adoption post](/posts/2026-05-21-you-cannot-push-a-developer/) made the case for it. This post puts it back in context as one option, not the option.

**[Anthropic Superpowers](https://github.com/obra/superpowers).** [Jesse Vincent's](https://github.com/obra) open framework, shipped as fourteen `SKILL.md` files and a session hook. The workflow is the same shape this blog has been writing about: brainstorm, spec, plan, TDD, subagent development, review, finalize. Works across [Claude Code](https://claude.com/claude-code), [Cursor](https://cursor.com), [OpenAI Codex](https://github.com/openai/codex), [Copilot CLI](https://github.com/github/gh-copilot), [Gemini CLI](https://github.com/google-gemini/gemini-cli), and [OpenCode](https://opencode.ai). [Anthropic marketplace plugin](https://claude.com/plugins/superpowers). Around 170k GitHub stars by mid-2026. Best fit when you want strong opinionated defaults you can read in plain Markdown and tweak per-project.

**[GitHub Spec-Kit](https://github.com/github/spec-kit).** Agent-agnostic open-source toolkit. A clean four-phase workflow: spec, plan, tasks, code. Works across 30+ AI coding agents. Best fit when the team is already in the GitHub ecosystem and wants minimal new infrastructure, a CLI to drop into any repo.

**[Product Requirements Prompts](https://github.com/coleam00/context-engineering-intro)** (PRPs, the context-engineering pattern). Not a full framework, a discipline. A PRP is a prompt engineered for AI consumption, not a PRD written for humans. It bundles file paths, library versions, code examples, validation gates, and a confidence score with the intent. Best fit when you do not want a new methodology to adopt, only a sharper way to write the prompts you already write. Pairs with any of the above.

## Same physics, different vocabulary

| | "describe the problem" | "spec" | "steps" |
|---|---|---|---|
| **AI-DLC** | Inception | Inception artifacts + steering files | Bolts |
| **Superpowers** | Brainstorm | Spec | Plan + TDD + Subagent |
| **Spec-Kit** | Spec | Plan | Tasks |
| **PRPs** | Goal + justification | The PRP itself | Validation gates |

Same load-bearing moves under all four. Pick the vocabulary your team already speaks.

## Why now

Not as a sales pitch, as an observation.

The four are open-source, maintained, and have communities loud enough to find help in. The cost of an experiment is one branch and one afternoon. Tooling has converged on Markdown specs, agent-agnostic interfaces, working across IDEs. A failed experiment costs an hour. A working one changes how the team ships.

This is the curve where you stop watching and start shipping.

## Scaling the work

A framework shows you the path. Walking it once is one developer's pace. Walking it many times at once is where the real change shows up. Three layers, bottom-up.

**Git worktrees, the primitive.** A [git worktree](https://code.claude.com/docs/en/worktrees) gives each agent its own working directory on the same repo. Multiple branches, one git history, zero file collisions. Claude Code has native `--worktree` (`-w`) support that creates the worktree, branches, and starts a session in one step. The pattern is: spec the feature, decompose into steps, spawn one worktree per step, review the diffs in order, merge.

The foundation is what makes this safe. Bad spec, parallel agents writing conflicting interpretations. Good spec, parallel agents finishing in an afternoon.

**Claude Code Agent Teams, the coordination.** Worktrees give isolation. [Agent Teams](https://code.claude.com/docs/en/agent-teams) adds coordination. One Claude Code session acts as the team lead. Others act as teammates, each in its own context window and worktree, communicating directly. Experimental, enabled by setting `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` in `settings.json` or the environment. Anthropic's first-party answer to multi-agent orchestration, sitting naturally on top of worktrees.

Third-party orchestration UIs cover the same ground if you prefer a dashboard or a TUI. [Conductor](https://conductor.build) by Melty Labs wraps the worktree-per-agent pattern with a dashboard. [Claude Squad](https://github.com/smtg-ai/claude-squad) wraps it in a tmux TUI and supports [Codex](https://github.com/openai/codex), [Aider](https://aider.chat), and [Gemini](https://github.com/google-gemini/gemini-cli) alongside Claude. Pick the surface area that fits the team.

**Beads, the memory.** Long parallel runs hit a different ceiling. Each agent wakes up with no memory of yesterday's work. [Beads](https://github.com/steveyegge/beads) by [Steve Yegge](https://steve-yegge.medium.com/introducing-beads-a-coding-agent-memory-system-637d7d92514a) is a git-native, SQLite-backed issue tracker built specifically as memory for coding agents. Hash-based IDs prevent merge collisions across branches. Semantic decay summarizes old work to save context. Dependency links between tasks survive across sessions. Beads is not a framework, it is the memory component that pairs with any of them.

The stack reads bottom-up: foundation, framework, worktrees, coordination, memory. Each layer assumes the one below it.

## Close

Pick the framework whose vocabulary your team already speaks. Do the three foundations. Then parallelize.

The framework shows you the path. The foundation is what makes the path walkable. Worktrees let you walk it many times at once. Coordination keeps the walkers from stepping on each other. Memory keeps each walk from starting from zero.

You do not need all of this on day one. Pick one foundation move you skip today and add it tomorrow. Pick one framework and try it on a real feature this week. The next move opens itself.
