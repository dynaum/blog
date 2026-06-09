---
title: "It Only Ever Guesses the Next Word"
subtitle: "The model does not decide what to say. It decides the next word, throws everything back in, and decides again. The paragraph you read as one thought was built one guess at a time. Once you see the loop, three things stop being mysterious."
date: 2026-06-08
description: "An LLM has no plan and no stored answer. It predicts one token, appends it, and runs the whole input again. That single loop explains why the same prompt gives different answers, why the model can't plan ahead, and why output costs more than input."
cover: /assets/img/2026-06-08-how-the-model-guesses-next.png
coverAlt: "A single bright amber point on the left extending into a chain of fainter repeating points trailing right, a loop motif lit with a cool teal rim against a near-black background."
---

The model never decides what to say. It decides the next word. Then it throws your whole prompt and that one new word back in, and decides the next word. Then it does it again. A paragraph you read as a single thought was built one guess at a time, hundreds of times over, with no idea at the start where it would end up.

That is the part people skip. They picture the model reading the question, thinking, and writing the answer. What it actually does is run the same small step over and over. Once you see the loop, three things you fight with every day stop being mysterious.

## The loop

Your text becomes tokens, then numbers, then vectors the model can do math on. That is the input path, and it is where most people stop imagining. Here is what happens next.

The model takes that input and produces one thing: [a probability for every token in its vocabulary](https://arxiv.org/abs/2005.14165). Tens of thousands of numbers, each saying how likely that token is to come next. Not the answer. Just the odds on the next single token.

It picks one. It glues that token onto the end of the input. Then it runs the whole thing again, now one token longer, and produces a fresh set of odds for the token after that.

That loop is the entire act of generation. There is no place inside the model where the full answer sits waiting. The model has no idea what its third sentence will be when it writes the first word. It only ever computes the next token, and the reply is what you get after the loop has run a few hundred times. (What lets it weigh the whole input each pass is called [attention](https://arxiv.org/abs/1706.03762). You do not need its machinery to use any of this.)

## Why the same prompt gives different answers

If the model just took the single most likely token every time, the same prompt would always give the same reply. It often does not, and now you can see why.

The model does not have to take the top token. It [samples from the probabilities](https://arxiv.org/abs/1904.09751). The most likely token usually wins, but a less likely one sometimes gets picked, and that one choice changes every token that follows.

[Temperature](https://arxiv.org/abs/2402.05201) is the knob on that. Low temperature pushes the model toward the top choice every time: focused, repeatable, and prone to repeating itself. High temperature flattens the odds so unlikely tokens get a real chance: more varied, more creative, more likely to wander off. The randomness is not a bug in the model. It is a setting you control.

## Why it can't plan ahead

The model commits one token at a time, and it cannot take a token back. Once a word is out, it is part of the input forever, and every later token has to live with it.

So the model writes itself into corners. It starts a sentence one way, and three tokens in there is no graceful finish, but it cannot revise the opening. It can only pick the best next token given the mess it already wrote. A lot of clumsy output is the model committed to a path it would not have chosen with foresight.

This is also why ["think step by step"](https://arxiv.org/abs/2201.11903) works, and it is not a trick. Every token the model generates becomes input for the next pass. When you make it write out its reasoning before the answer, that reasoning is now context the final tokens get to condition on. You are not waking up a smarter model. You are giving the loop more of the right material to stand on before it commits to the part you care about.

## Why output costs more than input

Look at any API price sheet and output tokens cost more than input tokens. The loop explains it.

Your input is [read in one pass](https://arxiv.org/abs/2309.06180). The model ingests the whole prompt together and produces the first set of odds. Output is the opposite. Each output token is a separate run of the model, one after another, because each one depends on the token before it. A 500-token answer is roughly 500 sequential passes.

That sequential work is the cost. It is why output is priced higher, and why a long answer streams out and feels slow while a long prompt gets read almost at once. You are watching the loop turn, one token per tick.

## Close

There is no answer inside the model. There is a loop that guesses the next token, and a set of odds it samples from, and an input that grows by one token each turn.

Everything you steer lives in that input. What you put in front of the loop, how much room you give it to reason, how much randomness you allow. The model runs the step. You shape what the step has to work with. The words are for you. The loop runs on tokens.
