# QA / Pipeline-Trust Post — Design Spec

**Date:** 2026-05-23
**Status:** Draft, awaiting Elber's review.
**Author:** Session co-design (Elber Ribeiro + Claude).

## One-sentence pitch

A field-note post arguing that QA is the bottleneck that decides delivery throughput, that trust in the pipeline is the unlock, and that AI-written Playwright tests orchestrated by Testkube is the practical path to both.

## Framing decision

Employer-neutral, general advice. No team, colleague, or specific pipeline is named. Elber writes as an architect inside "a large engineering org" and, where it matters, "a regulated domain where wrong code has consequences." Same protection as the AI-DLC post.

## Goals

- Land the thesis: **pipeline trust is the unlock for delivery**. Without it, every other delivery improvement is downstream of fear.
- Name the five properties that make a CI pipeline trustworthy.
- Explain the **record-then-refine** pattern for AI-written Playwright tests, and why "ask the AI to imagine a test" fails.
- Explain why **Testkube** belongs above the CI runner, not inside it, and when it is the right fit.
- Tie the post to the series: trust from Frictionless, steering files from AI-DLC, shared test patterns from the context post, spec-then-AI from the loop post.

## Non-goals (YAGNI)

- A Playwright tutorial. The docs are the docs.
- A Testkube install guide. The Helm chart is the Helm chart.
- A comparison shootout (Playwright vs Cypress, Testkube vs Jenkins). Brief one-line nods, not a chart.
- Naming the employer, a team, or a colleague.
- A QA maturity model with stages. This is a field note, not a framework launch.
- Selling AI as a magic test-writing button. The post is explicit about the human review the pattern still requires.
- Affiliate links. This is methodology.

## Topic background

**Playwright** is Microsoft's open-source browser automation framework, the current industry default for end-to-end web tests. The relevant 2026 piece is the **AI ecosystem around it**: a `playwright codegen` recorder, a Playwright **MCP** server for agents, and a "record-then-refine" pattern where the model gets a real interaction trace as its input and produces clean, idiomatic tests as output. The teams that get value pair AI agents with CI visibility and flaky-test tracking.

**Testkube** is a Kubernetes-native test orchestration platform from Kubeshop, positioned (their own words) as the "Open Testing Platform for AI-Driven Engineering Teams." It runs any dockerizable test framework (Playwright, Cypress, Selenium, K6, Postman) inside the cluster, with native **parallelization and sharding** and **centralized artifacts** (logs, reports, videos, traces). It separates test orchestration from CI logic, which is the move that lets a pipeline scale past what a GitHub Actions runner can give you.

The post does not teach either tool. It uses them as the concrete answer to two distinct problems: "who writes the tests" and "where do they run."

## The angle

The thesis lands before the tools: **trust the pipeline, or you will not ship.** Every "we want to ship faster" conversation is, when you trace it back, a conversation about whether the pipeline is trusted enough to let people merge without ceremony. The five properties of a trusted pipeline give the post its spine. Playwright + AI and Testkube enter as the practical answers, not as the thesis.

Elber is self-cast as someone who learned this the hard way: pushing for more deploys per week, then realizing the throughput was capped by fear of the pipeline, not by deploy mechanics.

## The thesis: trust is the unlock

The post argues that pipeline trust has five properties, in order of importance:

1. **Deterministic.** A red build is a real failure; a green build is safe to ship. Flake destroys trust faster than any other failure mode, because once a single test has cried wolf, every red build is now suspect.
2. **Comprehensive enough.** Covers the user flows that matter, not every method. Coverage theater hurts trust because green builds still ship bugs.
3. **Fast enough.** Feedback inside the developer's flow window. A 45-minute pipeline gets ignored, batched, or worked around. Under 10 minutes is the goal.
4. **Owned.** A test that nobody is responsible for is a test that rots. The pattern that keeps tests current is more important than the tests themselves.
5. **Honest.** No skipped tests hiding regressions, no flake-quarantine drawer that quietly grows, no green builds covering known failures.

A pipeline with all five gets trusted. A pipeline missing any one of them does not. And without trust, every deploy is a meeting.

## AI to write Playwright: record then refine

The post explains the working pattern, which is the spec-driven loop applied to tests:

- **Do not ask the AI to imagine a flow.** It hallucinates selectors and invents assertions that pass for the wrong reason.
- **Record first, refine second.** Use `playwright codegen` (or a Playwright MCP session) to capture a real interaction trace. That trace is the AI's input, the way a spec is the AI's input for a feature.
- **Refine to the rules.** The model rewrites the recording into idiomatic Playwright: `getByRole`, `getByLabel`, `getByTestId` selectors; web-first assertions; no `nth` / `first` / `last` chaining; no hard `waitForTimeout`; helpers extracted; one test, one concern.
- **Review like code.** A generated test is a draft. It enters the same review as any other code, because a wrong test that passes is worse than no test.

This is exactly the architect-owns-intent, model-owns-execution split from post one, with the test recording playing the role of the spec.

## Testkube: orchestration above the runner

The post explains why Testkube belongs above the CI runner, not inside it:

- A 200-test Playwright suite on a single GitHub Actions runner is a 25-minute serial run. The same suite sharded across 20 Testkube pods is 90 seconds. Property 3 (fast enough) lives or dies here.
- Test runs stay alive past the CI job. Artifacts, traces, videos, and flake history live in one place that does not vanish when the runner does.
- The CI job becomes one line: "trigger Testkube, wait, gate on result." All the testing complexity moves out of the YAML.
- It is **K8s-native** by design. If the team already lives on Kubernetes, this fits. If the team is on a small Vercel project with no cluster, Testkube is overkill, the honest answer is the GitHub-Actions matrix.

The post will be explicit about that fit: Testkube is the right answer when you already run on Kubernetes, when one runner cannot give you the parallelism you need, or when you need test results to outlive the CI job. Otherwise it is more platform than the problem deserves.

## Series callbacks

- **Post 3, Frictionless.** Trust is the sixth SPACE dimension Forsgren and Noda add for the AI era. This post is what Trust looks like inside a CI pipeline.
- **Post 4, AI-DLC.** The five Playwright rules above are exactly a set of steering files for the test-writing agent. Same pattern.
- **Post 5, shared context.** Test fixtures, helpers, selector conventions, and the testid policy belong in the shared vault. The pipeline only stays trusted because the conventions that produce trustworthy tests are written down once and reused.
- **Post 2, the spec-driven loop.** Record-then-refine is the loop applied to tests. The recording is the spec.

## Proposed structure

1. **Hook.** Every "ship faster" conversation is actually a "trust the pipeline" conversation. Self-cast: I learned this by pushing for more deploys and being held back by fear, not by mechanics.
2. **The five properties of a trusted pipeline.** Each property in one short paragraph, in order of importance.
3. **The bottleneck is writing the tests.** Why test coverage is hard at the rate features ship, and why this is where AI changes the equation.
4. **Record then refine.** The pattern, the rules, the review.
5. **The bottleneck is running them.** Why a 25-minute pipeline is a non-pipeline.
6. **Testkube above the runner.** What it is, why it lives outside CI logic, when it is the right fit, when it is overkill.
7. **Tying it back.** Pipeline trust is the Trust dimension from Frictionless made concrete. The steering files and shared context posts are where the patterns live.
8. **Close.** You do not unlock delivery by deploying more. You unlock it by trusting the gate that decides whether you can.

Target length: 800 to 1000 words. Meatier essay, like the AI-DLC and context posts.

## Working title

**"Trust the Pipeline"**

Subtitle: *Every "ship faster" conversation is actually a "trust the pipeline" conversation. Five properties of a trusted CI, plus the AI-written Playwright and Testkube setup that gets you there.*

Alternative titles:
- "QA Is What Unlocks Delivery"
- "The Bottleneck Is Always the Pipeline"
- "Five Properties of a CI Pipeline You Can Trust"
- "Stop Shipping Around the Pipeline"

## Links

- Playwright: https://playwright.dev/
- Playwright MCP (Microsoft): https://github.com/microsoft/playwright-mcp
- Testkube: https://testkube.io/
- Testkube Playwright executor: https://docs.testkube.io/test-types/executor-playwright
- Internal: the spec-driven loop post, `/posts/2026-05-19-the-spec-driven-loop/`
- Internal: the Frictionless post, `/posts/2026-05-20-frictionless-the-book-behind-the-loop/`
- Internal: the AI-DLC post, `/posts/2026-05-21-you-cannot-push-a-developer/`
- Internal: the shared-context post, `/posts/2026-05-22-your-ai-context-belongs-to-the-team/`

## Cover image plan

Same FLUX pipeline and dark amber-and-teal palette as posts two through five. Concept: a long dark corridor or pipeline of gates and arches, each gate lit by a small warm amber lantern, the path forward clearly traceable through every checkpoint. Painterly. No text in the image. Each gate is a test; every gate burns clean.

## Open questions for Elber

- Are you comfortable reusing the "regulated domain where wrong code has consequences" line from the AI-DLC post? Recommendation: yes, it is the truthful frame for why pipeline trust matters more in your context.
- Do you have one concrete anonymized win to mention ("we went from a 45-minute pipeline to 4 minutes" or similar)? It would land harder than the general argument. Recommendation: include if you have it, skip if it would expose the employer.
- Do you want the post to name Testkube specifically, or stay tool-agnostic? Recommendation: name it. Specifying is more honest and useful than "an orchestration platform."
- Is the self-cast as "the architect who learned trust is the bottleneck the hard way" acceptable? Recommendation: yes, the same self-aware frame that worked in post four.
- Any rule on the five-rules-of-testing list you want to add, swap, or drop?

## Decisions

- **Employer-neutral, general advice.** No team or colleague named.
- **Thesis first, tools second.** The five properties of pipeline trust carry the post; Playwright + Testkube are the concrete answers, not the lede.
- **Honest about fit.** Testkube is named, and the post says when it is overkill (no K8s, small suite).
- **Series callbacks required.** Trust from Frictionless, steering files from AI-DLC, shared patterns from the context post, spec-then-AI from the loop post.
- **No affiliate links.** Methodology post.
- **Cover generated, not commissioned.** Consistent with posts two through five.

## Sequencing

Post six in the build-with-AI arc, after the shared-context post. Publish after Elber reviews this spec and answers the open questions. Same flow as before: spec, draft to iCloud, review, cover, publish, LinkedIn, then PT-BR translation per the [vault playbook](../../../Documents/obsidian/web/principles/writing-a-blog-post.md). No publish without Elber's go-ahead.
