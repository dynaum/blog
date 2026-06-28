# Design spec: "She Gave Me a Paper Form. I Built an App."

## One-sentence pitch

A doctor handed me a paper form to track my blood pressure, and instead of
filling it in I built bplog in an afternoon, because the cost of a real personal
tool has dropped below the cost of tolerating the friction.

## Goals

- Open on the real, relatable doctor moment: asked to log BP for a few weeks,
  offered paper.
- Make the build-threshold point: a few years ago paper was rational, now
  building the tool is the easy path.
- Launch bplog: live at bplog.dynaum.com, open source (MIT, dynaum/bplog).
- Lead the payoff on building it fast with AI: an afternoon, not a project.
- Show that fast did not mean sloppy: local-first, AHA classification,
  accessibility, a real doctor report.
- End with an invitation: use it or fork it.

## Non-goals (load-bearing)

- Not medical advice. No blood-pressure guidance, no health claims.
- Not a build tutorial. No React/MUI/Vite how-to, no code walkthrough.
- Not "code your own everything." Name when paper or an existing app is fine.
- Not "AI built it alone." The operator stayed in the loop, the same as the rest
  of the series.
- Not naming the employer.

## The angle

Spine: story leads, launch follows. The doctor reaching for paper is the hook
and the symbol. Paper is the default for "track this yourself," and the default
should move. The lesson is the collapsed build threshold, proven by bplog: a
complete, accessible, local-first PWA was an afternoon with AI carrying the
breadth (scaffolding, MUI, charts, PWA layer, tests). Supporting beats:
local-first data ownership and the printable doctor report, the one job paper
had, done better.

## Proposed structure

1. Hook: the doctor's office. Asked to track BP for a few weeks, she reaches for a
   paper form. I nodded, then thought: why paper?
2. The calculation flipped. Paper was once rational; an app meant weeks. Not now.
3. What I built. bplog: two readings a day, on-device, trends, a doctor report.
   Live and open source. Link.
4. The point: an afternoon, not a project. AI handled scaffolding, MUI, charts,
   PWA, tests. The cost of a real tool fell below the cost of the friction.
   Brief stack mention, link to "Build Your Own Tools."
5. Fast was not sloppy. Local-first (data stays on your phone), AHA
   classification, accessibility (WCAG AA, axe in the test suite), a real
   printable report. Complete because the model carries the breadth.
6. The reframe. Paper is the default for "track this yourself." The default
   should move. A form you will lose plus a photo your doctor cannot read,
   versus an afternoon. Build the thing.
7. Close: invitation. Free, open source, on-device. Use it or fork it. Link
   bplog.dynaum.com.

## Length and format

Field note, 800-1000 words. First person, architect-by-day builder voice.
Doctor-office hook, not the Lanterns story. Honest, concrete, no hype.

## Links

- bplog.dynaum.com (the app) and github.com/dynaum/bplog (the repo).
- Build Your Own Tools (2026-05-28-build-your-own-tools) for the threshold.
- Optional: Stratify launch (2026-06-14-stratify-launch) as the larger sibling
  proof. Keep links optional, no count references.

## Cover plan

Series palette (deep charcoal, honey-amber focal glow, teal rim light). Concept:
a paper blood-pressure form on a dark desk under warm amber light giving way to a
glowing phone screen showing a clean trend chart, teal rim light, brushstroke
texture, soft bloom. No text in the image.

## Open questions

- Title chosen: "She Gave Me a Paper Form. I Built an App." Alternatives
  considered: "Paper, or an Afternoon," "Why I Didn't Use the Paper."

## Decisions

- Spine: story + launch.
- Payoff lead: built it fast with AI (the threshold collapsed).
- Anchor: the real doctor visit, asked to log BP on paper.
- Length: field note, 800-1000 words.
- Date: 2026-06-28 (current date).
