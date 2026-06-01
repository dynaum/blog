---
name: writing-blog-post
description: Use when writing, drafting, translating, or publishing a post for blog.dynaum.com (the Eleventy blog in this repo), including generating its cover image, the PT-BR twin, deploying to GitHub Pages, and the LinkedIn companion.
---

# Writing a blog post for blog.dynaum.com

Spec first, draft second, publish last. The author (Elber) owns intent and every
go-ahead. A push to `main` deploys live with no second gate, so **never publish
without an explicit go-ahead.**

**REQUIRED BACKGROUND:** Use superpowers:brainstorming for the spec (steps 1-3).
The repo `CLAUDE.md` holds the canonical step list, style, and conventions; read
it. This skill adds the executable detail and the mistakes to avoid. The prose
playbook also lives in the Obsidian vault at
`~/Documents/obsidian/web/principles/writing-a-blog-post.md`.

## Flow (see CLAUDE.md for the authoritative order)

1. **Spec.** Brainstorm, then `docs/superpowers/specs/YYYY-MM-DD-name-design.md`.
   Non-goals is the load-bearing section. Commit it.
2. **Draft.** `src/posts/YYYY-MM-DD-slug.md`, dated one day after the latest post
   in `src/posts/`. Recommendation ~550-650 words; essay ~800-1000. Vary the hook.
3. **Review.** Present the full draft text inline in the chat (Elber reviews on
   the phone app, so paste the whole post, do not just link the file). Wait for
   approval.
4. **Cover.** Only after text is approved (see Cover).
5. **PT-BR twin.** `src/pt-br/posts/<same-filename>.md` (see Translation).
6. **Build + verify** (see Verify).
7. **Publish on go-ahead:** commit EN + PT-BR + cover, push `main`, confirm deploy.
8. **Vault catalog** (see Vault).
9. **LinkedIn:** 80-130 words, ends with the post URL, no hashtags. Posted by
   hand. **Tease, do not summarize:** open the gap and make the reader click.
   Name that there is an answer (e.g. "two ways, most people pick the costly
   one") without giving it. Do not restate the post's argument, lists, or
   payoff. If a reader gets the point without clicking, the teaser failed.
   Offer a PT-BR version too. **Both language versions link to the English post
   URL** (`/posts/SLUG/`), never the `/pt-br/` URL.

## Frontmatter

```yaml
title: "..."
subtitle: "..."
date: YYYY-MM-DD
description: "..."
cover: /assets/img/SLUG.png   # omit for a no-cover post
coverAlt: "..."               # describe the image
```

## Cover

Generated with the repo's canonical tool. Needs `FAL_KEY` in the env. Concept
changes per post; the fixed series palette is appended by the tool.

```bash
python3 tools/gen-cover.py YYYY-MM-DD-slug "<concept sentence>"
```

Writes `src/assets/img/<slug>.png` at 1344x768. View it before committing; if the
file is tiny (a few hundred bytes) the API returned an error page, not an image,
so rerun. Send it to the user for approval; regenerate with a new concept if rejected.

## Translation

English is canonical. The PT-BR twin uses the **same filename** (that shared slug
pairs them for the language switcher). Translate `title`, `subtitle`,
`description`, `coverAlt`, and the body. Keep the same `date` and `cover` path.
Repoint internal links: `/posts/...` becomes `/pt-br/posts/...`; external links
stay. Only article content is translated, not site chrome. PT-BR affiliate
disclosure: *"Os links da Amazon acima são links de afiliado. Se você comprar por
um deles, eu recebo uma pequena comissão, sem custo extra para você. Só recomendo
livros que eu mesmo estou lendo."*

## Verify (after `npm run build`, before publish)

```bash
grep -o 'src="/assets/img/SLUG.png"' _site/posts/SLUG/index.html       # cover wired
grep -o 'tag=dynaum21-20' _site/posts/SLUG/index.html | wc -l           # affiliate count
grep -o 'href="/pt-br/posts/' _site/pt-br/posts/SLUG/index.html | head  # PT-BR repointed
grep -n "—\|;" src/posts/SLUG.md                                        # style: expect none
```

## Publish (only on explicit go-ahead)

Commit EN + PT-BR + cover (+ spec) together. Push `main`. Confirm:

```bash
gh run list --branch main --limit 1   # wait for completed/success
curl -s -o /dev/null -w "%{http_code}" https://blog.dynaum.com/posts/SLUG/
```

End commit messages with the Co-Authored-By trailer.

## Vault

After publish, update the Obsidian catalog (outside this repo, not in the push):
- `~/Documents/obsidian/web/blog/posts.md` — add the post entry, bump the count.
- `~/Documents/obsidian/web/blog/README.md` — add to the series list, bump count.

## Common mistakes

- Reinventing the cover step with curl. Use `tools/gen-cover.py`; it is the tool
  the whole series uses.
- Generating the cover before the text is approved. Wait for step 3.
- Saving an error page as a `.png`. View the file; tiny size means rerun.
- Forgetting to repoint the PT-BR twin's internal links to `/pt-br/`.
- Pushing to `main` without an explicit go-ahead. It deploys live immediately.
- Equal post dates. Each post is dated one day after the previous one.
- Naming the employer. Keep ModMed unnamed unless explicitly cleared; anonymize
  as "a regulated domain where wrong code has consequences."
