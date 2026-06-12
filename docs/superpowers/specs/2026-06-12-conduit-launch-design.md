# Design spec: Conduit launch post

- **Post file:** `src/posts/2026-06-12-conduit-launch.md`
- **Date:** 2026-06-12 (one day after the prompt-vs-tool post)
- **Type:** Essay, 800 to 1000 words
- **Thread:** Systems. Launch post. Pays off the "third shelf" pointer from "What Goes in the Prompt, What Goes in the Tool".

## One-sentence pitch

A RAG application is 20 percent retrieval logic and 80 percent data plumbing every team rebuilds from scratch, and Conduit is the open-source engine I built to own that plumbing: connectors, parsing, chunking, embedding, incremental sync, and freshness monitoring.

## Goals

- Launch Conduit (github.com/dynaum/conduit) to the blog's audience with the problem first and the product second.
- Make the value land for both halves of the audience: developers (stop babysitting ingestion scripts, the table is yours) and product people (freshness is answer quality, observable instead of discovered through wrong answers).
- Use the build story as proof the blog's method ships real software: the spec-driven loop built this product, specs in the repo.
- State the open-core model in one honest line, no pitch.

## Non-goals

- **Not a RAG tutorial.** No retrieval-architecture explainer. Yesterday's post holds the concepts; this one launches the tool.
- **No code blocks beyond at most one command.** The quickstart lives in the repo README. The post sells the problem and the shape, not the syntax.
- **No competitor comparisons by name.** No Vectorize, LlamaIndex, LangChain, Unstructured call-outs. "Every team rebuilds this" is the antagonist.
- **No cloud-tier pitch.** One sentence naming the open-core model. Nothing about pricing, hosting plans, or roadmap promises.
- **No connector catalog.** Name the source types in one breath (files, websites, Postgres, S3, GitHub), do not enumerate features per connector.
- **No victory lap.** The built-with-the-loop section is proof of method, kept short and concrete.

## The angle

Product leads, story proves. The reader who hit the "third shelf" in yesterday's post knows retrieval is where stable-but-large knowledge lives. This post opens the box: getting knowledge onto that shelf and keeping it fresh is the unglamorous 80 percent. Five chores every team repeats (connectors, chunking, embedding pipelines, incremental sync, freshness), one silent failure mode (the first signal of a stale index is a user getting a wrong answer), and one engine that owns all of it without owning your store or your retrieval logic.

Authorship voice: first person singular. One honest line inside the build section acknowledging the collaborator: the team was me and the model, the same division of labor the series describes.

## Proposed structure

1. **Hook.** The 80/20 inversion: you sat down to build retrieval, you spent the quarter on plumbing. Inline link to the third-shelf section of the prompt-vs-tool post.
2. **The problem.** The five repeated chores, then the silent failure: nothing tells you the index went stale. Stale index, confident wrong answer (echoes "It Never Knows That It Doesn't Know" without needing the link).
3. **What Conduit is.** Point it at sources and your vector store. Incremental by design: run sync twice, the second run skips everything; edit one document, only it re-embeds; delete one, its vectors disappear. Structure-aware chunking with queryable metadata (heading path, page, language). It does not own your vector store or your retrieval logic; the embeddings table is yours, read it with SQL. One honest open-core line: the engine is MIT and open source, a hosted control plane is the part I plan to charge for later.
4. **For developers, for product people.** Developers: delete the fragile ingestion script, build the feature on a table that stays current. Product people: freshness is answer quality; `status` turns "is the AI wrong because the data is old" into a question with an answer instead of a support ticket.
5. **Built the way the blog says.** The spec-driven loop shipped this: brainstorm, spec, plan, implement, specs committed in the repo. The afternoon-cost curve from Build Your Own Tools, scaled from a tool to a product. Short.
6. **What this is not.** Not a RAG framework, not a vector database, not a retrieval library, and not finished: v1, five source types, an open connector contract for the long tail.
7. **Close.** Repo link, the two-minute quickstart pointer, and an invitation: point it at a folder and watch the second sync skip everything.

## Links

- `https://github.com/dynaum/conduit` — the repo (primary CTA).
- `/posts/2026-06-11-prompt-vs-tool/` — the third shelf this post opens.
- `/posts/2026-05-28-build-your-own-tools/` — the cost-curve argument.
- `/posts/2026-05-19-the-spec-driven-loop/` — the method that built it.

## Cover plan

Series palette via `tools/gen-cover.py`. Concept: a network of dark industrial pipes converging into a single glowing amber conduit feeding a vessel of light, teal rim light on the pipe joints.

## Open questions

- None outstanding. Frame (product leads, story proves), voice (first person singular), and open-core treatment (one honest line) were settled in review on 2026-06-12.

## Decisions

- **Frame:** product leads, build story proves the method. Chosen over story-first and an even split.
- **Voice:** first person singular, with one line crediting the model as collaborator inside the build section.
- **Open-core:** one plain sentence, no pitch. Chosen over omitting it and over a full section.
- **Slug:** `conduit-launch`.
- **Antagonist:** "every team rebuilds this plumbing", not named competitors.
