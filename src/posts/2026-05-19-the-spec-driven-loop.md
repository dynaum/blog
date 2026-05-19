---
title: "The Spec-Driven Loop: How I Actually Work With an AI"
subtitle: "Brainstorm, spec, plan, implement. Each one a committed document before a line of code. The non-goals section is the highest-leverage thing I write all week."
date: 2026-05-19
description: "The repeatable method behind Lanterns, generalized: why a written spec with explicit non-goals makes an AI collaborator trustworthy, with real artifacts from the repo."
cover: /assets/img/2026-05-19-the-spec-driven-loop.png
coverAlt: "A single warm lantern glowing on a dark architect's desk at night, stacked papers catching the light, faint code on a screen through the window."
---

[Post one](/posts/2026-05-18-building-lanterns-with-ai/) told the story of how Lanterns started. It ended on a promise: more posts on the specific pieces, starting with the loop itself. This is that post.

The loop is not game-specific. I use the same four steps for healthcare backend work at my day job and for a cozy game at night. The medium changes. The discipline does not.

## The loop

Four steps. Each produces a committed document before the next begins:

```
brainstorm  →  spec  →  plan  →  implement
   (talk)     (.md)    (.md)    (code + commits)
```

The order is the whole point. No spec until the brainstorm settles. No plan until the spec is approved. No code until the plan exists. The model is fast enough to skip straight to code, and skipping is the most expensive mistake you make with it.

You see the loop in the git history, not just in my description of it. The inventory-cap feature landed as this sequence:

```
a35ddd4  docs: spec for inventory cap with slot-based swap
6bb80be  docs: implementation plan for inventory cap with slot-based swap
de63871  feat(arena): Inventory data model with 6-slot cap and ever-held tracking
c386d03  refactor(arena): route picks through Inventory; stub apply path
...
24f8fac  Merge feat/inventory-cap: 6-slot capped, swap-based upgrade inventory
```

Spec commit. Then plan commit. Then thirteen feature commits. The documents are dated and version-controlled next to the code they produced. A year from now I read the spec to remember why, not the diff to guess.

## Step 1: brainstorm

This step is talk, not files. I describe intent. The model pushes back, proposes alternatives, names risks. The goal is one paragraph both of us agree on.

The inventory-cap spec records where this landed, including a rejected branch:

> Slot-specific affordances (active-ability slots separate from passive slots, that was option C in the brainstorm and was rejected).

Writing the rejected option down matters. Six weeks later, when someone asks "why not separate the active slots?", the answer is in the repo. The brainstorm is cheap. Re-litigating a settled decision is not.

## Step 2: the spec, and its non-goals

The spec states the pitch, the pillars, the mechanic stated precisely, and the non-goals. The non-goals section is the most valuable thing I write all week.

Here is a real one, verbatim, from the local co-op design:

> **Scope intentionally excluded from v1**
> - 3+ players
> - Split-screen
> - Network multiplayer (only local same-screen)
> - Friendly fire between players' beams
> - Trading upgrades between players
> - Shared HP / downed-is-dead mode
> - Competitive modes
>
> These are all reasonable future versions but double the complexity each. The first v1 should be: two friends, one couch, cozy.

And from the inventory-cap spec:

> **Out of scope (explicit)**
> - Drag-and-drop slot rearrangement.
> - A "skip this pick" button when full. Will be added later if playtests show forced swaps feel punishing.
> - Tooltips on hover/long-press in the in-fight strip.
> - Upgrade family rebalancing or new upgrades. The cap is a structural change, not a content change.

Every line in those lists is an idea good enough to be tempting. Each one is also a week of work and a new category of bug. The non-goals section is where "wouldn't it be cool if" goes to die before it costs you anything.

This is the part the model is unexpectedly good at. Ask an AI to add a feature and it will add the feature, plus three you did not ask for. Make non-goals a required section of every spec and the conversation inverts. Now the model argues *for* cutting scope, because the document demands a reason for everything kept. The discipline lives in the ritual, not in remembering to be disciplined.

## Step 3: the plan, and the decisions log

Once the spec is approved, the plan turns it into ordered steps. It also carries a decisions log: each non-obvious call, with the reason attached. From the inventory-cap work:

> - **Cap size: 6.** Aligns with Vampire Survivors / Brotato conventions, matches average run length so the swap mechanic actually triggers.
> - **Per-pick slot accounting (no auto-merge of duplicates).** Each pick costs a slot, including identical ones. Honest about the cost of stacking.
> - **Effect reversal via reset + re-apply.** Single source of truth drives every stat. No per-upgrade reverse logic.

A decision without its reason rots. Six months on you cannot tell a deliberate constraint from an accident, so you are afraid to touch either. The reason is what makes the code safe to change later.

## Step 4: implement

Only now does code happen, and this is the step people assume is the whole job. It is the least interesting one. With the spec and plan written, implementation is execution against a contract. The model is excellent at it: tireless, structurally consistent, happy to extract a 2,000-line scene file into subsystems on schedule instead of letting it rot.

The leverage was never typing speed. It is that steps one through three removed every ambiguity before the first line of code, so the model never had to guess what I meant. A model that does not guess does not wander.

## Why this generalizes

None of the above is about games. Replace "lantern bloom" with "claims adjudication" and the loop is identical. The reason it works is the reason it works for human teams: a written spec with explicit non-goals is the cheapest place to be wrong. Being wrong in a paragraph costs a paragraph. Being wrong in a merged feature costs a sprint.

The division from post one still holds, and the loop is what enforces it:

> I own intent and judgment. The model owns structure and execution. The spec is the contract between us.

The contract is the load-bearing word. Without it, "AI-assisted" means a fast intern with no brief. With it, the model is the strongest participant in a process that already made good teams good.

Next in this series: the local co-op design, and the mobile web port. Both ran this exact loop. Both have the receipts in the repo.
