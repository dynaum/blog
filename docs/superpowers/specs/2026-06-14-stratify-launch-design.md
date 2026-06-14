# Design spec: Stratify launch post

- **Post file:** `src/posts/2026-06-14-stratify-launch.md`
- **Date:** 2026-06-14 (one day after the tools-own-the-facts post)
- **Type:** Essay, 800 to 1000 words
- **Thread:** Systems. Launch post. The second solo product after Conduit, used as the largest proof yet of the blog's recurring claim: one person, working the loop, ships complete software.

## One-sentence pitch

Stratify is a polyglot static-analysis engine I built solo with the spec-driven loop, and its real headline is not the six analyses or the five languages, it is that one person shipped a complete platform this size because the architecture kept every piece small enough for the loop to hold.

## Goals

- Launch Stratify (github.com/stratify-dev/stratify) with the build-story as the spine: the headline is the size of what one person shipped, and the usage is the evidence.
- Show the usage at medium depth: the `stratify check .` command with its real output, then the five surfaces named as the fan-out (CLI/SARIF, CI gate, MCP, editor LSP, OpenTelemetry).
- Name the one design decision that made the scope cheap: a universal IR every analysis reads instead of the source, so five languages cost five small adapters, not five rewrites of six analyses.
- Make the deeper argument: the architecture that lets a human team extend a codebase cheaply is the same architecture that lets the loop build it reliably. Small, well-bounded, spec-able units are why the loop holds at product size.
- Define "complete" honestly: tests per language per surface, CI, releases, Homebrew, a Marketplace Action, SARIF, MCP. The boring last mile is part of what one person now ships.
- One honest line on the division of labor: first person singular, the team was me and the model.

## Non-goals

- **Not a static-analysis tutorial.** No explainer on cyclomatic complexity, dead-code resolution, or dependency cycles. Name what each analysis finds in one breath, do not teach it.
- **Not a Rust or tree-sitter deep dive.** The IR is named as the load-bearing decision, not walked through as code. No language internals.
- **No AI-autonomy hype.** "The model built it by itself" is false and off-brand. The claim is about the loop plus architecture, not the model acting alone. No "revolutionary", no "the future is here".
- **No competitor call-outs by name.** No SonarQube, Semgrep, CodeQL, ESLint mentions. The antagonist is "this used to take a funded team and a year".
- **No commercial pitch.** Stratify is pure open source. No paid tier, no hosted plan, no roadmap promises. (Differs from Conduit on purpose.)
- **No surface-by-surface README rehash.** Medium usage depth: one command with output, the five surfaces named in a tight beat. Syntax lives in the repo.
- **Do not clone the Conduit structure.** Conduit was product-first with the build story as a closing section. Here the build story is the spine from the first line. Different shape, not a reskin.
- **No Lanterns game-story opening.** Vary the hook.

## The angle

Build-story as spine. The post opens on the size of the thing, then turns immediately: the interesting part is not that Stratify exists, it is how little it took to build something this complete. Usage proves the size is real. The IR decision explains why the scope stayed flat. And the closing argument ties it to the whole blog: the loop does not hold because the model is magic, it holds because good architecture keeps every unit small enough to spec, build, and test in isolation, and that is a thing a person decides, not the model. Stratify is the largest data point so far for the claim the series keeps making.

Authorship voice: first person singular. One honest line acknowledging the collaborator inside the division-of-labor beat: I owned intent, the IR decision, and the judgment calls (like reporting `possibly unused` instead of guessing); the model owned structure and execution.

## Proposed structure

1. **Hook.** The inventory as a punch: five languages, six analyses, five surfaces, one binary, one person. Then the turn: a year ago that last clause would have needed a team and a year. The headline is not the tool, it is the size one person can now ship.
2. **What it does (usage, medium).** `stratify check .` with the real two-line output. Then the fan-out: the same analysis powers the CLI and SARIF, a CI quality gate, an MCP server your coding agent queries, an editor language server, and OpenTelemetry dashboards across a fleet of repos. One engine, five places you already work.
3. **The one decision that made it cheap.** The universal IR. Every analysis reads the IR, never the source. Five languages parse into the same model, so each of the six analyses is written once and works everywhere. Adding a language is one adapter and zero analysis changes. That is why five languages did not cost five times the work.
4. **Why that architecture is also why the loop held.** The same boundaries that let a human extend it cheaply are what let the model build it reliably. Each analysis is a small unit with one job, a clear input (the IR), and a testable output (findings). The loop holds at this size because the architecture keeps every piece small enough to hold in context, spec, and verify. Link to agents-are-systems and the spec-driven loop.
5. **What "complete" means here.** Not a demo. A binary you install with Homebrew, a versioned Marketplace Action that starts in seconds, SARIF for code scanning, an MCP server, an LSP, OTLP export, and an end-to-end test per language per surface. The unglamorous last mile is part of the deliverable, and the loop did that mile too. This is the payoff of "complete".
6. **The honest part.** First person singular. The team was me and the model, the same division of labor the series describes. I owned intent and the load-bearing decisions, the model owned structure and execution. One line on where I still had to steer (confidence levels: never flag working code as dead just because resolution was hard).
7. **What this is not.** Not finished (v0.1, five languages, an IR contract for the long tail). Not a replacement for language-native tools. Not proof the model works alone. Pure open source.
8. **Close.** Repo link and the one command. Invitation: run `stratify check .` on your messiest polyglot repo and read the confidence levels.

## Links

- `https://github.com/stratify-dev/stratify` — the repo (primary CTA).
- `/posts/2026-05-19-the-spec-driven-loop/` — the method that built it.
- `/posts/2026-05-28-build-your-own-tools/` — the cost curve, an afternoon for a tool, carried to a platform.
- `/posts/2026-06-03-agents-are-systems-not-prompts/` — architecture is why the loop holds.
- `/posts/2026-06-12-conduit-launch/` — the first solo product; "I did this once already".

## Cover plan

Series palette via `tools/gen-cover.py`. Concept: five distinct mineral strata (the five languages) compressing downward into a single glowing amber core, which fans back out into beams of light (the surfaces). Teal rim light tracing the strata edges. Captures five into one into many, and the name Stratify. No text.

## Open questions

- None outstanding. Frame (build-story as spine), business model (pure open source), and usage depth (medium: one command plus five surfaces) settled in review on 2026-06-14.

## Decisions

- **Frame:** build-story as the spine, usage as evidence. Chosen over product-first (would clone Conduit) and interleave.
- **Business model:** pure open source, no paid-tier line. Chosen on purpose to differ from Conduit.
- **Usage depth:** medium, one command with output plus the five surfaces named. Chosen over Conduit's one-command cap and over a heavy per-surface walkthrough.
- **Voice:** first person singular, one line crediting the model as collaborator.
- **Antagonist:** "this used to take a funded team and a year", not named competitors.
- **Slug:** `stratify-launch`.
