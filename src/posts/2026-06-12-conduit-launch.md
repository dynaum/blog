---
title: "Conduit: The Plumbing Every RAG Team Rebuilds"
subtitle: "A RAG application is 20 percent retrieval logic and 80 percent data plumbing, and every team rebuilds the same 80 percent from scratch. I built an open-source engine that owns it. Today it is public."
date: 2026-06-12
description: "Announcing Conduit, the open-core data freshness engine for RAG. Connectors, chunking, embedding, incremental sync, and freshness monitoring in one engine that writes to your vector store instead of owning it. Built solo with the spec-driven loop."
cover: /assets/img/2026-06-12-conduit-launch.png
coverAlt: "A network of dark industrial pipes converging into a single conduit glowing warm amber, feeding a vessel of light, with teal rim light tracing the pipe joints."
---

Nobody sets out to build a pipeline. You set out to build the feature: a support bot that knows the docs, a search box that understands the codebase, an assistant that answers from your knowledge instead of guessing. Then you discover the ratio. Retrieval, the part you wanted to build, is about 20 percent of the work. The other 80 percent is plumbing, and every team rebuilds the same plumbing from scratch.

I got tired of the ratio. So I built Conduit, and today it is public.

## The 80 percent

[Knowledge that is stable but too big for every prompt](/posts/2026-06-11-prompt-vs-tool/) lives in retrieval. Getting it there, and keeping it true, is a list of chores every team repeats.

Connectors come first. Your knowledge lives in folders, websites, databases, buckets, and repos, and each source has its own API, its own auth, and its own way of changing. Then chunking, splitting documents into pieces worth retrieving, which depends on the document type and is easy to get subtly wrong. Then the embedding pipeline, which looks like a one-liner in a demo and becomes real engineering the day volume and failures arrive. Then incremental sync, because documents change, and the updated version has to reach the vector store without re-processing the world.

Then freshness, the chore nobody assigns. This one carries the silent failure. Nothing tells you a source went unreachable or a document went stale. The index does not complain. The model reads old chunks the way it reads everything, as ground truth, and answers with full confidence. The first signal your pipeline broke is a user getting a wrong answer, politely.

Every team writes this stack once, badly, under deadline. Then maintains it forever.

## What Conduit is

[Conduit](https://github.com/dynaum/conduit) is an engine that owns that 80 percent. You point it at your sources, files, websites, Postgres, S3, GitHub, and at your vector store. It ingests, parses, chunks, embeds, and keeps everything in sync.

The load-bearing word is sync. Run it twice and the second run skips everything. Edit one document and only that document re-embeds. Delete one and its vectors disappear on the next run. A failed document is recorded and retried later while the rest of the run completes. The chunking is structure-aware: Markdown splits by heading, PDFs by page, code at top-level boundaries, and every chunk carries its heading path, page number, or language as metadata you query.

Two things Conduit refuses to own, on purpose. It does not own your vector store: the embeddings land in your Postgres table, and you read them with plain SQL, however your application likes. And it does not own your retrieval logic: ranking, filtering, and what you do with the chunks stay yours. Conduit is the extract-and-load layer underneath, nothing more.

One honest line about the model. The engine is open source under MIT, and the part I plan to charge for later is a hosted control plane for teams who do not want to run the scheduling and monitoring themselves.

## For developers, for product people

If you are the developer, you have probably already written the fragile version: an ingestion script that worked until someone renamed a folder, with re-embedding logic you never quite trust. Conduit is the permission to delete it. The table stays current, the failures are recorded and retried, and your time goes back to the feature you actually planned to build.

If you are the product person, the word that matters is freshness, because freshness is answer quality. An assistant reading last month's pricing gives wrong answers in a confident tone, and until now your detection mechanism was a complaint. Conduit's `status` shows every source, every run, and every failure, so "is the AI wrong because the data is old" becomes a question with an answer instead of a support ticket with a vibe.

## Built the way this blog says

This project came out of the same loop I keep describing: brainstorm, spec, plan, implement, with [the spec as the contract](/posts/2026-05-19-the-spec-driven-loop/) at every step. The design specs are committed in the repo next to the code they produced. The team was me and the model, the same division of labor as always: I owned intent and judgment, the model owned structure and execution.

A while back I argued that [a custom tool now costs an afternoon](/posts/2026-05-28-build-your-own-tools/). Conduit is that cost curve carried further: a solo developer shipping a product that used to take a funded team, not because the typing got faster, but because the loop holds at larger sizes. The spec for a product is bigger than the spec for a tool. It is still a spec.

## What this is not

- Not a RAG framework. Conduit does not retrieve, rank, or prompt. It loads and keeps fresh.
- Not a vector database. It writes to the store you already have, starting with pgvector.
- Not a retrieval library. There is nothing to import. It is a binary that runs.
- Not finished. This is a v1 with five source types and an open connector contract, built so the community owns the long tail of sources.

## Try it

Two minutes with Docker: clone the [repo](https://github.com/dynaum/conduit), point the example config at a folder, and run sync. Then run it again, and watch the second run skip everything. That skip is the whole product. The plumbing finally remembers what it already did.
