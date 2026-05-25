# Many Frameworks, One Foundation — Design Spec

**Date:** 2026-05-25
**Status:** Draft, awaiting Elber's review.
**Author:** Session co-design (Elber Ribeiro + Claude).

## One-sentence pitch

A field-note post surveying four viable AI-development methodologies in 2026 (AI-DLC, Anthropic Superpowers, GitHub Spec-Kit, and Product Requirements Prompts), arguing the framework matters less than the foundation under it, and that the real upgrade is parallelizing the work once the foundation is in place using git worktrees and orchestration on top.

## Framing decision

Employer-neutral, general advice. The post is a methodology survey + a scaling argument, not a personal story about adoption. Self-cast is gentler: "I have been the loud advocate for one framework. Spending real time with the others taught me the foundation does the work, and worktrees do the scaling."

## Goals

- Show that **AI-DLC is one option, not the option.** Survey four credible frameworks.
- Land the thesis: **the framework matters less than the foundation under it.** Three foundations: problem described well, specs written, work broken into steps.
- Make the case that **this is the moment to try.** Tools are mature, communities are loud, errors are cheap, the methodologies are converging on the same shape.
- **Frameworks show you the path, parallelization lets you walk many at once.** Make the scaling section the climax: git worktrees as the primitive, Claude Code Agent Teams as the coordination layer, Beads as memory across long runs.
- Close the series arc: posts 2 through 7 built the foundation. This post says any of these frameworks works on top of it, and parallelization is the scaling move once the foundation is solid.

## Non-goals (YAGNI)

- A feature-by-feature shootout. The point is the frameworks share the load-bearing shape, not which one wins.
- A "best for which team" grid. Honest answer: pick the one whose vocabulary your team already speaks.
- A git worktree tutorial. Pointers, the flag, the pattern, not a step-by-step.
- An exhaustive tool catalog. Tools are not methodologies.
- Naming the employer, a team, or a colleague.
- Marketing language. No "revolutionary", no "supercharge", no "10x".
- Affiliate links.

## The thesis

The four frameworks below differ in vocabulary, tooling depth, and surface area. They all converge on the same three load-bearing moves:

1. **Describe the problem well.** A user, a pain, a why.
2. **Write specs.** Pitch, non-goals, success criteria, decision log.
3. **Break the work into steps.** Ordered, testable, small enough that a single agent run can finish one.

A team that does these three things gets value from any of the frameworks. A team that skips them gets a faster mess from all of them.

## The four frameworks (tight take, one paragraph each)

**[AWS AI-DLC](https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/).** The institutional version. Inception → Construction → Operations, "bolts" instead of sprints, **steering files** constrain the agent, [open-source workflows on GitHub](https://github.com/awslabs/aidlc-workflows). Best fit when the org already lives on AWS, already uses Kubernetes, and is ready to standardize an entire engineering function on one approach.

**[Anthropic Superpowers](https://github.com/obra/superpowers).** Jesse Vincent's open framework, shipped as fourteen `SKILL.md` files and a session hook. The workflow is the same shape we have been writing about: Brainstorm → Spec → Plan → TDD → Subagent Development → Review → Finalize. Works across Claude Code, Cursor, Codex, Copilot CLI, Gemini CLI, OpenCode. Anthropic marketplace plugin. ~170k GitHub stars by mid-2026. Best fit when you want strong, opinionated defaults you can read in plain Markdown and tweak per-project.

**[GitHub Spec-Kit](https://github.com/github/spec-kit).** Agent-agnostic open-source toolkit. A clean four-phase workflow: Spec → Plan → Tasks → Code. Works across 30+ AI coding agents. Best fit when the team is already in the GitHub ecosystem and wants minimal new infrastructure: a CLI you can drop into any repo.

**[Product Requirements Prompts](https://github.com/coleam00/context-engineering-intro)** (PRPs, the context-engineering pattern). Not a full framework, a discipline. A PRP is a prompt engineered for AI consumption, not a PRD written for humans. It bundles file paths, library versions, code examples, validation gates, and a confidence score with the intent. Best fit when you do not want a new methodology to adopt, just a sharper way to write the prompts you already write. Pairs with any of the above.

## The pattern under all four (comparison table)

| | What it calls "describe the problem" | What it calls "spec" | What it calls "steps" |
|---|---|---|---|
| **AI-DLC** | Inception | Inception artifacts + steering files | Bolts |
| **Superpowers** | Brainstorm | Spec | Plan + TDD + Subagent |
| **Spec-Kit** | Spec | Plan | Tasks |
| **PRPs** | Goal + justification | The PRP itself | Validation gates |

Same physics, different vocabularies. Pick the vocabulary your team already speaks.

## The "best moment to try" argument

Not as a sales pitch, as an observation:

- The four frameworks above are all open-source, all maintained, all have communities loud enough to find help in.
- The cost of an experiment is the cost of one branch and one afternoon.
- Tooling has converged: Markdown specs, agent-agnostic, work across IDEs.
- A failed experiment costs you the hour. A working one changes how the team ships.

This is the curve where you stop watching and start shipping.

## Scaling the work (the climax of the post)

A framework shows you the path. Walking it once is one developer's pace. Walking it many times at once is where the real change shows up. Three layers, in order from foundation to coordination.

### 1. Git worktrees (the primitive)

[Git worktrees](https://code.claude.com/docs/en/worktrees) give each agent its own working directory on the same repo. Multiple branches, same git history, zero file collisions. Claude Code has native `--worktree` (`-w`) support that creates the worktree, branches, and starts a session in one step.

The pattern is: spec the feature, decompose into steps, spawn one worktree per step, review the diffs in order, merge.

The foundation is what makes this safe. Bad spec, parallel agents writing conflicting interpretations. Good spec, parallel agents finishing in an afternoon.

### 2. Claude Code Agent Teams (the coordination layer)

Worktrees give isolation. **[Agent Teams](https://code.claude.com/docs/en/agent-teams)** adds coordination: one Claude Code session acts as the team lead, others act as teammates, each in its own context window and worktree, communicating directly. Experimental, enable with `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` in `settings.json` or env. This is Anthropic's first-party answer to multi-agent orchestration, and it sits naturally on top of worktrees.

Third-party orchestration UIs cover the same ground: **[Conductor](https://conductor.build)** by Melty Labs ships a dashboard over multiple agents in worktrees, **[Claude Squad](https://github.com/smtg-ai/claude-squad)** wraps the same pattern in a tmux TUI and supports Codex / Aider / Gemini in addition to Claude. Pick the surface area that fits the team.

### 3. Beads (memory across runs)

Long parallel runs hit a different ceiling: each agent wakes up with no memory of yesterday's work. **[Beads](https://github.com/steveyegge/beads)** by Steve Yegge is a Git-native, SQLite-backed issue tracker built specifically as memory for coding agents. Hash-based IDs prevent merge collisions across branches, semantic decay summarizes old work to save context, dependency links between tasks survive across sessions. Beads is not a framework, it is the memory component that pairs with any of them. The user [raised this distinction](https://github.com/steveyegge/beads) and it is the right one.

The stack reads bottom-up: foundation → framework → parallelization → coordination → memory.

## Proposed structure

1. **Hook.** I have been the loud advocate for one framework. Spending time with the others taught me the foundation does the work, and worktrees do the scaling.
2. **The thesis.** Three foundations, any framework. Skip the foundations and every framework underperforms.
3. **The four.** One paragraph each.
4. **The comparison table.** Same physics, different vocabularies.
5. **The "now" argument.** Why this is the moment.
6. **Scaling the work.** Worktrees → Agent Teams → Beads. The post's climax.
7. **Close.** Pick the framework whose vocabulary your team already speaks. Do the three foundations. Then parallelize.

Target length: 1000 to 1200 words. Longer than the average essay because the scaling section is now substantial, by design.

## Working title

**"Pick a Framework, Any Framework"**

Subtitle: *AI-DLC is one option, not the option. Four methodologies in 2026, the foundation they all share, and the worktrees-and-orchestration upgrade that scales any of them.*

Alternative titles:
- "Foundation Over Framework"
- "Many Paths, Same Foundation"
- "The Framework Shows the Path. Worktrees Walk It Many Times."
- "Try Any of Them, Then Parallelize"

## Links

- AWS AI-DLC: https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/
- AI-DLC workflows repo: https://github.com/awslabs/aidlc-workflows
- Superpowers (obra/superpowers): https://github.com/obra/superpowers
- Superpowers on Claude marketplace: https://claude.com/plugins/superpowers
- GitHub Spec-Kit: https://github.com/github/spec-kit
- Context Engineering / PRPs: https://github.com/coleam00/context-engineering-intro
- Claude Code worktrees: https://code.claude.com/docs/en/worktrees
- Claude Code Agent Teams: https://code.claude.com/docs/en/agent-teams
- Conductor (Melty): https://conductor.build
- Claude Squad: https://github.com/smtg-ai/claude-squad
- Beads (Steve Yegge): https://github.com/steveyegge/beads
- Internal: AI-DLC adoption post, `/posts/2026-05-21-you-cannot-push-a-developer/`
- Internal: spec-driven loop post, `/posts/2026-05-19-the-spec-driven-loop/`
- Internal: shared context post, `/posts/2026-05-22-your-ai-context-belongs-to-the-team/`
- Internal: product context post, `/posts/2026-05-24-context-is-not-a-dev-job/`

## Cover image plan

Same FLUX pipeline and dark amber-and-teal palette as the rest of the series. Concept: several different stone doorways and arches in a row, each a different shape and material, all opening onto the same warmly lit corridor beyond. Many paths, same destination. Painterly. No text in the image.

## Resolved questions (Elber's answers on 2026-05-25)

- BMAD-METHOD was wrong (mis-heard from "beads"). Beads is a memory component, not a methodology. Replaced with: a fourth framework slot for PRPs, plus Beads slotted into the Scaling section in its actual role.
- **Comparison shown as a table**, not prose.
- **Scaling/worktrees is the climax of the post**, not a short coda. Frameworks show the path; worktrees and orchestration let you walk many at once.
- **Another recommendation:** Claude Code Agent Teams (first-party Anthropic, sits on top of worktrees), with Conductor and Claude Squad as third-party orchestration alternatives, and Beads as the memory layer across long parallel runs.

## Decisions

- **Four frameworks** (AI-DLC, Superpowers, Spec-Kit, PRPs). BMAD dropped. Beads moved to the Scaling section as a memory component, not a methodology.
- **Employer-neutral.** No team or colleague named.
- **Thesis first, frameworks second, scaling as the climax.**
- **"Now" framed as observation, not sales.** No hype words.
- **Comparison table, not prose.**
- **Cover generated, not commissioned.** Consistent with posts two through seven.
- **No affiliate links.**

## Sequencing

Post eight in the build-with-AI arc, after the product-context post. Publish after Elber reviews this revised spec. Same flow as before: spec, draft to iCloud, review, cover, publish EN + PT-BR together per the playbook, then LinkedIn.
