---
title: "Did It Actually Work?"
subtitle: "Working with AI assumes output you can trust. This post measures it. Velocity is a vanity metric now. Trust is the number that survives, and three health metrics tell you whether the loop is working."
date: 2026-05-29
description: "Velocity is the wrong metric in the AI era. Trust is the right one. Why reviewing AI-generated code is a discipline, the three health metrics that tell you the loop is working (change failure rate, rework rate, time-to-trust), and why the operator stays in the loop."
cover: /assets/img/2026-05-29-did-it-actually-work.png
coverAlt: "A dark workshop bench at night. A single finished object rests under a warm amber lantern. Beside it sits a pair of calipers traced with cool teal rim light, mid-measurement."
---

The AI development loop is well understood by now. Spec the work, share the context, run the pipeline, automate the boring ops, scale to many agents, build your own tools. All of it assumes the same thing underneath: output you can trust. Almost nobody asks the question that decides whether any of it was worth doing.

Did it actually work?

The loop is fast. That was the point. But fast is the easy half to measure and the wrong half to celebrate. An agent ships ten pull requests in an afternoon. The throughput chart climbs. The chart is lying if half of those get reverted next week.

## Velocity is the wrong number

For a decade, teams measured delivery by speed. Lead time, deploy frequency, throughput. Those numbers worked because writing the code was the bottleneck, so moving the code faster meant the team was healthier.

The AI era broke the proxy. Writing the code is no longer the bottleneck. A model produces more diff per hour than any team used to. So the speed numbers go up by default, whether the work is good or not. More PRs, more lines, faster merges. Vanity metrics, all of them, the moment the cost of producing code drops to near zero.

If you measure an AI-assisted team by velocity, you measure the one thing AI inflates for free.

## Trust is the right one

[Frictionless](/posts/2026-05-20-frictionless-the-book-behind-the-loop/) by Nicole Forsgren and Abi Noda named the metric that survives the AI era: Trust. The question is simple. Do you trust the output enough to ship it without redoing the work?

Trust is the number that does not inflate for free. An agent writes ten PRs. If you trust two of them enough to ship and rewrite the other eight, your velocity was theater and your real output was two. Trust is what is left after you subtract the rework.

Speed still matters. It is downstream of Trust now. A team that trusts its AI output ships fast as a side effect. A team that does not trust it ships rework with extra steps and a prettier chart.

## Review is a discipline, not a rubber stamp

Trust is earned or lost in one place: the review. The model owns execution, the developer owns the decision. The review is where the developer makes the decision. Three concrete moves separate a real review from a nod.

**Read the diff, not the summary.** The agent's pull-request body is a hypothesis about what it did. The diff is what it did. The gap between those two is where the bugs live. Read the diff.

**Run it.** A green test suite the agent wrote is necessary and not sufficient. The agent wrote the tests and the code from the same understanding, so a bad assumption passes its own tests happily. Run the thing. Watch it behave on the case you care about.

**Check it against the spec.** The [spec](/posts/2026-05-19-the-spec-driven-loop/) said what the change is for and what it is not for. The review confirms the change does that, and only that. Scope creep from an eager model is the quiet failure mode. The spec is the ruler you measure against.

A rubber-stamp review of AI output is the fastest way to lose Trust without noticing. It feels productive. It ships the eight PRs you should have rewritten.

## Three metrics that tell you the loop works

You do not need thirty dashboards. You need three numbers you act on.

**Change failure rate.** Of the changes you shipped, how many needed a fix, a revert, or a hotfix. This is the published [DORA](https://dora.dev) baseline, and it reads differently in the AI era. A climbing change failure rate after you adopt AI is a direct signal that the review step got too thin. The output looked fine and was not.

**Rework rate.** How often AI output gets thrown away or rewritten before it ships. This is the most honest AI-specific number, because it is exactly the inverse of Trust. Low rework means the spec was clear and the model delivered. High rework means the spec was weak or the model is guessing, and your velocity chart is fiction.

**Time-to-trust.** How long from "the agent proposed it" to "a human is confident enough to ship it." This is the real cycle time of an AI-assisted team. The agent's part is seconds. The human's part is the review and the validation. If time-to-trust is not dropping over weeks, the loop is not paying off, and more agents will not fix it.

## The operator stays in the loop

[Save the Boring Time](/posts/2026-05-26-save-the-boring-time/) ended on a rule: the agent triages, drafts, proposes, and never executes on production alone. A developer who gave an agent deploy keys for thirty days got a 13-hour outage out of it. The operator-in-the-loop rule is the safety side of Trust.

Measuring Trust is how you know the operator is adding value and not just nodding. If change failure rate is flat and rework is low and time-to-trust is dropping, the human review is real work that pays. If those numbers drift while the human keeps approving, the loop has a rubber stamp where a review should be. The metrics tell you which.

## What this is not

- This is not anti-metrics. Speed still counts. It sits downstream of Trust now, not above it.
- This is not "measure everything." Three numbers you act on beat thirty you ignore. Pick the three, watch them, change something when they move.
- This is not a one-time audit. Trust is a running measurement, the same way observability was the running foundation for ops. You watch it, or you lose it.

## Close

The loop is built to run fast. Fast was never the point. Trust was. The loop is only worth running if the output is good enough to ship without redoing it, and the only way to know is to measure it.

Velocity tells you the agent is busy. Trust tells you the work was worth doing. Measure the one that survives.
