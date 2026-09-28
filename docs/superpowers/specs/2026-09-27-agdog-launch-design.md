# Design spec: agdog launch post

- **Post file:** `src/posts/2026-09-27-agdog-launch.md`
- **Date:** 2026-09-27 (today)
- **Type:** Essay, 800 to 1000 words
- **Thread:** Systems. Launch post. The fourth solo product after Conduit, Stratify, and kubeside. The argument the series has not made yet: a monitor that does not know what an agent is will hide your own machine from you.

## One-sentence pitch

agdog groups CPU, GPU, and memory by the agent that owns each process instead of by process or device, and writing one new signature for it exposed a bug that had been hiding every python-launched agent on my Mac for two months.

## Goals

- Launch agdog (github.com/dynaum/agdog, `brew install dynaum/tap/agdog`) with **attribution as the spine**: a process is not a unit of work, a device is not a unit of work, an agent is.
- Use one worked example end to end: the same document, the same eleven typed questions, one CLI flag apart. `doceval --backend laya` runs a local model. `--backend jev` calls a hosted one. agdog is what tells you which of the two is actually on your machine.
- Carry the honesty beat as a real event, not a posture: the test that proved Laya attribution works also proved agdog had been wrong. The `.app/Contents/` GUI-app exclusion matched `Python.app/Contents/MacOS/Python`, where every Homebrew interpreter lives, so Laya, ComfyUI, and kohya all fell into `unassigned` on macOS.
- Show the socket as the thing that makes agdog agent-native rather than a dashboard, with real captured events.
- State the unverified edges plainly. No NVIDIA hardware here, so the NVML path has no real-card coverage.
- One honest line on the division of labor, first person singular.

## Non-goals

- **Not an htop or nvitop teardown.** Both are named once, as lineage, never as the inferior thing. The antagonist is the grouping key, not a product. agdog's own README calls it "htop and nvitop, fused," so naming them is honest. Ranking them is not.
- **Not a Rust or ratatui walkthrough.** No crate list, no TUI architecture, no `sysinfo` versus `nvml-wrapper` comparison. Name the stack in one clause near the end.
- **No benchmark claim about Jev versus Laya.** One document, one profile, one run each. Report what the two runs printed. Do not generalize to which model is better, do not imply hosted beats local, do not extrapolate the timings.
- **Do not make Laya look broken.** Its confidence is uncalibrated out of the box, which its own authors document and a temperature fit on your own data fixes. The uncalibrated output is a real tradeoff of running locally, not a defect to score points off.
- **No GPU numbers I cannot stand behind.** This Mac reads GPU utilization through IOKit. There is no NVIDIA card here. Nothing in the post may imply verified per-process VRAM on NVIDIA or Windows.
- **No cost theater.** `--gpu-hourly` exists and derives a per-agent cost. With no GPU-hour bill to cite, it gets at most a clause, never a paragraph.
- **No "finished" framing.** 44 commits over eleven weeks. Early but runnable is the honest label, and it is the one the README uses.
- **No feature inventory.** The aggregate strip, per-GPU panels, sparkline, alerts, sort keys, and filter all ship. The post names the attribution model, one worked example, and the socket. The rest is the README's job.
- **No employer named.** Standing rule.
- **No Lanterns game-story opening.** Vary the hook.
- **No roadmap promises.** Per-process VRAM on Windows and calibration work are real gaps. Naming a gap is honest. Promising a date is not.

## The angle

Every monitor on your machine picks a grouping key, and the key is the design. `htop` groups by process. `nvitop` groups by device. Both were right for a machine that ran one job at a time.

The machine I actually work on runs seven coding sessions, an inference server, and whatever local model a script decided to load. Each of those is a tree of processes, not a process. So the question I have is never "what is PID 68715 doing," it is "which agent owns that 7.5 gigabytes, and is it stuck." No monitor answers that, because none of them knows what an agent is.

That is the whole product. Attribution is not a feature on top of a monitor, it is the monitor. Everything else in agdog exists to render the grouping.

The post earns this with one test rather than an argument. `doceval` asks eleven typed questions about a document and takes a `--backend` flag. With `--backend laya` the model runs here: agdog shows `laya infer working 219% 7.5G`. With `--backend jev` the same eleven questions go to a hosted model: agdog shows nothing, because nothing ran here. One flag, two entirely different machines doing the work, and the fastest way to see which is the monitor.

Then the turn. To make the Laya row appear at all I added a signature, and the test I wrote for the real macOS command line failed. Not because the signature was wrong. Because `is_excluded` dropped the process first: the rule that keeps Electron and `.app` bundles out of the agent list also matched `.../Python.app/Contents/MacOS/Python`, which is where Homebrew and python.org interpreters live. Every python-launched agent on this machine had been landing in `unassigned` since July. My own monitor had been hiding a third of my local AI work from me, quietly, and the only reason I found out is that I sat down to write one test with a real command line in it.

This lands on [It Never Knows That It Doesn't Know](/posts/2026-06-09-it-never-knows-it-doesnt-know/). agdog already refuses to invent GPUs it cannot read. It was still happy to report a confident, complete, wrong agent list.

Authorship voice: first person singular. One honest line in the build beat. I owned the grouping key, the refusal to fabricate numbers, and the decision to bump the version rather than quietly patch. The model owned structure and execution.

## Proposed structure

1. **Hook (confession).** I started a local model on my own machine, opened my own monitor, and it was not there. 890 processes in a single row called `unassigned`, 427% CPU, 21 gigabytes, no names.
2. **The grouping key.** `htop` groups by process. `nvitop` groups by device. Neither is wrong. Both answer a question about a machine that runs one job. Mine runs seven coding sessions and whatever a script loaded. The unit of work is an agent, and an agent is a tree.
3. **What you see.** The real `agdog agents` table: sessions named by their project directory, kind, state, CPU, memory, a `↳` subagent row. State colors as one line, not a legend.
4. **The test, one flag apart.** `doceval eval --backend laya` versus `--backend jev` on the same post, same profile. Real footers: `laya-multilingual · 0 tokens · 9.0s` and `jev-1.13.0 · 3,179 tokens · 0.6s`. The local run scored nothing usable because Laya's confidence is uncalibrated out of the box. The hosted run returned 0.82. Both numbers stay unspun. Then the point: agdog is what shows you the local run exists at all. Tie to [The Frontier Model Is Overqualified](/posts/2026-06-16-frontier-model-overqualified/) in one clause, because a 3.4 megabyte decision model answering eleven typed questions is that argument at its limit.
5. **Attribution, and the bug the test found.** Three tiers, highest confidence first: an `AGENT_ID` tag (Linux only, and say why), a command-line signature, then process-tree ancestry. Then the `Python.app` failure in full, and what it cost: two months of a confident wrong answer. The epistemic cross-link lands here.
6. **The socket.** Real captured events over the Unix socket. The reason it matters: an orchestrator subscribes and reacts to a stuck job instead of scraping a screen. One sentence that it is a local IPC primitive with no network port. Optional half-clause link to [prompt versus tool](/posts/2026-06-11-prompt-vs-tool/) if the word count allows.
7. **Edges and close.** What is verified per platform and what is not, in three lines. `brew install dynaum/tap/agdog`. The invitation: run it on a machine with a real NVIDIA card under real load and tell me whether the per-process VRAM numbers hold, because that is the one claim I cannot test here.

## Facts locked (verified 2026-09-27)

- Repo public at `https://github.com/dynaum/agdog`, MIT, Rust edition 2024, ratatui + sysinfo + nvml-wrapper.
- 44 commits, first on 2026-07-13. Eleven weeks.
- 3,291 lines of Rust in `src/`, 624 in `tests/`, 53 tests passing on macOS.
- `brew install dynaum/tap/agdog` serves 0.5.0 today. This session's fix is 0.5.1, committed locally and unpushed at the time of writing.
- `agdog agents` on this Mac, before the fix: seven `claude:<project>` rows, one `ollama` row, and `unassigned unknown working 890 427% 21.2G`.
- After the fix, with a Laya batch running: `laya infer working 1 219% 7.5G`.
- Launched from inside a coding session, the same run nests: `↳ laya sub working` under `claude:blog`.
- `agdog watch` captured real events, e.g. `{"kind":"state_changed","agent_id":"claude:stratify","from":"working","to":"idle","ts_secs":9}`.
- `doceval eval --backend laya` on `2026-08-01-kubeside-launch.md`: footer `laya-multilingual · 0 tokens · 9.0s · 0 cached`, verdict UNSCORED, all ten dimensions flagged for review below the 0.6 confidence gate.
- `doceval eval --backend jev` on the same file: footer `jev-1.13.0 · 3,179 tokens · 0.6s · 0 cached`, composite 0.82 GOOD, two dimensions flagged.
- Laya is `laya` 0.3.21, Apache-2.0, `convaiinnovations/laya`, a non-autoregressive System 1 decision model. The checkpoint cache on this machine is 3.4 MB.
- Jev is TypeSafe's hosted System One model, needs `TYPESAFE_API_KEY`, billed per token, calibrated confidence, 28,000-token document limit against Laya's 6,500.
- `is_excluded` bug: `.app/Contents/` matched `Python.app/Contents/MacOS/Python`. Present since the exclusion landed. `Python.app` is now exempt, covered by a test.

## Links

- `https://github.com/dynaum/agdog` — the repo (primary CTA).
- `/posts/2026-06-09-it-never-knows-it-doesnt-know/` — a confident, complete, wrong answer.
- `/posts/2026-06-16-frontier-model-overqualified/` — the right-sized model.
- `/posts/2026-07-18-how-the-day-runs/` — the parallel sessions the table is full of.
- `/posts/2026-08-01-kubeside-launch/` — the previous solo launch, and the document both backends scored.
- `/posts/2026-06-11-prompt-vs-tool/` — optional, for the socket beat.

## Cover plan

Series palette via the repo's cover tool. Concept: a dark field of many small identical dim blocks, and narrow amber light drawing a few of them together into three or four distinct clusters, each cluster lit as one connected shape while the loose blocks between them stay unlit. Teal rim light along the cluster edges. It reads as attribution: the same processes, grouped into owners. No text.

## Companion deliverables

- **Show HN.** Title plus a first-comment body, shown in the conversation, never saved to iCloud. Plain, no marketing, per HN norms: what it is, why the grouping key matters, what is verified and what is not, and the NVIDIA hardware ask. Links the repo, not the blog post.
- **LinkedIn.** 30 to 40 words, leads on a familiar pain, teases the two-month bug without naming the cause, ends with the English post URL.
- **X.** Two or three lines, same rules, ends with the English post URL.

## Open questions

- None outstanding. Angle (attribution as spine), the Jev/Laya example, the honesty beat, and the competitor policy (named as lineage only) settled in review on 2026-09-27.

## Decisions

- **Frame:** the grouping key as the spine, with the `--backend` test as evidence and the `Python.app` bug as the turn. Chosen over a straight feature tour (agdog's README already does that better) and over leading with the bug (it is the turn, not the thesis).
- **Competitors:** `htop` and `nvitop` named once as lineage, never ranked.
- **Jev and Laya:** reported, not benchmarked. Both footers quoted verbatim, no winner declared.
- **Unverified claims:** the NVML path has no real-card coverage and the post says so.
- **Version:** the fix ships as 0.5.1. The post links the repo, so the release must be pushed before or with publish.
- **Slug:** `agdog-launch`.
