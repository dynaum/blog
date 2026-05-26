---
title: "Save the Boring Time"
subtitle: "The biggest AI time-save is not writing features, it is the ops work that surrounds them. Three flows, two automation surfaces, and the one rule that keeps it safe."
date: 2026-05-26
description: "Three ops flows where AI saves the most boring time per dollar (incident triage, prod enhancements, metrics pattern recognition), the two automation surfaces that run them (GitHub Actions and in-cluster Kubernetes agents), and the operator-in-the-loop rule that keeps a 13-hour outage from happening."
cover: /assets/img/2026-05-26-save-the-boring-time.png
coverAlt: "A dark operations room at night. The back wall is a grid of small glowing status indicators in muted teal and amber. A single warm amber lantern on a dark desk in the foreground sits beside an empty chair."
---

Eight posts on this blog about AI in the build cycle. The cycle is real and the value is real. But measure where developers spend their wasted time, and the answer is rarely "writing features." The answer is the work that surrounds writing features: triaging an alert at 03:00, reading three terabytes of logs after a deploy went wrong, scrolling Grafana to figure out why p95 climbed, hunting for the perf regression that ate a quarter.

That work is the boring time. It is also where the divide of labor this blog has been writing about pays best. The model gathers, reads, correlates, and drafts a concrete plan. The developer validates it and decides. Same physics as the build cycle. Different surface area, with a much bigger pool of boring minutes to save.

I work in a regulated domain where wrong code has consequences. Wrong incident response with consequences is even faster than wrong code shipping with consequences. That tilts the case harder. Anything that gets human eyes on the right hypothesis sooner is worth setting up.

## Three flows

**1. Incident triage.**

An alert fires. Today the on-call developer opens five tabs: logs, metrics, the most recent deploy, the issue tracker, the runbook. The first thirty minutes are gather-and-correlate. The next hour is decide.

The flow with AI: the alert triggers an agent that reads the alert, the related logs, the recent deploys, the relevant runbook, the recent PRs, the test history for affected files. It opens an issue (or replies to the PagerDuty incident) with a triaged summary, a ranked list of suspects, and a "what I would investigate first" plan. The developer wakes up to a triaged ticket, not a blank screen.

The category has a name now. Open-source options in this space in 2026 include [k8sgpt](https://github.com/k8sgpt-ai/k8sgpt), a CNCF Sandbox project that scans Kubernetes clusters and explains the findings through an LLM, and [HolmesGPT](https://github.com/robusta-dev/holmesgpt) by Robusta, an open-source incident-response agent that reads logs, alerts, runbooks, and metrics to produce a ranked diagnosis. When the alert flows through GitHub Issues, the [official Claude Code Action](https://github.com/anthropics/claude-code-action) handles the triage step inside a workflow.

**2. Prod enhancements.**

A scheduled agent reads the codebase, the perf metrics, the recent traces, the dead-code report. It identifies the actual hotspots, not the theoretical ones. It writes a PR with the fix, the new tests, and a short "here is why" body. The developer reviews and merges, or rejects with one comment.

Concrete examples: drop an N+1 query the agent found by correlating a slow trace with a query log, add caching on the hot endpoint, lazy-load the heavy component blocking LCP, delete the dead code path nobody calls.

This works because the agent has the same signals a senior engineer has after a slow Monday morning of digging, except it digs every night, on schedule, and the output is a PR you review, not a Jira ticket you procrastinate on.

**3. Pattern recognition on metrics.**

An agent watches dashboards (Grafana, Datadog, Honeycomb, your APM of choice) on a cadence. When p95 climbs, when error rate creeps, when a queue depth pattern shifts, it correlates the change with the deploy timeline, the feature flags, the commits, the dependencies. It posts a short "what changed and what looks suspicious" summary to the right Slack channel.

The developer goes from "scroll Grafana, then `git log`, then `kubectl get`" to "read the summary, decide if it is real." Same boring time, gone.

## Where the agent lives

Two surfaces, and the right one depends on what the agent needs to read.

**[GitHub Actions](https://github.com/anthropics/claude-code-action).** Event-driven, repo-scoped, easy to set up. The Claude Code Action listens for issue events, PR reviews, `@claude` mentions, or scheduled crons. Token use is metered. The published Auto-Triage Issues pattern shows a 62% reduction in token use across hundreds of runs once the prompt is tuned. Best fit for issue triage, PR triage, scheduled prod-enhancement scans, and any flow where the trigger is a repo event or a cron. The action runs on GitHub's runners, so it cannot see inside your cluster.

**In-cluster agent.** When the agent needs to read what is happening inside the cluster (Prometheus queries, Loki logs, traces, services not reachable from outside), it has to live inside. The pattern is a Kubernetes Job or Deployment running the agent with a scoped service account granting exactly the read permissions it needs. The canonical open-source framework for this is [kagent](https://github.com/kagent-dev/kagent), a CNCF Sandbox project originally from Solo.io. Agents are defined as Kubernetes CRDs, versioned in Git, reviewed in PRs, and deployed with the same tools the platform team already uses. Vendor-neutral on the LLM and tool side, with OpenTelemetry traces and Prometheus metrics built in. Best fit for incident triage that needs internal state, perf scans that need live APM access, and metrics pattern recognition that needs Prometheus directly.

Honest call. GitHub Actions is the right starting point. It is one YAML file, no platform-team conversation. You graduate to in-cluster when the agent needs context the action cannot reach.

## The non-negotiable: operator in the loop

In February 2026 a developer publicly documented a [30-day experiment](https://dev.to/mjkloski/i-gave-an-ai-agent-my-deploy-keys-for-30-days-heres-the-incident-report-1ad5) where an autonomous agent had production deploy keys. The agent caused a 13-hour outage by deleting an entire production environment while trying to fix a config error. Read [the incident report](https://dev.to/mjkloski/i-gave-an-ai-agent-my-deploy-keys-for-30-days-heres-the-incident-report-1ad5) if you are considering autonomy. It is a faster argument than any spec section.

The lesson is not "AI is dangerous." The lesson is the same one this blog has been writing for nine posts: **the model owns execution, the developer owns the decision.** For ops that means the agent triages, drafts, proposes. It does not act on production without a human approval step.

## The foundation, again

None of this works without the foundation underneath. For the build cycle, the foundation was specs and shared context. For ops, the foundation is **observability**: logs are searchable, metrics are real, traces exist, alerts are tuned, runbooks are written. The agent reads what is written. If the alert is wrong, the agent triages the wrong thing. If the runbook does not exist, the agent guesses.

Build observability first, then add the agent on top. The agent is the leverage layer, not the missing foundation.

## Close

The build cycle is one place AI saves time. Ops is the other, and it is larger, because that is where developers waste the most. Three flows save the most boring minutes: incident triage, prod enhancements, metrics pattern recognition. Two surfaces run them: [GitHub Actions](https://github.com/anthropics/claude-code-action) to start, in-cluster when you graduate. One rule keeps it safe: the developer validates the concrete plan, the agent never executes on production alone.

The build cycle was eight posts of foundation. This is what the foundation was for.
