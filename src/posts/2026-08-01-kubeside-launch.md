---
title: "kubeside: The Refusal Is the Product"
subtitle: "A Kubernetes client scoped to the developer who ships the app, not the operator who runs the cluster. It answers four questions and refuses everything else, and the refusing is the part worth talking about."
date: 2026-08-01
description: "Announcing kubeside, an open-source Kubernetes client for application developers. Four questions across qa, stg, and prod, nothing written to disk, and a long list of features deliberately refused. Why naming the one person a tool serves turns the feature list into a subtraction problem."
cover: /assets/img/2026-08-01-kubeside-launch.png
coverAlt: "A dense field of dim geometric containers receding into darkness with one narrow amber corridor cut straight through them, lighting only a few containers along its path while the rest stay unlit, muted teal rim light on the block edges, brushstroke texture and soft bloom."
---

Three terminals open. A tab per replica. A guess about which version production is actually running.

The questions were never hard. Is my app up. What changed. What do the logs say. What configuration did the container get. Nobody built the screen for them.

Today kubeside is public.

## The wrong shape

Every Kubernetes UI mirrors the API tree. Pick a resource kind, browse instances, pick a cluster from a switcher. Good shape for the person who runs the cluster. Wrong shape for the person who ships an app.

A developer thinks in services, not ReplicaSets. Their unit of work is one app across qa, stg, and prod. Their questions are historical more often than live: what changed, who changed it, what did the container actually receive. So the dashboards end up as launchers for `kubectl`, and four questions stay unanswered.

## Four questions

kubeside answers exactly those four, side by side across every environment your kubeconfig reaches.

```
$ kubeside --print
── kind-kubeside-demo  [live]  high risk
   NAMESPACE  APP             KIND        READY  GROUPED BY          WHY
■  team-b     search-indexer  Deployment  0/2    recommended-labels  pod search-indexer-75f4d is in ImagePullBackOff
●  team-a     checkout        Deployment  4/4    recommended-labels
●  team-b     billing         CronJob     —      workload-name
```

Health is derived, and the row names what derived it. A pod stuck in `ImagePullBackOff` beats a red dot. The `GROUPED BY` column names the rule behind each row, so a list looking wrong tells you why it looks wrong.

The payoff screen is the promotion matrix. One row per app, one column per environment. A version prod has and staging does not floats to the top, because a hotfix nobody back-merged is the worst thing on that screen. Same tag with a different digest gets called out. An environment you cannot read says `not readable`, which is not the same as `absent`.

## The refusal

Here is the whole list of what kubeside will not do. No node view. No PersistentVolume browsing. No RBAC editor. No CRD browser. No Helm chart management. No cost reporting. No topology graph. No YAML editor beyond a read-only viewer. No plugin system.

Each one is a real need belonging to somebody else's tool. Ship any of them and this becomes a general-purpose dashboard, which is the thing there is already enough of.

The list is the product decision. I wrote the personas before any code existed. Five people the tool serves, and one more: the platform engineer, marked in the document as stakeholder, not a user. Every item on that list is something they need, and none of it shipped. Their tools are excellent. This is not one of them.

Name the single person a tool serves and the feature list stops being a wish list. It becomes a subtraction problem. Every no is a screen nobody designed, a permission model nobody reasoned about, a test suite nobody wrote. The nos are why ten days was enough.

Same move as [writing the persona down as a rule](/posts/2026-07-18-how-the-day-runs/) before handing work to an agent, one level up. There it aims a session. Here it draws a product boundary.

## The bet

kubeside writes nothing to disk. No database, no cache file, no history directory. Stop the server and nothing is left behind.

Sounds like a limitation until you see what it forces. The timeline is reconstructed on demand from history Kubernetes already keeps: ReplicaSets, ControllerRevisions, Helm release secrets, pod termination states, and events still inside the apiserver's TTL. Changes carry an actor read from `managedFields`, so the `kubectl` nobody admits to shows up next to the rollout it caused.

Everyone assumes history needs storage, so nobody assembled the history the cluster already holds. It was sitting there the whole time.

The bet pays twice. Two developers open kubeside during the same incident and see the same timeline, because both read the same cluster. A local database could never promise that.

## What it says when it does not know

The rule I care about most: absence of knowledge is not absence of a thing.

Where the reconstruction runs out, kubeside draws a horizon and labels it.

```
replicaset · older rollouts pruned by revisionHistoryLimit; revision 11 is the oldest the cluster still holds
event      · older events have expired from the apiserver, which keeps roughly an hour by default
session    · kubeside started watching here; anything before this comes from the cluster's own history
```

A metric it could not take is reported as unavailable, never as zero. A kind it could not list is named. A cluster it cannot reach says so in its own row instead of contributing silence to somebody else's list.

The same rule covers permissions. A control you lack is never hidden. It stays visible, disabled, and names the verb the cluster refused. A control that vanishes teaches nothing. One reading `needs create on pods/exec in team-a` tells you exactly what to go ask for.

This is the [same argument about knowing](/posts/2026-06-09-it-never-knows-it-doesnt-know/) the blog keeps making about models, applied to a dashboard. A tool rendering a gap as a quiet period is lying to you in the one hour you most needed it honest.

## Ten days

One Go binary with the UI embedded. It reads the kubeconfig already on your machine, loads every context, and runs exec credential plugins natively. If `kubectl` works, kubeside works. No agent in your cluster, no installer, no setup step. Credentials stay in the process, and the browser only talks to `127.0.0.1`.

Eighty commits, the first one ten days before this post. Tests came before implementation, and the repo now carries roughly a line of test per line of source across 518 test functions. CI runs the suite on Linux, macOS, and Windows, because compiling is not the same as working. A security review went over the write paths and the local server before v1.0.0, and everything it found is fixed.

The division of labor was the usual one. I owned the scope, the refusal list, and the rules about what the tool says when it does not know. The model owned structure and execution.

## Try it

```
brew install dynaum/tap/kubeside
kubeside
```

Apache-2.0, on [GitHub](https://github.com/dynaum/kubeside), documented at [kubeside.dynaum.com](https://kubeside.dynaum.com/).

One thing would help more than a star. Run `kubeside --print` against a cluster whose labelling nobody controlled, and tell me whether the app list matches what you call your apps. A cluster grouping mostly by `workload-name` is one where the label conventions earned nothing, and that is a finding about the cluster, not a bug in the tool.

That grouping is the whole bet. A clean demo cluster proves nothing, because its labels are perfect by construction. Only somebody else's messy cluster settles it.
