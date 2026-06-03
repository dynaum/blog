# The Five I Actually Run — Design Spec

**Date:** 2026-06-02
**Status:** Draft, awaiting Elber's review.
**Author:** Session co-design (Elber Ribeiro + Claude).

## One-sentence pitch

A short recommendation post naming the five tools the author runs daily, framed not as a trending roundup but as the principles this series argued for, now shipped as installable software, with one honest section on the limits.

## Framing decision

Principles-now-installable, not a listicle. The series has spent fifteen posts arguing for a method, shared context, memory, trusted tests, and the judgment a model lacks. This post shows those ideas have become tools you can install. The recommendation is earned by the track record, not by what trends. Anti-hype guardrail: no star counts (sources disagree and the numbers are commonly hallucinated), no rankings, plain links, and one honesty section. First-person architect voice. Day job stays anonymized.

## Goals

- Land the framing: I recommend these because they are the principles of this blog made installable, not because they trend.
- Name five real tools, each tied to a past post, each described accurately.
- Keep it tight (~750 words), so each tool gets three to four honest sentences, not a brochure.
- Close honestly: one section on what this is not (not a buyer's guide, tools change, your stack will differ).
- Stay accurate. Verified facts only. No star counts. Obsidian has no official MCP; do not imply one.

## Non-goals (YAGNI)

- A ranked top-N or a comprehensive market survey. Five tools I run, not the best five that exist.
- Install tutorials or config walkthroughs. Link the repo, do not document it.
- Star counts or popularity numbers. Sources disagree; omit entirely.
- Affiliate links. These are free or open-source tools; plain links only.
- Restating the posts each tool maps to. One line of callback each, not a re-argument.
- Naming the employer, a team, or a colleague.

## The five tools (verified facts)

Each: what it is (accurate), the principle/post it maps to, why I run it. Three to four sentences.

1. **Superpowers** ([github.com/obra/superpowers](https://github.com/obra/superpowers), Jesse Vincent). An agentic skills framework that enforces a structured workflow: spec, plan, TDD, systematic debugging, shipped as a Claude Code plugin that also works across other agents. This is the [spec-driven loop](/posts/2026-05-19-the-spec-driven-loop/) as installable software. I run it because it forces the discipline on the days I would skip it.

2. **claude-mem** ([github.com/thedotmack/claude-mem](https://github.com/thedotmack/claude-mem), Alex Newman). A persistent-memory plugin that captures what the agent did in a session, compresses it, stores it locally, and feeds the relevant parts into future sessions, so context survives across sessions and compaction. This is [fix the system, not the output](/posts/2026-05-31-fix-the-system-not-the-output/) automated: the decision is remembered without me re-explaining it.

3. **Obsidian** ([obsidian.md](https://obsidian.md)). A local-first Markdown notes app; a vault is a plain folder of files an agent can read directly. This is [your AI context belongs to the team](/posts/2026-05-22-your-ai-context-belongs-to-the-team/), the durable knowledge base. Honest note: there is no official MCP server, the integrations are community-built, but the plain-folder format is the point.

4. **Playwright MCP** ([github.com/microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp), Microsoft). The official MCP server that lets an agent drive a browser through structured accessibility snapshots, not screenshots. This is the record-then-refine half of [trust the pipeline](/posts/2026-05-23-trust-the-pipeline/): the agent works the real UI, you keep the trusted tests.

5. **ui-ux-pro-max** ([github.com/nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)). A UI/UX design-intelligence skill: styles, color palettes, font pairings, layout and UX guidance the model pulls from when building interfaces. This is the taste a raw model lacks, the gap [don't just use the model](/posts/2026-05-30-dont-just-use-the-model/) named, packaged as a skill. Opinionated by design, which is the value.

## What this is not (the honesty section)

One block at the end.

- Not a buyer's guide or a ranked top-five. These are the ones I run, not a claim about the whole field.
- Not permanent. This list is true today. Tools in this space turn over fast; the principles outlast any of them.
- Not your stack. Yours should match your work. Take the principle, pick the tool that fits, and swap when a better one ships.
- No affiliation. I run these unpaid. No sponsorship, no affiliate links.

## Series callbacks

The whole post is callbacks by design, one line each, mapping a tool to the post that argued its principle. The meta-point in the close: the series stopped being only ideas. The ideas now have install commands.

## Proposed structure

1. **Hook.** I do not recommend tools because they trend. I recommend the five that turned ideas this blog argued for into software I open every day.
2. **The five.** One short block each: what it is, the principle it maps to, why I run it.
3. **What this is not.** The honesty block.
4. **Close.** The series was a set of principles. Now the principles ship as plugins. Take the idea first, the tool second.

Target length: about 750 words.

## Working title

**"The Five I Actually Run"** (approved)

Subtitle (draft): *Not a trending roundup. Five tools that turned the principles this blog has argued for into software I open every day, each one tied to the post that made the case.*

## Links

External (plain, no affiliate):
- Superpowers, https://github.com/obra/superpowers
- claude-mem, https://github.com/thedotmack/claude-mem
- Obsidian, https://obsidian.md
- Playwright MCP, https://github.com/microsoft/playwright-mcp
- ui-ux-pro-max, https://github.com/nextlevelbuilder/ui-ux-pro-max-skill

Internal:
- The spec-driven loop, `/posts/2026-05-19-the-spec-driven-loop/`
- Your AI context belongs to the team, `/posts/2026-05-22-your-ai-context-belongs-to-the-team/`
- Trust the Pipeline, `/posts/2026-05-23-trust-the-pipeline/`
- Don't Just Use the Model, `/posts/2026-05-30-dont-just-use-the-model/`
- Fix the System, Not the Output, `/posts/2026-05-31-fix-the-system-not-the-output/`

## Cover image plan

Same FLUX pipeline and dark amber-and-teal palette as the series. Concept: five well-used hand tools laid out in a row on a dark workbench, each different, each catching the warm amber light, with cooler teal rim light along the metal. A curated, personal toolkit, not a store shelf. Painterly, soft bloom, brushstroke texture. No text.

## Open questions for Elber

- Five tools at ~750 words is tight (about 110 words each). Hold the five, or cut to four for more room each? Recommendation: hold five, keep each lean. The reader wants the map, not an essay per tool.
- Obsidian has no official MCP. State that caveat inline (as planned) so the post stays accurate? Recommendation: yes, one honest clause.
- Order of the five. Proposed: Superpowers, claude-mem, Obsidian, Playwright MCP, ui-ux-pro-max (method, memory, knowledge, testing, design). Recommendation: keep this order; it walks the build cycle.

## Decisions

- **Principles-now-installable framing.** Each tool maps to a past post.
- **Five tools, ~110 words each**, verified facts, no star counts.
- **One honesty section**, plus the Obsidian-MCP caveat inline.
- **Plain links, no affiliate, no sponsorship.**
- **Cover generated, not commissioned. Day job anonymized.**

## Sequencing

Latest post in the build-with-AI arc, after `2026-06-01-know-when-to-stop`. Same flow: spec, draft for inline review, cover once approved, publish EN + PT-BR together, update the vault catalog, then the LinkedIn teaser (English only, links the English post).
