# Agents Are Systems, Not Prompts — Design Spec

**Date:** 2026-06-03
**Status:** Draft, awaiting Elber's review.
**Author:** Session co-design (Elber Ribeiro + Claude).

## One-sentence pitch

An essay arguing that building an agent to run in your own system is systems engineering, not prompt-writing, with the four decisions that actually decide whether it works (understand the problem, control memory, manage context, match the model to the task) plus a three-part system prompt (behavior, guardrails, limits), and the framework choice treated as the easy, late part.

## Framing decision

Systems-not-prompts. This is the first post in the series about building agents the developer runs themselves (with LangChain or CrewAI), as opposed to using Claude Code or hosted tools. The thesis: a production agent is architecture, and the framework is the smallest decision in it. The honest, durable substance is the four upstream decisions plus the prompt structure. First-person architect voice. Day job anonymized as "a regulated domain where wrong code has consequences." Tools and MCP are explicitly out of scope; they are the next post.

## Goals

- Land the thesis: an agent is a system, not a clever prompt in a loop. Memory, context, model routing, and guardrails are architecture decisions.
- Make "the framework is the easy part" concrete: name LangChain (LangGraph) and CrewAI as the two reference points, say the choice matters less than the four decisions, move on.
- Give the four decisions real weight: understand the problem, control memory, manage context, match the model to the task.
- Give the system prompt a clear three-part structure: behavior, guardrails, limits.
- Tie to the series spine and the foundation theme: the decisions before the build are what make it work.

## Non-goals (YAGNI)

- Tools and MCP. Explicitly deferred to the next post. Do not describe tool-calling, function schemas, or MCP servers here.
- A framework tutorial or code samples. Name LangChain and CrewAI, do not teach them.
- A framework survey or ranking. Two reference points only; do not catalog OpenAI Agents SDK, Pydantic AI, ADK, AutoGen. (AutoGen is in maintenance mode anyway; do not present it as current.)
- Star counts or popularity numbers. Omit.
- Hosted/no-code agent builders, or Claude Code itself. This post is about agents the developer codes and runs.
- Naming the employer, a team, or a colleague.
- Affiliate links.

## The thesis

People ask "LangChain or CrewAI?" first. It is the wrong first question. A production agent is not a clever prompt running in a loop. It is a system with a memory policy, a context budget, a model-routing decision, and guardrails. Those are architecture decisions, and they decide whether the agent works long before the framework does. The framework is an afternoon. The four decisions are the whole game. Treat building an agent the way you treat building any system, because that is what it is.

## The framework is the easy part

One short section. LangChain, through LangGraph, is the stateful-orchestration option: components plus a graph for long-running, multi-step agents. CrewAI is the role-based multi-agent option: agents as a crew with defined roles, independent of LangChain now. Both are Python, both are maintained, both converge on the same shape. Pick the one whose model fits your problem and move on. The choice is real but small, and it is reversible. The decisions below are neither.

## The four decisions

Each gets a real paragraph.

1. **Understand the problem.** An autonomous system magnifies a vague spec. A human fills a gap with judgment; an agent fills it with whatever is statistically nearby, then acts on it, at scale, without pausing to ask. Before any code, you write what the agent is for, what done looks like, and where its authority ends. A fuzzy problem produces a wandering agent. This is the load-bearing decision and the one most often skipped.

2. **Control memory.** An agent without a memory policy either forgets everything between steps or remembers everything until the context drowns. Neither works. Decide explicitly: what persists across runs, what lives only within a run, what gets summarized, what gets discarded. Memory is a design decision with a cost, not a free feature you turn on. State what the agent keeps and why.

3. **Manage context.** Context is a budget, not a bucket. Every token you spend on stale history is a token not spent on the task, and a bloated context makes the model drift the same way a vague prompt does. Decide what goes into the window on each step, in what order, and what gets evicted. The skill is feeding the model exactly what the current step needs, nothing more.

4. **Match the model to the task.** One model for every step is waste at one end and weakness at the other. A cheap fast model for classification and routing, a strong model for the hard reasoning step, the smallest model that clears the bar for everything else. Matching model to task is a cost and reliability decision you make per step, not once for the whole agent.

## The system prompt: behavior, guardrails, limits

The agent's system prompt is not a wish. It has three load-bearing parts.

- **Behavior.** The role and how it acts. What it does, in what order, in what voice, with what defaults. Specific enough that the agent does not invent its own job.
- **Guardrails.** The hard nevers. What it must not do under any input, including the inputs you did not foresee. In a regulated domain, this is where the non-negotiable constraints live, stated as absolutes, not preferences.
- **Limits.** Scope and stopping conditions. What is out of bounds, and when to stop and hand back to a human instead of pushing on. An agent with no stop condition does not know when it is done, so it keeps going.

A prompt with all three is a contract the agent can hold. A prompt missing one is where the failure gets in.

## What this is not

- Not a framework war. LangChain and CrewAI both work. The post is not about which.
- Not about tools or MCP. That is the next post, on purpose. Here the agent reasons and decides; giving it hands is its own topic.
- Not a claim that prompts do not matter. They matter a lot, which is exactly why the prompt gets a structure instead of a vibe.

## Series callbacks

- **The division of labor.** The series says the developer owns judgment, the model owns execution. Building an agent is encoding that division into a system: the guardrails and limits are where your judgment lives when you are not in the loop.
- **Post 13, Don't Just Use the Model.** Matching the model to the task is the applied version of understanding what the model is and is not good at.
- **The foundation theme.** The four decisions are the foundation under the agent, the same way specs and context were the foundation under using AI.

## Proposed structure

1. **Hook.** "LangChain or CrewAI?" is the wrong first question. An agent is a system, not a prompt.
2. **The framework is the easy part.** Name the two, say the choice is small, move on.
3. **The four decisions.** Understand the problem, control memory, manage context, match the model.
4. **The system prompt.** Behavior, guardrails, limits.
5. **What this is not.** Three honest bullets, including the explicit "tools next post."
6. **Close.** Build the agent like a system, because it is one. The prompt is a contract, not a wish.

Target length: 900 to 1100 words.

## Working title

**"Agents Are Systems, Not Prompts"** (approved)

Subtitle (draft): *Everyone asks LangChain or CrewAI first. Wrong question. A production agent is architecture: a memory policy, a context budget, a model decision, and a prompt with guardrails. The framework is the easy part.*

## Links

External (plain, no affiliate), used lightly as the two reference points:
- LangChain / LangGraph, https://github.com/langchain-ai/langgraph
- CrewAI, https://github.com/crewAIInc/crewAI

Internal:
- Don't Just Use the Model, `/posts/2026-05-30-dont-just-use-the-model/`
- Pick a Framework, Any Framework, `/posts/2026-05-25-pick-a-framework-any-framework/` (optional, the framework-choice-matters-less echo)

## Cover image plan

Same FLUX pipeline and dark amber-and-teal palette as the series. Concept: a cross-section of a machine or engine on a dark workbench, several distinct connected components (a memory drum, a routing valve, a governor) wired together and glowing warm amber from within, teal rim light on the housings. A system of parts, not a single glowing prompt. Painterly, soft bloom, brushstroke texture. No text.

## Open questions for Elber

- Confirm tools/MCP stays fully out, even as a one-line tease at the end ("tools are the next post"). Recommendation: one explicit line in "what this is not" pointing forward, no detail. It sets up the next post cleanly.
- LangGraph naming: refer to it as "LangChain (through LangGraph)" so the reader who knows the ecosystem is not confused, since LangGraph is the agent layer now. Recommendation: yes, one clause.
- Include the optional post-8 (Pick a Framework) callback, or keep only post 13? Recommendation: keep post 13 inline; mention post 8's idea ("the framework matters less than the foundation") without a second link to avoid clutter.

## Decisions

- **Systems-not-prompts thesis.** Architecture, not prompt-writing.
- **Framework is the easy part.** LangChain (LangGraph) and CrewAI only, no ranking.
- **Four decisions** with a real paragraph each: problem, memory, context, model-matching.
- **Three-part prompt:** behavior, guardrails, limits.
- **Tools/MCP deferred** to the next post, stated once.
- **No affiliate links, no star counts. Cover generated. Day job anonymized.**

## Sequencing

Latest post in the build-with-AI arc, after `2026-06-02-the-five-i-actually-run`. First of a two-post pair on building agents (this one on the system; the next on tools and MCP). Same flow: spec, draft for inline review, cover once approved, publish EN + PT-BR together, update the vault catalog, then the LinkedIn teaser (English only, short, links the English post).
