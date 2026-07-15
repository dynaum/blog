# Design spec: "The Model Was Never the Bottleneck"

## One-sentence pitch

Your company rolled out Claude and Copilot to everyone and still ships at the
same speed, because the AI collapsed the cost of writing code and left every
slower cost upstream of code exactly where it was.

## Goals

- Reframe the common complaint ("why aren't we faster with Claude?") as a
  measurement error: the org is timing the wrong part of the work.
- Name the real bottlenecks concretely enough that the reader recognizes their
  own last two weeks: meetings that should have been specs, tribal knowledge,
  undocumented contracts, priority by loudest voice, approval latency, rework
  from vague intent.
- Make the arithmetic land: if coding was 3 of 5 days and AI cuts it to an hour,
  you saved 3 days and the other 2 are now the whole visible cost.
- Serve as the front-door post the existing solution posts answer.
- Hand the reader a self-test, not a lecture.

## Non-goals

- Not a tool comparison (Claude vs Copilot). The tool is not the subject.
- Not a how-to. It diagnoses and points to the fixes; it does not re-explain
  them. Link out, do not restate.
- Not a productivity-metrics essay. No DORA, no cycle-time frameworks. Keep it
  human and concrete.
- Not anti-AI. The AI did its job. The point is that its job was the smaller job.
- Do not name the employer. Anonymize as "a regulated domain where wrong code
  has consequences" / "a team I know."
- Not a rant about meetings. Meetings are one friction among several, not the
  thesis.

## The angle

The AI is an honest instrument. It made one part of the work nearly free, and by
doing so it turned a spotlight on everything that part used to hide. The team was
never mostly-coding. It felt mostly-coding because coding was the visible,
effortful, in-the-editor part. Remove it and the waiting, the deciding, the
re-explaining, and the approving are suddenly the whole job, in plain view. The
complaint "we're not faster" is really "we finally see where the time goes."

Tone: a mirror, not a scold. First person, architect-by-day. The reader should
feel recognized, then a little exposed, then pointed at a door.

## Proposed structure (~850-950 words, essay)

1. **Hook.** The sentence a leader says in month three of the rollout: "We gave
   everyone Claude. Why aren't we shipping faster?" Sit with it. It is a fair
   question with an uncomfortable answer.
2. **The measurement error.** The team was never spending most of its time
   writing code. It only looked that way. The arithmetic of the 5-day feature.
3. **The frictions, named.** Six short, concrete patterns the reader will
   recognize. Each two-to-three sentences, no padding:
   - the meeting that should have been a spec
   - the one person who knows
   - the contract that lives in someone's head
   - priority by loudest voice
   - code done Tuesday, merged Friday
   - "improve onboarding" and three rounds of rework
4. **Why the AI exposes them instead of fixing them.** The model resolves
   ambiguity in the code, not in the intent. Feed it a vague ticket and it ships
   a confident wrong thing fast. Speed amplifies whatever you point it at.
5. **The good news buried in the bad.** This is not a failure of the rollout.
   The AI did the expensive-looking part for free and handed you a precise map
   of your real constraints. Most teams never get that map.
6. **The door.** The fixes already exist and they are boring: write the intent
   down before the meeting, commit the context so the one person is not the
   bottleneck, decide priority once and in writing. Link the relevant posts.
7. **The challenge / close.** The self-test. Next time something takes too long,
   time it. Hours the AI wrote code vs hours of everything else. If coding was
   the thin slice, stop asking the model to go faster. It already did. The next
   speedup is yours to build, and it is not a tool.

## Links (internal)

- Context Is Not a Dev Job (/posts/context-is-not-a-dev-job/) — intent lives
  outside engineering.
- The Spec-Driven Loop (/posts/the-spec-driven-loop/) — write it down first.
- Pay the Setup Tax Once (/posts/commit-the-context/) — kill the tribal-knowledge
  bottleneck.
- Fix the System, Not the Output (/posts/fix-the-system-not-the-output/) — capture
  the decision once. (optional, if it fits the door section)

## Cover plan

Concept: a fast, bright assembly line feeding into a long queue of people waiting
at a single desk. Or: a race car stopped at a toll booth. The visual thesis is
"fast thing, slow gate." Series palette handles the mood (honey-amber focal glow,
teal rim light, near-black charcoal, painterly). Lean toward: a single lit desk
where work piles up while a bright automated line in the background runs empty.

## Open questions

1. Title. Candidates:
   - "The Model Was Never the Bottleneck"
   - "You Made Coding Cheap. Now What?"
   - "Faster Code, Same Speed"
   - "The Bottleneck Was Never the Code"
   Leaning "The Model Was Never the Bottleneck" (direct, names the reframe).
2. Six frictions or trim to four/five? Six is a lot; risk of list fatigue. Maybe
   four sharp ones + one grouped line. Decide at draft.
3. Slug: `not-the-model` vs `bottleneck-was-never-the-code`. Leaning
   `not-the-model`.

## Decisions

- Framing: anonymized (standing rule). [confirmed]
- Payoff: diagnose, then point to existing solution posts. Front-door post.
  [confirmed]
- Length: essay, ~850-950 words.
- Date: 2026-07-14.
