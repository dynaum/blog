---
title: "agdog: Your Monitor Does Not Know What an Agent Is"
subtitle: "A terminal monitor that groups CPU, GPU, and memory by the agent that owns them. Writing one new signature for it proved my own monitor had been hiding a third of my machine from me since July."
date: 2026-09-27
description: "Announcing agdog, an open-source terminal monitor that groups resources by the agent that owns each process instead of by process or device. The same eleven questions answered by a local model and a hosted one, one flag apart, and the bug a real command line exposed."
cover: /assets/img/2026-09-27-agdog-launch.png
coverAlt: "A vast grid of identical dark charcoal blocks receding into the distance, with three of them glowing warm amber from within while every other block stays unlit, muted teal rim light along the dark edges and soft bloom around the lit ones."
---

I started a model on my own machine, opened my own monitor, and the run was not there.

One row held everything I had not named. 890 processes, 427% CPU, 21 gigabytes, labeled `unassigned`. Somewhere in there a decision model was chewing through 400 support tickets, and my monitor had nothing to say about it.

Today agdog is public.

## The grouping key

Every monitor picks a grouping key, and the key is the whole design.

`htop` groups by process. `nvitop` groups by device. Neither is wrong. Both answer a precise question about a machine running one job at a time.

My machine does not run one job. Right now it runs seven coding sessions, an inference server, and whatever a script decided to load. Each of those is a tree of processes, not a process. A coding session is a binary, a dozen node children, and a couple of MCP servers.

So the question I have is never "what is PID 68715 doing." It is "which agent owns that 7.5 gigabytes, and is it stuck." Nothing on my machine answered that, because nothing on my machine knew what an agent was.

## What you see

```
$ agdog agents
AGENT                        KIND    STATE    PROC  CPU%    MEM  task
claude:blog                  coding  working    19   27%   0.9G  claude --resume e302a7b9
  ↳ claude:observer-sessions sub     idle                        [process]
claude:stratify              coding  idle       11    3%   0.7G  claude --resume 6840a557
claude:firestore             coding  idle       10    1%   0.3G  claude
laya                         infer   working     1  219%   7.5G  /opt/homebrew/Cellar/pyth
ollama                       infer   idle        1    0%   0.0G  /opt/homebrew/opt/ollama/
unassigned                   unknown working   828  279%  17.8G  /System/Library/Framework
```

That is a real capture with four session rows trimmed out. One row per agent. Parallel sessions take the name of their project directory, so `claude:blog` and `claude:stratify` never blur into one `claude` row. Child processes roll into the session that spawned them, and a subagent nests under its parent with a `↳`. Everything that is not an agent lands in `unassigned`, hidden until you press `a`.

State is derived from utilization and hold time: working, idle, stuck when memory is held with no activity, runaway when something is pegged and sustained, crashed. Stuck is the one I built this for. A wedged render holds its memory and looks exactly like a busy one in every other tool.

## One flag apart

Here is the test that made the point.

`doceval` asks eleven typed questions about a document. Is the voice active. Is the opening strong. Does a reader leave with the takeaway. It takes a `--backend` flag, and two models answer. Jev is hosted. Layla runs on your machine from open weights, and its whole checkpoint is 3.4 megabytes.

Same document, same eleven questions, one flag between them.

```
$ doceval eval --backend laya kubeside-launch.md
  kubeside-launch.md    --    UNSCORED
  ... ten dimensions, every one flagged for review ...
  laya-multilingual · 0 tokens · 9.0s · 0 cached

$ doceval eval --backend jev kubeside-launch.md
  kubeside-launch.md   0.82   GOOD
  ... ten dimensions, two flagged for review ...
  jev-1.13.0 · 3,179 tokens · 0.6s · 0 cached
```

The local run cost nothing and left no network. It also scored nothing usable: Layla ships over-confident, so every dimension fell below the confidence gate and got flagged for review. Fitting a temperature on your own data fixes that, which is work the hosted model already did. One run each on one document proves nothing about which model is better. That was never the question.

The question was where the work happened. With `--backend laya`, agdog shows `laya infer working 219% 7.5G`. With `--backend jev`, agdog shows nothing at all, because nothing ran here. Eleven questions left the building over HTTPS and came back as numbers.

A 3.4 megabyte model answering typed questions is [the overqualified-model argument](/posts/2026-06-16-frontier-model-overqualified/) at its limit.

## Attribution is the product

Three tiers, highest confidence first.

An explicit `AGENT_ID` environment tag wins over everything. Export it and the process is grouped under that name whatever the binary is called. Linux only, and the reason is worth knowing: macOS refuses to expose another process's environment, even to a parent. The tier is documented as unavailable there rather than left looking broken.

Below that, command-line signatures. Then process-tree ancestry, so a worker inherits its parent's agent.

That middle tier is where Layla was missing, so I sat down to add it. Layla ships as a console script, which means a venv run execs python with the script as an argument and the program name is `Python`, not `laya`. Fine. I wrote a test with the real command line pasted in.

It failed.

Not because the new signature was wrong. Because a rule above it dropped the process first. agdog excludes anything under `.app/Contents/` so that Electron apps and GUI helpers never masquerade as agents. A Homebrew interpreter lives at `.../Python.app/Contents/MacOS/Python`. Every python-launched agent on this machine had been falling into `unassigned` since July: Layla, ComfyUI, kohya training runs, all of it.

Two months of a confident, complete, wrong answer. The monitor I wrote to tell me what my machine was doing had been quietly hiding a third of it, and the only reason I found out is that I pasted a real command line into a test instead of a plausible one.

agdog already refuses to invent GPUs it cannot read. [Refusing to invent numbers](/posts/2026-06-09-it-never-knows-it-doesnt-know/) turns out to be the easy half. The hard half is a list that looks complete.

## Not a dashboard

A screen is a dead end for an orchestrator. So state changes also go out as JSON over a local socket, a Unix socket or a named pipe on Windows, both access-controlled by the OS with no network port open.

```
$ agdog watch
{"kind":"state_changed","agent_id":"claude:stratify","from":"working","to":"idle","ts_secs":9}
{"kind":"state_changed","agent_id":"claude:stratify","from":"idle","to":"working","ts_secs":22}
```

A session going quiet is the boring case. The same line shape carries a run going stuck or runaway, which is the one worth wiring up. Subscribe and react: kill the runaway, requeue the stuck job, hold the next batch until VRAM frees up. No screen scraping.

## What is verified, and what is not

Eleven weeks, 44 commits, one Rust binary on ratatui with no install-time dependencies. 53 tests pass on macOS.

macOS is the platform I use, so it is the one I trust: attribution, per-core CPU, and GPU utilization through IOKit all read real data. On Linux, process and memory attribution and the `AGENT_ID` tag are verified on real hosts. On Windows, attribution and the named pipe run as tests against a real host in CI.

The gap is hardware. I do not own an NVIDIA card. The NVML path compiles, is covered by unit tests, and has never read a real GPU under real load. Fabricated numbers appear only under `AGDOG_DEMO=1`, and the footer labels them `mock (simulated)`. With no readable GPU, agdog says so instead of drawing a device.

I owned the grouping key and the rule about never inventing a number. The model owned structure and execution.

## Try it

```
brew install dynaum/tap/agdog
agdog
```

MIT, on [GitHub](https://github.com/dynaum/agdog).

One thing helps more than a star. Run it on a machine with a real NVIDIA card under real load and tell me whether the per-process VRAM numbers match `nvidia-smi`. That is the one claim I cannot settle from here, and a clean bench run would not settle it either. It takes somebody's actual overloaded box.
