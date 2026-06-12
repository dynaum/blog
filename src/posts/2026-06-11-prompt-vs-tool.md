---
title: "What Goes in the Prompt, What Goes in the Tool"
subtitle: "An agent keeps its knowledge in two places, and most broken agents have something on the wrong side. One question decides the split: does this change between calls? No: prompt. Yes: tool."
date: 2026-06-11
description: "Where agent knowledge belongs: stable rules, role, and vocabulary in the prompt, live data and state behind tools. The two mirrored failure modes (stale snapshots in the prompt, conditional behavior buried in tools) and the one-question test that fixes both."
cover: /assets/img/2026-06-11-prompt-vs-tool.png
coverAlt: "A dark workbench split down the middle. On the left, a pinned, well-worn paper contract glows warm amber. On the right, a row of hanging tools catches a muted teal rim light."
---

An agent keeps what it knows in two places. The prompt, which it reads on every turn. And the tools, which it calls when it decides to. Every piece of knowledge you hand an agent lands on one side or the other, and most broken agents I see are broken because something landed on the wrong side.

The failures look unrelated. One agent quotes a price from last Tuesday. Another follows the refund policy on some turns and ignores it on others. Same mistake, mirrored. Here is what it looks like up close.

## Version one: live data in the prompt

Picture an order-support agent for a small store. On build day, the developer pastes the catalog into the system prompt. Product names, prices, what is in stock. The demo is great. The agent knows everything, answers instantly, never makes a tool call. Ship it.

By Friday it lies. Prices changed on Wednesday. The blue lamp sold out on Thursday. The agent keeps quoting Monday's snapshot, and it does so with total confidence, because nothing in its context says the data aged. A model [answers from whatever is in front of it](/posts/2026-06-09-it-never-knows-it-doesnt-know/) and has no channel for "this number is stale." Text in the prompt carries no timestamp the model respects. It is all equally true as far as the model is concerned, forever.

Live data pasted into a prompt is a photograph taped over a window. It looks like the view. It was the view, once.

## Version two: behavior buried in the tool

So the developer fixes it. Inventory and prices move behind a lookup tool. The agent calls it, gets fresh numbers, the lying stops. And while wiring the refund tool, the developer puts the refund policy where it felt local: inside the tool. The thirty-day limit, the receipt requirement, the exceptions, all written into the tool's payload, the place the agent sees when it goes looking.

Now the behavior is conditional. On turns where the agent checks the refund tool, it knows the policy and holds the line. On turns where the customer is persuasive and the agent reasons its way to "this case is obviously fine" without touching the tool, the policy does not exist. The agent grants a refund outside policy, politely and confidently, on exactly the turn the rule was supposed to apply.

A rule the agent must follow on every turn cannot live somewhere the agent visits on some turns. Behavior in a tool is a contract kept in a drawer.

## The rule

For each piece of knowledge, ask one question: does this change between calls?

No: it goes in the prompt. The agent's role, the policies, the vocabulary, the tone, the limits. The things true on every turn, for every customer, until you change them on purpose. This is the [prompt as a contract](/posts/2026-06-03-agents-are-systems-not-prompts/), and a contract only works if it is present every time the agent acts.

Yes: it goes behind a tool. Inventory, prices, order state, account history, today's schedule. Anything with a timestamp. The agent fetches it at the moment of use and gets the current truth instead of a snapshot.

The economics agree with the correctness. Prompt text is a cost you pay on every call, so knowledge earns its seat there by being needed on every call. A tool costs tokens only when used. Misplace in one direction and you pay every turn for data already going stale. Misplace in the other and you save tokens by making your rules optional.

## The third shelf

One honest complication. Some knowledge is stable but too big to ride in every prompt. The full product manual. A style guide. The documentation for a codebase. It changes rarely, so by the rule it is prompt material, but at that size it would drown the context.

That knowledge goes on a third shelf: retrieval. Fetched like a tool, consumed like a prompt. RAG pipelines do this, and so do skill files an agent loads when a task calls for them. The test gains a clause. Stable and small: prompt. Stable and large: retrieved text. Changing: tool. That is the whole extension, and the details are their own post.

## What this is not

- Not a RAG explainer. Retrieval gets a shelf here, not an architecture. No chunking, no embeddings.
- Not about access. What the agent is allowed to reach and do is [its own decision with its own post](/posts/2026-06-04-dont-give-your-agent-root/). This post decides where knowledge lives, not what the agent may touch.
- Not prompt engineering. No phrasing tricks. A perfectly worded policy in the wrong place still fails.

## Close

The prompt is the contract. The tools are the hands. The contract holds what is always true. The hands fetch what is true right now.

Most agents that misbehave are not missing knowledge. They have it on the wrong side of that line, a snapshot doing the job of a lookup, or a rule doing its job only when summoned. Sort every piece of knowledge by its rate of change and the line draws itself.
