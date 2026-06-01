---
title: "Know When to Stop"
subtitle: "The skill that separates a senior from an eager junior is knowing when the model is the wrong tool. Availability is not fitness. Four times to put the prompt down."
date: 2026-06-01
description: "A counterweight to a pro-AI series: knowing when not to reach for the model is a senior skill. Four cases where the AI costs more than it saves, framed as judgment, not skepticism."
cover: /assets/img/2026-06-01-know-when-to-stop.png
coverAlt: "A workbench at night, a hand resting on a simple screwdriver in warm amber light, while a larger powered machine sits switched off and cool in teal shadow beside it."
---

I lost an hour last week to a task the model had no business touching. A small data file needed reshaping. The model was right there, so I prompted it. The output was close. I corrected it. Closer. I corrected it again. An hour in, I had a result I still had to read line by line to trust. A five-line script would have done it in ten minutes, correct by construction, no review needed.

The model did not fail. I did. I reached for it because it was available, and available is not the same as fit.

This blog has spent fourteen posts on using AI well. This one is the counterweight, and I have earned the right to write it. Knowing when to stop is the skill that separates a senior from an eager junior. The junior reaches for the model every time, because it is there and it is fast. The senior knows, before the hour is gone, that this is one of the times to put the prompt down.

## Four times to stop

**When the review costs more than the work saved.** The model can produce almost any small change in seconds. You still have to read every line to trust it, and below a certain size that reading is slower than just typing the fix. A three-line edit you understand cold is not a job for a prompt. The model shifts your work from writing to reviewing, and for small, obvious changes, writing was the cheaper half.

**When the answer must be exact and you cannot verify it cheaply.** A regex you will eyeball and approve wrong. A financial rounding rule. A boundary condition where a plausible-but-wrong answer is expensive. The model produces fluent, confident output with no signal of its own doubt. If checking the answer is as hard as producing it, the model saved you nothing and handed you a risk. I work in a regulated domain where wrong code has consequences, and there a confident wrong answer is worse than no answer.

**When the problem is deterministic.** A rename across a dozen files. A structured query. A format conversion. A codemod. These have exact tools that are correct by construction, every time. Asking a probabilistic model to do what a deterministic tool does perfectly is trading a guarantee for a guess. Use the rename. Run the query. The boring tool is the right tool.

**When you cannot own the output.** If you do not understand the result well enough to review it, you cannot ship it, and pasting it anyway is how code nobody understands enters the codebase. Stop before the paste. Either learn enough to own it, or do not use it. This is the operator-in-the-loop rule from [the ops post](/posts/2026-05-26-save-the-boring-time/), pointed at your own keyboard. The model proposes. You decide. You cannot decide on something you cannot read.

## The receipt

The data file was one. Here is the one that stings more. The week before, I asked the model to build a piece of tooling, and it built something new and reasonable. The problem is that the tool already existed in the repo. I had reached for the model to build before I looked to see what was already there. I paid for a thing I already owned.

Both misses are the same mistake. The model was the first thing I grabbed, not the right thing. The cost was not a bug or a bad output. The cost was the hour, and the hour does not come back.

## What this is not

- Not anti-AI. The fourteen posts before this one stand. For most of the work, the model is still the right tool, and reaching for it is still the right instinct. This is the boundary of that instinct, named honestly.
- Not a rule you apply mechanically. There is no line count, no checklist, no score. It is judgment, and judgment is the part that stays yours.
- Not an excuse to dodge the tool. "I will just do it by hand" can be its own laziness, the avoidance of learning a thing that would pay off for months. Stopping is right when the model is the wrong fit, not when you are ducking the on-ramp.

## Close

The series has always split the work the same way. The model owns execution. You own judgment. The first judgment, before any of the rest, is whether the model should touch this task at all. That decision happens in the first ten seconds, and getting it wrong costs the next sixty minutes.

Reaching for the model is easy, because it is always there. Knowing when not to is the harder skill, and the one worth building.
