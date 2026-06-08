# Design spec: "The Model Never Reads Your Words"

## One-sentence pitch

A first-principles explainer of what a token is, framed so that understanding it makes you a better builder: it explains cost, context limits, and prompt design.

## Goals

- Explain what a token is, in detail and in plain language, for a developer who uses LLMs but never looked under the hood.
- Trace the input path: text → tokens → token IDs (integers) → embeddings (vectors).
- Cash the concept out in three things the builder controls: cost, context limits, prompt design.
- Carry one worked example through the mechanics so the abstraction stays concrete.

## Non-goals (load-bearing)

- No attention, no transformer architecture, no next-token prediction mechanics. Stop at embeddings.
- No training. How embeddings get learned is out of scope.
- No tokenizer-algorithm detail. BPE may be named once, not explained.
- Not a tooling tutorial. No "here is how to count tokens with this library" walkthrough.
- No math. Vectors are described as lists of numbers, not derived.

## The angle

Tokens are not trivia, they are leverage. A builder can ship a whole feature on an LLM and never know what a token is. It works until cost, context, or weird behavior bites. The post starts from the gap (the model never sees your words) and ends on control (the translation is yours to design).

## Hook

The reveal. You type English. The model reads integers. It never sees a single letter of what you wrote. Everything you send is translated before the model touches it.

## Depth

text → tokens → token IDs → embeddings. Stop before attention.

## Proposed structure

1. **Hook.** The model never sees your words. It sees numbers. The input is translated before the model touches it.
2. **What a token is.** The detailed core. A token is a chunk of text, often a whole word, often a piece of one. Tokenization splits your text into these chunks. Show a real sentence broken up. Common words are one token, rare words split into several, spaces and punctuation count. Rough ratio ~750 tokens per 1000 English words.
3. **From token to number.** Each token maps to an ID, an integer in a fixed vocabulary. The model receives a list of integers. Show a short string becoming a few IDs.
4. **From number to meaning (embeddings).** Each ID becomes a vector, a list of numbers the model can do math on. Similar meanings sit near each other. This is where identifying the input actually happens. Stop here.
5. **Why you should care.** Three payoffs, each tied back to tokens:
   - Cost. You pay per token, not per word. Code and JSON are token-dense.
   - Context. The window is measured in tokens. A short prompt full of structure eats more than you would guess.
   - Prompt design. Formatting and word choice change the tokens the model sees, so they change the output.
6. **Close.** You do not need to count tokens by hand. You need to stop thinking the model reads English. It reads numbers, and the translation is yours to design.

## Length

Essay range, ~850-950 words.

## Links

- Optional inline link to a tokenizer playground (e.g. the OpenAI/Tiktokenizer demo) so a reader can see tokenization live. Decide during draft; keep it optional.

## Cover plan

A line of glowing text dissolving into a stream of floating numbers. Warm amber where letters become digits, teal rim light on the numeric stream. Series palette appended by the tool.

## Open questions

- Which model's vocabulary to gesture at for the worked example? Keep it generic (no exact IDs claimed as real) to avoid being wrong about a specific tokenizer. Decision: use illustrative IDs, label them as illustrative.
- Link to a live tokenizer or not? Decision: optional, add if it reads naturally.

## Decisions

- Angle B (better builder), depth B (tokens → embeddings), hook A (the reveal).
- Payoffs: cost, context, prompt design.
- Date: 2026-06-07.
- Worked example: one short sentence, carried from tokens through IDs. Illustrative IDs, labeled as such.
