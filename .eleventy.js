module.exports = function (eleventyConfig) {
  eleventyConfig.addPassthroughCopy({ "src/styles.css": "styles.css" });
  eleventyConfig.addPassthroughCopy({ "src/favicon.svg": "favicon.svg" });
  eleventyConfig.addPassthroughCopy({ "src/assets": "assets" });
  eleventyConfig.addPassthroughCopy("CNAME");

  eleventyConfig.addFilter("readableDate", (d, locale) =>
    new Intl.DateTimeFormat(locale || "en-US", {
      year: "numeric",
      month: "long",
      day: "numeric",
      timeZone: "UTC",
    }).format(new Date(d))
  );

  eleventyConfig.addFilter("htmlDateString", (d) =>
    new Date(d).toISOString().slice(0, 10)
  );

  eleventyConfig.addShortcode("year", () => `${new Date().getFullYear()}`);

  // English posts (default language, served at the root).
  eleventyConfig.addCollection("posts", (api) =>
    api.getFilteredByGlob("src/posts/*.md").sort((a, b) => b.date - a.date)
  );

  // Brazilian Portuguese posts, served under /pt-br/.
  eleventyConfig.addCollection("postsPtBr", (api) =>
    api.getFilteredByGlob("src/pt-br/posts/*.md").sort((a, b) => b.date - a.date)
  );

  // Every localized page (posts and indexes), used to pair language versions.
  eleventyConfig.addCollection("localized", (api) =>
    api.getAll().filter((item) => item.data.lang)
  );

  // All language versions of one page, matched by translationKey (falls
  // back to fileSlug, which pairs dated post files across languages).
  eleventyConfig.addFilter("translations", (localized, key) =>
    (localized || []).filter(
      (item) => (item.data.translationKey || item.page.fileSlug) === key
    )
  );

  return {
    dir: {
      input: "src",
      includes: "_includes",
      data: "_data",
      output: "_site",
    },
    markdownTemplateEngine: "njk",
    htmlTemplateEngine: "njk",
  };
};
