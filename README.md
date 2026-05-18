# blog.dynaum.com

Field notes on building software and games with AI as a real collaborator.

Static site built with [Eleventy](https://www.11ty.dev/). Posts are Markdown in
`src/posts/`. The visual language is a sibling of [dynaum.com](https://dynaum.com)
— deep-ink console aesthetic, shared design tokens.

## Develop

```sh
npm install
npm run serve   # http://localhost:8080 with live reload
npm run build   # outputs static site to _site/
```

## Add a post

Create `src/posts/YYYY-MM-DD-slug.md` with front matter:

```yaml
---
title: "Post title"
subtitle: "One-line hook (optional)"
date: 2026-05-18
description: "Meta description for SEO / social."
---
```

Layout and tagging are inherited from `src/posts/posts.json`.

## Deploy

Every push to `main` triggers `.github/workflows/deploy.yml`, which builds the
site and publishes it to GitHub Pages. The custom domain `blog.dynaum.com` is
set via the `CNAME` file and a `CNAME` DNS record managed in the
`digitalocean-dns` Terraform repo.
