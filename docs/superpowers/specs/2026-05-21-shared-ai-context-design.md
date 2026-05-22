# Shared AI Context Post — Design Spec

**Date:** 2026-05-21
**Status:** Draft, awaiting Elber's review.
**Author:** Session co-design (Elber Ribeiro + Claude).

## One-sentence pitch

A post arguing that the context you build with AI in private sessions is a team asset, not a personal one, and that documenting it in a shared knowledge base (Obsidian works well) saves the whole team time and makes AI-DLC easier.

## Framing decision

Employer-neutral, general advice. The post is written for any team, not as a ModMed account. No team or colleague is named. This keeps it safe and keeps the advice broadly useful.

## Goals

- Name the waste: every developer privately re-teaches the AI the same context, and that context dies with the session.
- Reframe AI context as shared infrastructure, the same way code and docs are shared.
- Recommend Obsidian as a practical tool for an AI knowledge base, and explain the one reason it fits.
- Tie the idea to the series: shared context is what keeps the model from wandering (post two) and what makes AI-DLC adoption easier (post four).

## Non-goals (YAGNI)

- An Obsidian setup tutorial. Point at Obsidian, do not teach it step by step.
- A note-tool shootout (Notion vs Obsidian vs others). Recommend Obsidian, note in one line that any folder-of-markdown tool works.
- Naming the employer, a team, or a colleague.
- A deep dive into AI-DLC steering file syntax.
- Selling anything. Obsidian is free for personal use, no affiliate link.

## The core idea

Every session with an AI is a teaching session. You explain the codebase shape, the conventions, the domain rules, the gotchas, the history of why things are the way they are. That teaching is real work and it produces real value.

The problem: the value is private. It lives in one session, one local `CLAUDE.md`, one person's head. The session ends and most of it evaporates. The next teammate opens a fresh session and re-teaches the model the same things. The team pays the same tax over and over, and nobody sees the meter running.

The reframe: AI context is infrastructure. The knowledge base you build for your own AI is the same knowledge base your teammates need. It should be shared, durable, and versioned, like code.

## Why Obsidian

The key reason, stated once and clearly: an Obsidian vault is a plain folder of Markdown files. Humans read it through a clean interface with links and a graph. An AI agent reads the exact same files directly, with no export step. The knowledge base humans maintain and the knowledge base the AI consumes are one thing, not two.

Supporting reasons, kept brief:
- Bidirectional links connect context. A system note links to the principle behind it.
- It is git-friendly, so the knowledge base versions alongside the work.
- Any folder-of-Markdown tool works. Obsidian is a good default, not the only answer.

## A structure that works

- A `principles/` folder for the durable "how we think" rules.
- A folder per system or domain for the specifics.
- Each note small and single-topic, linked to the others.

This mirrors a structure Elber already uses. The post presents it as a recommendation, not a personal tour.

## What belongs in it

The gotchas, the "why" behind decisions, the domain vocabulary, the non-obvious constraints, the dead ends already explored. The test: if you would explain it to a new hire on their first week, and you would also explain it to a fresh AI session, it belongs in the shared base. New hires and fresh sessions need the same things.

## The AI-DLC payoff

AI-DLC runs on steering files, which are shared rule files. A team with a real shared context base already has the raw material. The steering files become a curation of the knowledge base, not a writing job from scratch. Better shared context lowers the friction that blocks AI-DLC adoption. That is the callback to post four: friction is what stalls adoption, and good context removes it.

## Proposed structure

1. **Hook:** every AI session is a teaching session, and the teaching is being thrown away.
2. **The waste:** private context, the per-person re-teaching tax.
3. **The reframe:** AI context is infrastructure, not a personal artifact.
4. **Why Obsidian:** the one key reason (same files for humans and the AI), plus the brief supporting reasons.
5. **A structure that works:** principles folder, folder per system, small linked notes, and what belongs inside.
6. **The AI-DLC payoff:** shared context feeds steering files and eases adoption. Callbacks to posts two and four.
7. **Close:** the context you build today is the time a teammate does not lose tomorrow. Stop hoarding it.

Target length: 700 to 900 words.

## Working title

**"Your AI Context Belongs to the Team"**

Alternative titles:
- "Stop Re-Explaining the Codebase"
- "Context Is a Team Sport"
- "The Knowledge Base Nobody Shares"

## Links

- Obsidian: https://obsidian.md/
- Internal link: the spec-driven loop post, `/posts/2026-05-19-the-spec-driven-loop/`
- Internal link: the AI-DLC post, `/posts/2026-05-21-you-cannot-push-a-developer/`

## Cover image plan

Same FLUX pipeline and dark amber-and-teal palette as posts two through four. Concept: a painterly constellation of small glowing amber notes or cards, connected by fine threads of teal light, like a shared map or a knowledge graph seen in the dark. It pictures linked, shared context without any text. Reuse `src/assets/img/` and the `cover` frontmatter field.

## Open questions for Elber

- Reference your own Obsidian vaults as a concrete example, or keep it a general recommendation? Recommendation: a light first-person mention ("I keep a vault with a principles folder and a folder per system"), no detail beyond that.
- Mention `CLAUDE.md` / `AGENTS.md` as the in-repo context layer, with Obsidian as the broader base? Recommendation: yes, one sentence. It grounds the idea.
- Recommend a specific sharing mechanism (git vs Obsidian Sync), or stay mechanism-agnostic? Recommendation: mechanism-agnostic, mention git in passing.
- Any anonymized anecdote about context being re-explained, or keep it general? Recommendation: general is fine.

## Decisions

- **Employer-neutral, general advice.** No team or colleague named.
- **Obsidian recommended, with one clear reason.** The same-files point is the load-bearing argument. Other tools acknowledged in one line.
- **Series callbacks required.** Post two (context keeps the model from wandering) and post four (shared context eases AI-DLC adoption).
- **No affiliate link.** Obsidian is free for personal use.
- **Cover generated, not commissioned.** Consistent with posts two through four.

## Sequencing

Post five in the build-with-AI arc, after the AI-DLC post. Target date 2026-05-22. Same flow: spec, draft, review, publish. No publish without Elber's go-ahead.
