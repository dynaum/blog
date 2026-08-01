# Design spec: kubeside launch post

- **Post file:** `src/posts/2026-08-01-kubeside-launch.md`
- **Date:** 2026-08-01 (today)
- **Type:** Essay, 800 to 1000 words
- **Thread:** Systems. Launch post. The third solo product after Conduit and Stratify, used to make an argument the series has not made yet: the non-goals list is the product decision.

## One-sentence pitch

kubeside is a Kubernetes client scoped to the developer who ships the app rather than the operator who runs the cluster, and the reason it works is the list of things it refuses to do.

## Goals

- Launch kubeside (github.com/dynaum/kubeside, kubeside.dynaum.com) with **scoping as the spine**: every Kubernetes UI mirrors the API tree because that is the operator's shape, kubeside picks one person and answers four questions for them.
- Make the refusal list load-bearing prose, not a footnote. No node view, no PersistentVolume browsing, no RBAC editor, no CRD browser, no Helm management, no cost reporting, no topology graph, no plugin system. Each is a real need belonging to somebody else's tool.
- Show the four questions concretely, with the promotion matrix as the payoff screen.
- Name the central technical bet: nothing is written to disk. The timeline is reconstructed from history Kubernetes already keeps.
- Carry the epistemic-honesty through-line: absence of knowledge is not absence of a thing. Horizons, labelled gaps, disabled controls that name the verb.
- Keep the build story to two paragraphs. It is evidence, not the spine.
- One honest line on the division of labor, first person singular.

## Non-goals

- **Not a Kubernetes tutorial.** No explainer on ReplicaSets, ControllerRevisions, `managedFields`, or SelfSubjectAccessReview. Name the mechanism in one breath, do not teach it.
- **Not a Go or React deep dive.** No package walkthrough, no dependency list, no architecture diagram in prose.
- **No competitor named.** No k9s, Lens, Freelens, Headlamp, Rancher, or the archived Kubernetes Dashboard. The antagonist is the API-tree shape, not a product. (Consistent with the Stratify spec. The unsent Show HN draft in `LAUNCH.md` opens on k9s by name. The blog post does not.)
- **No employer named.** The cluster pain is described without any org detail, per the standing rule.
- **Do not clone the Stratify post.** Stratify's spine was "look how little it took to build this." Here the build story is two paragraphs near the end. If the draft starts sounding like a size flex, the spine has slipped.
- **No research-dump section.** `docs/01-problem.md` cites issue numbers and reaction counts from other projects' trackers. That research earns the argument. It does not go in the post. Quoting a rival's bug count reads as a swipe.
- **No feature inventory.** Twelve packages ship. The post names four questions and one payoff screen, and leaves the rest to the docs site.
- **No AI-autonomy hype.** The claim is the loop plus a scoped design, never the model acting alone.
- **No aspirational claims.** Two documented-but-unshipped things stay out: the architecture doc's frontend stack (Tailwind, TanStack, Zustand, uPlot, visx, none of which shipped) and "zero polling, informers only" (today it is a 5-second poll per subscribed view, and `internal/informers` is empty). Describe what shipped.
- **No roadmap promises.** `--serve` mode, informers, and envtest are all real plans. None of them belong in a launch post.
- **No Lanterns game-story opening.** Vary the hook.

## The angle

Scoping as the spine. A tool that serves everybody serves the operator, because the operator's mental model is the API tree and the API tree is what a generic dashboard renders. The moment you write down which single person the tool is for, the feature list stops being a wish list and becomes a subtraction problem.

So the post's argument is: kubeside is good at four things because it refuses the other thirty. The refusal is what let one person build a complete Kubernetes client in ten days. Every "no" is a screen nobody had to design, a permission model nobody had to reason about, and a test suite nobody had to write.

This lands directly on top of [How the Day Actually Runs](/posts/2026-07-18-how-the-day-runs/), which argued for writing the user down as a rule before building. kubeside is that argument carried to a whole product: the personas were written first, one of them was explicitly marked *stakeholder, not a user*, and everything the stakeholder needed got refused.

Authorship voice: first person singular. One honest line inside the build beat. I owned the scope, the refusal list, and the epistemic rules. The model owned structure and execution.

## Proposed structure

1. **Hook.** The concrete failure, no org detail. Three terminals, a tab per replica, and a guess about which version production is actually running. Not because the questions are hard. Because nobody built the screen for them.
2. **The shape problem.** Every Kubernetes UI mirrors the API tree: pick a kind, browse instances, pick a cluster from a switcher. Right shape for the person who runs the cluster, wrong shape for the person who ships an app. A developer's unit of work is one app across qa, stg, and prod, and their questions are historical more often than live: what changed, who changed it, what did the container actually get.
3. **The four questions.** Is my app up. What changed and when. What do the logs say across every pod at once. What configuration did the container actually receive. Then the promotion matrix as the payoff: one row per app, one column per environment, and a version prod has that staging does not floats to the top, because a hotfix nobody back-merged is the worst thing on that screen. Include the `kubeside --print` output block, trimmed, because the `GROUPED BY` column carries the design argument in one line.
4. **The refusal.** The non-goals list as prose. Each entry is a legitimate need belonging to somebody else's tool. Shipping any of them turns this into a general-purpose dashboard, which is the thing there is already enough of. The paragraph that earns the post: writing down the one person the tool serves is what makes the list of nos obvious, and the list of nos is what made ten days enough.
5. **The bet: nothing on disk.** No database, no cache file, no history directory. Stop the server and nothing is left behind. The timeline is reconstructed on demand from ReplicaSets, ControllerRevisions, Helm release secrets, pod termination states, and events still inside the apiserver's TTL. Everyone assumes history needs storage, so nobody assembled the history the cluster already keeps. Second-order payoff: two developers open kubeside and see the same timeline, because both read the same cluster.
6. **Honesty about the edges.** Where its knowledge ends it draws a horizon and labels it. A source your role cannot read becomes a named gap, never a quiet period. A metric it could not take is reported as unavailable, never as zero. A control you lack permission for is disabled and names the verb the cluster refused, instead of disappearing. Tie to [It Never Knows It Doesn't Know](/posts/2026-06-09-it-never-knows-it-doesnt-know/): a system that cannot say "I don't know" is the one you should not trust.
7. **The build, two paragraphs.** One Go binary with the UI embedded, reads the kubeconfig already on your machine, runs exec credential plugins natively. If `kubectl` works, kubeside works. Tests before implementation, roughly a line of test per line of source, CI on Linux, macOS, and Windows because compiling is not the same as working. A security review before v1.0.0 and everything it found is fixed. Ten days from the first commit. The division-of-labor line lives here.
8. **Close.** `brew install dynaum/tap/kubeside`. The invitation is the open question from `LAUNCH.md`, reframed for a reader: run `kubeside --print` on a cluster whose labelling nobody controlled, and tell me whether the app list matches what you call your apps. That is the bet, and only somebody else's messy cluster can settle it.

## Facts locked (verified 2026-08-01)

- Repo public at `https://github.com/dynaum/kubeside`, Apache-2.0, docs at `https://kubeside.dynaum.com/`.
- v1.0.1 is latest, released 2026-07-31. Homebrew tap `dynaum/homebrew-tap` serves 1.0.1, so `brew install dynaum/tap/kubeside` is accurate today.
- 80 commits, first on 2026-07-22. Ten days.
- Go: 11,178 source lines, 11,197 test lines, 518 test functions. Frontend: 161 test cases.
- CI runs the test suite on ubuntu, macos, and windows. Six release archives across three OSes and two architectures.
- Local server on `127.0.0.1:7654`. The browser never talks to an apiserver.

## Links

- `https://github.com/dynaum/kubeside` — the repo (primary CTA).
- `https://kubeside.dynaum.com/` — the docs site.
- `/posts/2026-07-18-how-the-day-runs/` — write the person down first.
- `/posts/2026-06-09-it-never-knows-it-doesnt-know/` — a system that cannot say "I don't know".
- `/posts/2026-06-14-stratify-launch/` — the previous solo product.

## Cover plan

Series palette via `tools/gen-cover.py`. Concept: a dense field of dim geometric containers receding into the dark, with one narrow amber corridor cut straight through them, lighting only three or four containers along its path while the rest stay unlit. Teal rim light on the edges of the unlit blocks. It reads as scope: one lit path through a crowded field, everything else deliberately left dark. No text.

## Open questions

- None outstanding. Angle (refusal as spine), competitor policy (no names), day-job framing (anonymized), and the four secondary beats settled in review on 2026-08-01.

## Decisions

- **Frame:** scoping and refusal as the spine, usage as evidence. Chosen over the build-story spine (would clone Stratify) and over the no-storage bet leading (that is a paragraph, not an argument about who a tool is for).
- **Competitors:** described by shape, never named. The `LAUNCH.md` Show HN draft names k9s. The blog post does not.
- **Day job:** anonymized cluster pain, no employer signal.
- **Beats included:** no-storage bet, epistemic honesty, promotion matrix, build story (short).
- **Accuracy:** describe what shipped. The architecture doc's frontend stack and its "zero polling" line are both aspirational and stay out.
- **Slug:** `kubeside-launch`.
