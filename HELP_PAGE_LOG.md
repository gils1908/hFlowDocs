# hFlow help — change log and doc backlog

Maintainers only: not published on help.hflow.pro. For each substantive change under `hFlowDocs/`, append a new entry at the top (next `DOC-nnnn`). Move completed backlog items into an entry’s **Summary** or delete them; do not leave internal to-do wording in published MDX (see `.cursor/rules/help-pages-implications.mdc` in the app repo).

## Entries (newest first)

### DOC-0002 — 2026-04-30 — Maintainer log and no internal backlog on published pages

**Summary:** Added this log, removed “Screenshot needed” / “Still needed” sections from Students MDX, pointed contributors at the log for missing visuals and follow-ups. Extended Cursor help rule and push skills; softened release-notes placeholder on `changelog.mdx`.

**Files (this repo):**

- added `HELP_PAGE_LOG.md`
- changed `README.md`
- changed `hflow/changelog.mdx`
- changed `hflow/students.mdx`
- changed `hflow/students/roles-and-permissions.mdx`
- changed `hflow/students/add-students.mdx`
- changed `hflow/students/view-student-data.mdx`
- changed `hflow/students/delete-student.mdx`

**Related (Gilat app repo):** `.cursor/rules/help-pages-implications.mdc`, `.cursor/skills/push-docs/SKILL.md`, `.cursor/skills/push/SKILL.md`, `.cursor/skills/push-all/SKILL.md`

### DOC-0001 — 2026-04-29 — Students help pilot and Mintlify site

**Summary:** Pilot “Using hFlow” Students section: hub page, admin vs teacher roles, add students (manual + CSV), delete student, view drawer; navigation in `docs.json`; demo-data disclaimers; embedded screenshots for admin header, Add Student modal, and student drawer.

**Files:**

- changed `docs.json`
- changed `index.mdx`
- changed `quickstart.mdx`
- added/changed multiple `hflow/*.mdx` and `hflow/students/*.mdx`
- added `images/students/admin-students-header.png`
- added `images/students/add-student-modal.png`
- added `images/students/student-drawer-overview.png`

## Open doc backlog (maintainers)

- [ ] Students hub: screenshot — table header and filter bar (admin view)
- [ ] Students hub: screenshot — table in teacher view (assignment-focused header)
- [ ] Roles: screenshot — teacher Students header (assignment selector, search-only controls)
- [ ] Add students: screenshots — Import CSV flow (pick → confirm → results)
- [ ] Add students: screenshot or example — failures export with `failure_reason`
- [ ] View drawer: screenshot — teacher read-only notes (if visually distinct from admin)
- [ ] Delete student: screenshot — enrollment detail with **Remove student from roster**
- [ ] Delete student: screenshot — final confirmation (**Remove student**)
