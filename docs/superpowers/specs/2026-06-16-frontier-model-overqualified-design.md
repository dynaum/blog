# Design spec: "The Frontier Model Is Overqualified"

## One-sentence pitch

Most of your token bill goes to clerical work billed at frontier rates, and
open-weight models are now good enough to do that cheap tier for cents.

## Goals

- Make the reader check their own token breakdown by task, not just the total.
- Argue that task difficulty is bimodal: a few hard steps, a long clerical tail.
- Show that open-weight models now clear the bar for the easy tier, and cheap
  inference makes that tier nearly free.
- Give a concrete line: which jobs to demote, which to keep on the frontier.
- Name real models and real ways to run them cheap.

## Non-goals (load-bearing)

- Not a benchmark or leaderboard roundup. No score tables.
- Not "open beats closed" and not anti-frontier. The post is about routing work
  to the right tier, not loyalty to a vendor or a license.
- Not a self-hosting tutorial. One paragraph on how, not a setup guide.
- Not about fine-tuning. Off-the-shelf open models only.
- No exact version numbers treated as gospel. Name families and a standout or
  two; the reader re-checks current options. Models churn fast.
- Not naming the employer. Any work anecdote stays anonymized.

## The angle

Spine: open-weight models are the lever. Right-sizing is the why. The frontier
model is overqualified for summaries, extraction, classification, routing,
reranking. You keep paying genius rates for filing because it is one API call
and nobody looked at the breakdown. Open models changed the math: the easy tier
is now cheap enough that not splitting it is the expensive choice.

## Proposed structure

1. Hook: cost-shock. A token bill. The shock is the breakdown, not the total.
   Most of it was clerical, all billed at frontier rates.
2. The insight: difficulty is bimodal. A few hard reasoning steps, a long tail
   of easy ones. Genius rates for clerical work.
3. Why open models changed the math: open-weight families now clear the easy
   tier. Llama, Qwen, Mistral, gpt-oss, Gemma. Not true two years ago.
4. Where the line sits: demote summarize/extract/classify/route/rerank; keep
   multi-step reasoning, code, judgment on the frontier.
5. How to run it cheap: hosted (Groq, Together, Fireworks, OpenRouter) for zero
   ops, or Ollama/vLLM to self-host. One line on a router.
6. The honest caveat: eval the swap, do not trust vibes. Open models churn,
   re-check. Savings only matter at volume.
7. Close: the frontier model is for the hard 10%. Stop sending it your clerical
   work.

## Length and format

Essay, 800-1000 words. First person, architect-by-day builder voice. Cost-shock
opening hook (not the Lanterns game story). Honest, concrete, no hype.

## Links

- Inline link to the cost/efficiency neighbors in the series where natural:
  "Don't Make the Model Do a Build Step" (2026-06-13 tools-own-the-facts) and
  the context-window posts. Keep links optional, no count references.

## Cover plan

Series palette (deep charcoal, honey-amber focal glow, teal rim light). Concept:
a small warm worklamp lighting a wide desk of routine paperwork, a distant
oversized chandelier left dark. The cheap light does the everyday work.

## Open questions

- Real numbers in the hook, or illustrative? Default: illustrative, honest about
  being representative. Confirm at draft review if Elber has real figures.
- Title: "The Frontier Model Is Overqualified" (chosen).

## Decisions

- Spine: open-source as the lever, right-sizing as the why.
- Anchor: a cost-shock moment.
- Concreteness: name models and providers; essay length.
- Title: "The Frontier Model Is Overqualified."
- Date: 2026-06-16 (one day after the latest post).
