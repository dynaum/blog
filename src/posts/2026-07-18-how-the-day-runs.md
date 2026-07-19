---
title: "How the Day Actually Runs"
subtitle: "A real day building and running software with AI: predefined user personas aim every agent at the hardest person, parallel agents in worktrees do the building, and loops walk production all night as those same personas."
date: 2026-07-18
description: "A day-in-the-life recommendation. User personas written as rules point every agent at the hardest real user, worktrees let parallel agents build without colliding, and loops plus goals hold production by walking the critical flows as those personas. One connective idea: write the person down once, reuse them everywhere."
cover: /assets/img/2026-07-18-how-the-day-runs.png
coverAlt: "A dark workbench seen from above at night with several lit work stations active at once, a different figure marker standing at each one for a user persona, and one steady amber lamp left on over a small monitor showing a heartbeat line, muted teal rim light, brushstroke texture and soft bloom."
---

An elderly patient opened the app, tapped the submit button twice because the first tap gave no feedback, and sent nothing. The screen looked done to me. It was not done to her. I would never have caught it, because I am not her. My thumbs are fast, my eyes are good, and I already know what the button does.

So I stopped building for me. Here is how a normal day runs now.

## Morning: I build for a person, written down

I do not prompt an agent to "build the intake form." I hand it a person. The patient. The elderly user with zero tech knowledge and a cracked phone screen. The administrator working a batch of two hundred records before lunch. Each one is a written rule: what they know, what they fear, the device in their hand, the thing that makes them quit and call support.

Handed the elderly persona, the agent catches the double-tap with no feedback. Handed the patient persona, it flags the low-contrast button and the error message that reads like a stack trace. Handed the administrator persona, it notices the batch screen has no way to undo one wrong row out of two hundred.

The rule is the whole point. A persona you keep in your head is a stereotype you apply when you remember to. A persona written down is a lens every agent uses every time, whether I am watching or not. It is the same move as [committing your context](/posts/2026-06-15-commit-the-context/): write it once, and the repo hands it to the model on every session instead of you re-explaining the user forever.

## Midday: more than one agent means worktrees

By late morning I am running three agents, and the moment there is more than one, I become the bottleneck and the filesystem becomes the first casualty. Two agents editing the same checkout collide. One reformats a file the other is halfway through. Branches tangle.

A worktree fixes this at the root. Each agent gets its own copy of the repo on its own branch, its own working directory, its own space to be wrong in. Now one agent builds the administrator batch screen while another walks the patient flow end to end, at the same time, and neither touches the other's files. This is the requirement that makes parallel agents real, not a nicety. Run two agents in one directory and you will spend the afternoon untangling instead of shipping. I learned the [multi-agent problem](/posts/2026-05-27-many-agents-one-chat/) the slow way. The worktree is the part that makes it safe.

The personas travel into every worktree. The same rule files load in each copy, so the patient is the same patient whether an agent is building the feature, reviewing the diff, or checking it in production. I wrote the person down once. Every agent, everywhere, reads the same one.

## Background: loops hold production all night

The part a single-agent day never has: work that runs while I sleep. A loop is a standing watch, and mine do not watch abstractly. They watch as the persona.

One loop walks the critical flow, the login and the one task that pays the bills, as the low-tech elderly user. It taps slowly, it misreads, it hesitates, and when the flow breaks or turns confusing it opens an issue before a real person hits it. A second loop scans dependencies and code for known vulnerabilities and files a report the moment something lands on a CVE list. A third piece is not a loop at all. When a break gets flagged, I hand it to a goal: fix this, and the condition clears only when the flow passes again and a fresh model confirms it.

That split matters, and I [wrote about it before](/posts/2026-07-07-wake-up-and-done/). A loop owns the clock, it comes back on a cadence and watches the outside world. A goal owns the finish line, judged by a second model that did not write the fix. A loop is good at noticing. It is bad at deciding it is done. So the loop notices the broken patient flow, and the goal drives the fix to a checked close. Watching and fixing are different jobs, and giving each its own tool is why the coverage holds.

## Why this works, and it is not the model

None of this is because the model got smarter this quarter. The day is covered because the work is aimed.

The personas make the software about the right person, the hardest one instead of the imaginary average. The worktrees make three agents safe instead of a merge disaster. The loops make coverage constant instead of a thing I remember to check on Fridays. Aim beats horsepower. A frontier model pointed at the wrong user builds a beautiful thing nobody can use. A cheaper model pointed at the patient, running in an isolated worktree, watched by a loop that walks her flow at 3am, ships something that works for her.

## Set it up in this order

Do not build the whole day at once. Add one constraint at a time.

Write one persona rule file today, and make it your hardest user, not your easiest. The person who cannot see well, cannot tap precisely, or has never used software like yours. Add a worktree the first time you catch yourself running two agents in one directory. Point one loop at your single most important production flow this week, and have it walk that flow as that persona.

Each piece pays for itself alone. Together they turn into a day that runs itself between your decisions, and every part of it is looking at the person who actually uses what you ship.
