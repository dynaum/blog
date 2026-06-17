# Design spec: Commit the Context

- **Post file:** `src/posts/2026-06-15-commit-the-context.md`
- **Date:** 2026-06-15 (one day after the Stratify launch post)
- **Type:** Essay, 800 to 900 words
- **Thread:** Systems / workflow. The mechanics companion to "Your AI Context Belongs to the Team" (post 5). Post 5 made the philosophy case and reached for the vault; this post is the concrete in-repo machine: `CLAUDE.md` as committed, layered context that kills the setup tax.

## One-sentence pitch

The model forgets your repo between every session, so someone re-teaches it the same standing facts forever, and the fix is to write those facts once in a committed, layered `CLAUDE.md` so the repo briefs the model for the whole team and every future session.

## Goals

- Show `CLAUDE.md` as the file the model loads first, automatically, at the start of every session in a repo: write the standing facts once, commit, every developer's every session starts pre-briefed.
- Make the four-layer hierarchy a practical tool, not trivia: user (`~/.claude/CLAUDE.md`, your preferences across all projects), project (`./CLAUDE.md`, committed team facts), local (`CLAUDE.local.md`, gitignored, machine-specific), and the managed/policy layer for orgs. Concatenated, the layer closest to the work loads last.
- Show folder-scoped context: a subfolder `CLAUDE.md` loads on demand only when the model touches files in that subtree, so a monorepo gets per-package context without bloating every session.
- Cover the multi-project angle through the user layer: `~/.claude/CLAUDE.md` carries your durable preferences into every repo, the cross-project version of the same move, paired with the vault for durable domain knowledge.
- Land the core argument: an uncommitted context file is a personal note, a committed one is infrastructure. Commit it and the setup tax is paid once for the team and every future session, and it versions with the code so it stays true.

## The angle

The setup tax, paid once and version-controlled. The hook is a confession: the same sentences typed into every fresh session ("this repo uses pnpm not npm, tests live here, do not touch the generated files"), by you, your teammates, and every new chat. The model forgets between sessions because the context window is a desk, not a memory (link post 10). So the repeated teaching is structural, not laziness. The fix is to move the lesson out of the chat and into the repo, where git keeps it true.

Boundary that keeps this post distinct: it is the mechanics companion to post 5, not a re-argument of it. Post 5 owns "context is infrastructure" and the Obsidian vault for durable cross-project knowledge. This post assumes that and goes one level down, into the committed in-repo layer and how it stacks. Post 7 owns the product/intent half, untouched here. The vault gets a one-line pairing, not a re-explanation.

Authorship voice: first person singular, architect-by-day builder. Concrete, no hype.

## Proposed structure

1. **Hook (confession).** The same standing facts retyped into every fresh session, by everyone, forever. The model forgets between sessions ([the context window is a desk, not a memory](/posts/2026-06-10-context-window-desk-not-memory/)). Someone re-teaches it every time, unless the repo carries the lesson.
2. **The file the model reads first.** `CLAUDE.md`: committed Markdown loaded automatically at the start of every session in that repo. Write the standing facts once, commit, every developer's every session starts pre-briefed. The setup tax goes from per-developer-per-session to once.
3. **Four layers, nearest wins.** User (`~/.claude/CLAUDE.md`) for your preferences across all projects, project (`./CLAUDE.md`) for committed team facts, local (`CLAUDE.local.md`, gitignored) for machine-specific bits, and a managed policy layer for orgs. All concatenated, the layer closest to the work loads last. The split that matters: team facts committed, personal and machine facts out of the repo.
4. **Context that follows the folder.** A subfolder `CLAUDE.md` loads on demand when the model works in that subtree. A monorepo gets per-package rules without every session carrying the whole tree. Context scales with the codebase.
5. **Across projects, not just across people.** The user layer is the cross-project version of the same move: durable preferences ride into every repo you open. Pair it with the vault from post 5 for durable domain knowledge ([link](/posts/2026-05-22-your-ai-context-belongs-to-the-team/)). One line, not a vault re-explainer.
6. **Commit it, or pay the tax forever.** The core argument. Uncommitted context is a personal note; committed context is infrastructure. The moment you commit `CLAUDE.md` the setup tax is paid once for the whole team and every future session, and it versions with the code so it stays current. The "second time you explain it is a bug" discipline from post 5, now concrete and in git. One line that this is Claude Code's name and `AGENTS.md` is the cross-tool twin, so the post is not Claude-only.
7. **Close.** The model starts every session from zero. `CLAUDE.md` is how the repo remembers for it. Commit it and nobody pays the setup tax twice.

## Links

- `/posts/2026-05-22-your-ai-context-belongs-to-the-team/` — the philosophy and the vault; this post is its mechanics companion.
- `/posts/2026-06-10-context-window-desk-not-memory/` — why the model forgets, the reason the setup tax exists.
- `/posts/2026-05-24-context-is-not-a-dev-job/` — the product/intent half, optional one-line nod.
- `https://code.claude.com/docs/en/memory.md` — the memory-file reference, for readers who want the exact syntax and import rules.

## Cover plan

Series palette via `tools/gen-cover.py`. Concept: a stack of translucent layered sheets of Markdown text, each glowing warmer toward a single bright amber sheet at the base, the layers fanning slightly so the stacking reads as hierarchy, teal rim light along the sheet edges. No text legible. Captures layered, committed context.

## Open questions

- **Title.** Primary: "Commit the Context". Alternates: "Pay the Setup Tax Once", "The Repo Should Remember for the Model". Decide at draft time.

## Decisions

- **Frame:** the setup tax paid once and version-controlled. Mechanics companion to post 5, not a re-argument.
- **No non-goals section.** Removed at Elber's request; the one boundary (companion to post 5, not its repeat) lives in the angle instead.
- **Accuracy:** mechanics verified against code.claude.com/docs/en/memory.md (four-layer hierarchy, on-demand subfolder loading, committed vs gitignored local, AGENTS.md not native).
- **Multi-project angle:** carried by the user layer plus the vault pairing, not a separate section.
- **Slug:** `commit-the-context`.
