---
title: "Context Is Not a Dev Job"
subtitle: "Half the context an AI needs lives in the heads of the people outside engineering who own intent. AI-DLC only works when that half gets written down, in the same vault and the same spec template the engineers use."
date: 2026-05-24
description: "The shared AI context was half a foundation. The other half is product, design, and the people who own intent: user, problem, success criteria, non-goals, constraints, why. AI-DLC only works when both halves get written."
cover: /assets/img/2026-05-24-context-is-not-a-dev-job.png
coverAlt: "An open notebook on a dark wooden desk at night, both pages catching the warm glow of a single amber lantern between them. One shared work, two pages, one light."
---

Last week's post made the case for shared AI context. It was half a post. The half I left out is the more expensive one.

Everything in that post was engineering context. The codebase shape, the conventions, the gotchas, the testid policy. A real foundation has another half: the user, the problem, the why, the success criteria, the things the feature is not trying to do. That half lives in the heads of the people outside engineering who own intent. Product managers, designers, business analysts, depending on the org. They have always owned this. AI-DLC raises one new demand on them: write it down where the agent can read it.

Most teams skip this half. The engineering vault grows. The product half stays in meetings, briefs, threads, and people's heads. The agent gets fed a clean technical context and a thin or missing intent context. It executes against the engineer's best guess at what the brief meant. Then a week later the demo lands and the person who wrote the brief says "this is not what I meant." Classic disappointment, now faster.

I work in a regulated domain where wrong code has consequences. Wrong intent shipping faster is worse than wrong intent shipping slowly. The product half of the context is what stops the agent from executing a misunderstanding at scale.

**What the product half contains.**

A short list, the same shape as an engineering spec:

- **The user.** Who is this for, in one sentence, no marketing language.
- **The problem.** What pain we are removing, in their words.
- **The success criteria.** What has to be true for the feature to count as done. Measurable where possible.
- **The non-goals.** The things this is not trying to do. Same discipline as an engineering spec, maybe more important on the product side, because product is where scope creep starts.
- **The constraints that cannot move.** Regulatory, contractual, brand. The things the agent must not violate even when it would be easier to.
- **The decision log.** Why this approach over the rejected one. Same rejected-option pattern engineering uses, applied to product trade-offs.

Engineers already write some of these for technical specs. Product writes them at the product level. The vault structure stays the same: a principles folder for the durable rules, a folder per system or domain for the specifics. The principles folder gets product principles alongside the engineering ones. The per-system folders get both technical and product notes. One vault, two authors.

**Writing for the agent.**

The smallest, most useful illustration. "Make the onboarding intuitive" is the brief a PM hands an engineer. The engineer fills the gap with their own taste. Good engineers fill it well. The agent fills it with whatever pattern is most common in its training data. That is almost never what the brief meant.

The same brief, written for the agent:

- A new user reaches their first useful state within two clicks from any page.
- The first useful state is the dashboard with their first data already populated, not an empty state.
- Required steps from sign-up to first useful state: account, name, one project. Anything more is a non-goal for v1.

The agent can act on the second. It cannot act on the first. Every adjective the brief would have left to the engineer's judgment is now a place the agent will invent something. Write the criterion or accept what it invents.

There is no follow-up question. The agent does not pause to clarify. It runs against the brief it has, right now, while the brief writer is in another meeting. Explicit input is what makes async work.

**Reframe.**

This is more of the brief-writer's actual job, not more of the engineer's job offloaded onto them. "Be explicit about intent" has always been the job. The new collaborator raises the bar on what explicit has to look like.

People who write better intent get better software, faster. The feedback loop tightens. That is the win they care about. It is also the same loop the [spec-driven loop post](/posts/2026-05-19-the-spec-driven-loop/) described, with the spec's product half written by the person closest to the answer.

**The same five reasons, from the other side.**

If you read the [AI-DLC adoption post](/posts/2026-05-21-you-cannot-push-a-developer/), the five reasons developers resist a new methodology have a product-side mirror. Burned before by methodology fads. The 10-15x number sounds like marketing. The current brief-and-meeting loop already ships features. The agent's output still needs review, which feels like work moving from briefing to reviewing. And it came from engineering, which crosses into product's craft from the outside.

Same answer as for engineers. Show on a real feature. Kill the first week of friction. Make the easy path the good path. Let peers convert peers. Accept an uneven pace.

The last reason is the hardest. Asking the people who own intent to write into engineering's template can feel like an encroachment on their craft. The reframe of "this is your craft, sharpened, not engineering's process imposed on you" has to come from someone with credibility on both sides. Otherwise it lands as a takeover.

You cannot push a PM either.

**The pattern that works.**

One person outside engineering who is willing. One real feature, not a toy. Their next ticket, the one they would have briefed verbally.

They write the brief into the same spec template the engineers use. An engineer pairs with them on the first draft. The engineer's job in the pairing is to ask the questions the agent would otherwise have to guess at, and to write the answers down. The PM internalizes the questions for next time. The engineer and the agent then build to the brief. Demo.

They see their words shape the output. That is the moment that brings the next person in.

The [last post](/posts/2026-05-22-your-ai-context-belongs-to-the-team/) said your AI context belongs to the team. The team is bigger than engineering. A foundation needs both halves. The half you skip is the half the agent will guess at, and the agent guesses at scale.

What the engineers write keeps the model from wandering. What product writes tells it where to walk.
