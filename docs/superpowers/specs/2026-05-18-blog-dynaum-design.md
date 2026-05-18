# blog.dynaum.com — Design Spec

**Date:** 2026-05-18
**Status:** Approved, implemented.
**Author:** session co-design (Elber Ribeiro + Claude).

## One-sentence pitch

A personal blog at `blog.dynaum.com` for articles about building software and
games with AI, opening with the story of how Lanterns was built.

## Goals

- A public blog repo (`dynaum/blog`) that is cheap to add posts to (drop a
  Markdown file).
- Subdomain `blog.dynaum.com` wired through the existing DNS-as-code setup.
- Visual continuity with `dynaum.com` — the blog should read as a sibling of
  the main site, not a generic theme.
- First post published: how Lanterns started (tool, engine decision, AI's role).

## Non-goals (YAGNI)

Comments, analytics, RSS/Atom, tags or search, multi-author support, a CMS,
pagination. None are needed for a low-frequency personal blog. Any can be added
later if a real need appears.

## Stack decision

**Eleventy (11ty), Markdown posts, deployed to GitHub Pages via GitHub Actions.**

Alternatives considered:

- **Pure hand-authored static HTML** — matches `dynaum.github.io` exactly, zero
  build, but every post is hand-written HTML plus a manually maintained index.
  Rejected: drudgery scales badly with post count.
- **Astro** — more capable, component-driven, but a heavier toolchain than a
  text blog needs. Rejected: complexity not justified.

Eleventy is the middle ground: Markdown in, static HTML out, tiny dependency
surface, Node/npm toolchain (consistent with the rest of the user's tooling and
their package-manager preference), and GitHub Actions deploy (already used for
the Lanterns web build).

## Architecture

Static site generator. No runtime, no server, no database.

```
src/
  _data/site.js         — site-wide metadata (title, url, author)
  _includes/base.njk    — HTML skeleton: head, sticky console header, footer
  _includes/post.njk    — article layout (rule-row, title, prose, back link)
  index.njk             — post list (newest first)
  posts/
    posts.json          — directory data: layout + "posts" tag for all posts
    YYYY-MM-DD-slug.md   — one Markdown file per post
  styles.css            — ported dynaum.com console design tokens + prose
  favicon.svg           — copied from dynaum.com for brand continuity
.eleventy.js            — config: passthrough, date filters, posts collection
CNAME                   — blog.dynaum.com (GitHub Pages custom domain)
.github/workflows/deploy.yml — build + deploy to GitHub Pages
```

**Data flow:** `eleventy` reads `src/`, renders Markdown posts through
`post.njk` → `base.njk`, builds the index from the `posts` collection (sorted by
date desc), copies `styles.css`, `favicon.svg`, and `CNAME` through untouched,
and writes static HTML to `_site/`. GitHub Actions uploads `_site/` as a Pages
artifact and deploys it.

**Filters/shortcodes:** `readableDate` (Intl, UTC) and `htmlDateString` for
`<time>` elements; a `year` shortcode for the footer copyright. No third-party
date library — keeps the dependency surface to a single dev dependency.

## DNS

`blog.dynaum.com` is a `CNAME → dynaum.github.io.` record, mirroring the
existing `www.dynaum.com` record exactly (same type, same trailing-dot value,
`ttl = 1800`, no import block because the record is new). It is added to
`dns.tf` in the `digitalocean-dns` Terraform repo. GitHub Pages routes the
correct site by Host header / the repo's `CNAME` file — the same mechanism that
already serves `www`.

This deliberately does **not** use the DigitalOcean CDN + Cloudflare Pages path
that `lanterns.dynaum.com` uses. That path exists only because the game web
build ships large WASM assets; a text blog has no such need.

The DNS change is applied by the user with `terraform apply` after reviewing
`terraform plan` — infra changes against the live DigitalOcean account are not
auto-applied.

## Testing

Build correctness is verified locally (`npm run build`, inspect `_site/`) and in
CI on every push. There is no application logic to unit-test — the site is
static content through a generator. The meaningful verification is: the site
builds, the post renders, and `blog.dynaum.com` resolves and serves it once DNS
propagates.

## First post

`2026-05-18-building-lanterns-with-ai.md` — "Building a Game with AI Only: How
Lanterns Started." Sourced from real repo evidence: the Lanterns design spec,
the engine-pivot commit `f294c14` (vanilla Canvas → Godot 4 and its stated
rationale), the `docs/superpowers/specs/` trail, and the `Co-Authored-By:
Claude` commit history. Covers: the idea, the spec-first tool/workflow, the
engine decision framework, an honest account of the AI's role, and where
Lanterns is today.
