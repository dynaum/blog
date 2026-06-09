# Design spec: "It Only Ever Guesses the Next Word"

## One-sentence pitch

The sequel to the token post: the model has no plan and no stored answer, it predicts one token, appends it, and runs again, and that loop explains why output is random, can't plan ahead, and costs more than input.

## Goals

- Explain the next-token loop in plain language, picking up exactly where the token post stopped (at embeddings).
- Land the core surprise: there is no answer inside the model, only the next token, predicted over and over.
- Cash it out in three builder-facing payoffs: sampling/temperature, no planning ahead, output cost.
- Stand alone. A reader can land here cold; link back to the token post optionally, do not depend on it.

## Non-goals (load-bearing)

- No attention mechanics. One sentence names that attention is what does the looking-back, then moves on.
- No transformer internals, no training, no math of sampling.
- top-p / top-k may be named once, not explained or derived.
- Not a decoding-strategy or temperature-tuning how-to.

## The angle

Same as the series: mechanics as builder leverage, not trivia. The model does not compose a reply. It guesses a token, appends it, and re-runs the whole input. Understanding the loop demystifies three things builders hit every day.

## Hook

The scale confession. The model never decides what to say. It decides the next word, throws everything back in, and decides again. A paragraph you read as one thought was built one guess at a time, hundreds of times over.

## Scope

Black box. The model takes the token vectors and outputs a probability for every token in its vocabulary. No internals.

## Proposed structure

1. **Hook.** The scale confession. One thought, built hundreds of guesses at a time.
2. **The loop.** Input becomes vectors (one-line callback to the token post). The model outputs a probability for every token in the vocabulary. It picks one. It appends that token to the input and runs again. The loop is the whole thing. The answer is never computed up front.
3. **Why the same prompt gives different answers (payoff A).** It samples from the probabilities instead of always taking the top one. Temperature is the knob: low is focused and repetitive, high is varied and risky. A choice, not a flaw.
4. **Why it can't plan ahead (payoff B).** Each token is committed with no backtracking. It writes into corners. This is also why "think step by step" works: every token it generates becomes input it can condition on, so producing reasoning first gives the final answer better ground.
5. **Why output costs more than input (payoff D).** Input is read in one pass. Output is generated one token at a time, each a full run of the model. The sequential work is why output tokens cost more and why long answers feel slow.
6. **Close.** No answer inside the model. A loop, and you shape what it conditions on. Tie back: the words are for you, the loop runs on tokens.

## Length

Essay, ~850-950 words.

## Links

- Optional inline link back to "The Model Never Reads Your Words" (2026-06-07-what-is-a-token) at the embeddings callback. Keep optional, post stands alone.

## Cover plan

A single bright amber point extending into a chain of fainter repeating points, a loop or sequence motif. Teal rim light, near-black ground. Series palette appended by the tool.

## Open questions

- Name top-p/top-k? Decision: name temperature only in the body, leave top-p/top-k out unless a sentence reads naturally. Keep the sampling section about the idea, not the knobs.
- How explicit on "think step by step"? Decision: explain it as a consequence of the loop, not as a prompting tip section. One tight paragraph.

## Decisions

- Sequel to the token post, picks up at embeddings.
- Scope A (black box), payoffs A (sampling/temperature), B (no planning), D (output cost), hook A (scale confession).
- Date: 2026-06-08.
- One sentence names attention exists, no mechanics.
