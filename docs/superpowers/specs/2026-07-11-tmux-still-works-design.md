# Design spec — "tmux Still Works. I Switched Anyway."

Date: 2026-07-11
Slug: `2026-07-11-tmux-still-works`
Type: essay, 800-1000 words

## One-sentence pitch

tmux never failed me, I moved to herdr anyway, and the reason has nothing to do with tmux being bad and everything to do with staying willing to change.

## The angle

Most tool-switch posts start with a complaint. This one starts with the opposite: the old tool worked. Years of it. No pain, no bug, no breaking point. The switch happened because **the work changed**, not because the tool broke.

The work now is supervising several coding agents at once. tmux is adapting to that. herdr was built for it. Both statements are true, and the second one is the whole argument: a tool built for the shape of your current work will beat a tool retrofitted onto it, at least for a while.

Then the turn, delivered as a personal stance and not a lecture: the same willingness applies to where you work. If years pass and nothing about how you work has changed, that is information. When a place stops updating, I move. Stated once, as my own decision, then the post ends.

## Goals

- Make "the tool worked and I switched anyway" the load-bearing idea.
- Be concrete about what herdr does that tmux does not: agent state per pane (idle / working / blocked / done), sessions that survive, an API agents can drive.
- Be honest about the cost: muscle memory is real, the first days are slower, and that cost is the price of admission, not a bug.
- Land the personal conclusion about environments in one short section, in first person, no advice voice.
- Say plainly that going back to tmux is a fine outcome. Trying was the point.

## Non-goals

- **Not a herdr review or tutorial.** No install steps, no keybindings, no config dump, no feature table.
- **Not a tmux takedown.** tmux is good software. Saying otherwise would break the premise.
- **Not career advice.** No "you should quit your job." The environment section is my decision, not a recommendation.
- **Not a novelty-chasing manifesto.** Rewriting your setup every quarter is its own failure. The post names that.
- **No employer named.** Anonymize if it comes up.
- No benchmark numbers I have not measured.

## Structure

1. **Hook (confession).** tmux never failed me. That is what made leaving it hard.
2. **What actually changed.** Not the tool. The work. The terminal stopped being a place where I type and became a place where I watch processes I did not type into.
3. **Retrofit vs. built for it.** tmux is adapting to agents. herdr starts there: pane state, a sidebar that tells me which agent is blocked on me. Small difference in features, large difference in what the tool assumes I am doing.
4. **The cost, told straight.** Muscle memory, prefix keys, the reflex that fires before the thought. Days of feeling slow. The cost is small and it is visible. The cost of never paying it is large and invisible until it is not.
5. **The turn (short).** The switch was not about a multiplexer. It was a decision about staying changeable. The same test applies to the room you sit in: if the way you work has not changed in years, and nobody around you wants it to, that is the answer. When a place stops updating, I move on.
6. **Close.** I might go back. That would still count as knowing, instead of assuming.

## Links

- herdr: https://herdr.dev/
- Optional inline link to an existing post if it fits naturally. No forcing.

## Cover plan

Concept sentence: a worn wooden-handled hand tool set down on a dark workbench while a hand reaches for a newer precision instrument beside it, the old tool still clean and usable.

Series palette is appended by `tools/gen-cover.py`. Generate only after the text is approved.

## Open questions

1. Any concrete detail from the first days on herdr worth naming (a specific reflex that misfired, a moment the sidebar saved a wait)? Add it in section 4 if so.
2. Keep or cut the explicit "when a place stops updating, I move" sentence? Spec keeps it, once.

## Decisions

- Tone: personal, no advice voice. The reader draws their own conclusion.
- Balance: roughly two-thirds tool story, one-third the mindset turn.
- Hook is a confession, not the game story, not a question.
