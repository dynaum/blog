# Don't Give Your Agent Root — Design Spec

**Date:** 2026-06-04
**Status:** Draft, awaiting Elber's review.
**Author:** Session co-design (Elber Ribeiro + Claude).

## One-sentence pitch

An essay arguing that connecting an agent to your data with MCP is the easy, solved part, so the real work is two access decisions, what data the agent can reach and what it can do with it, which converge on one principle: least privilege for a non-human actor.

## Framing decision

Part two of the agent pair (part one: "Agents Are Systems, Not Prompts," on the system; this one on tools and giving the agent hands). Lead by demystifying MCP as the plug, then make least-privilege the spine. The hook frames it as a security decision because MCP made the connection trivial. First-person architect voice. Day job anonymized as "a regulated domain where wrong code has consequences," which carries real weight here since access control is the whole point. Redis is the single named worked example, accurate per verification, not a survey.

## Goals

- Demystify MCP accurately: it is the standardized interface that exposes tools and data to an agent, not the tool and not the data. The plug, not the appliance or the electricity.
- Land the thesis: because MCP makes the connection trivial, the decisions that matter are access decisions, and the right frame is least privilege for a non-human actor.
- Treat the two decisions distinctly, then converge: what data does the agent need (scope the resources to the minimum), and how do you control access (scope the verbs, gate the dangerous ones), both being least privilege.
- Give one concrete, accurate worked example: front your existing data with MCP, using Redis (RDI syncing your primary DB via CDC, Redis exposing scoped MCP tools).
- Tie to the series: the operator-in-the-loop rule (ops post) and the guardrails/limits from part one are where this access discipline lives.

## Non-goals (YAGNI)

- An MCP tutorial or protocol internals. Name Resources/Tools/Prompts at most in passing; do not teach JSON-RPC, transports, or how to write a server.
- A vendor survey or ranking. Redis is the one named example; do not catalog every datastore or MCP server.
- A Redis ad. Use Redis accurately as an example of the pattern, not as the recommendation. The spine is the two decisions.
- Re-explaining part one. Link it once as the setup, do not restate "agents are systems."
- Prompt-injection deep dive. Name it as a reason access control matters, do not turn the post into a threat-model paper.
- Star counts. Omit.
- Naming the employer, a team, or a colleague. Affiliate links.

## Accuracy guardrails (from verification)

- MCP: Anthropic, open application-layer protocol (Resources, Tools, Prompts). Say "the standard interface/connection," not "just the transport," which undersells it.
- "Put MCP in front of your existing API or datastore" is a real, recommended pattern. Caveat: curate and aggregate endpoints into agent-meaningful tools, do not dump the whole API surface.
- Redis Data Integration (RDI): real, CDC-based sync from a primary database into Redis in near real time (uses Debezium). Docs at redis.io.
- Redis Iris: real, launched 2026-05-18, a context engine for agents. The MCP tie-in is Redis Context Retriever, which auto-generates MCP tools over your data. RDI is both standalone and one of Iris's five tools. Use exact names if named.
- Official Redis MCP Server (github.com/redis/mcp-redis): real, maintained by Redis, lets an agent use Redis as a tool/data source via MCP.

## The thesis

Giving an agent tools used to be the hard part. MCP made it trivial. MCP is the standard plug: a defined way for an agent to discover and call tools and read data, the same shape no matter what is behind it. The appliance (the tool) and the electricity (your data) are still yours to choose. Once the plug is standard, the connection stops being the interesting decision. What becomes interesting, and what most people skip, is everything the plug now makes easy to get wrong: how much of your data the agent can reach, and how much it is allowed to do. That is not a connection problem. It is an access-control problem, and the frame is least privilege for an actor that is not a person.

## What MCP is (and is not)

Short section. MCP, from Anthropic, is an open protocol that standardizes how an agent connects to tools and data. It defines how a server exposes things the agent can read and functions the agent can call. It is the interface, not the capability. You can put an MCP server in front of an existing REST API or an existing datastore without changing either; the server translates them into tools and resources the agent understands. The honest caveat: a thin one-to-one wrapper that exposes every endpoint is the easy version and usually the wrong one. A good MCP server curates, exposing agent-meaningful tools, not your whole surface area. That curation is already an access decision in disguise.

## Decision one: what data does the agent need

Scope the resources to the minimum. An agent does not need your database. It needs the slice of it that the task requires. The instinct, because MCP makes it easy, is to expose everything and let the agent figure out what is relevant. That is the same mistake as a vague prompt: a wide surface invites the agent to wander, to pull data it should not see, to leak something through an answer. Decide what the agent reads the way you decide a service account's read scope. Name the tables, the fields, the rows it is allowed to touch. The smallest data surface that does the job is the right one, for the same reason it is right for a human contractor: what it cannot reach, it cannot misuse.

## Decision two: how do you control access

Scope the verbs, and gate the dangerous ones. Reading is one thing; acting is another. An agent that can read is a risk you can bound. An agent that can write, delete, deploy, or spend is a risk you have to gate. Decide, per tool, what the agent may do, not just what it may see. The dangerous verbs get a human approval step, the operator-in-the-loop rule from [the ops post](/posts/2026-05-26-save-the-boring-time/), wired into the tool itself. And because an agent acts on inputs you did not write (a document, a webpage, a user message that could carry an instruction), the access boundary is the only thing you control fully. The prompt can be subverted. The permission cannot, if you set it right.

## Converge: least privilege for a non-human actor

Both decisions are one principle. You would not give a new contractor root on day one. You would give them read access to the one system they need and a request flow for anything destructive. An agent is a contractor that never sleeps, acts in milliseconds, and does exactly what its access allows, no more and no less. Least privilege was always the rule for human actors. The agent is a new kind of actor, and the rule did not change. MCP just made it urgent, because it removed the friction that used to limit the blast radius by accident.

## The worked example: front your data with MCP

One concrete path, named and accurate. Your data lives in a primary database, say Postgres. You do not point the agent at production. You put a layer in front. [Redis Data Integration](https://redis.io/docs/latest/integrate/redis-data-integration/) keeps a Redis copy in sync via change data capture, so the agent reads a fast, current, separate copy instead of your source of truth. Redis exposes that copy to the agent through MCP, via the official [Redis MCP server](https://github.com/redis/mcp-redis) or, with the newer [Redis Iris](https://redis.io/iris/) context engine, a Context Retriever that generates scoped MCP tools over a semantic model of your data. The point is not Redis specifically. The point is the shape: a controlled, scoped, read-appropriate layer between the agent and your real data, with the access decisions made in that layer. Any datastore with an MCP path can play the role. Redis is one that has the pieces today.

## What this is not

- Not anti-MCP. MCP is good, and the connection being easy is the win. The post is about what the win exposes.
- Not a Redis pitch. Redis is the worked example because the pieces line up, not because it is the only answer. Front your data with whatever fits.
- Not a threat-model paper. Prompt injection is named as a reason the access boundary matters, not dissected. The boundary is the defense; this post is about drawing it.

## Series callbacks

- **Part one, Agents Are Systems, Not Prompts.** That post said guardrails and limits are where your judgment lives when you are not in the loop. This post is the same judgment applied to the agent's hands: what it can reach and do.
- **The ops post, Save the Boring Time.** The operator-in-the-loop rule, here wired into the dangerous tools as an approval gate.
- **The division of labor.** The model owns execution; you own judgment. Access control is judgment encoded as permission, the version that holds even when the prompt is subverted.

## Proposed structure

1. **Hook.** Giving an agent tools used to be hard. MCP made it trivial. That is exactly why the access decision is now the one that matters.
2. **What MCP is.** The plug, not the appliance or the electricity. Front your API/DB with it; curate, do not dump.
3. **Decision one: what data does it need.** Scope the resources to the minimum.
4. **Decision two: how do you control access.** Scope the verbs, gate the dangerous ones, the boundary survives prompt injection.
5. **Converge: least privilege for a non-human actor.** Don't give your agent root.
6. **The worked example.** Front your data with MCP, Redis (RDI + MCP server / Iris) as the concrete path.
7. **What this is not.** Three honest bullets.
8. **Close.** The plug is standard now. The judgment is what you bring.

Target length: 900 to 1100 words.

## Working title

**"Don't Give Your Agent Root"** (approved)

Subtitle (draft): *MCP makes wiring an agent to your data trivial. That is exactly why the access decision is now the one that matters: what it can reach, what it can do, and why least privilege is the only rule that holds.*

## Links

External (plain, no affiliate):
- MCP, https://modelcontextprotocol.io
- Redis Data Integration, https://redis.io/docs/latest/integrate/redis-data-integration/
- Redis MCP server, https://github.com/redis/mcp-redis
- Redis Iris, https://redis.io/iris/

Internal:
- Agents Are Systems, Not Prompts, `/posts/2026-06-03-agents-are-systems-not-prompts/`
- Save the Boring Time, `/posts/2026-05-26-save-the-boring-time/`

## Cover image plan

Same FLUX pipeline and dark amber-and-teal palette as the series. Concept: a heavy vault door or a single guarded gate in a dark stone wall, open just a controlled crack with warm amber light spilling through the narrow gap, a teal-lit keyway or lock mechanism prominent. Controlled access, not an open door. Painterly, soft bloom, brushstroke texture. No text.

## Open questions for Elber

- Name Redis Iris specifically, or keep to RDI + the official Redis MCP server? Iris is new (2026-05-18); naming it is current but risks dating fast. Recommendation: name RDI and the official MCP server as the stable core, mention Iris/Context Retriever in one clause as the newer option. Accurate and future-proofed.
- The "least privilege / don't give it root" frame is the spine. Confirm the contractor analogy lands and is not too cute. Recommendation: keep it; it is concrete and it is how the access decision actually feels.
- One forward/back line to part one in the open, or keep the two posts loosely coupled? Recommendation: one line ("part one was the system; this is its hands"), no heavy callback.

## Decisions

- **MCP-is-the-plug hook, least-privilege spine.** Two decisions converging on one principle.
- **Two distinct sections** (data scope, access control) then a convergence section.
- **Redis as one named, accurate worked example**, RDI + official MCP server core, Iris/Context Retriever as the newer clause. Not a pitch.
- **No affiliate links, no star counts. Cover generated. Day job anonymized.**

## Sequencing

Latest post in the build-with-AI arc, after `2026-06-03-agents-are-systems-not-prompts`. Second of the two-post agent pair. Same flow: spec, draft for inline review, cover once approved, publish EN + PT-BR together, update the vault catalog, then the LinkedIn teaser (English only, short, links the English post).
