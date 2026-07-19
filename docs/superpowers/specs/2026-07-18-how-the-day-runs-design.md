# Design spec: "How the Day Actually Runs"

## One-sentence pitch

A real day-in-the-life of building and running production software with AI:
predefined user personas and their rules point every agent at the hardest real
user, parallel agents in worktrees do the building, and loops and goals keep
production covered by walking the critical flows as those personas, so the whole
day is accounted for.

## Goals

- Show the actual shape of a working day, not a concept. The reader should be
  able to copy the pattern by tomorrow.
- Make three threads click together as one system, with the user persona as the
  through-line that connects all three:
  1. **User personas + rules.** Predefined personas of the people who actually
     use the product: a patient, an elderly person with zero tech knowledge, an
     administrator running the back office. Each persona is a written rule set
     (what they know, what they fear, how they hold the phone, what breaks them).
     The agent stops building for an imaginary average user and builds for the
     hardest real one. The rule is what makes the persona repeatable across every
     agent and session.
  2. **Worktrees.** More than one agent at once means more than one working copy.
     Worktrees are the requirement, not a nice-to-have, because two agents in one
     directory step on each other. Each agent can work a different feature, or
     the same flow through a different persona's eyes.
  3. **Loops + goals for production.** The uncovered angle: aim loops at
     production health, and have them walk the critical flows *as the personas*.
     A loop that runs the login-to-task flow as the low-tech elderly persona and
     flags friction or a break before a real user hits it. A loop that scans for
     security vulnerabilities. A goal that takes a flagged break and drives the
     fix to a checked close.
- Land the new material: personas as the spec for who the software serves, reused
  by build, review, and standing production coverage alike.
- Keep it a recommendation. The reader leaves knowing what to set up first.

## Non-goals

- Not a re-teach of the /loop vs /goal distinction. Post 31 owns that. Reference
  it, do not repeat the cadence-vs-finish-line lecture.
- Not a re-teach of why multi-agent needs coordination. Post 10 owns the chat
  layer. This post names worktrees as the isolation primitive and moves on.
- Not a persona-writing tutorial or a UX-research methods post. Personas are the
  tool here, not the subject. Show them working, do not teach how to interview
  users.
- Not a tool pitch. Named persona archetypes, generic commands. No product
  endorsement, no naming the specific skills in the author's stack.
- Not a security tutorial. The security loop is one example among several.
- Not a "the AI runs my whole company unattended" hype piece. The human owns
  intent, priority, and the go-ahead. Loops surface, humans decide.
- Do not name the employer. Anonymize as "a regulated domain where wrong code has
  consequences." Patient/admin personas describe the domain, not the company.
- Not a literal hour-by-hour clock. The day is a frame, not a schedule to fill.

## The angle

Most AI-workflow writing shows one agent building for a user who does not exist:
a competent, patient, tech-comfortable average. Real products fail at the edges,
on the patient who cannot see the low-contrast button, the elderly user who taps
twice and submits nothing, the administrator drowning in a batch screen. The move
is to write those people down as personas with rules, once, and then point every
agent at them. The same personas that guide the morning's build guide the
review, and guide the loops that watch production all night. The connective
tissue is rules. A persona without a written rule is a stereotype. A parallel
agent without a worktree is a merge conflict. A loop without a goal is a clock
with no finish line. The day works because each piece has its constraint, and the
persona is the constraint that makes the software about the right person.

Tone: field note, first person, concrete. "Here is how a Tuesday goes." Calm,
not breathless. The reader should recognize the shape and think "I could run my
day like this."

## Proposed structure (~900-1000 words, field note)

1. **Hook.** Not the leadership question, not the game. Open on a concrete
   persona failure the average-user assumption hides: the elderly patient who
   tapped the button twice and submitted nothing, and how a developer would never
   have caught it because a developer is not that person. The fix is to make the
   agent be that person.
2. **Morning: personas and rules.** I do not build for a user. I build for a
   named person written down as a rule: the patient, the elderly user with zero
   tech knowledge, the administrator. Each rule says what they know, what they
   fear, the device in their hand, what makes them quit. Handed that, an agent
   catches the double-tap, the unreadable contrast, the error message that means
   nothing to a human. What makes it a persona and not a guess is the written
   rule behind it, the same lens every time. (Link: Pay the Setup Tax Once, Fix
   the System Not the Output.)
3. **Midday: parallel agents need worktrees.** Once I run more than one agent, I
   am the bottleneck, and the first thing that breaks is the filesystem. Two
   agents editing one checkout collide. A worktree gives each its own copy on its
   own branch. Now one agent builds the admin batch screen while another walks
   the patient flow, at the same time, without stepping on each other. (Link:
   Many Agents One Chat, Pick a Framework for the worktree primitive.)
4. **The bridge: the personas travel everywhere.** The same persona rule files
   load in every worktree and every session, so the patient is the same patient
   whether an agent is building the feature, reviewing the diff, or checking it
   in production. Write the person down once, reuse them everywhere.
5. **Background: loops and goals hold production.** The part no single-agent day
   has. A loop is a standing watch, and it watches as the persona:
   - a loop that walks the critical flow (login, the one task that matters) as
     the low-tech elderly persona and flags friction or a break before a user
     does
   - a loop that scans dependencies and code for known vulnerabilities and opens
     an issue when it finds one
   - a goal that takes a flagged break and drives the fix to a checked close
   The honest limit from post 31 in one line: a loop watches, a fresh goal
   confirms the fix. Watching and fixing are different jobs.
6. **Why this beats a bigger model or more people.** The day is covered not
   because the AI is smarter but because the work is aimed: personas make the
   software about the right person, worktrees make parallelism safe, loops make
   coverage constant. Aim beats horsepower.
7. **The recommendation / close.** What to set up first, in order: write one
   persona's rule file today, the hardest user you have, not the easiest. Add a
   worktree the first time you run two agents. Point one loop at your most
   important production flow this week, walking it as that persona. You do not
   build the whole day at once. You add one constraint at a time until the day
   runs itself between your decisions, and every part of it is looking at the
   person who actually uses what you ship.

## Links (internal)

- When Do I Wake Up, and When Am I Done? (/posts/2026-07-07-wake-up-and-done/) —
  the /loop vs /goal distinction this post applies to production.
- Many Agents, One Chat (/posts/2026-05-27-many-agents-one-chat/) — the
  multi-agent scaling problem.
- Pick a Framework, Any Framework (/posts/2026-05-25-pick-a-framework-any-framework/)
  — worktrees as the scaling primitive.
- Pay the Setup Tax Once (/posts/2026-06-15-commit-the-context/) — rules as
  committed, layered context.
- Context Is Not a Dev Job (/posts/2026-05-24-context-is-not-a-dev-job/) — the
  user and the problem are intent that lives outside engineering; personas are
  that intent written down. (optional, strong fit)

## Cover plan

Concept: a single dark workbench at night seen from above, several lit work
stations active at once (parallel worktrees), and at each station a different
face-mask or figure marker standing in for a user persona (patient, elderly user,
administrator). One steady amber lamp left on over a monitor showing a heartbeat
line (the production loop watching as a persona). Visual thesis: one maker,
many personas, one watch that never turns off. Series palette: honey-amber focal
glow, teal rim light, near-black charcoal, painterly, soft bloom. Avoid literal
text or faces that read as a specific real person.

## Open questions

1. Title. Candidates:
   - "How the Day Actually Runs"
   - "Build for the Hardest User, All Day"
   - "The Personas Never Log Off"
   - "One Maker, Many Users"
   Leaning "How the Day Actually Runs" (plain, field-note honest); "The Personas
   Never Log Off" is the sharper alt if we want the persona through-line in the
   title.
2. Slug: `how-the-day-runs` vs `personas-all-day`. Leaning `how-the-day-runs`.
3. Three background loops or trim to two? The persona-flow loop is the star and
   must stay; security loop and the goal-drives-fix are the supporting beats.
   Keep all three, tight. Decide at draft.

## Decisions

- Personas are USER personas (patient, low-tech elderly user, administrator), not
  internal build roles. The persona is the through-line across build, review, and
  production loops. [confirmed]
- Concreteness: named persona archetypes, generic commands, copyable pattern.
  [confirmed]
- Emphasis: even day-in-the-life, balanced across the three threads. [confirmed]
- Framing: anonymized day-job (standing rule); patient/admin describe the domain.
- Length: field note, ~900-1000 words.
- Date: 2026-07-18.
