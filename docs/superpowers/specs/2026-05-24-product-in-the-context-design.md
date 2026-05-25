# Product-in-the-Context Post — Design Spec

**Date:** 2026-05-24
**Status:** Draft, awaiting Elber's review.
**Author:** Session co-design (Elber Ribeiro + Claude).

## One-sentence pitch

A field-note post arguing that the AI context base is half engineering and half product, that the product half is the one most teams skip, and that AI-DLC only works when product people learn to write inputs the agent can read.

## Framing decision

Employer-neutral, general advice. No team or colleague named. Same protections as the AI-DLC and pipeline-trust posts: Elber writes as an architect inside "a large engineering org" and, where it matters, "a regulated domain where wrong code has consequences."

Also: respectful of product people. The post does not say PMs "don't get it." The post says the medium of communicating intent changed when the collaborator changed; product people have always owned intent, and they are being asked to add a new tool to a craft they already practice. No condescension, no "non-tech" othering language. Treat the new skill as a skill upgrade for everyone, not a deficiency in one group.

## Goals

- Land the thesis: **a context base built only by engineers is half a foundation, and the missing half is the more expensive one to lack.**
- Make the case that product people writing for the agent **is** their job, not extra work for engineering's benefit.
- Show what product people actually need to write, with the contrast between "make it intuitive" (useless to the agent) and a concrete acceptance criterion (usable).
- Map the resistance product people raise to the same five-reason pattern from the AI-DLC post, with the same answer: show, do not tell.
- Tie back to the series: shared context (post 5) gets a second author class, AI-DLC (post 4) needs the inception input no agent can invent, the spec-driven loop (post 2) has always had a product half.

## Non-goals (YAGNI)

- A PM-onboarding curriculum or course.
- A tooling shootout (Notion vs Linear vs Obsidian for product specs).
- Naming the employer, a team, a PM, a designer, or a colleague.
- "AI replaces PMs" or "AI replaces engineers" arguments. The post is about collaboration, not substitution.
- A maturity model with named stages.
- Selling AI as a magic understanding machine. The post is explicit that the agent reads what is written and reads nothing else.

## Topic background

The previous post in the series, **Your AI Context Belongs to the Team**, made the case for shared context but stayed inside engineering: codebase conventions, gotchas, the testid policy. The half left out is the product half: the user, the problem, the why behind decisions, the constraints that are non-negotiable, the success criteria the feature is judged against. That content lives in product people's heads, gets shared in meetings, and rarely lands in writing.

AI-DLC's **inception phase** is supposed to start with intent. If intent is verbal, the agent does not have it. The team writes a spec, and if the PM did not write to it, the spec is the engineer's best guess at what the PM meant. The agent then executes against the guess. A week later, the PM sees the demo and says "this is not what I meant." The classic disappointment, now happening faster.

The fix is structural: bring product into the writing. Same vault, same spec template, same non-goals discipline. Not as engineering's request, as the natural evolution of what a PM brief has always been.

## The angle

This post is a sequel to **Your AI Context Belongs to the Team**. Elber is again the one trying to drive the change, this time across the engineering/product line, and again self-cast: he is the architect who learned that pushing engineers to use AI-DLC was only half the job. The other half is harder, because it means asking people outside engineering to learn a process that looks, from the outside, like more work.

The reframe that carries the post: writing for the agent is more of the PM's actual job, not more of the engineer's job offloaded onto them. The job has always been "be explicit about intent." The new collaborator just raises the bar on explicit.

## What the product half of context contains

Concretely, what product writes that the agent uses:
- **The user.** Who is this for, in one sentence, no marketing language.
- **The problem.** What pain are we removing, said in their words.
- **The success criteria.** What has to be true for the feature to count as done. Measurable where possible.
- **The non-goals.** Same discipline as engineering specs. Maybe more important on the product side, because that is where scope creep starts.
- **The constraints that cannot move.** Regulatory, contractual, brand. The things the agent must not violate even when it would be easier to.
- **The decision log.** Why this approach over the rejected one. The same "rejected option C in the brainstorm" pattern from post two, applied to product trade-offs.

## The teaching: writing for the agent vs writing for a human

The smallest, most useful illustration. A human teammate hears "make the onboarding intuitive" and fills the gap with their own taste. The agent fills it with whatever pattern is most common in its training data, which is rarely what the PM meant.

Same brief, written for the agent:
- A new user reaches their first useful state within two clicks from any page.
- The first useful state is the dashboard with their first data already populated, not an empty state.
- Required steps from sign-up to first useful state: account, name, one project. Anything more is a non-goal for v1.

The model can act on the second. It cannot act on the first. The teaching is: every adjective the PM would have left to the engineer's judgment is now a place the agent will invent something. Either write the criterion or accept whatever it invents.

## Resistance, same five-reason pattern

Map directly to the **You Cannot Push a Developer** five, with the PM version of each:

1. **Burned before by methodology.** Every PM has lived through a process that promised speed and added meetings. A new mandated way of writing briefs pattern-matches.
2. **The productivity claim sounds like marketing.** Same 10-15x line, same skepticism, same legitimate discount until they see it on their own work.
3. **Their current way already works.** A skilled PM has a brief-and-meeting loop that ships features. Switching to writing-for-the-agent has a concrete cost against an uncertain payoff.
4. **The agent's output still needs review.** PMs who do not yet trust the agent see AI-DLC as moving their work from briefing to reviewing, with no time saved.
5. **It came from engineering.** A workflow brought by an architect crosses into product's craft from the outside. People adopt what they choose.

Same answer as for engineers, with the same self-awareness: show on a real feature, kill the first week of friction, make the easy path the good path, let peers convert peers, accept an uneven pace.

## The pattern that works

The post will name the practical move:
- One PM who is willing.
- One real feature, not a toy. Their next ticket, the one they would have briefed verbally.
- The PM writes the brief into the same spec template the engineers use. Engineer pairs with them once to make the first draft easier.
- The engineer + agent build to it. Demo.
- The PM sees their words shape the output. That is the win that brings the next PM.

Same physics as post four. You cannot push a PM either.

## Series callbacks

- **Post 5, shared context.** The vault needs a product side, not just an engineering side. The principles folder gets product-domain principles. Per-system folders include both technical and product notes.
- **Post 4, AI-DLC adoption.** Same five-reason pattern, same show-do-not-tell answer, now across the engineering/product line.
- **Post 2, spec-driven loop.** The spec has always had a product half. AI-DLC makes that half non-optional.
- **Post 6, trust the pipeline.** QA is the runtime foundation. Product context is the design-time foundation. Both are required for delivery.

## Proposed structure

1. **Hook.** The post you read last week was half a foundation. The other half is the more expensive one to lack.
2. **The thesis.** A context base built only by engineers cannot answer the questions only product can answer.
3. **What product writes.** Concrete list, six items, each one short. User, problem, success criteria, non-goals, constraints, decision log.
4. **The teaching, with one example.** "Make it intuitive" vs the explicit criterion. One paragraph that lands.
5. **The reframe.** This is more of the PM's actual job, not more of the engineer's. The job was always "be explicit about intent." The new collaborator raises the bar.
6. **Resistance, same five reasons.** Brief mapping. Not a re-write of post four, a reference to it.
7. **The pattern that works.** One willing PM, one real feature, show.
8. **Close.** Foundation requires both halves. The half you skip is the half the agent will guess.

Target length: 800 to 1000 words, like the AI-DLC and context posts.

## Working title

**"Context Is Not a Dev Job"**

Subtitle: *Half the context an AI needs lives in product people's heads. AI-DLC only works when that half gets written down, in the same vault and the same spec template the engineers use.*

Alternative titles:
- "The Half of Context You Are Missing"
- "Your Foundation Is Half Product"
- "Bring Product into the Pipeline"
- "The PM Has to Write Now"

## Links

- Internal: shared context, `/posts/2026-05-22-your-ai-context-belongs-to-the-team/`
- Internal: AI-DLC adoption, `/posts/2026-05-21-you-cannot-push-a-developer/`
- Internal: spec-driven loop, `/posts/2026-05-19-the-spec-driven-loop/`
- Internal: trust the pipeline, `/posts/2026-05-23-trust-the-pipeline/`

## Cover image plan

Same FLUX pipeline and dark amber-and-teal palette as posts two through six. Concept: two open notebooks side by side on a dark desk, one with diagrams and code-like sketches, the other with text and lists, both lit by a single warm amber lantern between them. Two contributors, one shared work, one shared light. Painterly. No text in the image.

## Open questions for Elber

- Reuse "regulated domain where wrong code has consequences" again? Recommendation: yes, it grounds why product clarity matters more in your context (wrong intent shipping faster is worse, not neutral).
- Self-cast as the architect trying to bring product across this line right now? Recommendation: yes, same honest frame that carried post four.
- Any concrete anonymized example of the "make it intuitive" pattern from a real brief, sanitized? It would land harder than my invented example. Skip if it would expose the employer.
- Do you want the post to explicitly call out PMs, or include designers and BAs in the same frame ("the people outside engineering who own intent")? Recommendation: the broader frame. The reasoning applies to anyone who briefs, not only PMs.

## Decisions

- **Employer-neutral, general advice.** No team or colleague named.
- **Respectful of product people.** No "non-tech" othering. The new skill is framed as a skill upgrade for everyone, not a deficiency in one group.
- **Thesis first, mechanics second.** "Foundation has two halves" carries the post; the practical list and the resistance mapping are the support.
- **Series callbacks required.** Posts 2, 4, 5, 6 all referenced.
- **No affiliate links.** Methodology post.
- **Cover generated, not commissioned.** Consistent with posts two through six.

## Sequencing

Post seven in the build-with-AI arc, after the trust-the-pipeline post. Publish after Elber reviews this spec and answers the open questions. Same flow as before: spec, draft to iCloud, review, cover, publish, LinkedIn, then ship the PT-BR translation with the English on his go-ahead (per the updated playbook).
