# Design spec: "When Do I Wake Up, and When Am I Done?"

## One-sentence pitch

Every unattended agent run has to answer two independent questions, when do I
wake up and when am I done, and `/loop` and `/goal` each answer exactly one, so
the power is in using each for its own job instead of forcing one to fake the
other.

## Goals

- Name the two axes plainly: cadence (what starts the next turn) and completion
  (what ends the work).
- Explain `/goal` accurately: a fresh small model checks your condition after
  every turn and clears the goal only when the condition holds. Next turn fires
  the instant the previous one finishes.
- Explain `/loop` accurately: an interval or a self-paced delay drives the next
  turn. It stops when you stop it or Claude judges the work done.
- Show each tool's blind spot, and that each blind spot is the other's job.
- Land the combination with one worked example: ship a branch. Loop polls CI on
  the world's clock, goal grinds the fix to a verifiable green.

## Non-goals (load-bearing)

- Not a command reference or a flags dump. Link the docs, do not transcribe them.
- Not cron, Routines, Desktop tasks, or GitHub Actions. One line that scheduling
  lives elsewhere, no detour.
- Not naming the employer. Any work anecdote stays anonymized.
- Not a "look what I automated overnight" brag. The payoff is the mental model,
  not a demo reel.
- No hype about autonomy or agents that run themselves while you sleep.

## The angle

Spine: an unattended run is two decisions, not one. "When do I wake up?" and
"When am I done?" are independent, and people collapse them into a single loop.
`/loop` is a clock. `/goal` is a fresh evaluator checking a condition. The two
failure modes are concrete. A loop told to run "until it's done" leans on the
working model to grade its own homework, weaker than a separate judge. A goal
alone stalls the moment the work waits on the outside world, because the
evaluator only reads the transcript and never runs tools, so nothing advances
the clock but a finished turn. Match the tool to the question and each covers the
other's gap.

## Proposed structure

1. Hook: an unattended run is really two decisions, and most people only picture
   one of them.
2. The two questions, named: when do I wake up, when am I done.
3. `/goal` is the finish line. A fresh model checks your condition each turn,
   clears it only when the condition holds. Blind spot: reads the transcript,
   runs no tools. Write the condition so Claude's own output proves it.
4. `/loop` is the clock. Interval or self-paced. Blind spot: it never decides
   done well, because the doer grades itself.
5. Each one's failure mode is the other one's job.
6. The combination, worked: ship a branch. Loop for the world's clock, goal for
   closure inside it.
7. Honest limits: one goal per session, evaluator can't run tools, loop needs
   the session open, seven-day expiry, and auto mode as the quiet third leg
   (approves tools within a turn, does not start a new one).
8. Close: match the tool to the question.

## Length and format

Essay, 850-950 words. First person, architect-by-day builder voice. Honest,
concrete, no hype. Vary the hook, do not lead with the Lanterns game story.

## Links

- Inline link to a neighbor in the series where natural, for example the context
  or right-sizing posts. Keep links optional, no count references.
- Link the official `/goal` and `/loop` docs once each, not transcribed.

## Cover plan

Series palette (deep charcoal, honey-amber focal glow, teal rim light). Concept:
a workshop wall holding two instruments, a warm amber wall clock for cadence and
a single lit lamp over a marked finish line on the bench for the condition met,
teal rim light, brushstroke texture, soft bloom. No text in the image.

## Open questions

- Worked example: keep it generic (a branch, CI, tests) as framed, or swap for a
  different concrete task. Default: generic. Confirm at draft review.
- Title: "When Do I Wake Up, and When Am I Done?" (working). Alternatives: "Two
  Questions Every Unattended Run Answers", "The Clock and the Finish Line".

## Decisions

- Angle: two questions, cadence vs completion.
- `/loop` = clock, `/goal` = evaluator. Each blind spot is the other's job.
- One worked example (ship a branch), generic by default.
- Essay length, series palette cover.
- Date: 2026-07-07 (current date).
