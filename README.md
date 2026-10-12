# Infinimesh website

Static site published at https://infinimesh.org/.

`index.html` is the page (inline CSS and SVG). `llms.txt`, `llms-full.txt`, `robots.txt`, `sitemap.xml` and `social/` sit at the root. `images/favico.webp` and `images/logo_03.png` are the mark. Apache-2.0.

## Check before you commit

```bash
make commit-check
```

This runs htmlhint, a lychee link check, a check that every sitemap URL and every infinimesh.org link in `llms.txt` and `llms-full.txt` has a file in this repo, actionlint, yamllint and gitleaks. CI runs the same checks on every pull request. On Linux, `sh scripts/install-lint-tools.sh` installs the tools; on macOS use `brew install htmlhint lychee actionlint yamllint gitleaks`.
