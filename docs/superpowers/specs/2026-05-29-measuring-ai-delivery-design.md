# Did It Actually Work? — Design Spec

**Date:** 2026-05-29
**Status:** Draft, awaiting Elber's review.
**Author:** Session co-design (Elber Ribeiro + Claude).

## One-sentence pitch

A field-note post that closes the series' open thread: every previous post assumed AI output you could trust, and none said how you verify or measure that trust. This post names the wrong metric (velocity), the right one (Trust from *Frictionless*), reviewing AI code as a discipline, and three health numbers that tell you the loop is working.

## Framing decision

Personal-developer and small-team focus, reflective in tone. This is the capstone of the eleven-post arc, so it earns a short look back: the loop is built, the tools exist, the agents run. The question nobody answered is whether the output was good. Light self-cast from the regulated domain, where "did it actually work" has consequences, not just velocity charts.

## Goals

- Land the thesis: **velocity is a vanity metric in the AI era. Trust is the metric that matters.** More PRs and more lines mean nothing if you re-do the work.
- Define Trust concretely, tied to *Frictionless* (post 3): do you trust the output enough to ship it without redoing it.
- Make **reviewing AI-generated code a discipline**, not a rubber stamp. The review is where Trust is earned or lost. Read the diff, run it, check it against the spec.
- Name **three health metrics**: change failure rate, rework rate, time-to-trust. Concrete, measurable, honest about what each tells you.
- Keep the **human in the loop**, tied to the operator-in-the-loop rule from Save the Boring Time (post 9).
- Close the eleven-post arc: the loop is only worth running if you measure whether it worked.

## Non-goals (YAGNI)

- A DORA-metrics tutorial. Name the numbers, do not teach the full framework.
- A tooling shootout for dashboards or analytics.
- Naming the employer, a team, or a colleague.
- "AI writes perfect code" hype. The whole point is that you verify.
- A statistics lecture on how to instrument the metrics.
- Affiliate links.

## The thesis

For a decade, teams measured delivery by speed: lead time, deploy frequency, throughput. The AI era broke the proxy. An agent produces ten PRs in an afternoon. The chart looks great. The chart is lying if half of them get reverted next week.

The number that survives the AI era is Trust. *Frictionless* by Forsgren and Noda named it as the metric for AI-assisted teams: do you trust the output enough to ship it without redoing the work. Speed without trust is rework with extra steps.

## Reviewing AI code as a discipline

The review is the load-bearing step. It is where Trust is earned or lost. Three concrete moves:

- **Read the diff, not the summary.** The agent's PR body is a hypothesis. The diff is the fact.
- **Run it.** A green test suite the agent wrote is necessary, not sufficient. Run the thing and watch it behave.
- **Check it against the spec.** The spec said what the change is for. The review confirms the change does that and only that.

A rubber-stamp review of AI output is the fastest way to lose Trust without noticing.

## Three health metrics

- **Change failure rate.** Of the changes you shipped, how many needed a fix, a revert, or a hotfix. Climbing CFR after adopting AI means the review step is too thin.
- **Rework rate.** How often AI output gets thrown away or rewritten before it ships. High rework means the spec was weak or the model is guessing. This is the most honest AI-specific number.
- **Time-to-trust.** How long from "the agent proposed it" to "a human is confident enough to ship it." This is the real cycle time. If it is not dropping, the loop is not paying off.

## What this is not

Honest section, three short bullets.

- This is not anti-metrics. Speed still matters. It is just downstream of Trust now.
- This is not "measure everything." Three numbers you act on beat thirty you ignore.
- This is not a one-time audit. Trust is a running measurement, the same way observability was the foundation for ops in post 9.

## Series callbacks

- **Post 3, Frictionless.** That post introduced the Trust metric. This post operationalizes it.
- **Post 6, Trust the Pipeline.** QA is where Trust gets enforced automatically. This post is the human half of the same measurement.
- **Post 9, Save the Boring Time.** Operator-in-the-loop kept the agent from a 13-hour outage. Measuring Trust is how you know the operator is adding value, not just nodding.
- **Post 2, the spec-driven loop.** The spec is what you review against. No spec, no honest review.

## Proposed structure

1. **Hook.** Eleven posts built the loop. Every one assumed output you trust. Nobody asked how you know.
2. **Velocity is the wrong number.** Vanity metric in the AI era.
3. **Trust is the right one.** Define it, tie to Frictionless.
4. **Review as a discipline.** Read the diff, run it, check the spec.
5. **Three health metrics.** Change failure rate, rework rate, time-to-trust.
6. **Operator in the loop.** Tie to post 9.
7. **What this is not.** Three honest bullets.
8. **Close.** The loop is only worth running if you measure whether it worked.

Target length: 900 to 1100 words.

## Working title

**"Did It Actually Work?"**

Subtitle: *The whole series assumed AI output you could trust. This is how you measure it. Velocity is a vanity metric now. Trust is the number that survives, and three health metrics tell you whether the loop is working.*

Alternative titles:
- "Velocity Is a Vanity Metric"
- "Measuring Trust"
- "The Number That Survives"
- "Trust, Not Throughput"

## Links

- Internal: the spec-driven loop, `/posts/2026-05-19-the-spec-driven-loop/`
- Internal: Frictionless, `/posts/2026-05-20-frictionless-the-book-behind-the-loop/`
- Internal: trust the pipeline, `/posts/2026-05-23-trust-the-pipeline/`
- Internal: save the boring time, `/posts/2026-05-26-save-the-boring-time/`
- External: *Frictionless* by Nicole Forsgren and Abi Noda (the Trust metric)
- External: DORA metrics (change failure rate as the published baseline)

## Cover image plan

Same FLUX pipeline and dark amber-and-teal palette as the series. Concept: a dark workshop bench at night with a single finished object under a warm amber lantern, and a magnifying glass or set of calipers resting beside it, cool teal rim light on the measuring tool. Painterly. No text. Conveys "measure what you made," not "make more."

## Open questions for Elber

- Capstone framing (post 12, closes the arc) or just the next daily post? Recommendation: capstone. The arc has a natural end here, and Trust is the thread that ties posts 3, 6, and 9 together.
- Three metrics or two? Recommendation: three. Change failure rate is the known baseline, rework rate is the AI-specific honest number, time-to-trust is the one that proves the loop pays off.
- Name *Frictionless* authors again, or assume post 3 covered it? Recommendation: name them once, link post 3 for the full treatment.

## Decisions

- **Trust over velocity** as the central claim.
- **Review as discipline**, three concrete moves.
- **Three health metrics**, one honest AI-specific number among them.
- **Operator-in-the-loop** carried forward from post 9.
- **No affiliate links. Cover generated, not commissioned.**

## Sequencing

Post twelve in the build-with-AI arc, the capstone after Build Your Own Tools. Publish after Elber reviews this spec. Same flow as before: spec, draft to iCloud, review, cover, publish EN + PT-BR together, then LinkedIn.
