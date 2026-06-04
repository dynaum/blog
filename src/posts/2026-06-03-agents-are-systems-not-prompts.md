---
title: "Agents Are Systems, Not Prompts"
subtitle: "Everyone asks LangChain or CrewAI first. Wrong question. A production agent is architecture: a memory policy, a context budget, a model decision, and a prompt with guardrails. The framework is the easy part."
date: 2026-06-03
description: "Building an agent that runs in your own system is systems engineering, not prompt-writing. The four decisions that decide whether it works (problem, memory, context, model-matching) and the three-part system prompt: behavior, guardrails, limits."
cover: /assets/img/2026-06-03-agents-are-systems-not-prompts.png
coverAlt: "A cross-section of an engine on a dark workbench, several distinct connected components wired together and glowing warm amber from within, teal rim light on the metal housings."
---

The first question people ask when they want to build an agent is "LangChain or CrewAI?" It is the wrong first question. The framework is the smallest decision you will make, and you are making it first because it is the only part that looks like a choice.

A production agent is not a clever prompt running in a loop. It is a system. It has a memory policy, a context budget, a decision about which model handles which step, and a prompt that acts as a contract. Those are architecture decisions, and they decide whether the agent works long before the framework does. Build an agent the way you build any system, because that is what it is.

## The framework is the easy part

Name your two. LangChain, through LangGraph, gives you components plus a graph for stateful, long-running, multi-step agents. CrewAI gives you role-based agents working as a crew, and it stands on its own now, no LangChain underneath. Both are Python. Both are maintained. Both converge on the same shape.

Pick the one whose model fits how you think about your problem, and move on. The choice is real, but it is small, and it is reversible. You can swap the framework in a week. You cannot swap a memory model you never designed. Spend your thinking where it does not come back cheap.

## The four decisions

**Understand the problem.** An autonomous system magnifies a vague spec. A human fills a gap in the brief with judgment. An agent fills it with whatever is statistically nearby, then acts on it, at scale, without pausing to ask. Before any code, write what the agent is for, what done looks like, and where its authority ends. A fuzzy problem produces a wandering agent, every time. This is the load-bearing decision and the one people skip to get to the fun part.

**Control memory.** An agent with no memory policy either forgets everything between steps or remembers everything until the context drowns. Neither works. Decide it on purpose. What persists across runs. What lives only inside a single run. What gets summarized into a sentence. What gets thrown away the moment the step ends. Memory is a design decision with a cost, not a switch you flip to on. State what the agent keeps, and state why.

**Manage context.** Context is a budget, not a bucket. Every token spent on stale history is a token not spent on the task in front of the model, and a bloated window makes the model drift the same way a rambling prompt does. Decide what enters the window on each step, in what order, and what gets evicted to make room. The skill is feeding the model exactly what this step needs and nothing else. Most agents that "get dumber over time" are not getting dumber. Their context is filling with noise.

**Match the model to the task.** One model for every step is waste at one end and weakness at the other. Use a cheap, fast model for classification and routing. Use a strong one for the hard reasoning step that actually needs it. Use the smallest model that clears the bar for everything in between. This is a decision you make per step, not once for the whole agent. Paying for the frontier model to parse a yes-or-no is how an agent gets expensive without getting better.

## The prompt: behavior, guardrails, limits

The system prompt is not a wish you whisper at the model. It is a contract, and a contract has parts.

**Behavior.** The role and how it acts. What it does, in what order, in what voice, with what defaults. Specific enough that the agent does not invent its own job description from the gaps you left.

**Guardrails.** The hard nevers. What it must not do under any input, including the inputs you did not imagine. I work in a regulated domain where wrong code has consequences, and this is where the non-negotiable constraints live, written as absolutes, not as preferences the model can weigh against being helpful.

**Limits.** Scope and stopping conditions. What is out of bounds, and when to stop and hand back to a human instead of pushing on. An agent with no stop condition does not know when it is done, so it never is. It loops, or it widens its own scope until it breaks something.

A prompt with all three is a contract the agent can hold to. A prompt missing one is the gap the failure walks through.

## What this is not

- Not a framework war. LangChain and CrewAI both work. The post is not about which one wins, because that is not the decision that matters.
- Not about tools or giving the agent hands. That is the next post, on purpose. Here the agent reasons and decides. Letting it act on the world is its own topic, with its own failure modes.
- Not a claim that prompts do not matter. They matter enormously, which is exactly why the prompt earns a structure instead of a vibe.

## Close

The framework is where everyone starts because it is the part that looks like building. The real building is upstream, in the decisions that do not have a logo: what the agent is for, what it remembers, what it sees, which model it uses, and the contract it runs under.

Get those right and any framework will carry them. Get them wrong and no framework will save you. The agent is a system. The prompt is a contract. The framework is just the room they live in.
