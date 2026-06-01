# Authoring standards — hFlow Help (help.hflow.pro)

**Mandatory for every edit:** Any time you add or change published help (`hflow/**/*.mdx`, `index.mdx`), follow this document end-to-end before you ship. The Gilat Cursor rule **[Help Page Implications](https://github.com/gils1908/Gilat/blob/main/.cursor/rules/help-pages-implications.mdc)** (always on for agents) points here.

This site targets **school staff** (teachers, coordinators, admins). Write in plain language; avoid repos, CLI commands, APIs, or internal ticket jargon on those pages.

**Published URLs (use consistently in links):**

| Purpose | URL |
|--------|-----|
| Sign in / daily use | **https://app.hflow.pro** |
| Marketing / public site | **https://www.hflow.pro** |
| Help (this site) | **https://help.hflow.pro** |

Do not link staff to bare `hflow.pro` for the app or help.

Maintainership (clone, Mintlify CLI, Git) lives in **`CONTRIBUTING.md`** and **`README.md`** — those documents are **not** linked from the public sidebar.

---

## Audience and honesty

Write as if explaining to a colleague at school: concrete steps, real control names (**Save**, **Enrollment**), and short paragraphs. Prefer “you” and active verbs (`Click …`, `Choose …`). Do **not** address developers or imply readers run shell commands unless the page is deliberately maintainer-only (none of those belong in navigation).

---

## Voice and phrasing (required)

Avoid **training-manual scaffolding** readers trip over—especially labels that fence off “what happens” from the instructions.

### Do **not** use

- Bold or heading lines such as **Expected outcome**, **Expected result**, **Expected results**, **You should expect**, etc.
- The same phrases in prose if they feel like checklist boilerplate (**“The expected outcome is…”**).

### Use instead

State **what happens next** in normal sentences immediately after steps (or weave one short sentence into the last step):

| Avoid | Prefer |
|--------|--------|
| **Expected outcome:** You land on Students. | After you sign in, you usually arrive on **Students** (your home page). |
| **Expected outcome:** Row appears in list. | A new row appears in the exports table with status queued, then processing, then complete. |
| Expected result: student shows on roster. | The student appears in the roster for that school year and grade. |

Prefer **natural time order**—“After saving…”, “When the file finishes…” , “Once you confirm…”—rather than detached “outcome” bullets.

(This pattern is summarized in **Structure § What happens next** below; both sections apply together.)

---

## Front matter

Every page:

```yaml
---
title: "Short title in sentence case"
description: "One line: what someone can accomplish on this page."
---
```

---

## Structure

1. **Opening paragraph** — Who this is for and what the feature lets them do.
2. **Demo data notice** — Use the existing blockquotes where realistic student/org examples appear (see student pages).
3. **Body** — Task-oriented **`## How to …`** sections with numbered steps.
4. **What happens next** — After each procedure, describe on-screen changes in **plain prose** (see **Voice and phrasing** above). No “expected outcome” style headings or labels.
5. **Admin vs teacher** — When behavior differs, use a `<Note>` or a short **`## Admin vs teacher`** subsection.
6. **Reference** — Include screenshots where they help (`## Reference`). Use neutral captions. Do **not** publish sections whose only purpose is to list missing assets (track gaps in **Open doc backlog** in `HELP_PAGE_LOG.md`).

---

## Screenshots and brand assets

- **Logos:** Official artwork lives in **`images/brand/`** (lockup for hero/home, small mark optional on long guides). Source files: Gilat app repo **`Assets/hFlow Logos/`** (`Light/lockup-framed-flat-h512.png` or `D_lockup_flat/hFlow-lockup-512.png` → `hflow-lockup.png` for light mode; `Dark/lockup-framed-flat-h512.png` → `hflow-lockup-dark.png` for dark mode). Dark exports include a full-width navy card — strip that fill before publishing so the PNG matches Mintlify’s transparent navbar (keep frame stroke, dots, and wordmark only). Export on a **1548×512** transparent canvas (same height as the light navbar lockup). For inline heroes, pair light and dark lockups with `block dark:hidden` / `hidden dark:block` at the same `maxWidth` (see `index.mdx`).
- **Videos:** Store MP4 files under **`videos/`** with kebab-case names. Use H.264 + AAC, **`movflags +faststart`**, and keep files roughly under ~25 MB when possible. Embed with `<video controls playsInline>` and `<source type="video/mp4">` (avoid wrapping in `<Frame>`—it can block playback). Path `/videos/…` from site root. **Commit and push** the MP4 in `hFlowDocs` or the file 404s on help.hflow.pro.
- **Product screenshots:** Store under **`images/<area>/`** (e.g. `images/students/`).
- Reference in MDX with stable paths such as `/images/students/example.png` or `/images/brand/hflow-lockup.png`.
- Refresh images when UI copy or layout materially changes.

---

## Navigation changes

Adding or renaming `.mdx` files requires updating **`docs.json`**. Prefer nested groups under product areas (**Students**, **Reports**, **Configuration**, …) so the sidebar matches the concepts in **`Screens.md`** in the **hFlow app** repo (Gilat).

---

## After substantive edits

- Append a **`DOC-nnnn`** entry to **`HELP_PAGE_LOG.md`** (date, summary, files list).
- For user-visible releases, consider a bullet in **`hflow/changelog.mdx`**.

Agents: for **pull-docs**, implications in plans, and **Proposed updates**, see **`.cursor/rules/help-pages-implications.mdc`** in the **Gilat** workspace (`hFlowDocs` clones alone do not include that path).
