# hFlow Help (Mintlify)

User-facing help for **hFlow**, published with [Mintlify](https://mintlify.com). Production site: **https://help.hflow.pro**

This repository is a **sibling** to the main hFlow app repo (e.g. clone it next to `Gilat/` as `hFlowDocs/`), similar to how the marketing site can live under `website/`.

## Local preview

From this directory (where `docs.json` is):

```bash
npm i -g mint
mint dev
```

Visit `http://localhost:3000`.

## Deploy

Mintlify **builds** your MDX. The live site must be served by **Mintlify** (or a reverse proxy to Mintlify), not by a plain Vercel “import this Git repo” static deployment.

- **Branch:** pushes to `main` should trigger Mintlify if the [GitHub app](https://dashboard.mintlify.com/settings/organization/github-app) is installed on **`gils1908/hFlowDocs`**.
- **Dashboard:** confirm the Mintlify project’s connected repo is **`gils1908/hFlowDocs`** (not an old starter repo such as `docs`). If the dashboard still points elsewhere, reconnect GitHub to this repository.
- **Domain:** add **help.hflow.pro** under Mintlify → [Custom domain](https://dashboard.mintlify.com/settings/deployment/custom-domain), then set DNS exactly as Mintlify shows (typically a **CNAME** for `help` → `cname.mintlify-dns.com`). See [Mintlify: Custom domain](https://mintlify.com/docs/settings/custom-domain).

### If help.hflow.pro shows raw Markdown / MDX (unstyled code)

That almost always means **a Vercel project is serving the repository as static files** (so the browser downloads `.mdx` as text). Mintlify never ran.

1. In **Vercel** → open the project that uses this repo (e.g. `hflow-docs`) → **Domains** → remove **help.hflow.pro** (or delete the project if it only exists for docs).
2. In **Mintlify** → add **help.hflow.pro** and complete DNS per their dashboard.
3. At your DNS host for `hflow.pro`, point **`help`** to Mintlify’s target (CNAME), not to Vercel’s A/ALIAS for the static site.

After DNS propagates, the URL should show the full Mintlify chrome (sidebar, theme), not monospaced source.

Optional: if you intentionally want docs on Vercel under another domain, use Mintlify’s [Vercel /docs subpath proxy](https://mintlify.com/docs/deploy/vercel) — do **not** expect raw MDX to render without that proxy or Mintlify hosting.

## When you change the product — update the docs

Use this checklist so help stays accurate:

1. **Identify the audience** — teachers, admins, or both?
2. **Update or add MDX** under `hflow/` (or new sections in `docs.json` if you add pages).
3. **Screenshots** — refresh images if the UI changed (store under `images/`).
4. **Release notes** — add a short bullet to `hflow/changelog.mdx` for user-visible changes.
5. **Preview** — run `mint dev` and click through the affected pages.
6. **Ship** — commit and push to `main`.

## AI-assisted writing

Optional Mintlify skill for editors using Cursor or other tools:

```bash
npx skills add https://mintlify.com/docs
```

## Repository

- **GitHub:** [gils1908/hFlowDocs](https://github.com/gils1908/hFlowDocs)

## License

See [LICENSE](LICENSE).
