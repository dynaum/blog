# Blog Internationalization — Design Spec

**Date:** 2026-05-22
**Status:** Draft, awaiting Elber's review.
**Author:** Session co-design (Elber Ribeiro + Claude).

## One-sentence pitch

Make blog.dynaum.com multilingual: English stays the default at the root, Brazilian Portuguese ships under `/pt-br/`, and the structure is built so Spanish slots in later with no rework.

## Goals

- Serve every article and the index in English (default) and PT-BR.
- Keep all existing English URLs unchanged, so shared and indexed links keep working.
- Build the i18n structure once, so adding Spanish later is dropping in translated files, not a rebuild.
- Translate the article content only. The site chrome (nav, index heading, footer, cookie note, labels) stays English on every page.
- Give readers a clear language switcher and give search engines correct `hreflang` signals.

## Non-goals (YAGNI)

- Spanish content now. The structure accommodates it, the translations come later, once a reviewer exists.
- Auto-translation with no human review. A translation is only as good as the person who can vouch for its voice.
- Translating the design specs in `docs/`. They are internal, English only.
- Browser-language auto-redirect. v1 uses an explicit switcher, no JavaScript routing.
- Right-to-left languages.
- Translating cover images. They carry no text and are shared across languages.
- A CMS or translation-management system. Markdown files, same as today.

## Approach decision

**Manual i18n, no plugin.** A `lang` field, per-language directories, per-language collections, a small language-metadata data file, and a language switcher in the template. Roughly fifty lines of `.eleventy.js` config plus template work.

Alternative considered: the official `@11ty/eleventy-plugin-i18n`. Rejected. The plugin expects every language under a directory prefix, including the default. That would move English from `/` to `/en/` and break every existing URL. Keeping English at the root is asymmetric, and a manual approach handles asymmetry cleanly. It also matches the blog's stated value of a tiny dependency surface.

## URL structure

- **English (default):** `/` for the index, `/posts/slug/` for posts. **Unchanged.** The five live posts keep their exact URLs.
- **PT-BR:** `/pt-br/` for the index, `/pt-br/posts/slug/` for posts.
- **Spanish (later):** `/es/` and `/es/posts/slug/`, mirroring PT-BR.

The default language carries no prefix. Only added languages get one.

## URL stability (hard requirement)

Every URL that resolves today must resolve to the same content after this change. This is a constraint the implementation is checked against, not a preference.

- The English index `/` and every English post `/posts/slug/` keep their exact paths.
- The implementation captures the full list of built URLs before the change and diffs it after. Every pre-existing URL must still be present and point to the same page.
- If any future change ever has to move an English URL, it ships with a redirect in the same change. Moving or renaming a live URL silently is not allowed.

The five posts are shared on LinkedIn and indexed by search engines. A broken URL loses inbound traffic and looks careless. Preserving them is non-negotiable.

## Content layout

```
src/
  index.njk              → /              English index
  posts/
    posts.json           lang: en, layout
    *.md                 → /posts/slug/   English posts, untouched
  pt-br/
    index.njk            → /pt-br/        PT-BR index
    posts/
      posts.json         lang: pt-br, layout
      *.md               → /pt-br/posts/slug/
  _data/
    site.js              site metadata
    strings.js           NEW: UI strings keyed by language
  _includes/
    base.njk             updated: lang attr, switcher, hreflang
    post.njk             updated: localized back link
  assets/img/            cover images, shared across languages
```

Adding Spanish later means adding `src/es/`, mirroring `src/pt-br/`.

## Pairing posts across languages

Each post carries a `translationKey` in its front matter, the shared slug, for example `the-spec-driven-loop`. The English file and its PT-BR counterpart use the same key. The language switcher finds a post's counterpart by matching `translationKey` in the other language's collection.

English is the canonical source. Every translation derives from the English original and is reviewed by a fluent speaker before publishing. PT-BR review is Elber's, he is native.

## Collections and the index

Posts are gathered into per-language collections (`postsEn`, `postsPtBr`, later `postsEs`), or one collection filtered by `lang`. Each language's index lists only its own posts, newest first. The implementation plan picks the simplest mechanism.

## UI strings

The site chrome stays English on every page. The nav, the index heading, eyebrow, and lede, the footer, the cookie note, and the rule-row labels are not translated. A PT-BR page is an English shell around translated article content. `src/_data/strings.js` holds only per-language metadata: the locale codes for `<html lang>` and `og:locale`, and the `EN` / `PT` switcher label.

Decided by Elber on 2026-05-22: keep the index title and footer in English, translate the article content only.

## Language switcher

A small switcher in the console-style header, in the blog's existing aesthetic. On a post, it links to the same post in the other language when a translation exists. On the index, it links to the other language's index.

When a post has no translation yet, the switcher hides that language's link rather than pointing at a dead end or a fallback page. A reader only sees a language link that leads somewhere real.

## SEO and metadata

- `<html lang>` set per page.
- `hreflang` alternate tags linking the language versions of each page, plus `x-default` to English.
- `og:locale` set per language (`en_US`, `pt_BR`).
- Canonical URL stays per language version.

## Effort

- **i18n scaffolding** (config, `strings.js`, `base.njk` and `post.njk` updates, switcher, `hreflang`, the PT-BR index): a few hours with AI assistance. One-time.
- **Back-translating the five existing posts to PT-BR**: producing the drafts is fast. The cost is Elber's review for voice, roughly an afternoon for the batch.
- **Per new post, going forward**: one extra translation and one extra review. This recurring tax is the real cost of a second language, and it is why Spanish waits for a reviewer.

## Resolved questions

All four resolved by Elber on 2026-05-22:

- **English keeps its root URLs.** Only added languages get a prefix. Confirmed.
- **A missing translation hides the switcher link.** A reader only ever sees a language link that leads to real content.
- **All five existing posts get translated to PT-BR now.** PT-BR launches complete, not backfilled.
- **No browser-language auto-redirect in v1.** Explicit switcher only, no routing JavaScript.

## Decisions

- **Manual i18n, no plugin.** Keeps English at the root and the dependency surface tiny.
- **English is default, at the root, URLs unchanged.** Preserves every shared and indexed link.
- **Chrome stays English, only article content is translated.** A PT-BR page is an English shell around a translated article. `strings.js` holds locale metadata only.
- **PT-BR ships under `/pt-br/`. Spanish is designed-for, not built.**
- **English is the canonical source.** Translations derive from it and are reviewed by a fluent speaker.
- **`translationKey` front matter pairs posts across languages.**
- **Cover images are shared. Design specs stay English only.**
- **The vault playbook gets a translation step.** After this ships, `principles/writing-a-blog-post.md` in the web vault needs the translate-and-review step added to the flow.

## Sequencing

Spec, then review, then an implementation plan, then build the scaffolding, then verify every pre-existing URL still resolves, then translate the five posts, then Elber reviews the PT-BR set, then publish. No publish without Elber's go-ahead. Same flow as a post.
