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

- **Branch:** pushes to `main` should trigger Mintlify if the [GitHub app](https://dashboard.mintlify.com/settings/organization/github-app) is installed on **`gils1908/hFlowDocs`**.
- **Dashboard:** confirm the Mintlify project’s connected repo is **`gils1908/hFlowDocs`** (not an old starter repo such as `docs`). If the dashboard still points elsewhere, reconnect GitHub to this repository.
- **Domain:** custom host **help.hflow.pro** is configured in Mintlify; DNS for `help.hflow.pro` should resolve (A records or CNAME per Mintlify’s domain instructions).

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
