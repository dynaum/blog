# AI-DLC Adoption Post — Design Spec

**Date:** 2026-05-20
**Status:** Draft, awaiting Elber's review.
**Author:** Session co-design (Elber Ribeiro + Claude).

## One-sentence pitch

A field-note post on how hard it is to move a large engineering org onto AWS AI-DLC, why good developers resist a mandated methodology for legitimate reasons, and what actually changes minds.

## Framing decision (locked)

The employer is **not named** anywhere in the post or in this spec. Elber writes as an architect inside "a large engineering org" and, where it matters, "a regulated domain where wrong code has consequences." The post treats developers who have not adopted AI-DLC with respect: it states their real reasons first, then answers them. No colleague is called out. This protects Elber professionally and produces a more persuasive post. Keeping the spec employer-neutral also makes it safe to commit to the public blog repo alongside the post.

## Goals

- Explain AWS AI-DLC clearly to the blog's audience.
- Tell the honest story of methodology adoption: the pitch is easy, the adoption is hard.
- Steelman the resistance. Give the five real reasons good developers hold back, with no strawman.
- Land a reframe: you do not push developers toward a methodology, you remove the reasons to say no.
- Tie the post to the series (AI-DLC as the institutional version of the spec-driven loop) and to the Trust idea from the Frictionless post.

## Non-goals (YAGNI)

- Naming the employer, a team, a manager, or any colleague.
- A setup tutorial for AI-DLC. AWS docs and the open-source repo cover that.
- Selling AI-DLC as a finished verdict. Elber is mid-adoption, the post says so.
- Repeating AWS's 10-15x productivity claim as fact. If cited, it is cited as a claim and then questioned.
- A change-management framework with a name and a diagram. This is a field note, not a methodology of its own.

## Topic background: what AWS AI-DLC is

- **AI-Driven Development Lifecycle (AI-DLC).** Introduced by AWS at re:Invent 2025.
- AI is a core collaborator under human oversight. AI plans and executes, humans hold the decisions.
- Replaces sprints with **bolts**, short cycles measured in hours or days.
- Three phases: **inception** (requirements and planning), **construction** (design, code, test), **operations** (deploy).
- Enforced by **steering files**, rule files that constrain how the agent works. Agent, IDE, and model agnostic, works across 7+ coding assistants.
- Open-sourced at `github.com/awslabs/aidlc-workflows`.
- AWS cites 10-15x productivity gains from early customers.

The honest hook: AI-DLC is close to the institutional version of the spec-driven loop from post two. Inception maps to brainstorm-plus-spec. Steering files map to the rules and non-goals. Elber believed in this before AWS branded it, which is exactly why he is now the one trying to drive its adoption.

## The angle

Elber is the one doing the pushing. He is an architect advocating AI-DLC inside his org. The post is self-aware about that. It is the story of the pusher learning that pushing does not work. That self-cast is what keeps the post honest instead of preachy.

The post corrects its own premise. The brief was "how hard it is to push developers in one direction." The post's answer: push is the wrong verb, and naming the wrong verb is the whole lesson.

## The heart of the post: steelman the resistance

Five real reasons good developers have not adopted AI-DLC yet. Each one stated with respect, no strawman.

1. **They have been burned by mandated process.** Engineers have lived through Agile theater and heavyweight frameworks that added ceremony and removed autonomy. A new mandated methodology pattern-matches to "more process to perform." That pattern-match is earned, not lazy.
2. **The productivity claim reads as vendor marketing.** "10-15x" is not credible to a professional skeptic until they see it on their own codebase. Discounting an unfalsifiable number is good engineering judgment.
3. **Their current workflow already works.** A fast, effective senior developer has a real working loop in their head. Switching to bolts and steering files has a concrete cost and an uncertain payoff. Holding the status quo is a rational position, not resistance for its own sake.
4. **AI output still has to be reviewed, and review is the bottleneck.** If a developer does not yet trust the agent's output, AI-DLC moves the work from writing to reviewing. In a regulated domain where wrong code has consequences, the caution behind that is correct.
5. **It is top-down.** Methodology pushed from leadership or an architecture group triggers autonomy resistance. People adopt what they choose and resist what they are assigned.

**The turn:** every one of those five reasons is about trust or friction, not laziness. That is the bridge back to the Frictionless post. Trust has to be built, and friction has to be removed. A mandate does neither.

## What actually moves an org

- **Show, do not tell.** One real win on a real codebase beats any deck or any productivity number.
- **Kill the first-week friction.** Ship the steering files pre-configured. Make the on-ramp instant. Most people who quit a tool quit it in week one.
- **Make the default path the good path.** Adoption should be the easy choice, not the disciplined one.
- **Let peers convert peers.** Adoption travels sideways between engineers who trust each other, not down from a memo.
- **Accept an uneven pace.** Not everyone adopts at once, and that is fine. Pace layers are normal.

## The reframe (closing)

You cannot push a developer toward a methodology. The verb was wrong from the start. You remove the friction, you answer the real objections, you make the win visible, and people walk there on their own. Pushing is hard because pushing is the wrong physics.

## Proposed structure

1. **Hook:** the "push them in one direction" premise, plus the confession that Elber is the one pushing.
2. **What AI-DLC is**, briefly, and the honest note that it formalizes what he already believed. Link to post two.
3. **The pitch is easy, the adoption is not.** Set up the gap.
4. **The steelman:** the five real reasons, each with respect.
5. **The turn:** all five are trust and friction. Callback to the Frictionless post.
6. **What actually moves an org:** the five moves above.
7. **The reframe:** you do not push a developer. Close.

Target length: 800 to 1000 words. Meatier than the Frictionless recommendation, closer to post two.

## Working title

**"You Cannot Push a Developer"**

Subtitle: *Adopting AWS AI-DLC across an engineering org taught me the verb was wrong. You do not push people toward a methodology. You remove the reasons to say no.*

Alternative titles:
- "The Hardest Part of AI-DLC Is Not the AI"
- "Adoption Is Not a Mandate"
- "Bolts, Steering Files, and the People Who Have Not Switched Yet"

## Links

- AWS DevOps blog, AI-DLC introduction: https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/
- AWS DevOps blog, open-sourcing the AI-DLC workflows: https://aws.amazon.com/blogs/devops/open-sourcing-adaptive-workflows-for-ai-driven-development-life-cycle/
- Open-source workflows repo: https://github.com/awslabs/aidlc-workflows
- Internal link: the spec-driven loop post, `/posts/2026-05-19-the-spec-driven-loop/`
- Internal link: the Frictionless post, `/posts/2026-05-20-frictionless-the-book-behind-the-loop/`

## Cover image plan

Same FLUX text-to-image pipeline and dark amber-and-teal palette as posts two and three. Concept: a scattering of small desk lanterns across a dark room, some glowing warm amber, some still unlit, no two at the same brightness. It pictures uneven adoption honestly, without scolding the unlit ones. No text in the image. Reuse `src/assets/img/` and the `cover` frontmatter field.

## Open questions for Elber

- Are you comfortable being self-cast as the architect who was doing the pushing and learned it does not work? It is the strongest frame, and it is personal.
- Is "a regulated domain where wrong code has consequences" an acceptable level of specificity? It points at healthcare without naming the employer.
- Do you have one anonymized, non-confidential objection a colleague actually raised that we can use as a concrete example? It would make the steelman land harder.
- Should AWS's 10-15x claim appear at all? Recommendation: cite it once, then question it, since questioning it is on-message.
- Is this post four of the build-with-AI series, or a standalone? Recommendation: post four. It fits "field notes," and the series callbacks are strong.

## Decisions

- **Employer unnamed throughout.** Locked by Elber. Applies to the post and to this spec, so the spec is safe to commit publicly.
- **Steelman before answer.** The five resistance reasons come before any rebuttal. Respect first.
- **The post corrects its own premise.** "Push" is named as the wrong verb. That is the thesis.
- **No affiliate links.** This is a methodology post, not a recommendation.
- **Series callbacks to posts two and three are required.** Trust and friction tie the arc together.
- **Cover generated, not commissioned.** Consistent with posts two and three.

## Sequencing

Post four in the build-with-AI arc, after the Frictionless post. Publish after Elber reviews this spec and answers the open questions. Same flow as before: spec, draft, review, publish. No publish without Elber's go-ahead.
