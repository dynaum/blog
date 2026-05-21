---
title: "You Cannot Push a Developer"
subtitle: "Adopting AWS AI-DLC across an engineering org taught me the verb was wrong. You do not push people toward a methodology. You remove the reasons to say no."
date: 2026-05-21
description: "Field notes on driving adoption of AWS AI-DLC: the five legitimate reasons good developers resist a mandated methodology, and what actually changes minds."
cover: /assets/img/2026-05-21-you-cannot-push-a-developer.png
coverAlt: "A dark open-plan office at night, small lanterns scattered across the desks, some glowing warm amber and some still unlit."
---

For a few months now I have been the person in the room arguing for a new way to build software. I have a methodology I believe in, a deck, and a real conviction it makes teams faster. I have been trying to push an engineering org in one direction. This post is what the pushing taught me.

The methodology is AWS **[AI-DLC](https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/)**, the AI-Driven Development Lifecycle, introduced at re:Invent 2025. The short version: AI is a core collaborator under human oversight. It plans and executes, you hold the decisions. Sprints become **bolts**, cycles measured in hours or days. The work runs through three phases, inception, construction, operations. A set of **steering files** constrains how the agent works, and they travel across whatever IDE or model a developer already uses.

I did not need convincing. If you read [the spec-driven loop post](/posts/2026-05-19-the-spec-driven-loop/), AI-DLC is close to the institutional version of what I already do alone. Inception is brainstorm plus spec. Steering files are rules and non-goals. AWS put a name and an [open-source repo](https://github.com/awslabs/aidlc-workflows) on a thing I already believed in. So I became an advocate. Advocacy, it turns out, is the easy part.

The pitch lands in a meeting. Heads nod. Then everyone goes back to their desk and works the way they worked last week.

The gap is the real story. So I stopped pitching and started listening to the developers who had not switched. Here is what I heard, and none of it is laziness.

**They have been burned by mandated process before.** Every senior engineer has lived through a framework that promised speed and delivered ceremony. A new mandated methodology pattern-matches to that memory. The skepticism is earned.

**The productivity numbers read as marketing.** AWS cites 10-15x gains. To a professional skeptic, an unfalsifiable multiplier is a reason to discount, not to believe. They will trust a number when they see it on their own codebase, and not one second before.

**Their current workflow already works.** A fast, effective developer has a real loop running in their head. Asking them to swap it for bolts and steering files is a concrete cost against an uncertain payoff. Holding the status quo is a rational call.

**AI output still has to be reviewed.** If you do not yet trust the agent, AI-DLC moves your work from writing code to reviewing code. I work in a regulated domain where wrong code has consequences. The caution behind that hesitation is correct, not fearful.

**It came from above.** A methodology pushed by an architect or by leadership triggers a simple human response. People adopt what they choose and resist what they are assigned. I was the above. I was the problem in my own rollout.

Look at those five again. Not one is about laziness or fear of AI. Every one is about trust or friction. It stopped me, because [the last post on this blog](/posts/2026-05-20-frictionless-the-book-behind-the-loop/) was about a book that says exactly this. Trust has to be built, written down, and kept. Friction has to be found and removed. A mandate builds no trust and removes no friction. A mandate only adds weight.

So I changed what I was doing. A few things have actually moved people.

**Show, do not tell.** One real win on a real codebase, the team's own codebase, outperforms every deck I ever made. A skeptic does not want my number. They want theirs.

**Kill the first week.** Most people who abandon a tool abandon it in the first few days, when nothing is set up and everything is friction. Ship the steering files pre-configured. Make the on-ramp take minutes, not an afternoon.

**Make the default path the good path.** Adoption should be the easy choice, not the disciplined one. If doing it right takes willpower, it will not last.

**Let peers convert peers.** Adoption travels sideways. One engineer telling another "this saved me a day" moves more than any architect with a slide. My job is to create those moments, not to be the messenger.

**Accept an uneven pace.** Not everyone switches at once. Fighting that rebuilds the mandate. The early adopters pull the next group, and the next group pulls the one after.

Here is what I got wrong from the start. The verb was push. You cannot push a developer toward a methodology. Push harder and you get compliance, the shallow kind, gone the moment you look away. The engineers I respect most do not respond to pushing, and that is a feature of good engineers, not a bug.

You do not push. You remove the reasons to say no, you answer the real objections, you make the better path the easier one, and you let the work speak. Then people walk there on their own.

Pushing is hard because pushing is the wrong physics. I spent a few months learning that. The methodology was never the hard part. I was.
