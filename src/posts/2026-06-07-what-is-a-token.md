---
title: "The Model Never Reads Your Words"
subtitle: "You type English. The model reads integers. It never sees a single letter of what you wrote. Understanding the thing in between, the token, is not trivia. It is the difference between guessing at cost, context, and prompt design, and knowing."
date: 2026-06-07
description: "An LLM never sees your text. Your words are translated into tokens, then into numbers, before the model touches them. A plain-language walk through what a token is, and why knowing it makes you better at cost, context limits, and prompt design."
cover: /assets/img/2026-06-07-what-is-a-token.png
coverAlt: "A line of glowing amber text dissolving left to right into a rising stream of floating numerals, the digits lit with a cool teal rim light against a near-black background."
---

You can ship a whole feature on top of an LLM and never know what a token is. I did, for a while. It works right up until the cost surprises you, or a prompt that looks short blows past the context window, or the model does something strange and you have no idle theory for why. All three trace back to one thing you skipped.

Here is the thing. The model never reads your words. You type English. The model reads integers. It does not see a single letter of what you wrote. Between your text and the model sits a translation step, and that step is where most of the surprises live.

## What a token is

A token is a chunk of text. Often a whole word. Often a piece of one.

Tokenization is the step that splits your text into those chunks. Take a sentence:

> The model never reads your words.

A tokenizer might cut that into: `The`, ` model`, ` never`, ` reads`, ` your`, ` words`, `.` Seven tokens. Notice the spaces ride along with the words, and the period is its own token. Common words tend to be a single token. That is why short, plain English is cheap.

Now a rarer word:

> tokenization

That one is not common enough to earn its own slot, so it gets broken into pieces, something like `token` and `ization`. One word, two tokens. The pattern holds across the board. Frequent words map to one token. Rare words, names, code identifiers, and odd spellings split into several.

This is also why models miscount letters and fumble strange words. The model never saw the letters. It saw a couple of chunks. Asking it how many r's are in a word is asking it to inspect something it was never handed.

A rough ratio to keep in your head: about 750 tokens per 1000 English words. Plain prose lands near there. The denser and stranger your text, the more the count climbs.

## From token to number

The chunks are still text, and the model does not work in text. So each token maps to an ID, a plain integer, drawn from a fixed list the model was built with. That list is the vocabulary, tens of thousands of entries, each one a token with a number attached.

So our sentence stops being words at all. It becomes a list of integers, one per token. Something like:

> `464`, `2746`, `2900`, `9743`, `534`, `2456`, `13`

Those exact numbers are illustrative, every model has its own vocabulary, but the shape is real. By the time your prompt reaches the model, it is a row of integers. No English. Just numbers standing in for chunks.

## From number to meaning

A bare integer carries no meaning. `464` is not larger or smaller in sense than `2746`. So one more step runs before the model reasons about anything.

Each token ID becomes a vector, a list of numbers. Not one number, a few hundred or a few thousand of them. That vector is the embedding. It places the token in a space where meaning has geometry. Tokens that mean similar things land near each other. The vectors for `cat` and `dog` sit closer together than the vectors for `cat` and `bicycle`.

This is where the model actually identifies your input. Not at the letters, which it never saw. Not at the integer IDs, which are just labels. At the embeddings, where each chunk has become a position in a space the model can do math on. From here the real work begins. But you already have what you came for.

## Why you should care

Three things you control, all of them token-shaped.

**Cost.** You pay per token, not per word. So the unit on your bill is the chunk, not the sentence. Plain English is dense with common words and cheap. Code, JSON, and structured data are the opposite. Brackets, quotes, indentation, and long identifiers each cost tokens, and they add up fast. A payload that looks small on screen can be twice the tokens you guessed.

**Context.** The context window is measured in tokens, never words. So a prompt that looks short can be heavy. Paste a config file or a stack trace and the token count jumps, because structure tokenizes badly. When you wonder how a few screens of text overflowed the window, this is the answer. You were counting words. The model was counting tokens.

**Prompt design.** The model responds to the tokens it receives, not the words you imagine you sent. Formatting changes the tokens. Word choice changes the tokens. Even whitespace changes the tokens. That is why a small rewrite sometimes shifts the output more than it should. You did not change the idea. You changed the chunks.

## Close

You do not need to count tokens by hand. You need to drop the assumption underneath the surprises.

The model does not read English. It reads numbers, and the path from your words to those numbers is yours to design. Cost, context, and prompt behavior stop being mysterious the moment you see the translation step that was always there. The words are for you. The tokens are for the model.
