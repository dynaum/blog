# Save the Boring Time — Design Spec

**Date:** 2026-05-26
**Status:** Draft, awaiting Elber's review.
**Author:** Session co-design (Elber Ribeiro + Claude).

## One-sentence pitch

A field-note post arguing that AI's biggest time-save is not in writing features, it is in the operations work that comes after, and that three flows (issue triage, prod enhancements, pattern recognition on metrics) plus two automation surfaces (GitHub Actions and in-cluster agents) save the most boring time per dollar, as long as a developer still validates the concrete plan.

## Framing decision

Employer-neutral, general advice. No team or colleague named. Same self-cast pattern as posts four and seven: "I spent eight posts writing about AI in the build cycle. The bigger time-save was somewhere else." The regulated-domain line returns, with the added stakes that incident response with wrong code has consequences faster than feature shipping with wrong code.

## Goals

- Land the thesis: **the boring time lives in ops**, not in writing the feature, and that is where the AI divide of labor pays best.
- Show three concrete flows where the divide of labor (model gathers and correlates, developer validates the concrete plan) maps cleanly to ops work: incident triage, prod enhancements, pattern recognition on metrics.
- Show two automation surfaces and when each fits: **GitHub Actions** (event-driven, repo-scoped, simple) and **in-cluster agents** (Kubernetes, full runtime access).
- Name the load-bearing safety condition: **operator-in-the-loop is non-negotiable.** A real 30-day case study where an unsupervised agent caused a 13-hour production outage is the reason.
- Tie back to the series: same intent/execution division, same foundation-first dependency (now: observability), same forcing-function pattern.

## Non-goals (YAGNI)

- A tool shootout (DrDroid vs Cleric vs Kestrel). Name them in passing as proof the category exists.
- An "AI replaces SRE" pitch. The opposite is the point.
- A GitHub Actions tutorial or a Kubernetes operator tutorial. Pointers and the patterns, not configs.
- A maturity model.
- Naming the employer, a team, or a colleague.
- Marketing language. No "10x", no "supercharge", no "revolution."
- Affiliate links.

## The thesis

Posts one through eight were about AI in the build cycle. The cycle is real and the value is real. But measure where developers actually lose time, and the answer is rarely "writing features." The answer is the work that surrounds writing features: triaging an alert at 03:00, reading three terabytes of logs after a deploy went wrong, scrolling Grafana to figure out why p95 climbed, hunting for the perf regression that ate a quarter.

That work is the boring time. It is also the work where the divide of labor we have been writing about pays best: the model gathers, reads, correlates, and drafts a concrete plan; the developer validates it and decides. Same physics as the build cycle. Different surface area, with a much bigger pool of boring minutes to save.

## The three flows

### 1. Issue debugging / incident triage

An alert fires. Today the on-call developer opens five tabs (logs, metrics, the most recent deploy, the issue tracker, the runbook) and starts from a blank screen. The first thirty minutes are gather-and-correlate. The next hour is decide.

The flow with AI: the alert triggers an agent that reads the alert, the related logs, the recent deploys, the relevant runbook, the recent PRs, the test history for affected files. It opens an issue (or replies to the PagerDuty incident) with a triaged summary, a ranked list of suspects, and a "what I would investigate first" plan. The developer wakes up to a triaged ticket, not a blank screen.

Tools in this category in 2026: [DrDroid](https://drdroid.io/), [Cleric](https://cleric.io/), [Kestrel AI](https://usekestrel.ai/), and the [claude-code-action](https://github.com/anthropics/claude-code-action) when the alert flows through GitHub Issues. The category has a name now: agentic operations.

### 2. Prod enhancements

A scheduled agent reads the codebase, the perf metrics, the recent traces, the dead-code report. It identifies the actual hotspots, not the theoretical ones. It writes a PR with the fix, the new tests, and a short "here is why" body. The developer reviews and merges, or rejects with one comment.

Concrete examples: drop an N+1 query the agent found by correlating a slow trace with a query log, add caching on the hot endpoint, lazy-load the heavy component blocking LCP, delete the dead code path nobody calls.

This works because the agent has the same signals a senior engineer has after a slow Monday morning of digging, except it digs every night, on schedule, and the output is a PR you review, not a Jira ticket you procrastinate on.

### 3. Pattern recognition on metrics

An agent watches dashboards (Grafana, Datadog, Honeycomb, your APM of choice) on a cadence. When p95 climbs, when error rate creeps, when a queue depth pattern shifts, it correlates the change with the deploy timeline, the feature flags, the commits, the dependencies. It posts a short "what changed and what looks suspicious" summary to the right Slack channel.

The developer goes from "scroll Grafana, then `git log`, then `kubectl get`" to "read the summary, decide if it is real." Same boring time, gone.

## The two automation surfaces

### GitHub Actions

Event-driven, repo-scoped, easy to set up. The [official claude-code-action](https://github.com/anthropics/claude-code-action) listens for issue events, PR reviews, `@claude` mentions, or scheduled crons. Token use is metered, and patterns like [Auto-Triage Issues](https://github.com/marketplace/actions/claude-code-action-official) show a 62% reduction in token usage across hundreds of runs once the prompt is tuned.

Best fit for issue triage, PR triage, scheduled prod-enhancement scans, and any flow where the trigger is a repo event or a cron. The action runs in GitHub's runners, so it cannot see inside your cluster.

### In-cluster agent (Kubernetes)

When the agent needs to read what is happening inside the cluster (Prometheus queries, Loki logs, traces, secrets, services not reachable from outside), it has to live inside. The pattern is a Kubernetes Job or Deployment running the agent with a scoped service account that grants exactly the read permissions it needs. Examples and frameworks for this exist (CastAI's agentic operations framing, and a growing class of "AI SRE" operators).

Best fit for incident triage that needs internal state, perf scans that need real APM access, and metrics pattern recognition that needs live Prometheus.

The honest call: GitHub Actions is the right starting point. It is one YAML file, no platform team conversation. You graduate to in-cluster when the agent needs context the action cannot reach.

## The non-negotiable: operator in the loop

In February 2026 a developer publicly documented a 30-day experiment where an autonomous agent had production deploy keys. The agent caused a 13-hour outage by deleting an entire production environment while trying to fix a config error. The lesson is not "AI is dangerous." The lesson is the same one this blog has been writing for eight posts: **the model owns execution, the developer owns the decision.** For ops that means the agent triages, drafts, proposes. It does not act on production without a human approval step.

Read the [postmortem](https://dev.to/mjkloski/i-gave-an-ai-agent-my-deploy-keys-for-30-days-heres-the-incident-report-1ad5) if you are considering autonomy. It is a faster argument than any spec section.

## The foundation, again

Same shape as the rest of the series. None of this works without the foundation underneath.

For the build cycle, the foundation was specs and shared context.

For ops, the foundation is **observability**: logs are searchable, metrics are real, traces exist, alerts are tuned, runbooks are written. The agent reads what is written. If the alert is wrong, the agent triages the wrong thing. If the runbook does not exist, the agent guesses.

The post is not subtle about this: build observability first, then add the agent on top. The agent is the leverage layer, not the missing foundation.

## Proposed structure

1. **Hook.** Eight posts on AI in the build cycle. The bigger time-save was somewhere else.
2. **The thesis.** The boring time lives in ops. Same divide of labor, more minutes to save.
3. **The three flows.** Incident triage, prod enhancements, metrics pattern recognition. One short section each.
4. **The two automation surfaces.** GitHub Actions for repo-event flows, in-cluster agents when the agent needs runtime state.
5. **The non-negotiable.** Operator in the loop. The 30-day-outage story.
6. **The foundation.** Observability is to ops what specs are to the build cycle.
7. **Close.** Build observability, point the agent at it, validate the plan, sleep.

Target length: 1000 to 1200 words.

## Working title

**"Save the Boring Time"**

Subtitle: *The biggest AI time-save is not writing features, it is the ops work that surrounds them. Three flows, two automation surfaces, and the one rule that keeps it safe.*

Alternative titles:
- "AI After the Deploy"
- "The Boring Part of Operations"
- "Triaged Before You Open the Alert"
- "Let the Agent Read the Logs"

## Links

- claude-code-action: https://github.com/anthropics/claude-code-action
- claude-code-action marketplace: https://github.com/marketplace/actions/claude-code-action-official
- DrDroid: https://drdroid.io/
- Cleric: https://cleric.io/
- Kestrel AI: https://usekestrel.ai/
- Cast AI (agentic operations): https://cast.ai/blog/agentic-operations/
- 30-day case study (deploy keys, outage): https://dev.to/mjkloski/i-gave-an-ai-agent-my-deploy-keys-for-30-days-heres-the-incident-report-1ad5
- Internal: spec-driven loop, `/posts/2026-05-19-the-spec-driven-loop/`
- Internal: shared context, `/posts/2026-05-22-your-ai-context-belongs-to-the-team/`
- Internal: pipeline trust, `/posts/2026-05-23-trust-the-pipeline/`
- Internal: pick a framework, `/posts/2026-05-25-pick-a-framework-any-framework/`

## Cover image plan

Same FLUX pipeline and dark amber-and-teal palette as posts two through eight. Concept: a dark control wall at night with a grid of many small glowing status indicators, mostly calm amber and teal, with a few brighter ones that need attention. A single warm desk lantern in the foreground shows where the human sits. The agent watches so you can sleep; you still decide. Painterly. No text in the image.

## Open questions for Elber

- Reuse "regulated domain where wrong code has consequences" again? Recommendation: yes, with the addition that wrong incident response with consequences is faster than wrong code shipping with consequences. Sharpens the stakes.
- Name DrDroid, Cleric, and Kestrel by name, or stay tool-agnostic? Recommendation: name them briefly, the way post 8 named Conductor and Claude Squad. The category is now real and proof-of-existence matters.
- Include the 30-day-outage cautionary tale? Recommendation: yes. It makes the "operator-in-the-loop" point in a paragraph what would otherwise take a section.
- Should the GitHub Actions vs in-cluster framing be a fork ("start with Actions, graduate to cluster") or two equal options? Recommendation: fork. GitHub Actions is one YAML; cluster is a platform conversation. Honest about the on-ramp.

## Decisions

- **Employer-neutral.** No team or colleague named.
- **Thesis first.** The boring time lives in ops. Tools and patterns are the supporting evidence.
- **Operator-in-the-loop is named and grounded** in the 30-day case study.
- **GitHub Actions is the on-ramp, in-cluster is the upgrade.** Honest about the path.
- **Observability is the foundation.** No agent fixes a missing log.
- **No affiliate links.** Methodology post.
- **Cover generated, not commissioned.** Consistent with the rest of the series.

## Sequencing

Post nine in the build-with-AI arc, after the frameworks post. Publish after Elber reviews this spec and answers the open questions. Same flow as before: spec, draft to iCloud, review, cover, publish EN + PT-BR together per the playbook, then LinkedIn.
