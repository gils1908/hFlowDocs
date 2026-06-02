# hFlow help — change log and doc backlog

Maintainers only: not published on help.hflow.pro. For each substantive change under `hFlowDocs/`, append a new entry at the top (next `DOC-nnnn`). Move completed backlog items into an entry’s **Summary** or delete them; do not leave internal to-do wording in published MDX (see `.cursor/rules/help-pages-implications.mdc` in the app repo).

## Entries (newest first)

### DOC-0049 — 2026-06-02 — Report a problem (H-182)

**Summary:** Added **Report a problem or suggest an idea** to Troubleshooting: FAB, four impact chips (including **Suggest an improvement**), screenshot, point-at-spot, Look on the page, student ID, receipt email, owner **Reported issues** withdraw flow.

**Files (this repo):**

- changed `hflow/troubleshooting.mdx`, `HELP_PAGE_LOG.md`

### DOC-0048 — 2026-06-01 — In-page logos: Welcome only

**Summary:** Removed inline brand images from Getting started, Languages, and Troubleshooting. Lockups remain on the Welcome page (`index.mdx`) and in the site header (`docs.json`) on all pages.

**Files (this repo):**

- changed `hflow/getting-started.mdx`, `hflow/languages.mdx`, `hflow/troubleshooting.mdx`, `AUTHORING.md`, `HELP_PAGE_LOG.md`

### DOC-0047 — 2026-06-01 — Light lockup: restore dark wordmark

**Summary:** Re-exported `hflow-lockup.png` from **`D_lockup_flat`** instead of `Light/lockup-flat-h512` (white wordmark invisible on light UI). Navbar and hero lockups show **hFlow** text again in light mode.

**Files (this repo):**

- changed `images/brand/hflow-lockup.png`, `hflow-lockup-sm.png`, `scripts/export-brand-assets.py`, `AUTHORING.md`, `HELP_PAGE_LOG.md`

### DOC-0046 — 2026-06-01 — Brand icons: flat light, framed dark

**Summary:** Re-exported help brand PNGs from **`Assets/hFlow Logos/`** (flat lockup/chart for light, framed lockup/chart for dark). **Languages** and **Troubleshooting** page marks now swap by theme. Favicon uses flat chart mark. Added **`scripts/export-brand-assets.py`** for future regenerations.

**Files (this repo):**

- changed `images/brand/*.png`, `docs.json`, `AUTHORING.md`, `hflow/languages.mdx`, `hflow/troubleshooting.mdx`, `scripts/export-brand-assets.py`, `HELP_PAGE_LOG.md`

### DOC-0045 — 2026-06-01 — Communications: template when switching students

**Summary:** Documented how the focus drafter picks a template when moving between students in a session (sent vs draft, last-used template, first-time default). Matches app behavior: draft students get the last template chosen in Communications Hub; sent students keep their sent template.

**Files (this repo):**

- changed `hflow/communications.mdx`, `HELP_PAGE_LOG.md`

### DOC-0044 — 2026-06-01 — Dark logo transparent background fix

**Summary:** Removed the full-width navy card baked into the Dark framed export and rebuilt `hflow-lockup-dark.png` on a transparent **1548×512** canvas (matching the light lockup). Keeps the framed icon stroke, dots, and white wordmark; frame fill and outer margins are transparent so the navbar/page background shows through.

**Files (this repo):**

- changed `images/brand/hflow-lockup-dark.png`, `AUTHORING.md`, `HELP_PAGE_LOG.md`

### DOC-0043 — 2026-06-01 — Dark navbar logo size fix

**Summary:** Rebuilt `hflow-lockup-dark.png` on a **1548×512** canvas (matching the light navbar lockup) by cropping the framed artwork to its icon/wordmark bounds and scaling up. The prior dark asset was **1645×820**, so Mintlify shrank the mark in the top-left navbar.

**Files (this repo):**

- changed `images/brand/hflow-lockup-dark.png`, `HELP_PAGE_LOG.md`

### DOC-0042 — 2026-06-01 — Dark mode lockup-framed logo

**Summary:** Replaced dark-theme help logo (`hflow-lockup-dark.png`) with **`Assets/hFlow Logos/Dark/lockup-framed-flat-h512.png`** (horizontal framed lockup for dark UI). Help home and Getting started dark hero images now use the same `280px` max width as the light lockup. Site header `docs.json` `logo.dark` path unchanged.

**Files (this repo):**

- changed `images/brand/hflow-lockup-dark.png`, `index.mdx`, `hflow/getting-started.mdx`, `AUTHORING.md`, `HELP_PAGE_LOG.md`

### DOC-0041 — 2026-06-01 — Sample CSV downloads via Google Drive

**Summary:** Getting started example student and assessment CSV links now point to Google Drive (Mintlify does not serve `.csv` on the current plan). Notes mention opening Drive and using **Download** to save the file.

**Files (this repo):**

- changed `hflow/getting-started.mdx`, `HELP_PAGE_LOG.md`

### DOC-0040 — 2026-05-31 — Dark theme logo: C_deep_3d (white wordmark)

**Summary:** Replaced dark-theme help logo (`hflow-lockup-dark.png`) with **`Assets/hFlow Logos/C_deep_3d/hFlow-512.png`** (square mark, white **hFlow** text on deep background). Light lockup unchanged. Prior dark asset was horizontal **`D_lockup_3d`** lockup with dark navy wordmark, which was hard to read on dark UI.

**Files (this repo):**

- changed `images/brand/hflow-lockup-dark.png`, `index.mdx`, `hflow/getting-started.mdx`, `AUTHORING.md`, `HELP_PAGE_LOG.md`

### DOC-0039 — 2026-05-31 — Dark mode lockup on help home and Getting started

**Summary:** Help home and Getting started now show the 3D dark lockup (`hflow-lockup-dark.png`) in dark mode at the same `280px` max width as the flat light lockup. Site header already used `docs.json` `logo.light` / `logo.dark` at matching navbar height.

**Files (this repo):**

- changed `index.mdx`, `hflow/getting-started.mdx`, `HELP_PAGE_LOG.md`

### DOC-0038 — 2026-05-31 — Data exports: delete is final

**Summary:** Note under delete section: deletion is final, cannot be undone, no restore—download first if needed.

**Files (this repo):**

- changed `hflow/configuration/data-exports.mdx`, `HELP_PAGE_LOG.md`

### DOC-0037 — 2026-05-31 — Data exports: server retention vs manual download

**Summary:** Under download steps, clarified completed exports stay in hFlow but are **not automatically downloaded**.

**Files (this repo):**

- changed `hflow/configuration/data-exports.mdx`, `HELP_PAGE_LOG.md`

### DOC-0036 — 2026-05-31 — Data exports help expanded

**Summary:** Expanded [Data exports](/hflow/configuration/data-exports): periodic backup recommendation, all school years per ZIP, 10 completed retention cap and storage-limit modal, download/delete/cancel, one job at a time, deleted students included. Removed outdated school-year checkbox steps.

**Files (this repo):**

- changed `hflow/configuration/data-exports.mdx`, `HELP_PAGE_LOG.md`

### DOC-0035 — 2026-05-31 — Benchmarks help under Languages nav

**Summary:** Moved **Benchmarks** from Configuration to **Languages** sidebar (order: Languages → Benchmarks → Tiers). Link from Languages page to benchmarks guide.

**Files (this repo):**

- changed `docs.json`, `hflow/languages.mdx`, `HELP_PAGE_LOG.md`

### DOC-0034 — 2026-05-31 — Benchmarks and tier rules help aligned with Languages

**Summary:** Rewrote [Benchmarks](/hflow/configuration/benchmarks) and [Tier rules](/hflow/configuration/tier-rules) to match the product: benchmarks derive from Tier 1 on **Languages**, read-only optional Configuration summary, no manual save-on-benchmarks flow. Clarified read-only **Benchmarks** table on Languages.

**Files (this repo):**

- changed `hflow/configuration/benchmarks.mdx`, `hflow/configuration/tier-rules.mdx`, `hflow/languages.mdx`, `HELP_PAGE_LOG.md`

### DOC-0033 — 2026-05-31 — Help nav restructure and student home page

**Summary:** Renamed sidebar **Shortcuts** → **Navigation**; moved **Tiers** under **Languages**; flattened **Students** (removed Guides subgroup). Replaced drawer doc with **[Student home page](/hflow/students/student-home-page)** (360° intro, header, Summary / Reading / Language tabs, assessments, checkpoints, notes, goals). Permanent redirect from `/hflow/students/view-student-data`. Updated cross-links across Students, Assessments, Getting started, roles, staff.

**Open doc backlog (screenshots):** Student home header, Summary tab (goals/notes/assessments/checkpoints), Reading and Language progress tabs.

**Files (this repo):**

- added `hflow/students/student-home-page.mdx`
- deleted `hflow/students/view-student-data.mdx`
- changed `docs.json`, `hflow/students.mdx`, `hflow/students/roles-and-permissions.mdx`, `hflow/students/student-progress-charts.mdx`, `hflow/assessments.mdx`, `hflow/getting-started.mdx`, `hflow/shortcuts.mdx`, `hflow/configuration/staff.mdx`, `hflow/tiers.mdx`, `index.mdx`, `hflow/changelog.mdx`, `HELP_PAGE_LOG.md`

### DOC-0032 — 2026-05-31 — Shortcuts help page

**Summary:** New standalone **[Shortcuts](/hflow/shortcuts)** guide: saved views / filter states, Tier 3 example, shortcuts vs [student groups](/hflow/students/groups), multi-screen reuse (Students, Assessments, reports), admin vs teacher, create/pin/rename/reorder/delete. Sidebar group **Shortcuts**; links from Students hub, Assessments, Reports.

**Open doc backlog (screenshots):** Shortcut chip (unsaved, saved, modified), Save shortcut dialog, Manage shortcuts with drag reorder, Pinned section in menu.

**Files (this repo):**

- added `hflow/shortcuts.mdx`
- changed `docs.json`, `hflow/students.mdx`, `hflow/assessments.mdx`, `hflow/reports.mdx`, `hflow/changelog.mdx`, `HELP_PAGE_LOG.md`

### DOC-0031 — 2026-05-31 — Getting started sample CSV downloads

**Summary:** Added **`samples/csv/hflow-sample-students.csv`** and **`hflow-sample-assessments.csv`** (fictitious data; reference only). **[Getting started](/hflow/getting-started)** explains CSV format, links downloads on steps 3 and 4 with **do not import as-is** guidance.

**Files (this repo):**

- added `samples/csv/hflow-sample-students.csv`, `samples/csv/hflow-sample-assessments.csv`
- changed `hflow/getting-started.mdx`, `hflow/changelog.mdx`, `HELP_PAGE_LOG.md`

### DOC-0030 — 2026-05-31 — Staff roles and permissions help

**Summary:** Rewrote **[Staff](/hflow/configuration/staff)** with Owner / Admin / Teacher definitions, navigation scope, assessment access, classroom assignments, and owner-only staff workflows. Updated **[Students: Admin vs Teacher](/hflow/students/roles-and-permissions)** to distinguish owners from admins and link to Staff. **Troubleshooting** sign-in section links to Staff for menu questions.

**Open doc backlog (screenshots):** Staff list (role groups), Add Staff modal (role + assessments checkbox), staff detail (role, Active, Assessments, assignments table).

**Files (this repo):**

- changed `hflow/configuration/staff.mdx`, `hflow/students/roles-and-permissions.mdx`, `hflow/troubleshooting.mdx`, `HELP_PAGE_LOG.md`

### DOC-0029 — 2026-05-31 — Ship hFlow brand logos to production

**Summary:** Added **`images/brand/`** PNG lockups (light + dark) and pushed **`docs.json`** `logo.light` / `logo.dark` paths so help.hflow.pro navbar matches local. Prior pushes only included the video commit without these assets.

**Files (this repo):**

- added `images/brand/hflow-lockup.png`, `hflow-lockup-sm.png`, `hflow-lockup-dark.png`, `hflow-mark.png`, `hflow-mark-sm.png`
- changed `docs.json`, `index.mdx`, and remaining unpublished help MDX from the May help refresh

### DOC-0028 — 2026-05-31 — Getting started video embed

**Summary:** Embedded setup walkthrough on **[Getting started](/hflow/getting-started)** (`<video>` + `<source>`, no `Frame`). **`videos/hflow-getting-started-guide.mp4`** re-encoded for web (H.264 + faststart); later prepended **hflow logo night** intro (~10 s) before the tutorial body. **Must be committed and pushed** to `hFlowDocs` for playback on help.hflow.pro.

**Files (this repo):**

- added `videos/hflow-getting-started-guide.mp4`
- changed `hflow/getting-started.mdx`, `AUTHORING.md`

### DOC-0027 — 2026-05-31 — Correct app / website / help URLs

**Summary:** Staff-facing links now use **app.hflow.pro** (app), **www.hflow.pro** (website), and **help.hflow.pro** (help). Updated **`docs.json`** navbar, **`index.mdx`**, **`getting-started.mdx`**, and **`AUTHORING.md`** domain table.

**Files (this repo):**

- changed `docs.json`, `index.mdx`, `hflow/getting-started.mdx`, `AUTHORING.md`

### DOC-0026 — 2026-05-31 — Getting started, brand logos, troubleshooting, assessment CSV

**Summary:** Rebuilt **[Getting started](/hflow/getting-started)** from the setup and data-import tutorial (org profile → languages/tiers → student CSV → assessment CSV). Added **`images/brand/`** lockup and mark PNGs from `Assets/hFlow Logos` (flat lockup for light theme, 3d lockup for dark); updated **`docs.json`** site logo paths. Expanded **Languages**, **Assessments** (CSV import section), and **Troubleshooting** (staff FAQs). Refreshed **`index.mdx`** with lockup and getting-started cards. Removed broken screenshot references (files were never in repo). **Org profile** save button label aligned to **Save Changes**.

**Open doc backlog (screenshots):** Students roster header, Add Student modal, student drawer (re-add under `images/students/` when captured).

**Files (this repo):**

- added `images/brand/hflow-lockup.png`, `hflow-lockup-sm.png`, `hflow-lockup-dark.png`, `hflow-mark.png`, `hflow-mark-sm.png`
- changed `docs.json`, `index.mdx`, `hflow/getting-started.mdx`, `hflow/languages.mdx`, `hflow/assessments.mdx`, `hflow/troubleshooting.mdx`, `hflow/changelog.mdx`, `hflow/configuration/org-profile.mdx`, `hflow/students.mdx`, `hflow/students/add-students.mdx`, `hflow/students/view-student-data.mdx`, `hflow/students/roles-and-permissions.mdx`

### DOC-0025 — 2026-05-28 — Communications sessions, groups, email template tokens

**Summary:** Replaced outdated Communications campaign guide with session-based hub workflow (groups, sessions, roster filters, focus drafter, Reset Template, Copy/Mark Sent). Added **Student groups** guide (Manage Groups, builder pool/roster, admin vs teacher filters). Updated **Email templates** for dropdown UI, template filters, and token panel (**Show for period**, **Filter tokens…**, categories).

**Open doc backlog (screenshots):** Communications hub (group/session, roster filters, donut); draft screen (Reset Template, preview, Copy/Mark Sent); Email Templates token panel; Groups builder (pool/roster transfer).

**Files (this repo):**

- changed `hflow/communications.mdx`, `hflow/configuration/email-templates.mdx`, `hflow/students.mdx`, `docs.json`
- added `hflow/students/groups.mdx`

### DOC-0024 — 2026-05-26 — H-188 Reading-only assessment card layouts

**Summary:** Documented roster period cells and Assessments gradebook cards when only reading is reported (no L/S/W), including “not reported” footers and return to full layout after L/S/W entry.

**Files (this repo):**

- changed `hflow/students.mdx`, `hflow/assessments.mdx`

### DOC-0023 — 2026-05-25 — Email templates auto-save

**Summary:** Updated **Email templates** help: custom templates auto-save with inline **Saving…** / **Saved** next to the name; removed manual Save and unsaved-changes dialog from the guide.

**Files (this repo):**

- changed `hflow/configuration/email-templates.mdx`

### DOC-0022 — 2026-05-18 — ACTFL proficiency scale reference page

**Summary:** Published **`hflow/actfl-proficiency-scale.mdx`** (intro from public ACTFL summaries, links to **[Language Testing International](https://www.languagetesting.com/actfl-proficiency-scale)** and **[ACTFL](https://www.actfl.org/)**, distinction versus **reading tiers**, where hFlow uses **1–9** domain levels / composite). Nav: **Assessments** group adds this page after **Assessments**. Cross-linked from **Assessments**, **Tiers**, **Student progress charts**; changelog entry.

**Files (this repo):**

- added `hflow/actfl-proficiency-scale.mdx`
- changed `docs.json`, `hflow/assessments.mdx`, `hflow/tiers.mdx`, `hflow/students/student-progress-charts.mdx`, `hflow/changelog.mdx`

### DOC-0021 — 2026-05-18 — Authoring guideline: mandatory every edit + Voice and phrasing

**Summary:** Made **`AUTHORING.md`** explicitly **mandatory** for every **`hflow/`** and **`index.mdx`** edit; added **Voice and phrasing** (forbid Expected outcome/result scaffolding; examples table), **Audience and honesty**, and tightened cross-references from **`CONTRIBUTING.md`**, **`README.md`**, **`AGENTS.md`**, Gilat **`help-pages-implications.mdc`**, and **`MAINTENANCE.md`** so contributors and agents re-read authoring rules on each help touch.

**Files (this repo):**

- changed `AUTHORING.md`, `README.md`, `CONTRIBUTING.md`, `AGENTS.md`

**Related (Gilat app repo):** `.cursor/rules/help-pages-implications.mdc`, `docs/llm/MAINTENANCE.md`

### DOC-0020 — 2026-05-18 — Plain-language outcomes (drop “Expected outcome”)

**Summary:** Removed **Expected outcome / Expected result** labels across **`hflow/**/*.mdx`**, rewriting follow-up sentences (“After saving…”, “You should see…”); updated **`AUTHORING.md`** and **`.cursor/rules/help-pages-implications.mdc`** to instruct plain prose instead of that pattern.

**Files (this repo):**

- changed `AUTHORING.md`
- changed many `hflow/**/*.mdx` pages (students, assessments, reports, languages, communications, configuration, getting-started)

**Related (Gilat app):** `.cursor/rules/help-pages-implications.mdc`

### DOC-0019 — 2026-05-18 — Help IA, audience split, Reports + Configuration guides

**Summary:** Sidebar reorganized around app concepts (**Welcome**, nested **Students** guides, **Assessments**, **Reports** with per-report pages, **Tiers**, **Languages**, **Communications**, **Configuration** guides). Removed maintainer **`quickstart`**, **`development`**, and **workflows** from navigation; redirects `/quickstart` and `/development` → `/`. Deleted placeholders **`admin-settings`** and **`workflows`**. Added **`hflow/getting-started`**, **Languages**, **Communications**, **candidate students**, and configuration topics (org profile, email templates, staff, data exports, benchmarks, tier rules). Added **`AUTHORING.md`**; **`CONTRIBUTING.md`** now carries clone/Mintlify/publish; **`.mintignore`** hides template folders (**`ai-tools`**, **`api-reference`**, **`essentials`**, **`snippets`**). Students hub and roles pages embed **`admin-students-header`** with `<Note>` for teacher layouts; enrollment steps use **Students → Enrollment**. Gilat **`MAINTENANCE.md`** checklist + **`help-pages-implications`** rule require **Proposed updates** bullets for help.

**Files (this repo):**

- added `AUTHORING.md`
- changed `.mintignore`, `CONTRIBUTING.md`, `README.md`, `docs.json`, `index.mdx`
- added `hflow/getting-started.mdx`, `hflow/languages.mdx`, `hflow/communications.mdx`, `hflow/students/candidate-students.mdx`
- added `hflow/reports/reading-tier-distribution.mdx`, `growth-reading.mdx`, `language-progress-report.mdx`, `grade-language-distribution.mdx`
- added `hflow/configuration/org-profile.mdx`, `email-templates.mdx`, `staff.mdx`, `data-exports.mdx`, `benchmarks.mdx`, `tier-rules.mdx`
- changed `hflow/reports.mdx`, `hflow/students.mdx`, `roles-and-permissions.mdx`, `view-student-data.mdx`, `delete-student.mdx`
- removed `quickstart.mdx`, `development.mdx`, `hflow/admin-settings.mdx`, `hflow/workflows.mdx`

**Related (Gilat app):** `.cursor/rules/help-pages-implications.mdc`, `docs/llm/MAINTENANCE.md`

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

- [ ] CSV import flow: screenshots for choose file → confirm row count → results summary (**Add students** page).
- [ ] CSV failures export: screenshot or sanitized example listing `failure_reason` column (**Add students**).
- [ ] Enrollment remove: screenshots for enrollment detail (**Remove student from roster**) and final confirmation (**Remove student**).
