---
title: "Don't Just Use the Model"
subtitle: "The series says the developer owns the decisions. But a decision about a machine you treat as magic is a guess. Three real calls that came from knowing how the model works, and three readable books to get you there."
date: 2026-05-30
description: "The quality of every decision about an AI system is capped by how well you understand the machine. Three real calls (RAG vs fine-tuning, designing around hallucination, when not to use an LLM) and three readable books to get there."
cover: /assets/img/2026-05-30-dont-just-use-the-model.png
coverAlt: "An open machine on a dark workbench at night, its casing lifted to reveal intricate inner gears glowing warm amber from within, a teal rim light tracing the metal edges."
---

I have watched more than one team try to teach a model their own product by fine-tuning it. Weeks of work. A dataset, a training run, a bill. Then they ask it a question about their own docs and it invents an answer with total confidence. The model was never the problem. Nobody had asked what fine-tuning actually changes.

This blog has said the same thing in every post. The developer owns intent and judgment. The model owns structure and execution. There is a precondition hiding in that line. Your judgment about an AI system is only as good as your understanding of how the system works. A decision about a machine you treat as magic is a guess wearing a confident face.

A user drives the model. A builder knows why it behaves. The gap between them is not prompt skill. It is knowing what the machine is doing when it answers. That knowledge is what tells you when to trust it, what to build around it, and when not to reach for it at all.

## Three decisions that came from knowing the machine

**RAG or fine-tuning.** Training writes patterns into weights. It does not build a fact store you can trust. Fine-tuning shifts behavior, tone, and format. It does not reliably teach the model your current data. So the question answers itself once you know the mechanism. "Answer from our docs, with current facts" is a retrieval problem. Inject the facts at inference with RAG. "Match our house voice, return our output shape" is a fine-tuning problem. The team that fine-tunes to inject knowledge burns weeks and still gets invented answers, because the knowledge went somewhere it was never going to live. Knowing the difference between training and inference is the entire call, and it is a week saved on the first morning.

**Hallucination is structural.** A language model samples the next token from a probability distribution. It always produces fluent text. It has no internal "I do not know," because confidence is not a value it computes. Once you know that, you stop prompting the model to be accurate and you design the accuracy in. Ground it with retrieval. Verify the output before it ships. Put a human gate on anything with consequences. This is the [Trust the Pipeline](/posts/2026-05-23-trust-the-pipeline/) argument moved one layer down. I work in a regulated domain where wrong code has consequences, and there the verification layer is not a nicety. It follows directly from understanding what the model is. It never follows from hoping the model behaves.

**Sometimes the answer is not a model at all.** The field is older and wider than the foundation models everyone talks about. A deterministic problem wants a deterministic tool. A constraint solver, a rules engine, a plain database query. A high-volume classification wants a small fast model, with the large one held back for the hard reasoning step. Reach for the biggest model on every problem and you pay for it in latency, in cost, and in flake you cannot explain. Knowing the broader map of the field is what lets you pick the right tool instead of the famous one.

## Where to start

None of this needs a PhD. It needs a few books and the willingness to read them. Here are the three I point people to, easiest first.

**[Artificial Intelligence: A Guide for Thinking Humans](https://www.amazon.com/dp/1250758041/ref=nosim?tag=dynaum21-20)** by Melanie Mitchell. The big picture, in plain language. What AI is, what it is not, and why the story that "the model understands" is the trap behind half the bad decisions above. No math required. Read this and the confidence trap stops fooling you.

**[Deep Learning](https://www.amazon.com/dp/0262537559/ref=nosim?tag=dynaum21-20)** by John D. Kelleher, in the MIT Press Essential Knowledge series. The mechanics, kept short. How a network learns, what training stores and what it does not, why a model generalizes and why it confabulates. A small book with a big payoff. Read this and the first two decisions stop being mysterious.

**[AI Engineering](https://www.amazon.com/dp/1098166302/ref=nosim?tag=dynaum21-20)** by Chip Huyen. The applied layer. RAG, evaluation, inference cost, when fine-tuning earns its keep. The decisions you make building real systems on foundation models. Read this and the understanding turns into the calls you make at work.

Read them in any order. Mitchell for the picture, Kelleher for the mechanism, Huyen for the build. Start at the top and work down, or start with Huyen where your work already is and drop a layer when a decision needs it.

## What this is not

- Not a rule that you read all three before you are allowed to build. One book is more than none.
- Not a call to retrain as a researcher. The argument is decision quality at the application layer, not a career change into training models.
- Not a vote against abstraction. You do not need to know how a compiler works to write most code. But the more decisions you own about a system, the less its internals stay optional.

## Close

Earlier posts built foundations for using AI well. Specs so the model does not wander. Shared context so the team stops re-explaining. Observability so the agent reads something true. This is the foundation under those foundations. Every one of them is a decision, and a decision about a machine is only as good as your picture of the machine.

A user gets output. A builder gets to decide whether the output should be trusted, and how to build the system so the answer is yes. Do not just use the model. Learn what it is doing when it answers. That is where the good decisions come from.

---

The Amazon links above are affiliate links. If you buy through one I get a small commission, at no extra cost to you. I only recommend books I am reading myself.
