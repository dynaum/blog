---
title: "Stratify: The Size of What One Person Ships Now"
subtitle: "A polyglot static-analysis engine. Five languages and six analyses through one model, reaching your terminal, CI, editor, AI agent, and dashboards. I built it solo with the spec-driven loop. The headline is not the tool. It is how little it took."
date: 2026-06-14
description: "Announcing Stratify, an open-source polyglot static-analysis engine: five languages, six analyses, one universal IR, and five surfaces. Built solo with the spec-driven loop, and why clean architecture is what lets one person ship a complete platform."
cover: /assets/img/2026-06-14-stratify-launch.png
coverAlt: "Five distinct mineral strata in cool tones compressing down into a single glowing amber core, which fans back out into bright beams of light, with teal rim light tracing the strata edges."
---

Five languages. Six analyses. Five surfaces. One binary. One person.

That last line is the headline. Stratify reads a whole repository written in Java, Ruby, TypeScript, Python, or Go, builds one model of it, and runs six static analyses on that model. The results reach you in five places: your terminal, a CI gate, your editor, your AI agent, and a fleet dashboard. I built it solo. A year ago the last sentence would have been a lie, or a funding round.

Today Stratify is public.

## What it does

Point it at a repo and run one command.

```
stratify check .
```

```
warn  Unused.java:2  unused function `neverCalled`
info  App.java:6  possibly unused function `helper`

2 finding(s).
```

Six analyses run in one pass: dead code, duplication, complexity, churn hotspots, dependency cycles, and layer boundaries that break your architecture rules. Every finding carries a confidence level. When Stratify cannot prove a function is dead, it says `possibly unused` instead of `unused`. It never flags working code as dead because resolution got hard.

The same engine fans out to five surfaces. The CLI prints findings or emits JSON and SARIF for code scanning. A GitHub Action turns any scan into a quality gate. An MCP server lets your coding agent query findings directly instead of parsing terminal text. A language server drops the same diagnostics into your editor. An OpenTelemetry exporter pushes every run to a dashboard, so you watch code health trend across a fleet of repos. One analysis, five places you already work.

That breadth is the usage story. The part I find more interesting comes next.

## The one decision that made it cheap

Five languages sounds like five times the work. It was not, because of a single decision made early.

Every analysis reads one shared model, never the source. tree-sitter parses each language into a Universal IR: symbols and references, each tagged with a confidence level. The six analyses read only that IR. They never see Java or Go or Ruby. They see the same shape every time.

So adding a language is one adapter that emits the IR. The six analyses come along untouched. That is how Stratify went from one language to five without changing a line of analysis code. The scope grew. The work did not grow with it.

## Why the same architecture let the loop hold

Here is the part this blog keeps circling.

The loop I describe, brainstorm, spec, plan, implement, does not hold because the model is magic. It holds because the architecture keeps every piece small. Each analysis is one unit with one job, one input, the IR, and one testable output, the findings. I hold a single analysis in my head. So does the model. The spec for it fits on a page. The test for it is a sample repo and an expected report.

Good boundaries are why a human team extends a codebase cheaply. The same boundaries are why the [loop builds it reliably](/posts/2026-06-03-agents-are-systems-not-prompts/). They are the same property. A codebase factored into small, well-bounded units is easy for a person to reason about and easy for a model to build, for one reason: you only hold one piece at a time.

The architecture is the thing a person decides. The model did not pick the IR. [I did](/posts/2026-05-19-the-spec-driven-loop/). That choice is what made everything after it tractable.

## What "complete" means here

A demo is easy. Complete is the boring part.

Complete means a binary you install with Homebrew or one curl line. A versioned GitHub Marketplace Action that downloads a prebuilt binary and starts in seconds. SARIF 2.1.0 that GitHub renders as inline annotations on a pull request. An MCP server and an editor language server. OTLP export with clean metric labels. An end-to-end test for every language on every surface, because five languages across six analyses across five surfaces is where the real bugs hide.

That last mile is most of the work in any real product. [Build Your Own Tools](/posts/2026-05-28-build-your-own-tools/) argued a custom tool now costs an afternoon. I shipped [Conduit](/posts/2026-06-12-conduit-launch/) the same way a few days back. Stratify is that curve carried to a platform. The afternoon became a few weeks. The team stayed at one.

## The honest part

The team was me and the model, the same division of labor every post here describes. I owned intent and the load-bearing calls. The IR. The choice to report `possibly unused` rather than guess, because a static analyzer that cries wolf gets turned off in a week. The model owned structure and execution: the adapters, the analyses, the surface wiring, the tests.

I steered most where correctness was subtle. Cross-file call resolution wants to over-report dead code the moment it loses a reference. Teaching it to say "I am not sure" instead of "this is dead" took judgment, not generation. That judgment is the job that stayed mine.

## What this is not

- Not finished. This is v0.1: five languages and an IR contract built so the long tail of languages is one adapter each.
- Not a replacement for your language-native tools. It is the one report that spans all of them.
- Not proof the model works alone. It is proof that one person, the loop, and a clean architecture ship what a team used to.
- Not for sale. Stratify is open source, full stop.

## Try it

Clone the [repo](https://github.com/stratify-dev/stratify), install the binary, and run `stratify check .` on your messiest polyglot repo. Read the confidence levels, not only the findings. The warnings are where it is sure. The rest is where it tells you it is guessing, which is the part most tools never admit.
