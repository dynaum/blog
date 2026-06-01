---
title: "Fix the System, Not the Output"
subtitle: "Correcting what the AI produced fixes today. Correcting how it works fixes every tomorrow. Re-explaining context is not just slow, it lets the goal drift. Capture the decision once."
date: 2026-05-31
description: "When an AI gets something wrong, fixing the output fixes one instance and fixing the system fixes every future one. Why re-explaining context drifts the goal, and the three homes for a captured decision: a skill, a memory, a project file."
cover: /assets/img/2026-05-31-fix-the-system-not-the-output.png
coverAlt: "A single chisel cutting one deep clean groove into dark stone, the cut glowing warm amber from within, with faint shallow repeated scratch-marks beside it in cooler teal that did not hold."
---

I caught myself typing the same correction for the third time. Same note to the model, same fix to the same kind of mistake, a different day. The third time is the one that stings, because by then it is not the model repeating itself. It is me.

There are two ways to respond when an AI gets something wrong. You can fix the output. You can fix the system.

Fixing the output means editing the artifact until it is right. The pull request is correct, the doc reads well, the bug is gone. You ship it. The thing that produced it is exactly as it was, so next week the same mistake arrives and you make the same correction again. Fixing the system means turning that correction into a rule the model reads before it acts, so the mistake cannot happen a second time.

Most of us fix the output every time. It feels productive. In the moment it is the faster move. Across the month it is the slower one, because you pay the cost on every repetition, and the repetitions do not stop on their own.

## Repetition is drift, not just delay

The usual complaint about re-explaining context is that it wastes time. The deeper cost is correctness.

Every time you explain something again, you phrase it a little differently. The model does not see your intent. It sees the words it got this time, and it builds to those words. Two slightly different explanations produce two slightly different results. The goal drifts a degree with every retelling, and you do not notice until the output is a few degrees off from where you started and you cannot point to the moment it bent.

A written decision removes the variance. One source of truth, phrased once, read the same way by every session. This is the spec-driven loop pointed at a later part of the cycle. The [spec](/posts/2026-05-19-the-spec-driven-loop/) exists so intent does not mutate between the idea and the code. The captured decision exists so intent does not mutate between the correction and the next time the work comes around.

## The receipt

This week, on this blog. I publish a post the same way every time. Spec, draft, cover, translate, verify, ship. For a long stretch I re-explained that flow to a fresh session on every single post. Then I stopped fixing the output and fixed the system. The flow is a skill now. The model loads it when I start a post, and I do not narrate the steps anymore.

A sharper one. Generating the cover image kept failing the same way, a downloaded error page saved as if it were a picture. I fixed that output more than once before I made it a rule. Now it is one line the model follows, and the failure is gone.

The honest part. Earlier the same week I rebuilt a piece of tooling that already existed, because I had never written down where it lived. I re-explained the goal, the model built something new, and it duplicated work that was already sitting in the repo. The lesson bit me before I finished writing it down. That is the whole argument in one bruise. The second time is a bug, and I shipped that bug myself.

## Where the decision lives

Once you decide to capture a correction, it needs a home. There are three, and the choice is about scope, not taste.

A **skill**, for a repeated procedure. When the thing you keep re-explaining is how to do something, write it as an instruction the model runs, not a paragraph it might read. Executable beats passive. A doc can be skipped. A skill is the step.

A **memory or a vault note**, for a durable decision that outlives one project. The preference, the reason behind a past call, the dead end you already walked so you do not walk it twice. Cross-project knowledge belongs somewhere every project can reach, not buried in one repo.

A **CLAUDE.md or AGENTS.md file**, for project-specific context. The conventions, the gotchas, the rules this one codebase needs. It loads every session, so the model starts informed instead of guessing and drifting.

The names are mine and the tools will change. The shapes will not. Every agent setup has the same three: a procedure, a durable fact, a project rule. Put the decision in the one that matches its scope, and it stops being something you say and starts being something the system knows.

## What this is not

- Not "document everything." A wiki nobody reads is the failure mode, not the goal. Capture durable rules, and prune the ones that go stale. A stale rule costs more than a missing one, because it lies with authority.
- Not "never correct the output." You still fix the artifact in front of you. Then you ask one question. Will I fix this again? If the answer is yes, you promote it.
- Not automating judgment. Deciding what is worth capturing is your job. The model cannot tell a one-off from a rule. You can.

## Close

The work was never the correction. Anyone can fix the output, and the model will happily accept the fix and forget it by the next session. The work is making the correction once, in a place that holds, so the next session starts where this one ended instead of where the last ten did.

Fix the output and you have a better artifact. Fix the system and you have a better system. Only one of them compounds.
