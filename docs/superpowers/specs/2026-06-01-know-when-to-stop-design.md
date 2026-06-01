# Know When to Stop — Design Spec

**Date:** 2026-06-01
**Status:** Draft, awaiting Elber's review.
**Author:** Session co-design (Elber Ribeiro + Claude).

## One-sentence pitch

An essay arguing that the skill separating a senior from an eager junior is knowing when an AI is the wrong tool, with four concrete cases where reaching for the model costs more than it saves, framed as judgment rather than skepticism.

## Framing decision

Counterweight to a pro-AI series, written from seniority, not doubt. The blog has spent fourteen posts on using AI well. This one earns the right to say "not here" precisely because of that track record. The risk is the tone reading as "AI is overrated." Defuse it two ways. First, the voice is the experienced builder who reaches for the right tool, not the skeptic who distrusts the new one. Second, every case is about a specific, recognizable failure, never a blanket claim. First-person architect voice. Day job anonymized as "a regulated domain where wrong code has consequences."

## Goals

- Land the thesis: **availability is not fitness.** The model being there does not make it the right tool. Knowing when to stop is a senior skill.
- Give four concrete cases where stopping is correct, each recognizable and specific.
- Keep the tone as judgment, not skepticism. The post is pro-using-the-right-tool, not anti-AI.
- Ground it in an honest receipt: a real moment of over-reaching for the model.
- Tie to the series: the division of labor still holds, this is the human exercising the judgment half.

## Non-goals (YAGNI)

- An anti-AI argument. The series stands; this is the boundary, not a retraction.
- A decision flowchart or scoring rubric. The point is judgment, not a checklist to mechanize.
- Restating post 13 (Don't Just Use the Model). That post argued understand the machine. This argues do not always reach for it. Link once, do not re-argue.
- A tooling comparison (which script, which linter). Name tools as examples, do not rank them.
- Naming the employer, a team, or a colleague.
- Affiliate links.

## The thesis

The series has a default: when there is work, reach for the model. This post names the exception that a senior internalizes and a junior misses. The model is available for everything, and available is not the same as fit. Reaching for it on the wrong task is not a small inefficiency. It is an hour spent prompting, re-prompting, and reviewing what a five-line script or ten minutes of hand-coding would have closed cleanly. The skill is knowing, before the hour is gone, that this is one of those tasks.

## The four cases (where to stop)

Each gets a short paragraph, a recognizable symptom, and the better move.

1. **When the review costs more than the work saved.** For a change small and verifiable by eye, reading the model's diff is slower than typing the fix. The model can produce it, but you still have to read every line to trust it, and that reading is the bottleneck. Below a certain size, just write it.

2. **When the answer must be exact and you cannot verify it cheaply.** A regex you will eyeball wrong. A financial calculation. A boundary condition where plausible-but-wrong is expensive. The model produces fluent, confident output with no signal of its own uncertainty. If checking it is as hard as doing it, the model saved nothing and added a risk. Regulated-domain framing fits here.

3. **When the problem is deterministic.** A rename across files, a query, a structured refactor, a format conversion. These have exact tools that are correct by construction. You do not ask a probabilistic model to do what a deterministic tool does perfectly. Use the rename, the codemod, the query.

4. **When you cannot own the output.** If you do not understand the result well enough to review it, you cannot ship it, and pasting it anyway is how unowned code enters the codebase. Stop before the paste. Either learn enough to own it, or do not use it. This is the operator-in-the-loop rule from the ops post, applied to your own keyboard.

## The receipt

Honest and self-deprecating. A real over-reach: a task where the model was the obvious thing to grab, an hour went into prompting and correcting, and a small script or a quick hand edit would have been done in ten minutes. The blog's own tooling-rebuild miss from the prior week (rebuilding something that already existed) is available as a second beat: reaching for the model to build, when the move was to look first. The lesson is the same. The cost of the wrong tool is paid in the hour you do not get back.

## What this is not

- Not anti-AI. The fourteen posts before this one stand. The right tool for most of the work is still the model. This is the boundary, named honestly.
- Not a rule you apply mechanically. There is no word-count threshold or checklist. It is judgment, and judgment is the part that stays human.
- Not an excuse to avoid learning the tool. "I will just do it by hand" can be its own dodge. Stopping is correct when the model is the wrong fit, not when you are avoiding the on-ramp.

## Series callbacks

- **The division of labor.** The series says the developer owns judgment, the model owns execution. This post is the judgment half exercised at the very start: deciding whether the model should touch this task at all.
- **Post 13, Don't Just Use the Model.** That one said understand how it works. This one says know when not to reach for it. Adjacent, not overlapping.
- **Post 9, Save the Boring Time.** The operator-in-the-loop rule (the model never acts alone on what matters) generalizes here to: the operator decides whether the model acts at all.

## Proposed structure

1. **Hook.** The confession: an hour lost to the model on a task a script would have closed in ten minutes. Availability is not fitness.
2. **The thesis.** Knowing when to stop is the senior skill the series has not named.
3. **The four cases.** Review cost, must-be-exact, deterministic, cannot-own-it.
4. **The receipt.** The honest over-reach, including the rebuilt-tooling beat.
5. **What this is not.** Three honest bullets.
6. **Close.** The judgment half of the work. The model executes; you decide whether it should.

Target length: 800 to 1000 words.

## Working title

**"Know When to Stop"** (approved)

Subtitle (draft): *The skill that separates a senior from an eager junior is knowing when the model is the wrong tool. Availability is not fitness. Four times to put the prompt down.*

## Links

External: none required.

Internal:
- Don't Just Use the Model, `/posts/2026-05-30-dont-just-use-the-model/`
- Save the Boring Time, `/posts/2026-05-26-save-the-boring-time/`

## Cover image plan

Same FLUX pipeline and dark amber-and-teal palette as the series. Concept: a workbench at night where a hand rests on a simple hand tool (a screwdriver or a small chisel) in warm amber light, while a larger, more elaborate powered machine sits switched off and cool in teal shadow beside it. The right tool chosen over the bigger one. Painterly, soft bloom, brushstroke texture. No text.

## Open questions for Elber

- Use the rebuilt-tooling miss as the second receipt beat, or keep the receipt to the single hour-on-a-script story? Recommendation: use both lightly. Two short beats land the pattern harder than one, and the rebuild story is recent and true.
- Four cases as planned, or is case 3 (deterministic) too obvious to spend a paragraph on? Recommendation: keep four. Obvious in the abstract, routinely violated in practice, which is exactly why it earns a line.
- Title confirmed "Know When to Stop." Keep, or revisit subtitle phrasing? Recommendation: keep.

## Decisions

- **Judgment-not-skepticism framing.** Senior voice, specific cases, no blanket claims.
- **Four cases**, each a recognizable symptom plus the better move.
- **Honest receipt**, including the recent rebuilt-tooling miss.
- **No affiliate links. Cover generated, not commissioned.**
- **Day job anonymized.** No employer, team, or colleague named.

## Sequencing

Latest post in the build-with-AI arc, after `2026-05-31-fix-the-system-not-the-output`. Same flow: spec, draft for inline review, cover once approved, publish EN + PT-BR together, update the vault catalog, then the LinkedIn teaser (English only, links the English post).
