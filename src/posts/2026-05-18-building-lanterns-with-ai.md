---
title: "Building a Game with AI Only: How Lanterns Started"
subtitle: "A cozy twilight garden, built spec-first with Claude as the collaborator — and the one decision that changed everything."
date: 2026-05-18
description: "How Lanterns went from a one-sentence pitch to a Steam-bound game, why we switched engines mid-project, and what 'AI-built' actually means in practice."
---

I'm a software architect by day — healthcare systems, the kind of code where "move fast" is not a compliment. At night I make small games. **Lanterns** is the one I let an AI build with me, end to end, and this is the honest account of how it started: the tool, the engine decision that nearly went the wrong way, and how much of this the model is actually doing.

## The idea

Lanterns is a cozy twilight garden. The whole game spins off a single cognitive twist:

> You press a direction. The Keeper steps that way — and the lantern swings the *opposite* way.

That asymmetry is the entire game. Every puzzle, every arena wave, is an expression of "step one truth, light another." The pitch I started from was one sentence in a design doc:

> A twilight garden puzzle: step one way, the lantern swings the other — catch lost fireflies before the breeze carries them astray, and guide them home.

No code yet. Just intent. That mattered, because the first real artifact wasn't a prototype — it was a spec.

## The tool: Claude Code, spec-first

I built Lanterns with [Claude Code](https://claude.com/claude-code), but the part that made it work isn't "the AI writes code." It's the **workflow around it**: brainstorm → spec → plan → implement, each step a committed document before a line of game code exists.

The repo still carries the whole paper trail. There's a `docs/superpowers/specs/` folder with dated design documents:

```
2026-04-23-lanterns-design.md
2026-04-24-arena-multiplayer-design.md
2026-04-25-steam-launch-polish-design.md
2026-04-29-hunt-pack-design.md
2026-04-29-mobile-friendly-web-design.md
2026-05-14-inventory-cap-design.md
...
```

Each one is a real design negotiation: pitch, pillars, the mechanic stated precisely, explicit *non-goals*. The non-goals section is the most valuable thing in the process — it's where "wouldn't it be cool if…" goes to die before it costs a week. The model is genuinely good at the YAGNI conversation when you make it part of the ritual instead of an afterthought.

Only after a spec is approved does an implementation plan get written, and only then does code happen. As an architect this is just the discipline I'd want from any engineer — it turns out it's also the discipline that makes an AI collaborator trustworthy. The model doesn't wander when the destination is written down.

## The decision that almost went wrong: the engine

The first version of Lanterns was **vanilla HTML + JavaScript + Canvas**. No framework, no engine. It's the obvious choice for a grid puzzle game: fast to start, runs everywhere, nothing to install. The early commits build a clean pure-reducer game core in plain JS.

Then I hit the question every game project hits: *is this the engine I want to finish in, or just the one that was easy to start in?*

The spec made the pillars explicit, and one of them was non-negotiable:

> **Visuals are the product.** The mechanic is the skeleton; the glow, dusk, and hand-placed detail are the *reason* someone plays.

A cozy game lives and dies on its bloom — the way warm lantern light blooms into dusk. In Canvas, that glow is hand-rolled shader math and a lot of fragile compositing. The honest assessment, written into the design doc and then into a single decisive commit:

> *Switch tech stack to Godot 4 for native + Steam path. Replaces vanilla HTML+JS+Canvas architecture with Godot 4 / GDScript. Native desktop primary, HTML5 web demo secondary. Key wins: built-in WorldEnvironment glow (bloom), visual TileMap editor, AnimationPlayer, editor-driven level authoring, commercial-license-safe (MIT).*

The framework I'd use to *decide* this — and the part worth stealing — was four questions:

1. **What is the product actually selling?** Visuals. So the engine's rendering had to be a strength, not a project.
2. **Where does it need to ship?** Native desktop and Steam, with a web demo as the funnel — not the other way around.
3. **What's the license exposure?** This is a commercial release. Godot is MIT. That removes a whole category of future problem.
4. **What's the cost of switching *now* vs. later?** The game core was still a small pure reducer. Porting it was cheap. In six months it would not have been.

Question 4 is the one people get wrong. Switching engines feels expensive, so teams defer it until it's actually expensive. Doing the migration while the codebase was small was the single highest-leverage call in the project — and having an AI that could do the mechanical port quickly is exactly what made "switch now" the rational choice instead of the scary one.

## How much is the AI actually doing?

Honest answer: a lot, but not the part people think.

Look at the git history and nearly every commit carries a `Co-Authored-By: Claude` trailer. Every design spec was written in dialogue with the model. Features that I'd have budgeted a week for — local co-op multiplayer, a mobile touch build, an inventory-cap system with slot-swap UI — each landed as roughly a day to a day-and-a-half of focused work, spec included.

But the leverage isn't typing speed. It's that the model is a tireless collaborator for the *boring-but-decisive* work: writing the non-goals section, doing the mechanical engine port, keeping a 2,000-line scene file from rotting by extracting subsystems on schedule. The taste — what's cozy, what's cheap, when a mechanic is *fun* — still has to come from a human who's played it. The AI is extraordinary at execution and structure. It is not the one who knows the lantern bloom looks wrong.

The division that works for me: **I own intent and judgment; the model owns structure and execution; the spec is the contract between us.**

## Where Lanterns is now

It's real. It's playable in your browser right now at **[lanterns.dynaum.com](https://lanterns.dynaum.com)** — a cozy bullet-heaven arena with local co-op, built in Godot 4, Steam-bound. The puzzle mode that started it all is still in there, one config flag away.

The thing I keep coming back to: none of this worked because the AI is magic. It worked because the process — spec, non-goals, decide-the-hard-thing-early — is the same process that makes *human* teams good, and the model is a genuinely strong participant in it when you hold that line.

More posts coming on the specific pieces: the co-op design, the mobile port, and the spec-driven loop itself. This is post one.
