---
title: "The Frontier Model Is Overqualified"
subtitle: "Most of your token bill goes to summaries, tags, and routing, all billed at genius rates. Open-weight models do the cheap tier for cents."
date: 2026-06-16
description: "A month of token usage shows the surprise is the breakdown, not the total. Clerical jobs like summarizing, classifying, and routing get billed at frontier rates. Open-weight models do the cheap tier for cents. Where to draw the line, and how to run the cheap side."
cover: /assets/img/2026-06-16-frontier-model-overqualified.png
coverAlt: "A deep charcoal workshop where a small warm amber worklamp lights a wide desk of routine paperwork, while a distant oversized chandelier hangs dark and unlit, teal rim light and brushstroke texture with soft bloom."
---

The number on the invoice was not the surprise. The breakdown was.

I pulled a month of token usage for a side project, expecting the cost to sit in the hard work. The reasoning steps. The code generation. The places where the model earns its keep. Instead, most of the spend sat somewhere else. Summaries of documents. Tagging items by category. Deciding which of four routes a request should take. Short, repetitive, dull jobs. Each one billed at the same frontier rate as the hard thinking, because each one was the same API call to the same expensive model.

I had hired a senior engineer to do data entry, and I was paying senior engineer rates for every keystroke.

## Difficulty is bimodal

Look at the work an LLM does in a real pipeline and the difficulty splits into two piles, not a smooth curve.

One pile is genuinely hard. Multi-step reasoning. Writing code correct enough to compile and run. Weighing tradeoffs with no clean answer. This is where a frontier model pulls ahead, and the gap is wide enough to feel.

The other pile is clerical. Summarize this passage. Is this ticket a bug or a feature. Pull the three dates out of this email. Pick the right tool for this query. These jobs have a right answer a competent intern reaches every time. They do not need the smartest model in the world. They need a model fluent in plain English and good at following instructions.

Most pipelines send both piles to the same model, because routing them separately is more work than writing one client and pointing everything at it. So the clerical pile rides along at frontier prices. At low volume nobody notices. At real volume the clerical pile is the bill. It is the same waste I keep running into: paying a model a premium for work a cheaper thing does as well. Last week I argued you should not [make the model do a build step](/posts/2026-06-13-tools-own-the-facts/). This is the same mistake wearing different clothes.

## Open models cleared the easy bar

Here is what changed, and why this is worth writing now instead of two years ago.

The open-weight models are good. Not good-for-free. Good. Llama, Qwen, Mistral, Gemma, and OpenAI's own gpt-oss release clear the easy tier without breaking a sweat. Summarization, classification, extraction, routing: a mid-sized open model does these as well as the frontier model does, because the task never needed frontier reasoning in the first place. The ceiling for clerical work is low, and these models sit well above it.

Two years ago this was not true. The open models hallucinated structure, drifted off instructions, and fell apart on anything past a toy prompt. You paid for a frontier model because the cheap option did not work. The excuse is gone.

## Where to draw the line

The split is not subtle once you look for it. Demote anything on this list to a small open model:

- Summarizing a document or a thread.
- Classifying: bug or feature, urgent or not, which of five buckets.
- Extracting fields from messy text into clean structure.
- Routing a request to the right tool or the right downstream model.
- Reranking a list of retrieved chunks by relevance.

Keep these on the frontier model:

- Multi-step reasoning where one wrong turn ruins the answer.
- Code generation you intend to run.
- Judgment calls with real stakes and no clean rule.

The test is simple. Would a sharp intern get this right with clear instructions? Send it to the cheap model. Does it need a senior engineer's judgment? Pay for the senior engineer.

## How to run the cheap tier

Two paths, and neither is a weekend project.

Hosted inference is the zero-ops path. Groq, Together, Fireworks, and OpenRouter all serve open models behind an API shaped like the one you already call. You change a base URL and a model name. The per-token price for a small open model runs a fraction of a frontier model, sometimes a tenth or less. For most people this is the whole answer.

Self-hosting is the other path. Ollama on a workstation for development, vLLM on a GPU box for production. You trade setup and ops for inference priced in electricity instead of per-token margin. This pays off at high, steady volume, and not before.

Either way, the piece tying it together is a small router in front of your calls. Tag each job by tier, send the clerical pile to the cheap endpoint, send the hard pile to the frontier. A dozen lines of code, and it owns the whole saving.

## Be honest about the swap

Do not trust vibes on this. Before you move a job to a cheaper model, run both on the same hundred inputs and compare. Cheaper is only cheaper if the output still holds. Sometimes a job you assumed was clerical leans on reasoning you did not see, and the small model exposes it. Better to learn this from an eval than from production.

Two more honest notes. Open models churn fast, so the right pick this quarter is not the right pick next quarter. Re-check. And the savings only matter at volume. At a hundred calls a month, leave everything on the frontier model and spend your attention elsewhere.

## Close

The frontier model is for the hard ten percent. The reasoning, the code, the judgment. You are paying the premium for those, and they are worth it.

The other ninety percent is filing. Summaries, tags, extractions, routes. An open model a fraction of the size does the same work as well, for a fraction of the price.

Stop sending your clerical work to the genius. It is overqualified, and it is charging you for the privilege.
