---
title: "When Do I Wake Up, and When Am I Done?"
subtitle: "Every unattended run answers two questions. /loop answers one, /goal answers the other, and the trouble starts when you make one fake the job of both."
date: 2026-07-07
description: "An agent left running faces two separate decisions on every turn: when to wake up, and when to stop. /loop is a clock. /goal is a fresh evaluator checking a condition. Each has a blind spot that is exactly the other's strength. Here is how to match the command to the question."
cover: /assets/img/2026-07-07-wake-up-and-done.png
coverAlt: "A deep charcoal workshop wall holding two instruments, a warm amber wall clock glowing on the left and a single lit lamp over a marked finish line on the workbench, muted teal rim light, brushstroke texture and soft bloom."
---

Leave an agent running and it faces two questions on every turn. When do I wake up. When am I done.

They feel like one question. They are not. One is about cadence. The other is about the finish line. Claude Code gives you a separate command for each, and the trouble starts the moment you make one do the other's job.

## Two questions, not one

Any run that continues without you prompting each step has to decide two things. What starts the next turn. What ends the work. A cron job answers the first and never the second. A checklist answers the second and says nothing about timing. An agent needs both answered, and they pull in different directions.

Name them plainly. Cadence: how often do I come back. Completion: how do I know to stop. Keep them apart in your head and the right tool for each falls out on its own.

## The finish line

[`/goal`](https://code.claude.com/docs/en/goal) sets a completion condition. After each turn, a small fast model reads the conversation and decides whether the condition holds. If it does not, Claude takes another turn on its own. The goal clears when the condition is met. The next turn fires the instant the last one ends, so the work runs back to back with no waiting on a clock.

```text
/goal all tests in test/auth pass and the lint step is clean
```

The blind spot is worth stating out loud. The evaluator reads the transcript. It runs no tools. It cannot open a file or run a test itself. So write the condition as something Claude's own output proves. "All tests in test/auth pass" works, because Claude runs the tests and the result lands in the transcript for the evaluator to read. "The service is healthy in production" does not, because nothing in the conversation shows it.

The strength: the judge is a fresh model, not the one that did the work. Completion gets decided by a second pair of eyes.

## The clock

[`/loop`](https://code.claude.com/docs/en/scheduled-tasks) reruns a prompt on a schedule. Give it an interval and it fires on that cadence. Omit the interval and Claude picks the delay each round, short while a build is finishing, longer once things go quiet. A loop keeps going until you stop it or Claude decides the work is done.

```text
/loop check whether CI passed and address any review comments
```

The blind spot mirrors the goal's. The model doing the work is the same model deciding it is finished. The doer grades its own homework. Fine for a poll where done is obvious. Weak for real work, where the finish line is a claim you want checked by someone other than the one making it.

The strength: a loop owns the clock. It waits, it comes back, it paces itself against the outside world.

## Each gap is the other's job

Set the two blind spots side by side and the pattern is hard to miss.

A goal cannot wait on the outside world. Nothing advances the clock but a finished turn, and the evaluator sees only what is written down. A loop cannot judge completion well, because the judge and the worker are the same model.

Now read the strengths across. A loop owns the clock a goal lacks. A goal owns the fresh judge a loop lacks. The gap in one is the whole point of the other.

## One run, both questions

Say you push a branch and want it green and merged without babysitting. Two clocks are running. Yours, and CI's. CI finishes on its own schedule, minutes from now, and nothing in your session moves it along. This is the waiting phase, and it belongs to the loop. Claude wakes on its own cadence, reads the run, waits longer once the branch goes quiet.

Then CI comes back red. The work turns inward. Now every piece of state lives in the transcript: the failing log, the fix, the rerun. This is the closing phase, and it belongs to the goal. Set the condition. Every job on this branch is green and git status is clean. Claude grinds turn after turn, and a fresh model confirms the finish instead of the model that wrote the fix.

A real task has both phases. The skill is naming which one you are in and reaching for the command that fits. The loop bridges to the outside world. The goal drives to a checked close. Neither does both well.

## The honest edges

A few limits, so nothing surprises you. One goal per session, so it is one finish line at a time. The goal evaluator never runs tools, so a condition it cannot read in the transcript will never register as met. A loop fires only while the session is open and idle, so close the terminal and the clock stops. Loops expire on their own after seven days.

There is a quiet third piece under both. Auto mode approves tool calls inside a turn, so each turn runs unattended. It does not start the next turn. Goal and loop start turns. Auto mode lets each turn run without stopping to ask. You want all three for truly hands-off work.

## Close

Before you set a run loose, ask which question you are answering. Do you need a cadence, or a finish line. If the work waits on something outside the session, you need a clock, and that is `/loop`. If the work has an end state Claude can prove in its own output, you need a judge, and that is `/goal`. Most tasks hold a stretch of each.

Name the question first. The command follows.
