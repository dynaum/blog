# Design spec: Don't make the model do a build step

## One-sentence pitch

The context an AI needs splits into facts and judgment; facts like a code graph,
API surface, and dependency map can be generated deterministically from source
and kept fresh on every commit, so asking an LLM to produce or maintain them is
slower, costs tokens, and rots.

## Goals

- Make one clean argument: tools own the facts, the LLM owns judgment.
- Give the reader three concrete, deterministic artifacts they can generate today:
  code graph, API surface, dependency/arch map.
- Name the boundary case (product view / intent) that proves the rule: the one
  map no tool and no LLM can derive, so a human writes it.
- Reframe documentation for AI as a build step, not a writing task.

## Non-goals

- Not a tools tutorial. No tree-sitter, ctags, or OpenAPI walkthrough. Name the
  category, not the config.
- Not anti-LLM. The model is the point; it just shouldn't invent the facts.
- Not a repeat of the human-context posts. "Your AI Context Belongs to the Team"
  and "Context Is Not a Dev Job" covered intent written by people. This post
  covers facts derived from source. The product view is named only as the
  boundary, not re-explained.
- Not a Conduit ad. The freshness echo is one light line, optional inline link.

## The angle

The divide. The context an agent needs has two kinds of input:

- **Facts, derived from source.** Code graph (who defines, who calls), API
  surface (types, routes, schemas), dependency/arch map (module boundaries,
  direction, what's deprecated). A script reads the AST. The truth comes from the
  code, not a guess. Deterministic, cheap, always fresh on commit.
- **Judgment, the LLM's job.** Reasoning over those facts plus stated intent to
  write the change.
- **Intent, written by a human.** The product view: goal, non-goals, success
  criteria. The one thing neither a tool nor an LLM can derive, because it isn't
  in the source. This is the boundary case.

The mistake is making the model do the first kind. Every session an agent greps
to rebuild a map a build step could have handed it. You pay tokens and latency to
re-derive what never changed, and you trust a guess where you could have had a
fact.

## Proposed structure (essay, ~800-1000 words)

1. **Hook (real pain).** Watch an agent grep the same files every session to
   rebuild the same map. A 2-second script already knows the answer. You're
   paying the model to be a worse version of a build step.
2. **The split.** Facts vs judgment. Name it plainly.
3. **The deterministic three.** Code graph, API surface, dependency/arch map.
   Generated, committed, regenerated on every push. No LLM in the loop. The truth
   is in the source; a tool just reads it.
4. **The boundary case.** The product view. The one map a tool can't build,
   because intent lives in heads, not source. A human writes it once. It's the
   LLM's other input. (Light link back to the human-context posts.)
5. **Why this beats letting the model do it.** Cost, speed, trust. A generated
   map can't be out of date; an LLM's mental model is stale the moment code
   changes. Freshness comes from a pipeline, not an author (light Conduit echo,
   optional inline link).
6. **Close.** Stop asking the model to be a worse build step. Hand it a fresh map
   and a clear intent, then let it think.

## Links

- Internal: "Your AI Context Belongs to the Team" (2026-05-22), "Context Is Not a
  Dev Job" (2026-05-24) for the intent half; "Conduit" (2026-06-12) for the
  freshness-from-a-pipeline echo. Inline, optional.

## Cover plan

Series palette. Concept: a deep charcoal scene where a glowing amber blueprint or
wiring diagram of a structure is being drawn by a mechanical/automated line of
teal light, machine-precise, no human hand. The map draws itself. Brushstroke
texture, soft bloom, no text.

## Open questions

- Title: "Don't Make the Model Do a Build Step" vs "Let the Build Step Write the
  Docs" vs something tighter. Decide in the draft.

## Decisions

- Spine: don't use an LLM for what a build step can do (economic + reliability).
- Anchor artifacts: all four (code graph, API surface, product view, dependency/
  arch map), with the product view framed as the boundary case.
- Throughline: lead from the real pain, then generalize.
- Length: essay field note, ~800-1000 words.
- Date: 2026-06-13 (one day after the Conduit launch post).
