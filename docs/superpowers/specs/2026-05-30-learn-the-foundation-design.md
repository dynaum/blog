# Don't Just Use the Model — Design Spec

**Date:** 2026-05-30
**Status:** Draft, awaiting Elber's review.
**Author:** Session co-design (Elber Ribeiro + Claude).

## One-sentence pitch

An essay arguing that the quality of every decision you make about an AI system is capped by how well you understand how the system actually works, with three real decisions where knowing the internals saved weeks or prevented a bad system, and three readable books as the way in.

## Framing decision

Decision-quality angle, not credentials. The series has said the developer owns judgment and the model owns execution. This post adds the catch: judgment about a machine you treat as magic is guesswork. The risk is sounding like gatekeeping ("read these or you are not a real engineer"). Two things defuse it. First, the three books are readable, not a math gauntlet, so the bar is low and the message is "this is reachable." Second, the argument is about outcomes, the right call and the cost of the wrong one, never about who is allowed in the room. First-person architect voice. Day job stays anonymized as "a regulated domain where wrong code has consequences."

## Goals

- Land the thesis: **your judgment about an AI system is only as good as your understanding of how it works.** A user drives the model. A builder knows why it behaves.
- Prove it with **three real decisions**, each showing the value of the right call and the cost of the black-box version.
- Recommend **three books as a reading ladder**, each tied to a layer of understanding that produces better decisions.
- Keep the tone anti-gatekeeping. The books are approachable. The point is "learn this, it is reachable," not "you are not qualified."
- Tie to the series spine and the recurring foundation theme: specs, context, and observability were foundations for *using* AI. Understanding the machine is the foundation under all of them.

## Non-goals (YAGNI)

- A machine-learning tutorial. The post says what each decision turns on, it does not teach backprop or attention math.
- A book-by-book deep review. One tight paragraph per book: what it teaches, why it changes a decision.
- A model or vendor shootout. No ranking of providers, no "best model" claim.
- Hype or fear-marketing ("prompting is dead, learn this or be left behind"). The case is decision quality, not a career threat.
- Naming the employer, a team, or a colleague.
- A claim that everyone must read all three. The ladder is an offer, not a mandate.

## The thesis

The whole series has split the work the same way: the developer owns intent and judgment, the model owns structure and execution. This post names the part that line hides. Judgment about an AI system is only as good as your model of how the system works. You cannot make the right architectural call about a machine you treat as a black box. You can only guess, and confident guessing is how good teams ship the wrong thing fast.

A user operates the model. A builder understands it. The gap between them is not prompt skill. It is knowing what the machine is doing when it answers, which is exactly the knowledge that tells you when to trust it, what to put around it, and when not to reach for it at all.

## The three real decisions

Each decision: the right call, what understanding produced it, and the cost of the black-box version.

**1. RAG vs fine-tuning.** Training writes patterns into weights. It does not build a reliable fact store. Fine-tuning shifts behavior, tone, and format. It does not teach the model your current data in a way you can trust to be correct and fresh. So a "answer from our docs, cite current facts" problem is a retrieval problem: inject the facts at inference with RAG. A "match our house style, follow our output shape" problem is a fine-tuning problem. The black-box version: teams spend weeks fine-tuning a model to answer questions about their own product, and it still makes up answers, because the knowledge was never going where they thought. Knowing the difference between training and inference is the whole call, and it is a week saved on day one.

**2. Hallucination is structural, not a bug.** A language model samples the next token from a probability distribution. It always produces fluent output and has no internal "I do not know." It cannot tell you it is unsure, because confidence is not a thing it computes. Once you know that, you stop trying to prompt the model into being accurate and you design the accuracy in: grounding with retrieval, verification on the way out, a human gate on anything that matters. This is the [Trust the Pipeline](/posts/2026-05-23-trust-the-pipeline/) move applied one layer down. In a regulated domain where wrong code has consequences, this is not optional, and it only follows from understanding what the model is.

**3. Sometimes the answer is not an LLM.** The field is older and wider than foundation models. A deterministic problem wants a deterministic tool: a constraint solver, a rules engine, a plain search. A high-volume cheap classification wants a small fast model, with the large model reserved for the hard reasoning step. The black-box version reaches for the biggest model on every problem, then pays for it in latency, cost, and flake. Knowing the broader map of AI is what lets you pick the right tool instead of the famous one.

## The three books

A reading ladder, each tied to a layer of understanding. One paragraph each.

**[Artificial Intelligence: A Guide for Thinking Humans](https://www.amazon.com/dp/1250758041/ref=nosim?tag=dynaum21-20)** by Melanie Mitchell. The broad mental model. What AI actually is, what it is not, and why the anthropomorphic story ("the model understands") is the trap behind half of bad AI decisions. Readable, no math required. This is the book that fixes decision three and the confidence trap in decision two.

**[Deep Learning](https://www.amazon.com/dp/0262537559/ref=nosim?tag=dynaum21-20)** by John D. Kelleher (MIT Press Essential Knowledge series). The mechanics, concise. How a network actually learns, what training does and does not store, why a model generalizes and why it confabulates. Short and approachable. This is the book that makes decisions one and two obvious instead of mysterious.

**[AI Engineering](https://www.amazon.com/dp/1098166302/ref=nosim?tag=dynaum21-20)** by Chip Huyen (O'Reilly). The applied layer. RAG, evaluation, inference cost, fine-tuning, the decisions you make building real systems on foundation models. This is the book that turns the understanding from the first two into the calls you make at work.

Order them however you read best: Mitchell for the picture, Kelleher for the mechanism, Huyen for the build. Foundation up, or start with Huyen where the work is and go down when a decision needs it.

Affiliate disclosure required, one line, paired with the links. Amazon Associates tag `dynaum21-20`. Honest note: I recommend books I am reading myself.

## What this is not

Honest section, short.

- Not "you must read all three to be allowed to build with AI." The ladder is an offer. One book read is more than zero.
- Not a call to retrain as an ML researcher. The argument is decision quality at the application layer, not a career pivot into model training.
- Not anti-abstraction. You do not need to know how a compiler works to write most code. But the more decisions you own about a system, the more its internals stop being optional.

## Series callbacks

- **The spine.** "The developer owns judgment, the model owns execution" runs through every post. This one names its precondition: judgment needs a working model of the machine.
- **Post 6, Trust the Pipeline.** Designing verification around a model that cannot self-report confidence is the same trust move, one layer down.
- **The foundation theme** (posts 5, 7, 9). Specs, shared context, and observability are foundations for using AI well. Understanding how AI works is the foundation under those foundations.

## Proposed structure

1. **Hook.** The fine-tuning-for-knowledge mistake. Teams burn weeks teaching a model their docs by fine-tuning, and it still makes things up. The model was never the problem.
2. **Thesis.** Your judgment about an AI system is capped by your understanding of it. A user drives the model. A builder knows why it behaves.
3. **Three real decisions.** RAG vs fine-tuning, hallucination is structural, sometimes not an LLM. Value plus the cost of the black-box version each.
4. **Where to start.** The three books as a ladder, one paragraph each, tied to a layer.
5. **What this is not.** Anti-gatekeeping bullets.
6. **Close.** The foundation under the foundation. The best decision comes from understanding the machine, not just operating it.

Target length: 800 to 1000 words.

## Working title

**"Don't Just Use the Model"** (approved)

Subtitle (draft): *The series says the developer owns the decisions. But a decision about a machine you treat as magic is a guess. Three real calls that came from knowing how the model works, and three readable books to get you there.*

## Links

External:
- [AI Engineering](https://www.amazon.com/dp/1098166302/ref=nosim?tag=dynaum21-20), Chip Huyen (O'Reilly). ASIN 1098166302.
- [Artificial Intelligence: A Guide for Thinking Humans](https://www.amazon.com/dp/1250758041/ref=nosim?tag=dynaum21-20), Melanie Mitchell. ASIN 1250758041.
- [Deep Learning](https://www.amazon.com/dp/0262537559/ref=nosim?tag=dynaum21-20), John D. Kelleher (MIT Press Essential Knowledge). ASIN 0262537559.

Internal:
- Trust the Pipeline, `/posts/2026-05-23-trust-the-pipeline/`
- The spec-driven loop, `/posts/2026-05-19-the-spec-driven-loop/` (for the spine line, optional)
- Your AI context belongs to the team, `/posts/2026-05-22-your-ai-context-belongs-to-the-team/` (foundation theme, optional)

## Cover image plan

Same FLUX pipeline and dark amber-and-teal palette as the series. Concept: an open machine on a dark workbench at night, a panel lifted or a casing opened to reveal intricate inner gears or an engine core glowing warm honey-amber from inside, cooler teal-cyan rim light tracing the metal edges, one warm lantern nearby. Painterly, soft bloom, brushstroke texture. No text. Conveys "seeing what is underneath" rather than operating the surface.

## Open questions for Elber

- The hook frames the fine-tuning mistake as something seen across teams, not a single named event, to stay honest and anonymized. Good? Recommendation: yes.
- Three decisions or two? Recommendation: three. They map cleanly to the three books and to the three layers (concept, mechanism, application).
- Include the optional internal links to the spec-driven loop and shared-context posts, or keep only the Trust the Pipeline callback? Recommendation: keep Trust the Pipeline inline, mention the others lightly in the close without links, to avoid link clutter.

## Decisions

- **Decision-quality angle, anti-gatekeeping.** Outcomes, not credentials. Books are readable, the bar is low.
- **Three real decisions** with value and the cost of the black-box version.
- **Three books as a ladder**, one paragraph each, mapped to layers.
- **Affiliate links on all three** with the one-line FTC disclosure, tag `dynaum21-20`.
- **Day job anonymized.** No employer, team, or colleague named.
- **Cover generated, not commissioned.** Consistent with the series.

## Sequencing

Latest post in the build-with-AI arc, after the measuring-delivery post (`2026-05-29-did-it-actually-work`). Same flow as before: spec, draft to iCloud for review, cover image once approved, publish EN + PT-BR together per the playbook, then LinkedIn. Note: the vault catalog `web/blog/posts.md` currently stops at post 11 and needs updating to include `2026-05-29-did-it-actually-work` and this post.
