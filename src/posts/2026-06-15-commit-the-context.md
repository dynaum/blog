---
title: "Pay the Setup Tax Once"
subtitle: "The model forgets your repo between every session, so someone re-teaches it the same facts forever. A committed, layered CLAUDE.md is how the repo briefs the model for the whole team and every session that follows."
date: 2026-06-15
description: "How to kill the AI setup tax with CLAUDE.md: the file the model reads first, its four layers (user, project, local, policy), folder-scoped loading in a monorepo, and why committing it turns personal notes into team infrastructure."
cover: /assets/img/2026-06-15-commit-the-context.png
coverAlt: "A stack of translucent layered sheets of faint Markdown text, each glowing warmer toward a single bright amber sheet at the base, the layers fanning slightly to read as hierarchy, with teal rim light along the sheet edges."
---

Open a fresh session on a repo and the first thing you do is teach. "This project uses pnpm, not npm. The tests live in `test`, not next to the source. Do not edit anything under `generated`." You have typed these sentences before. You will type them again tomorrow. So will the developer next to you.

The model forgets every repo between sessions. [The context window is a desk, not a memory](/posts/2026-06-10-context-window-desk-not-memory/): each session starts clean, and the standing facts about your codebase leave when the tab closes. The teaching is not optional and nobody is being lazy. It is structural. Somebody re-pays it every session, forever, unless the repo itself carries the lesson.

The repo carries it instead. The fix is one committed file.

## The file the model reads first

`CLAUDE.md` is a Markdown file in your repo that the model reads automatically at the start of every session. No command, no paste. You write the project's standing facts in it once: the build and test commands, the conventions, the directories not to touch, the gotcha that bit you last month. Commit it. From then on, every developer's every session opens with that context already on the desk.

That is the whole move. The setup tax drops from once-per-developer-per-session to once, total. The twenty minutes of getting the model up to speed becomes a file you wrote in March.

## Four layers, nearest wins

The file is not one file. It is a stack.

- **Your layer.** `~/.claude/CLAUDE.md` holds your preferences across every project you open: your style, your habits, the way you like commits written. It rides into every repo and stays out of all of them.
- **The project layer.** `./CLAUDE.md` at the repo root holds the team facts. This is the one you commit.
- **The local layer.** `CLAUDE.local.md`, gitignored, holds what is true only on your machine: a sandbox URL, a local path, a personal shortcut. Yours, never pushed.
- **The policy layer.** Organizations set a managed file every repo inherits, for the rules that are not up for debate.

The model concatenates all of them, and the layer closest to your work loads last, so the specific wins over the general. The split that earns its keep is the middle two. Team facts go in the committed file. Personal and machine facts go in the gitignored one. Commit what everyone needs, keep out what only you need, and the repo never carries someone else's local path.

## Context that follows the folder

One `CLAUDE.md` at the root does not have to hold everything. Drop a `CLAUDE.md` inside a subfolder and the model loads it only when it works on files in that subtree.

This is what makes it scale. A monorepo with a Go service, a React app, and a shared schema gets three small context files, each sitting next to the code it describes. The model working in the React app never carries the Go service's rules. Each folder briefs the model about itself, on demand, and no single session drags the whole tree along.

## Across projects, not only across people

The setup tax is not only a team cost. You pay it across your own projects too. Every new repo you open is another clean desk.

The user layer is the cross-project fix. The preferences you put in `~/.claude/CLAUDE.md` follow you into every project, so the way you work is set once for all of them. For durable knowledge that outlives any single repo, the domain rules and the hard-won lessons, [a shared vault](/posts/2026-05-22-your-ai-context-belongs-to-the-team/) is the home, and the project file points at the specifics. The vault holds what stays true across projects. The committed file holds what is true for this one.

## Commit it, or pay the tax forever

Here is the line that matters. An uncommitted context file is a personal note. A committed one is infrastructure.

A note helps you, on your machine, until you reformat your laptop. Infrastructure helps everyone, on every machine, on every session, and it versions with the code so it stays true as the code changes. The moment you commit `CLAUDE.md`, the setup tax is paid once for the whole team and every session that follows. When you catch yourself explaining the same thing twice, that is the bug, and the fix is a paragraph in a file you already have.

One note on names. `CLAUDE.md` is Claude Code's filename. `AGENTS.md` is the same idea other tools read. Same move, different label.

## The repo remembers for you

The model starts every session from zero. It will, every time, by design. `CLAUDE.md` is how the repo remembers on its behalf. Write the standing facts down, commit them, and the next developer to open a session, including the future version of you, starts already briefed. Pay the tax once.
