# Design spec: "You Can't Write a Context File for a Person"

## One-sentence pitch

I have written context files for every system I work on, and none of that
technique transfers to managing a person, because the input a manager reads is
absence and absence never enters a context window.

## Goals

- Land one narrow, defensible claim: feedback fails automation not because
  people are mysterious, but because its signal is what did not happen, and
  nothing that did not happen produces a token.
- Name the absences concretely enough that the reader recognizes a specific
  person on their own team.
- Demystify "reading between the lines." Frame it as a diff against a baseline
  the manager built over months, not as intuition or talent.
- Show that challenging correctly is calibration, learned per person, paid for
  by getting it wrong with that person first.
- Carry the AI-moment twist: uniform output erased the cheap proxies for judging
  people, so the read moved to judgment and intent, which have no tooling.
- Retire "soft skills" as the name. The word sounds optional. The work is
  technique: which sentence, which week, which room.
- Concede honestly what AI does help with here, so the post is not a defence.

## Non-goals

- Not a management how-to. No framework, no named feedback model, no numbered
  list of tips. The post diagnoses one thing and stops.
- Not anti-AI. The rehearsal-partner section is required, not decorative.
- Not sentimental. No talk of souls, humanity, or what makes us special. The
  argument is mechanical: wrong input, not sacred subject.
- Not a claim about the far future. The claim is about the input, not about
  model capability. Do not predict what models will never do.
- Not a rerun of "You Cannot Push a Developer." That post is adoption across an
  org. This post is reading one person in one room. Link it, do not restate it.
- Do not name the employer. Do not describe a real, identifiable person. Every
  anecdote is a composite.
- No leadership-guru tone. First person, specific, and willing to be wrong.

## The angle

Every context file in my work succeeds for the same reason: the facts are
present and writable. Repo structure, deploy steps, user personas, rules the
agent loads every session. Write them once, load them forever.

Feedback breaks the pattern at the first step. Its input is not present. The
question someone stopped asking. The pull request nobody opened. The four words
at the end of a call. A model reads what is in the window. Managing reads what
is missing from it. You cannot write down a thing that did not happen, so there
is nothing to commit.

Then the AI moment made the read harder. Output flattened across the team. A
junior's pull request now looks like a senior's. The surface everyone used to
judge people by got quieter, so the signal moved underneath, to judgment and
intent, where no tool reaches.

Tone: field note. Honest about trying and failing. Concrete over clever.

## Proposed structure (~850-1000 words, essay)

1. **Hook, flat statement.** I have written context files for my repos, my
   deploys, my users. I have never managed to write one for a person.
2. **I tried, and trying was reasonable.** Feedback looks like pattern work.
   There are frameworks, structures, a shape to a good conversation. The model
   returns a page of correct, professional sentences. Not one of them survives
   contact with the person.
3. **Why it fails.** The input is absence. Five short, concrete cases, two or
   three sentences each, no padding:
   - the question he stopped asking in design review
   - the pull request nobody opened
   - "yeah, it's fine," four words, end of the call
   - the estimate that doubled with no reason offered
   - the engineer who went quiet after one bad meeting
   None of these left a trace a tool reads.
4. **Reading between the lines is history.** Not intuition. A diff against a
   baseline only you hold, built from months of how this person sounds when
   things are fine. State the honest mechanic so the post does not drift
   mystical.
5. **Challenging correctly is calibration.** The same sentence sharpens one
   engineer and shuts another down for a month. You learn the difference by
   getting it wrong with that person first. A bad call here does not cost a
   retry. It costs the person.
6. **The twist.** Output got uniform. The cheap proxies broke. Judging and
   growing people is harder after AI, not easier, and the people learning to
   manage now have fewer free signals to practice on. "Soft skills" is the
   wrong name for the hardest thing left.
7. **What AI is genuinely good for here.** Rehearsal partner. Ugly first draft
   I throw away. Catching my own vagueness before I take it into the room. It
   never knows the person. The decision and the sentence stay mine.
8. **Close.** People will learn to use these tools. That part levels out fast.
   The part that does not transfer is the one worth practicing now, and there
   is no file for it.

## Links (internal)

- You Cannot Push a Developer (/posts/2026-05-21-you-cannot-push-a-developer/)
  in the calibration or close section. Adoption is the org-scale version of the
  same physics.
- Pay the Setup Tax Once (/posts/2026-06-15-commit-the-context/) in the hook or
  section 2. This is the technique the post says does not transfer.
- The Model Was Never the Bottleneck (/posts/2026-07-14-not-the-model/) in the
  twist section. The bottleneck moved to people, and so did the hard reading.

## Cover plan

Concept: two chairs facing each other across a dim room. One side stacked with
neat written pages under the warm amber glow. The other chair empty, in teal
shadow. Visual thesis: everything written down on one side, a person on the
other, and the light does not reach across.

Series palette handled by tools/gen-cover.py. No text in the image.

## Open questions

1. Title. Candidates:
   - "You Can't Write a Context File for a Person" (leaning, ties to series
     vocabulary and then breaks from it)
   - "The Part You Can't Write Down"
   - "Read the Silence"
   - "Nobody Ships a Skill File for a Person"
2. Slug: `context-file-for-a-person` (leaning) vs `no-file-for-a-person`.
3. Five absences in section 3, or trim to four? Five risks list fatigue in a
   900-word post. Decide at draft, cut the weakest.

## Decisions

- Spine: the signal never enters the context. Confirmed.
- Vantage: both formal management and influence without authority, no title
  pinned in the text. Confirmed.
- Hook: flat statement about context files. Confirmed.
- Framing: anonymized, composites only. Standing rule.
- Length: essay, 850 to 1000 words.
- Date: 2026-09-14.
