# Fix the System, Not the Output — Design Spec

**Date:** 2026-05-31
**Status:** Draft, awaiting Elber's review.
**Author:** Session co-design (Elber Ribeiro + Claude).

## One-sentence pitch

An essay arguing that when an AI gets something wrong, correcting the output fixes today while correcting the system fixes every tomorrow, and that re-explaining context is not just slow but a goal-drift risk, so the move is to promote a repeated correction into a durable rule the agent reads back: a skill, a memory, or a project file.

## Framing decision

Behavioral angle, one level below the shared-context post. Post 5 (Your AI Context Belongs to the Team) already argued context should be written down and shared. This post does not restate that. It names the trigger (catching yourself correcting the same thing twice) and the action (capture it as an enforced rule, not a patched artifact). First-person architect voice. Day job stays anonymized; the receipt is the blog's own tooling, so no employer exposure. The post is self-referential on purpose: the lesson bit the author this week.

## Goals

- Land the thesis: **fix the system, not the output.** Correcting the artifact fixes one instance. Correcting the system makes the mistake unable to recur.
- Make the drift argument: re-explaining context is a correctness risk, not only a time cost. The second telling is never identical to the first, and the model builds to the drift. One written decision is one source of truth.
- Give the capture move a concrete home: a skill for a repeated procedure, a memory or vault entry for a durable cross-project decision, a CLAUDE.md / AGENTS.md rule for project-specific context. Named but portable.
- Ground it in a real receipt: this week, this blog. The publish flow ran the same way many times, then became a skill. A recurring cover-generation mistake became one rule the agent now follows.
- Stay honest: the author had to be reminded the tooling already existed, which is the post's own lesson in action.

## Non-goals (YAGNI)

- Restating post 5. Link it once, build past it, do not re-argue "write it down."
- A tooling tutorial. Name skills, memory, CLAUDE.md as examples; do not document how to author them.
- A vendor pitch. The principle is tool-agnostic; the names are illustrations.
- "Document everything." That is the failure mode post 5 already warned against (stale docs rot). This post is about durable, enforced rules, not a growing wiki.
- "Never correct the output." You still fix the artifact. The point is to then promote the fix.
- Naming the employer, a team, or a colleague.
- Affiliate links.

## The thesis

There are two ways to respond when an AI gets something wrong. Fix the output: edit the artifact until it is right. The artifact ships, the system that produced it is unchanged, and next week you make the same correction again. Fix the system: turn the correction into a rule the agent reads before it acts, so the mistake cannot happen a second time.

Most people fix the output every time. It feels productive, and it is the faster move in the moment. It is the slower move across the month, because the cost is paid on every repetition, forever.

## Repetition is drift, not just delay

Re-explaining the same context is usually framed as wasted time. The deeper cost is correctness. Every time you explain something again, you phrase it a little differently. The model does not see your intent. It sees the words, and it builds to the words it got this time. Two slightly different explanations produce two slightly different results, and the goal drifts a degree with each retelling.

A written decision removes the variance. There is one source of truth, phrased once, and every session reads the same thing. This is the spec-driven loop again: the spec exists so intent does not mutate between the idea and the code. The captured decision is the same move, applied to the corrections you make after the fact.

## The receipt

This week, on this blog. I publish a post the same way every time: spec, draft, cover, translate, verify, ship. For a long stretch I re-explained that flow to a fresh session on every post. Then I stopped fixing the output and fixed the system. The flow is now a skill the agent loads when I start a post.

A sharper one: cover-image generation kept going wrong the same way, a downloaded error page saved as an image. I fixed that output more than once before I made it a rule. Now it is one line the agent follows, and the mistake is gone.

The honest part. Earlier in the same week I rebuilt a piece of tooling that already existed, because I had not captured where it lived. The lesson bit me before I wrote it down. That is the whole point. The second time is a bug, and I shipped that bug myself.

## Where the decision lives

Three homes, one rule each. The choice is about scope, not preference.

- **A skill,** for a repeated procedure. When the thing you keep re-explaining is *how to do X*, write it as an instruction the agent runs, not a paragraph it might read. Executable beats passive.
- **A memory or a vault note,** for a durable decision that outlives one project. The preference, the why behind a past call, the dead end you already walked. Cross-project knowledge belongs somewhere every project can reach.
- **A CLAUDE.md or AGENTS.md file,** for project-specific context. The conventions, the gotchas, the rules this one repo needs. It loads every session, so the agent starts informed instead of guessing.

The names are mine. The principle is not tied to them. Any agent setup has the same three shapes: a procedure, a durable fact, a project rule. Put the decision in the one that matches its scope.

## What this is not

- Not "document everything." A wiki nobody reads is the failure mode, not the goal. Capture durable, enforced rules, and prune the ones that go stale. A stale rule costs more than a missing one.
- Not "never correct the output." You still fix the artifact in front of you. Then you ask whether you will fix it again, and if the answer is yes, you promote it.
- Not automating judgment. Deciding what is worth capturing is yours. The agent does not know which corrections are one-offs and which are rules.

## Series callbacks

- **Post 5, Your AI Context Belongs to the Team.** That post said the context you build is a team asset; write it down and share it. This post is the trigger and the action beneath it: the moment you notice the repetition, and the move that ends it.
- **Post 2, The Spec-Driven Loop.** The spec keeps intent from drifting before the code. The captured decision keeps it from drifting after the correction. Same physics, later in the cycle.
- **The foundation theme.** Specs, shared context, observability were foundations for using AI. Capturing your corrections is how those foundations stop eroding.

## Proposed structure

1. **Hook.** The same correction, typed a third time. The moment you realize you are the one repeating yourself.
2. **Two ways to fix.** Output versus system. One fixes today, one fixes every tomorrow.
3. **Repetition is drift.** The correctness cost, not just the time cost. One written decision, one source of truth. Tie to the spec-driven loop.
4. **The receipt.** The blog's own skill and cover-rule, including the honest part where the lesson bit the author.
5. **Where the decision lives.** Skill, memory, project file. One rule each. Named but portable.
6. **What this is not.** Three honest bullets.
7. **Close.** The work is not the correction. The work is making it once.

Target length: 800 to 1000 words.

## Working title

**"Fix the System, Not the Output"** (approved)

Subtitle (draft): *Correcting what the AI produced fixes today. Correcting how it works fixes every tomorrow. Re-explaining context is not just slow, it lets the goal drift. Capture the decision once.*

## Links

External: none required.

Internal:
- Your AI context belongs to the team, `/posts/2026-05-22-your-ai-context-belongs-to-the-team/`
- The spec-driven loop, `/posts/2026-05-19-the-spec-driven-loop/`

## Cover image plan

Same FLUX pipeline and dark amber-and-teal palette as the series. Concept: a single chisel cutting one deep clean groove into dark stone, the cut groove glowing warm honey-amber from within, with faint shallow repeated scratch-marks beside it in cooler teal that did not hold. Painterly, soft bloom, brushstroke texture. No text. Conveys "carve it once" versus scratching the same line over and over.

## Open questions for Elber

- The honest "the lesson bit me this week" beat: keep it in, or does it undercut the argument? Recommendation: keep it. The blog's brand is honesty, and a confession hook earns more trust than a clean win.
- Three homes (skill / memory / project file) or two (executable / written)? Recommendation: three. It matches how you actually work and the scope distinction is the useful part.
- Name the toolchain (skill, CLAUDE.md, AGENTS.md) or stay abstract? Recommendation: name them as examples, frame the principle as portable. Decided in brainstorming.

## Decisions

- **Fix-the-system angle**, distinct from post 5 by being the trigger-and-action one level down.
- **Drift as the deeper cost**, not just wasted time.
- **Real receipt** from the blog's own tooling this week, including the honest miss.
- **Three homes** for a captured decision, named but portable.
- **No affiliate links. Cover generated, not commissioned.**
- **Day job anonymized.** No employer, team, or colleague named.

## Sequencing

Latest post in the build-with-AI arc, after the foundations post (`2026-05-30-dont-just-use-the-model`). Same flow: spec, draft to review, cover once approved, publish EN + PT-BR together, update the vault catalog, then LinkedIn.
