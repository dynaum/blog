---
title: "You Can't Write a Context File for a Person"
subtitle: "Every fact about my systems lives in a file an agent loads on demand. The signal I need to manage a person is the thing that never happened, and nothing missing produces a token."
date: 2026-09-14
description: "Feedback resists automation for a narrow, mechanical reason: its input is absence. Field notes on reading people, challenging them correctly, and why the AI moment made both harder."
cover: /assets/img/2026-09-14-context-file-for-a-person.png
coverAlt: "Two empty wooden chairs under a single hanging lamp in a dim green room, a stack of written pages on the floor beside one of them, just outside the light."
---

I have written context files for my repositories, my deploy steps, my users. I have never managed to write one for a person.

Every one of those files works the same way. I know a fact, I write it down once, and [every session after that loads it for free](/posts/2026-06-15-commit-the-context/). The technique is boring and it has never failed me on a system.

Last month I had a hard conversation coming. An engineer whose work had slipped, and three weeks of me putting off saying so. So I did what I do with every other hard thing. I opened a session and asked for help preparing.

It gave me a page. The structure was right. Open with the specific behavior, separate the work from the person, ask before telling, close with a concrete next step. Professional and defensible. I read it twice and did not use one sentence of it.

Trying was not a stupid idea. Feedback looks like pattern work from the outside. There are frameworks for it. There is a shape to a good conversation, and models are excellent at shape.

## The input was never there

The reason it failed is narrow and mechanical. I had nothing to put in.

Here is what I had been reading for three weeks.

He stopped asking questions in design review. He used to be the person who found the hole in a plan on slide four. For a month he agreed with everything.

A pull request that never opened. He said he would take the migration work. He never declined it. Nothing ever appeared.

"Yeah, it's fine." Four words, end of a call, about a refactor he had argued hard for two weeks earlier.

Now list what a model had access to. The pull requests he did open. The tickets he closed. Meeting transcripts, if I pasted them in. All present, all fine. Every artifact showed an engineer having a normal quarter.

The signal was in none of them. The signal was the question he did not ask. A tool reads what is there. Managing reads what is missing, and a thing that did not happen leaves nothing behind to write down. There is no file, because there is no fact.

## Reading between the lines is history, not instinct

People call this intuition, which makes it sound like a gift you either have or do not.

It is a diff. I know what this person sounds like when things are fine, because I have six months of him being fine. The baseline lives nowhere except in me, built from unremarkable rooms, week after week. When a new week comes in different from the baseline, the difference is the entire message.

That is why a new manager cannot read a team in week one, and an outsider never reads it at all. Not a skill gap. A baseline gap. You have to be present for the boring months to understand the interesting one.

## Then you still have to say something

Assume you read it right. The hard part starts after.

I have two engineers in mind. To the first I say "this isn't your best work" and he gets sharper by Thursday. He wants the bar held high and he hears directness as respect. Say the same five words to the second and he goes quiet in design reviews for a month, and I spend six weeks earning the room back. With him the sentence has to arrive as a question. "Walk me through the tradeoff here." Same concern, same week, same goal, opposite sentence.

Nothing in the situation tells you which person is across from you. You learn it the expensive way, by being wrong with that specific person and paying for it. And the cost is not a retry. A bad prompt wastes a minute. A badly aimed sentence takes a month of someone's confidence.

## The AI moment made this harder, not easier

The tools flattened the output. A junior's pull request now reads like a senior's. Formatted, tested, clean commit message, sensible structure.

For years that surface was a free signal. You could tell who was thinking, who was struggling, and who was ready for more, by reading the work. That signal went quiet.

So the read moved underneath, into judgment and intent. Why this approach. What they chose not to do. Whether they understood what they shipped or [accepted what the model handed them](/posts/2026-07-14-not-the-model/). None of that arrives with tooling attached. The people learning to manage right now have fewer free signals to practice on than I had, and nobody has told them the signals are gone.

We call this soft skills, which is the worst name in our industry. It sounds optional and vaguely adjacent to being nice. It is technique. Which sentence, which week, which room, and whether you have [earned the standing to say it at all](/posts/2026-05-21-you-cannot-push-a-developer/).

## Where the model does help

I still use AI around this work, so let me be exact about where.

It is a good rehearsal partner. I write the unfair first version of what I want to say, the one with my frustration still in it, and ask which parts land as an attack. Useful, every time. Then I throw the draft away.

It catches me being vague. "Improve your communication" is a sentence with no behavior in it, and hearing that before the meeting instead of during it is worth the token cost.

What it does not have is him. It has my description of him, which is my read, already filtered through whatever I got wrong. Asking it to confirm my read is asking a mirror for a second opinion.

Everyone is going to learn these tools. That gap closes fast and it closes on its own. In two years, running an agent well will be table stakes, the way using a debugger is now.

The part that does not level out is the part with no file behind it. Noticing the question that stopped being asked. Knowing which of two sentences to use on a Tuesday. Being wrong about a person, and staying in the room afterward.

I commit everything else. I have never found a way to commit that.
