# blog.dynaum.com — project knowledge base

The repeatable flow for every post. Spec first, draft second, publish last. Never out of order.

## The flow

1. **Topic.** A one-line idea. If the day job is involved, settle the framing first.
2. **Spec.** Write a design spec before any prose: `docs/superpowers/specs/YYYY-MM-DD-name-design.md`. Sections: one-sentence pitch, goals, non-goals, the angle, proposed structure, links, cover plan, open questions, decisions. The non-goals section is the load-bearing one.
3. **Review the spec.** Answer the open questions, adjust the angle. Only then draft.
4. **Draft.** Write `src/posts/YYYY-MM-DD-slug.md` against the locked spec.
5. **Review the draft.** A clean `.txt` copy goes to iCloud Drive root (`~/Library/Mobile Documents/com~apple~CloudDocs/<Title> - draft.txt`) for phone reading. Approve, or send edits.
6. **Cover image.** Generate once the text is approved. See Cover images.
7. **Publish.** Build locally, commit the post + image + spec, push to `main`. GitHub Pages deploys in under a minute.
8. **Translate.** Write the PT-BR twin. See Translation.
9. **LinkedIn.** Write a short companion text. See LinkedIn.

Rule: **never publish without an explicit go-ahead.** A push to `main` deploys live with no second gate.

## The post file

`src/posts/YYYY-MM-DD-slug.md`. Front matter (`layout`, `tags`, `lang` come from `src/posts/posts.json`, do not repeat them):

```yaml
title: "..."
subtitle: "..."
date: YYYY-MM-DD
description: "..."
cover: /assets/img/SLUG.png   # optional hero image
coverAlt: "..."               # describe the image
```

Date each post a day after the previous one. Eleventy sorts the index newest-first.

## Writing style

Global style, strictly: no em dashes, no hashtags, no semicolons. Short sentences, active voice. First person, architect-by-day builder voice. Honest, concrete, no hype.

- Recommendation post: 550 to 650 words.
- Essay or field note: 800 to 1000 words.
- Vary the opening hook. Each post earns its own: the central idea, a question, a confession, a quote. Do not lead with the Lanterns game story.
- A post should stand alone. Do not reference the count of other posts ("eleven posts", "post 12", "the series so far"). A reader can land here cold. Inline links to related posts are fine because they are optional.

## Cover images

Generated, not commissioned. Tool: **fal-ai**, model `fal-ai/flux/dev`. Always use the script so every post uses the same flow:

```bash
set -a && source ~/.local_config && set +a   # loads FAL_KEY
python3 tools/gen-cover.py YYYY-MM-DD-slug "<per-post concept sentence>"
```

- Size 1344x768, PNG. Saved to `src/assets/img/SLUG.png`.
- Fixed palette (constant across the series, lives in `tools/gen-cover.py`): painterly digital illustration, deep near-black charcoal background, a warm honey-amber focal glow as the dominant light source, a muted teal-cyan rim light, brushstroke texture, soft bloom. No text or words in the image.
- Only the per-post concept changes. The palette never changes.
- After generating, view the PNG to confirm it matches the series before committing.

## LinkedIn

Each post gets a short companion text, posted by hand. Saved to iCloud alongside the draft.

- 80 to 130 words.
- Ends with the post URL (`https://blog.dynaum.com/posts/SLUG/`, PT-BR under `/pt-br/posts/SLUG/`).
- No hashtags. Same style rules as the post.
- Opens with a hook that is not the game story.

## Translation

Bilingual: English at the root, Brazilian Portuguese under `/pt-br/`. English is canonical.

- Each English post gets a PT-BR twin at `src/pt-br/posts/YYYY-MM-DD-slug.md`, the **same filename** as the English file. The shared slug pairs them for the language switcher.
- Translate `title`, `subtitle`, `description`, `coverAlt`, and the body. Keep the same `date` and `cover` path.
- Internal links point at `/pt-br/posts/...` in the PT-BR version.

## Affiliate links

For a book or product recommendation, use the Amazon Associates tag `dynaum21-20`:

```
https://www.amazon.com/dp/<ASIN>/ref=nosim?tag=dynaum21-20
```

Pair every affiliate link with a one-line FTC disclosure.

## Build

```bash
npm run build      # one-off build into _site/
npm run serve      # local preview
```
