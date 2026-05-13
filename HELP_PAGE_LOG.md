# hFlow help — change log and doc backlog

Maintainers only: not published on help.hflow.pro. For each substantive change under `hFlowDocs/`, append a new entry at the top (next `DOC-nnnn`). Move completed backlog items into an entry’s **Summary** or delete them; do not leave internal to-do wording in published MDX (see `.cursor/rules/help-pages-implications.mdc` in the app repo).

## Entries (newest first)

### DOC-0018 — 2026-05-12 — Reports menu + Copy Charts

**Summary:** Published **Org reports (Reports menu)**: how to open each header report, what each summarizes, **Copy Charts** on Growth, Language Progress, and Grade Language Distribution (including two-panel stitched PNG), clipboard vs download behavior, and that Reading Tier Distribution has no Copy Charts. Linked student progress charts to org reports for shared export behavior.

**Files (this repo):**

- added `hflow/reports.mdx`
- changed `docs.json` (nav order)
- changed `index.mdx` (Org reports card)
- changed `hflow/students/student-progress-charts.mdx` (**Copy Charts** label + cross-link)

**Related (Gilat app):** `AppShell` Reports dropdown; `grade-progress/page.tsx`, `grade-language-distribution/page.tsx`, `growth/page.tsx`, `StudentTrendReport.tsx`, `exportChart.ts`.

### DOC-0017 — 2026-05-09 — ACTFL chart: band abbrev inside bars

**Summary:** Documented that the ACTFL-by-skill bars show the proficiency band abbreviation (NL–AH) under the level digit inside each bar when space allows.

**Files (this repo):**

- changed `hflow/students/student-progress-charts.mdx`

**Related (Gilat app):** `LanguageProgressSection.tsx`.

### DOC-0016 — 2026-05-09 — Checkpoint drag order persistence

**Summary:** Added task steps for drag-and-drop checkpoint reordering, default date-based ordering behavior, and persistence scope (per student enrollment year + language) in the student profile help page.

**Files (this repo):**

- changed `hflow/students/view-student-data.mdx`

**Related (Gilat app):** `StudentProfileSummaryPanel.tsx`, `StudentProfileDrawer.tsx`, `src/app/api/student-years/[studentYearId]/checkpoint-order/route.ts`.

### DOC-0015 — 2026-05-09 — Students: IDs in drawer only; drawer above header

**Summary:** Roster rows no longer list ID/Ext ID on the table; copy controls for those values live in the profile drawer header. Documented z-order fix so the drawer is not covered by the app header.

**Files (this repo):**

- changed `hflow/students.mdx` (roster vs drawer IDs)
- changed `hflow/students/view-student-data.mdx` (drawer top summary)

**Related (Gilat app):** `src/app/students/page.tsx`, `StudentProfileDrawer.tsx`.

### DOC-0014 — 2026-05-09 — ACTFL overall display: hide trailing .0

**Summary:** User-facing composite string shows whole numbers without a decimal (e.g. `3 - NH` instead of `3.0 - NH`); fractional values still show one decimal.

**Files (this repo):**

- changed `hflow/assessments.mdx` (ACTFL overall bullet)

**Related (Gilat app):** `formatActflOverallDisplay` in `actflProficiencyLevels.ts`.

### DOC-0013 — 2026-05-09 — H-172: overall language, ACTFL composite, roster compact cards

**Summary:** Documented **grade-level overall** (auto + manual override rules), read-only **ACTFL overall**, bulk gradebook **G. overall** / **ACTFL Σ**, and Students roster **compact** layout with **Show Reading Only**. Noted that CSV/print/org export contracts are unchanged.

**Files (this repo):**

- changed `hflow/assessments.mdx` (replaced placeholder with task-oriented guide)
- changed `hflow/students.mdx` (roster period cells + Show Reading Only)

**Related (Gilat app):** `AssessmentFormModal`, `GradebookGrid` / `GradebookRow`, `StudentsPeriodCompactCard`, `overallLanguageScore.ts`.

### DOC-0012 — 2026-05-08 — Tier tooltip: worst-of accuracy vs fluency

**Summary:** Hover card for tier pills notes that placement uses the **more conservative** of the accuracy-based and fluency-based tier (each score matched to bands independently).

**Files (this repo):**

- changed `hflow/tiers.mdx` (median summary vs passage tiers)

**Related (Gilat app):** `TierPeriodHoverCard.tsx`, `assessmentMba.ts`.

### DOC-0011 — 2026-05-08 — Tiers: per-assessment vs overall (MBA roll-up)

**Summary:** Published help replaces the tiers placeholder with user-facing copy: per-row tiers use that enrollment year’s rules; multiple passages in one period roll up to the **worst** tier for overall placement. App migration `20260508231244_fix_student_tier_rollup_mba_passages.sql` implements that roll-up in `calculate_student_tier`.

**Files (this repo):**

- changed `hflow/tiers.mdx`

**Related (Gilat app):** `rollup_scheduled_tier_for_period`, `DATA_MODEL.md` tier section.

### DOC-0010 — 2026-05-07 — Language charts: BOY/MOY/EOY under each bar

**Summary:** Period abbreviations render **under every bar**; footer **BOY/MOY/EOY legend row removed**; extra bottom margin and x-axis offset reduce cramped labels.

**Files (this repo):**

- changed `hflow/students/student-progress-charts.mdx`

**Related (Gilat app):** `LanguageProgressSection`.

### DOC-0009 — 2026-05-07 — Language charts: no cohort toggles, unified ACTFL color, in-bar labels

**Summary:** Language progress bars drop **grade cohort** UI; ACTFL uses **one periwinkle** for all skills; labels **inside** bars with improved contrast; help updated.

**Files (this repo):**

- changed `hflow/students/student-progress-charts.mdx`

**Related (Gilat app):** `LanguageProgressSection`; student trend page no longer requests language cohort aggregates for charts.

### DOC-0008 — 2026-05-07 — Language charts: full-width footers, comprehension R/Y/G, always Listening

**Summary:** Language chart cards put period + grade-avg **below** the plot for width; comprehension chart uses **red/yellow/green** by level, always shows **four** skills, and adds a level **legend**.

**Files (this repo):**

- changed `hflow/students/student-progress-charts.mdx`

**Related (Gilat app):** `LanguageProgressSection`.

### DOC-0007 — 2026-05-07 — Language tab: bar charts for ACTFL and comprehension

**Summary:** Language progress uses **grouped bar charts** (skills on the x-axis, periods as bars); cohort averages as lighter companion bars; help text updated from line charts.

**Files (this repo):**

- changed `hflow/students/student-progress-charts.mdx`

**Related (Gilat app):** `LanguageProgressSection` bar charts.

### DOC-0006 — 2026-05-07 — Language charts: skill wording, overlap visibility, numeric comp labels

**Summary:** Student progress language tab copy uses **skill** (not domain); charts use dash patterns and colliding-point offsets; right chart point labels are **1 / 2 / 3** only.

**Files (this repo):**

- changed `hflow/students/student-progress-charts.mdx`

**Related (Gilat app):** Student trend `LanguageProgressSection`.

### DOC-0005 — 2026-05-07 — Language tab: comprehension chart L/S/W levels

**Summary:** Help text for the right-hand chart: reading comp plus listening/speaking/writing domain levels (1–3), shared colors with ACTFL chart.

**Files (this repo):**

- changed `hflow/students/student-progress-charts.mdx`

**Related (Gilat app):** H-168 follow-up.

### DOC-0004 — 2026-05-07 — Student progress charts (Reading vs Language tabs)

**Summary:** Documented the student trend report: folder tabs, language progress (ACTFL by domain, reading comprehension 1–3), org-wide grade cohort averages, `?tab=language`, and copy/export behavior.

**Files (this repo):**

- added `hflow/students/student-progress-charts.mdx`
- changed `docs.json`
- changed `hflow/students/view-student-data.mdx`

**Related (Gilat app):** Linear H-168.

### DOC-0003 — 2026-05-07 — Multi-select roster filters (admin vs teacher)

**Summary:** Documented admin multi-select for grade, class, and reading tier on Students (language single-select). Clarified teacher roster as the union of one or more selected assignments.

**Files (this repo):**

- changed `hflow/students/roles-and-permissions.mdx`

**Related (Gilat app):** Linear H-166 (filters across Students, Assessments, reports, Communications, Enrollment).

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

- [ ] Students hub: screenshot — table header and filter bar (admin view; multi-select grade, class, reading tier)
- [ ] Students hub: screenshot — table in teacher view (assignment-focused header)
- [ ] Roles: screenshot — teacher Students header (assignment selector, search-only controls)
- [ ] Add students: screenshots — Import CSV flow (pick → confirm → results)
- [ ] Add students: screenshot or example — failures export with `failure_reason`
- [ ] View drawer: screenshot — teacher read-only notes (if visually distinct from admin)
- [ ] Delete student: screenshot — enrollment detail with **Remove student from roster**
- [ ] Delete student: screenshot — final confirmation (**Remove student**)
