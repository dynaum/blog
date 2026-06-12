# Design spec: What Goes in the Prompt, What Goes in the Tool

- **Post file:** `src/posts/2026-06-11-prompt-vs-tool.md`
- **Date:** 2026-06-11 (one day after the desk post)
- **Type:** Essay, 800 to 1000 words
- **Thread:** Systems. Pairs with "Agents Are Systems, Not Prompts" and "Don't Give Your Agent Root".

## One-sentence pitch

An agent holds knowledge in two places, the prompt and the tools, and most broken agents put the right knowledge in the wrong place: stable knowledge belongs in the prompt, live knowledge belongs behind a tool.

## Goals

- Give the reader one portable decision rule: for each piece of knowledge, ask "does this change between calls?" No: prompt. Yes: tool.
- Name both failure modes as the same mistake mirrored, and show each one concretely.
- Connect the systems thread: the prompt is the contract (systems post), the tools are the hands (root post), this post decides what goes where.
- Acknowledge the middle ground (retrieval) honestly in one short section without turning into a RAG post.

## Non-goals

- **Not a RAG explainer.** Retrieval appears as the third shelf in one section. No chunking, no embeddings, no vector stores, no architecture diagrams.
- **Not about tool access or security.** What the agent is allowed to reach and do is the Root post's territory. This post is about where knowledge lives, not what it may touch.
- **Not prompt-engineering tips.** No wording tricks, no "magic phrases". Placement only.
- **Not about MCP mechanics.** The Root post covered the plug. Tools here are abstract: a function the agent calls.
- **Not a framework discussion.** No LangChain, no CrewAI. The rule holds in any framework.

## The angle

Two failure modes, one mistake mirrored:

1. **Live data pasted into the prompt.** Inventory, prices, account state, today's schedule, dumped into the system prompt at build time or session start. Stale by the second call. The agent answers from a snapshot with full confidence, because it has no signal the data aged. Links to "It Never Knows That It Doesn't Know".
2. **Behavior buried in the tool.** Rules, tone, vocabulary, policy stuffed into tool descriptions or return payloads. The agent only sees them when it happens to call that tool, so behavior that should be constant becomes conditional. The agent is polite on the turns it checks the order status and unguarded on the turns it does not.

The fix is rate of change. The prompt is for what is true on every call: role, rules, vocabulary, tone, limits. The tool is for what is true right now: data, state, lookups, anything with a timestamp.

## Worked example

One fictional, realistic support/triage agent (an order-support agent for a small store), shown three times and threaded through the post rather than boxed in its own section:

1. Version one: the day's inventory and prices pasted into the system prompt. Works in the demo, lies by Friday.
2. Version two: the refund policy moved into the refund tool's description. The agent grants a refund outside policy on a turn where the tool was never called.
3. The fixed split: policy, tone, and limits in the prompt; inventory, prices, and order state behind tools.

## Proposed structure

1. **Hook.** An agent keeps its knowledge in two places. Most broken agents are broken because something is on the wrong side. Do not open with the Lanterns story.
2. **The broken agent, version one.** Live data in the prompt. The stale-snapshot failure.
3. **The broken agent, version two.** Behavior inside the tool. The conditional-behavior failure.
4. **The rule.** Stable vs live. The one-question test: does this change between calls? Tie back to prompt-as-contract and context-as-budget.
5. **The third shelf.** Retrieval (RAG, skill files, fetched docs): knowledge stable enough to be text but too big to ride in every prompt. Fetched like a tool, consumed like a prompt. One short section, no architecture.
6. **What this is not.** Honest bullets mirroring the non-goals: not a RAG post, not about access (that is the Root post), not prompt tricks.
7. **Close.** The prompt is the contract. The tools are the hands. Knowledge goes where its rate of change says it goes.

## Links

- `/posts/2026-06-03-agents-are-systems-not-prompts/` — prompt as contract, context as budget.
- `/posts/2026-06-04-dont-give-your-agent-root/` — tools as hands, scoped access.
- `/posts/2026-06-09-it-never-knows-it-doesnt-know/` — confident answers from thin or stale ground.

## Cover plan

Series palette via `tools/gen-cover.py`. Concept: a dark workbench split in two, on one side a pinned, well-worn paper contract glowing warm amber, on the other a row of hanging tools with teal rim light, the split line down the middle of the bench.

## Open questions

- None outstanding. Angle (stable vs live), example (one agent, both mistakes), format (essay), and the retrieval middle ground (one section, third shelf) were settled in review on 2026-06-11.

## Decisions

- **Core rule:** stable vs live knowledge, decided by rate of change. Chosen over a pure cost/context-budget framing and a trust-boundary framing. Cost shows up as a supporting argument inside the rule section, not the headline.
- **Example:** one fictional order-support agent shown with both mistakes, then fixed. Chosen over using the blog's own tooling and over a checklist-only post.
- **Format:** essay (800 to 1000 words), matching the other systems posts, including the "What this is not" section.
- **Retrieval:** gets one short section as the third shelf. Not folded silently into tools, not deferred entirely.
- **Slug:** `prompt-vs-tool`, short, matches the backlog name.
