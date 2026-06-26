# Design spec: "Training Is Over Before You Arrive"

## One-sentence pitch

The model never learns from your chats; it is a finished, frozen object, and
what feels like learning inside a session is context, not training.

## Goals

- Kill the common belief that correcting the model in a chat teaches it.
- Explain frozen weights: training ended before the model shipped, and every
  session starts from the identical model.
- Show that in-session "learning" is just context shaping the next tokens.
- Separate fine-tuning (rewrites weights, offline, makes a new frozen model)
  from context (steers existing weights at runtime, what you do daily).
- Leave the reader with the practical reframe: you do not teach it, you brief it.

## Non-goals (load-bearing)

- Not about whether your chats train a future version of the model. Name the
  question, set it aside in a line or two. Provider-dependent, separate post.
- Not a fine-tuning how-to. No gradient-descent math, no training-loop detail.
- Not a deep dive on memory product features. Mention only as saved/staged
  context, not as the model learning.
- Not naming the employer.
- No heavy academic citation apparatus. Conceptual post, keep it light.

## The angle

Spine: the model is a finished object. It does not grow. The illusion of
learning comes from context living in the window for the length of a session.
Fine-tuning vs context falls out of this in one stroke: one rewrites the frozen
weights offline, the other steers them at runtime. Most "make it do X" is
context. Reframe for the reader: every session is day one, so you brief, you do
not teach.

## Proposed structure

1. Hook: the illusion. You correct the model mid-session, it adapts perfectly,
   feels like it learned. Next session, blank. It never learned. It re-read.
2. What training actually was: a one-time process that ended before the model
   shipped. Weights fixed at that moment. Everyone starts from the same model.
3. So what was that in-session learning? Context. The correction sat in the
   window and shaped the next tokens. Close the window, gone. Link to the desk
   post.
4. Fine-tuning vs context. Fine-tuning rewrites weights: rare, offline, makes a
   new frozen model. Context steers the existing weights at runtime: cheap,
   per-session, daily. Most "make it do X" is context, not training.
5. What it means practically: same model for everyone (reproducible), you brief
   not plead, memory features are saved context, your fix must be re-supplied
   every time. Link to commit-the-context / fix-the-system.
6. One honest aside: "does it train on me later?" Different question,
   provider-dependent, not this post.
7. Close: the model does not grow. You do not teach it, you brief it. Every
   session is day one.

## Length and format

Foundations essay, 800-1000 words. First person, architect-by-day builder voice.
Confession/observation hook (the illusion of learning), not the Lanterns story.
Honest, concrete, no hype.

## Links

- The Context Window Is a Desk, Not a Memory (2026-06-10) for statelessness.
- Pay the Setup Tax Once (2026-06-15-commit-the-context) and Fix the System, Not
  the Output (2026-05-31) for re-supplying the fix. Keep links optional, no
  count references.

## Cover plan

Series palette (deep charcoal, honey-amber focal glow, teal rim light). Concept:
a single finished sculpture or cast object set on a plinth under warm amber
light, complete and unchanging, while faint teal notes drift past it without
altering it. The object is done; the room moves, it does not.

## Open questions

- Title: "Training Is Over Before You Arrive" (chosen). Alt considered: "You
  Don't Teach It, You Brief It."

## Decisions

- Scope: mostly the first thread (frozen weights, in-session learning is
  context). Training-data question named and set aside.
- Length: foundations essay, 800-1000 words.
- Citations: light or none.
- Date: 2026-06-25 (current date; Elber's standing preference is to date posts with the current date, not one day after the previous post).
