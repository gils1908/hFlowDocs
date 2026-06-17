> **Customize this file**: Tailor this template to note specific contribution types, a Code of Conduct, or internal release steps.

# Contribute to the documentation

Thank you for contributing to **hFlow Help**. This repo is **maintainer-facing** setup; the published site at **help.hflow.pro** is written for teachers and administrators only. School-facing pages live under **`hflow/`** and **`index.mdx`**.

## How to contribute

### Option 1, Edit directly on GitHub or Mintlify

1. Navigate to the page you want to change.
2. Use the Mintlify/GitHub edit flow your team prefers.
3. Submit or merge according to **`main`** protections.

### Option 2, Local clone and preview

These steps are **not** shown to help-site readers.

#### 1. Clone the docs repo

If you use the hFlow application monorepo, clone help next to Gilat:

```bash
cd /path/to/Gilat
git clone https://github.com/gils1908/hFlowDocs.git hFlowDocs
cd hFlowDocs
```

You can also clone **`gils1908/hFlowDocs`** anywhere; you only need the directory that contains **`docs.json`**.

#### 2. Install the Mintlify CLI

**Prerequisites:** Node.js **19+**.

```bash
npm i -g mint
```

If the preview looks wrong, update the CLI:

```bash
mint update
```

#### 3. Preview locally

From the repo root (where **`docs.json`** lives):

```bash
mint dev
```

Open **http://localhost:3000**. The dev server reloads when you edit MDX.

Optional custom port:

```bash
mint dev --port 3333
```

#### 4. Validate style and links

```bash
./scripts/check-published-mdx-style.sh
mint broken-links
```

#### 5. Publish

1. Commit on a branch (or **`main`** if that is team policy).
2. Push to GitHub. Mintlify builds from the linked repo; confirm the [GitHub app](https://dashboard.mintlify.com/settings/organization/github-app) is installed on **`gils1908/hFlowDocs`**.
3. Custom domain and DNS: see [README.md](README.md).

#### Troubleshooting, Mintlify CLI

- **Sharp / darwin-arm64 error:** `npm remove -g mint`, upgrade Node to v19+, then `npm i -g mint`.
- **Unknown error:** delete **`~/.mintlify`** and run **`mint dev`** again.

## Sync with Mintlify / GitHub

Edits made in the **Mintlify web editor** commit to GitHub (usually **`main`**). Before you edit the same clone locally, or before agents push, sync so you never work on stale files or overwrite upstream changes.

1. From this repo root:
   ```bash
   git fetch origin
   git pull --rebase
   ```
   If your branch has no upstream yet: **`git pull --rebase origin main`**.

2. If you have **uncommitted** local changes when you need to pull:
   **`git stash push -u -m "wip"`**, then pull/rebase, then **`git stash pop`**. Resolve conflicts before continuing.

3. Prefer **`git pull --rebase`** on **`main`**. Avoid force-push unless you intentionally discard remote commits.

The Gilat workspace uses the **pull-docs** Cursor skill; see `.cursor/skills/pull-docs/SKILL.md` there.

## Authoring standards (school-facing)

**Before every change under `hflow/` or `index.mdx`, read [AUTHORING.md](AUTHORING.md) end-to-end**, especially **Voice and phrasing** (no em dashes; no **Expected outcome** / **Expected result** labels); **Audience** (non-developer); structure, screenshots, navigation, **`HELP_PAGE_LOG.md`**.

Concise reminders:

- Active voice (“Click **Save**”) and address the reader as **you**
- Bold UI labels (**Students**, **Import CSV**)
- One idea per sentence; describe what appears next in ordinary sentences after the steps
- No em dashes in published pages; run `./scripts/check-published-mdx-style.sh` before you commit
