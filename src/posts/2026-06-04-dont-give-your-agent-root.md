---
title: "Don't Give Your Agent Root"
subtitle: "MCP makes wiring an agent to your data trivial. That is exactly why the access decision is now the one that matters: what it can reach, what it can do, and why least privilege is the only rule that holds."
date: 2026-06-04
description: "Connecting an agent to your data with MCP is the easy part. The real work is two access decisions, what data the agent can reach and what it can do, both of which are least privilege for a non-human actor. With Redis as the worked example."
cover: /assets/img/2026-06-04-dont-give-your-agent-root.png
coverAlt: "A heavy vault door in a dark stone wall, open just a controlled crack with warm amber light spilling through the narrow gap, a teal-lit lock mechanism prominent in the foreground."
---

Last post was about the agent as a system. This one is about its hands.

Giving an agent tools used to be the hard part. You wrote a custom integration for every tool, every model, every datastore, and you wrote it again when any of them changed. MCP made that trivial. And the moment the hard part becomes trivial, a different part becomes the one that matters, and most people walk right past it.

## What MCP actually is

MCP, the Model Context Protocol, is a standard plug. Anthropic introduced it as an open protocol for how an agent connects to tools and data: a defined way for a server to expose things the agent can read and functions the agent can call, the same shape no matter what sits behind it.

That is the whole of it. MCP is the plug, not the appliance and not the electricity. The tool is still yours to build. The data is still yours to choose. You can put an MCP server in front of an existing REST API or an existing database without changing either, and the server translates them into things the agent understands.

One honest caveat, because it matters later. The easy version is a thin wrapper that exposes every endpoint and every table. That version is also usually the wrong one. A good MCP server curates. It exposes a few agent-meaningful tools, not your whole surface area. And the moment you curate, you are already making an access decision, whether you notice or not.

So the connection is solved. What is left is the part the standard plug makes easy to get wrong: how much of your data the agent can reach, and how much it is allowed to do. Two decisions. One principle.

## What data does the agent need

Scope the data to the minimum.

An agent does not need your database. It needs the slice the task requires. But MCP makes exposing everything as easy as exposing one table, so the instinct is to hand over the whole thing and let the agent figure out what is relevant. That is the same mistake as a vague prompt. A wide surface invites wandering. The agent pulls data it had no reason to touch, and leaks it through an answer you did not anticipate.

Decide what the agent reads the way you decide a service account's scope. Name the tables, the fields, the rows it is allowed to see. The smallest data surface that does the job is the right one, for the same reason it is right for a human contractor. What it cannot reach, it cannot misuse.

## What can the agent do

Scope the verbs, and gate the dangerous ones.

Reading is one thing. Acting is another. An agent that can only read is a risk you can bound. An agent that can write, delete, deploy, or spend is a risk you have to gate. Decide, per tool, what the agent may do, not only what it may see. The destructive verbs get a human approval step, the operator-in-the-loop rule, wired into the tool itself rather than left to the agent's good judgment.

There is a sharper reason the access boundary matters. An agent acts on inputs you did not write: a document it reads, a webpage it fetches, a user message that might carry a hidden instruction. The prompt can be subverted. The permission cannot, if you set it right. When a clever input talks your agent into doing something stupid, the only thing standing between the request and the damage is what you allowed the tool to do in the first place.

Both decisions are the same old principle. You would not give a new contractor root on their first day. You would give them read access to the one system they need and a request flow for anything destructive. An agent is a contractor that never sleeps, acts in milliseconds, and does exactly what its access allows, no more and no less. MCP did not break least privilege. It just removed the friction that used to enforce it by accident. Connecting everything is one config away now, so the discipline has to be a decision instead of a side effect.

## Front your data, do not expose it

Here is one concrete shape. Your data lives in a primary database, say Postgres. You do not point the agent at production.

You put a layer in front. [Redis Data Integration](https://redis.io/docs/latest/integrate/redis-data-integration/) keeps a Redis copy in sync through change data capture, so the agent reads a fast, current, separate copy instead of your source of truth. Redis then exposes that copy to the agent through MCP, with the official [Redis MCP server](https://github.com/redis/mcp-redis), or, with the newer [Redis Iris](https://redis.io/iris/) context engine, a retriever that generates scoped MCP tools over a semantic model of your data.

The point is not Redis. The point is the shape: a controlled, scoped layer between the agent and your real data, with the access decisions made in that layer. Any datastore with an MCP path can play the role. Redis is one that has the pieces today.

## What this is not

- Not anti-MCP. MCP is good, and the connection being easy is the win. This post is about what the win exposes.
- Not a Redis pitch. Redis is the worked example because the pieces line up, not because it is the only answer. Front your data with whatever fits.
- Not a threat-model paper. Prompt injection shows up here as a reason the boundary matters, not a thing to dissect. The boundary is the defense. Drawing it is the job.

## Close

The plug is standard now. That is real progress, and it means the interesting decision moved. It is no longer how you connect the agent to your data. It is what you let it reach and what you let it do once connected.

The model executes. You decide. With tools, deciding means drawing the access boundary, because that is the one part a clever prompt cannot talk its way past. Give the agent the keys to the one room it needs. Not root.
