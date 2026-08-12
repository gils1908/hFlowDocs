# hFlow help: change log and doc backlog

Maintainers only: not published on help.hflow.pro. For each substantive change under `hFlowDocs/`, append a new entry at the top (next `DOC-nnnn`). Move completed backlog items into an entry’s **Summary** or delete them; do not leave internal to-do wording in published MDX (see `.cursor/rules/help-pages-implications.mdc` in the app repo).

## Entries (newest first)

### DOC-0080 (2026-08-11): Document the appearance (Light/Dark/System) toggle

**Summary:** hFlow app added a Light/Dark/System appearance toggle (H-250), in the header next to the account menu and, on the sign-in screen, floating in the top right corner. Added a **How to switch appearance** section to **[Getting started](/hflow/getting-started)** covering where the control lives, the three options, and that the choice is saved to the account and follows the user across devices.

**Files (this repo):**

- changed `hflow/getting-started.mdx`, `HELP_PAGE_LOG.md`

### DOC-0079 (2026-08-09): Revert enrollment walkthrough to Guidde

**Summary:** Restored Guidde embed on **[Student Enrollment](/hflow/students/student-enrollment)** (reverted DOC-0078 Clueso swap). Clueso update tracked in Linear backlog.

**Files (this repo):**

- changed `hflow/students/student-enrollment.mdx`, `AUTHORING.md`, `HELP_PAGE_LOG.md`

### DOC-0078 (2026-08-09): Enrollment video switched to Clueso

**Summary:** **[Student Enrollment](/hflow/students/student-enrollment)** walkthrough embed replaced Guidde with Clueso (`watchclueso.com`). Fallback link updated; AUTHORING notes Clueso as a hosted iframe option.

**Files (this repo):**

- changed `hflow/students/student-enrollment.mdx`, `AUTHORING.md`, `HELP_PAGE_LOG.md`

### DOC-0077 (2026-08-08): Rename enrollment page title

**Summary:** Renamed **[Student Enrollment](/hflow/students/student-enrollment)** page title (removed “bulk”). Updated cross-links on Add students and the help changelog.

**Files (this repo):**

- changed `hflow/students/student-enrollment.mdx`, `hflow/students/add-students.mdx`, `hflow/changelog.mdx`, `HELP_PAGE_LOG.md`

### DOC-0076 (2026-08-08): Enrollment video embed fallback link

**Summary:** Simplified the Guidde iframe on **[Student enrollment (bulk)](/hflow/students/student-enrollment)** to Mintlify’s standard embed attributes and added a fallback link when the in-page player does not hydrate.

**Files (this repo):**

- changed `hflow/students/student-enrollment.mdx`, `HELP_PAGE_LOG.md`

### DOC-0075 (2026-08-08): Enrollment Guidde video walkthrough

**Summary:** **[Student enrollment (bulk)](/hflow/students/student-enrollment)** embeds a Guidde walkthrough (bulk enroll, assign class later, Classes assignment, enrollment history).

**Files (this repo):**

- changed `hflow/students/student-enrollment.mdx`, `AUTHORING.md`, `HELP_PAGE_LOG.md`

### DOC-0074 (2026-08-06): Bulk enroll review summary plain language

**Summary:** **[Student enrollment (bulk)](/hflow/students/student-enrollment)** review step describes how many students will enroll, target year/grade, and class choice in plain language (including **Assign a class later**).

**Files (this repo):**

- changed `hflow/students/student-enrollment.mdx`, `HELP_PAGE_LOG.md`

### DOC-0073 (2026-08-06): Class terminology (not section)

**Summary:** User-facing copy uses **class** consistently (not section) on enrollment fields, import help, staff assignment labels, and student help pages. Create action is **Create new class**; empty choice remains **Assign a class later**.

**Files (this repo):**

- changed `hflow/students/student-enrollment.mdx`, `hflow/students/add-students.mdx`, `hflow/students/candidate-students.mdx`, `hflow/students/classes.mdx`, `hflow/students.mdx`, `hflow/troubleshooting.mdx`, `hflow/getting-started.mdx`, `hflow/configuration/csv-imports.mdx`, `HELP_PAGE_LOG.md`

### DOC-0072 (2026-08-06): Enrollment class optional (Assign a class later)

**Summary:** Class selection on enroll is optional across **[Student enrollment (bulk)](/hflow/students/student-enrollment)**, **[Add students](/hflow/students/add-students)**, and **[Candidate students](/hflow/students/candidate-students)**. Options list classes for the **target** school year and grade only; users can pick a class, create one, or choose **Assign a class later** (Unassigned on Classes).

**Files (this repo):**

- changed `hflow/students/student-enrollment.mdx`, `hflow/students/add-students.mdx`, `hflow/students/candidate-students.mdx`, `HELP_PAGE_LOG.md`

### DOC-0071 (2026-08-06): Unenroll latest year + re-enroll matching on Add Student

**Summary:** **[Unenroll a student from the latest year](/hflow/students/delete-student)** rewritten: replaces whole-student "Remove from roster" with unenrolling only the student's most recent enrollment year (earlier years and the student record stay intact; assessments hidden, not deleted). **[Student enrollment (bulk)](/hflow/students/student-enrollment)** now calls out the **Select all** checkbox and the pencil "Manage enrollment" icon, and links to the unenroll page. **[Add students](/hflow/students/add-students)** documents the new existing-student match step on manual add (re-enroll vs create new, including the ambiguous pick-list); CSV import behavior is unchanged.

**Files (this repo):**

- changed `hflow/students/delete-student.mdx`, `hflow/students/student-enrollment.mdx`, `hflow/students/add-students.mdx`, `HELP_PAGE_LOG.md`

### DOC-0070 (2026-08-06): Candidate assessment Pre-K

**Summary:** **[Candidate students](/hflow/students/candidate-students)** notes that assessment grade can be **Pre-K** (one year before Kindergarten). Planned enrollment grade remains Kindergarten through 12th grade.

**Files (this repo):**

- changed `hflow/students/candidate-students.mdx`, `HELP_PAGE_LOG.md`

### DOC-0069 (2026-08-03): Class names unique school-wide on Classes board

**Summary:** **[Classes](/hflow/students/classes)** notes that classes belong to the selected school year (no automatic carry-over). Within a year, names are unique across the school (case-insensitive). Duplicate names keep the add-class draft open so you can edit the name in place. The same name may be reused in a different school year.

**Files (this repo):**

- changed `hflow/students/classes.mdx`, `HELP_PAGE_LOG.md`

### DOC-0068 (2026-08-03): Classes board and enrollment year-advance only

**Summary:** New **[Classes](/hflow/students/classes)** page for same-year class assignment (admins/owners). **Student enrollment (bulk)** no longer documents same-year class moves; points to Classes. Export/import round-trip noted on Add students path via app import help.

**Files (this repo):**

- added `hflow/students/classes.mdx`
- changed `hflow/students/student-enrollment.mdx`, `hflow/students/add-students.mdx`, `docs.json`, `HELP_PAGE_LOG.md`

### DOC-0067 (2026-08-02): Enrollment Enroll label, same-year section create, H-135 guidance

**Summary:** **Student enrollment (bulk)** documents Enroll vs Bulk Enroll by selection count; same-year moves and creating an additional section when sections already exist; first whole-grade split via CSV; and that same-year class changes must include every classmate who still has no class.

**Files (this repo):**

- changed `hflow/students/student-enrollment.mdx`, `HELP_PAGE_LOG.md`

### DOC-0066 (2026-08-02): Class filter follows selected school year

**Summary:** **Students** and **Student enrollment (bulk)** note that the **Class** filter lists only sections with students in the selected school year (not leftover sections from another year that share the same grade).

**Files (this repo):**

- changed `hflow/students.mdx`, `hflow/students/student-enrollment.mdx`, `HELP_PAGE_LOG.md`

### DOC-0065 (2026-08-02): Student enrollment bulk help

**Summary:** New **[Student enrollment (bulk)](/hflow/students/student-enrollment)** documents current Bulk Enroll mental model (one target year and one target class per run), steps, and examples (advance one section, remix into two classes, same-year reassignment, fix missing class after CSV). Cross-link from **Add students**. Nav entry under Students. App `?` for `/students/enrollment` should map to this page (Gilat help route).

**Files (this repo):**

- added `hflow/students/student-enrollment.mdx`
- changed `docs.json`, `hflow/students/add-students.mdx`, `hflow/changelog.mdx`, `HELP_PAGE_LOG.md`

### DOC-0064 (2026-06-23): Same-name students across grades (H-223)

**Summary:** **Add students** CSV section documents that two students with the same first and last name in the same school year but different grades import as separate records, and that `middle_name` or `external_student_id` is needed when they share the same grade and year.

**Files (this repo):**

- changed `hflow/students/add-students.mdx`, `HELP_PAGE_LOG.md`

### DOC-0063 (2026-06-16): Remove em dashes from published help

**Summary:** Replaced em dashes across all published `*.mdx` help pages (28 files) with commas, colons, or periods as appropriate. Updated **AUTHORING.md** to prohibit em dashes in staff-facing copy. Maintainer README/CONTRIBUTING/AGENTS cleaned for consistency.

**Files (this repo):**

- changed all `hflow/**/*.mdx`, `index.mdx`, `AUTHORING.md`, `README.md`, `CONTRIBUTING.md`, `AGENTS.md`, `HELP_PAGE_LOG.md`

### DOC-0062 (2026-06-16): CSV import undo (H-219)

**Summary:** New **[CSV imports and undo](/hflow/configuration/csv-imports)** for owners/admins: list uploads, download original CSV, three-step undo, plain-language rules for when undo is allowed or blocked (with practical examples, e.g. assessment edit after import). **Troubleshooting** split for teachers (contact owner, do not edit) vs owners/admins. Cross-links from **Add students** and **Assessments** CSV sections. **Changelog** bullet.

**Open doc backlog (screenshots):** CSV Imports table; Review undo modal (confirm and blocked states).

**Files (this repo):**

- added `hflow/configuration/csv-imports.mdx`
- changed `docs.json`, `hflow/troubleshooting.mdx`, `hflow/students/add-students.mdx`, `hflow/assessments.mdx`, `hflow/changelog.mdx`, `HELP_PAGE_LOG.md`

### DOC-0061 (2026-06-11): Fix help-site wallpaper (reliable full-bleed on deploy)

**Summary:** The full-bleed wallpaper kept rendering as a plain/near-empty background on the deployed site. Root cause: DOC-0058 moved the `style.css` rule from `#background-color` to `body`, but Mintlify paints an opaque full-viewport `#background-color` span (`fixed inset-0 bg-background-light dark:bg-background-dark -z-10`) over the `body`, so a `body` wallpaper is always hidden in production; meanwhile `docs.json` `background.image` only rendered Mintlify's default **top-right, natural-size** accent. Fix: paint the wallpaper onto `#background-color` (the stable full-viewport layer) with `cover`, and remove `background.image` from `docs.json` so no competing top-right accent is generated (`background.color` kept as fallback fill). Light mode uses a 30% `#FAFAFF` wash over the wallpaper so the pattern reads a notch subtler; dark mode unchanged. Verified the wallpaper assets return 200 at their root path on prod.

**Files (this repo):**

- changed `style.css`, `docs.json`, `HELP_PAGE_LOG.md`

### DOC-0060 (2026-06-11): Language metrics (reading accuracy & fluency)

**Summary:** New **[Language metrics](/hflow/language-metrics)** under Assessments: plain-language and formula explanations for implied correct, accuracy, fluency (WCPM), plain vs median-based (MBA) assessments, tier linkage, and pointers to ACTFL/overall fields. Cross-link from Assessments intro.

**Files (this repo):**

- added `hflow/language-metrics.mdx`
- changed `hflow/assessments.mdx`, `docs.json`, `HELP_PAGE_LOG.md`

### DOC-0059 (2026-06-09): Staff invite lifecycle (owner guide)

**Summary:** Expanded **[Staff](/hflow/configuration/staff)** with plain-language steps for sending and resending invites, what colleagues do when they receive the email, how owners monitor status on the **Staff** list (**Invite sent**, **Last Login**, **Show pending**), and common fixes (expired link, wrong email, password reset). Removed the unpublished **Reference** screenshot placeholder.

**Open doc backlog (screenshots):** Staff list (pending statuses, **Show pending**), pending invite page (**Send invite**), staff detail (**Last Login**, login activity).

**Files (this repo):**

- changed `hflow/configuration/staff.mdx`, `HELP_PAGE_LOG.md`

### DOC-0058 (2026-06-08): Fix background wallpaper visibility in help pages

**Summary:** Changed the CSS selector in `style.css` from `#background-color` to `body` so that the full-bleed `hflow-wallpaper` image displays correctly. The `#background-color` identifier was preventing the background images from showing due to Mintlify DOM updates.

**Files (this repo):**

- changed `style.css`

### DOC-0057 (2026-06-05): Help site triangle wallpaper (light/dark)

**Summary:** Added full-bleed hFlow triangle wallpapers for light and dark mode on help.hflow.pro. [Mintlify `background`](https://www.mintlify.com/docs/organize/settings-appearance#background) in `docs.json` sets `background.color` and `background.image` (light/dark paths). Root `style.css` applies `background-size: cover` on `#background-color` because Mintlify’s default image placement is top-right only. Assets: `images/brand/hflow-wallpaper-light.png`, `hflow-wallpaper-dark.png`.

**Files (this repo):**

- changed `docs.json`, `style.css`
- added `images/brand/hflow-wallpaper-light.png`, `hflow-wallpaper-dark.png`

### DOC-0056 (2026-06-05): Communication Hub optional add-on (H-215)

**Summary:** Documented that the **hFlow Communication Hub** (Communications and Email Templates) is an **optional add-on** to a school’s hFlow subscription. When the add-on is off, menu entries remain with a preview and message; **Close** returns to Students. Contact hFlow admin or account rep to enable.

**Files (this repo):**

- changed `hflow/communications.mdx`: Optional add-on section, Who can use, common issue
- changed `hflow/configuration/email-templates.mdx`: Optional add-on section

### DOC-0055 (2026-06-05): Communications template refresh banner (H-214)

**Summary:** Renamed **Reset Template** to **Refresh Template** on the draft screen. When Configuration saved a newer template version than the student draft was built from, hFlow shows a banner with **Refresh**; confirm step warns that preview edits may be lost. Email templates help updated to match.

**Files (this repo):**

- changed `hflow/communications.mdx`, `hflow/configuration/email-templates.mdx`, `hflow/students/groups.mdx`

### DOC-0054 (2026-06-04): Candidate assessments cards and list sort (H-213)

**Summary:** Candidate table sorted by last name then first name. Drawer assessments tab uses full language assessment cards (reading + listening/speaking/writing) with click-to-edit modal.

**Files (this repo):**

- changed `hflow/students/candidate-students.mdx`: list sort, assessment cards in drawer

### DOC-0053 (2026-06-03): Replace "correct words" with "errors" in assessments (H-210)

**Summary:** All reading metric references updated from "correct words" to "errors" (miscues). CSV column renamed `errors`; schools must update templates. Assessments page, gradebook, checkpoint modal, candidate assessments, and data export now show "Errors" instead of "Correct". Sample CSV header updated. Getting-started CSV guide updated.

**Files (this repo):**

- changed `hflow/assessments.mdx`: Err/Tot label, `errors` CSV column
- changed `hflow/getting-started.mdx`: CSV column in quick-start table
- changed `samples/csv/hflow-sample-assessments.csv`: header `errors`

### DOC-0052 (2026-06-03): In-app Help ? FAB + ladybug pre-report nudge (H-206)

**Summary:** Document dual bottom-right controls: **`?` Help** opens contextual help in a new tab; **ladybug** shows a short “check Help first” panel before the report sheet. App map: `src/lib/helpPageForAppRoute.ts`. App map updated: yes (same release).

**Open doc backlog:** Screenshot of dual FABs and pre-report panel → `images/support/` (optional Reference figure).

**Files (this repo):**

- changed `hflow/reporting-issues-and-suggestions.mdx`, `hflow/troubleshooting.mdx`, `HELP_PAGE_LOG.md`

### DOC-0051 (2026-06-03): Students print roster view

**Summary:** New **Print roster view** guide (open from Students header, columns, L/S/W when data exists, **Show Reading Only** forces reading-only print). App: `readingOnly=1` query param from Students print button. Linked from Students overview cards and admin/teacher roles page. Changelog bullet.

**Open doc backlog:** Screenshot of print tab with full L/S/W columns; screenshot with **Show Reading Only** (reading columns only) → `images/students/`.

**Files (this repo):**

- added `hflow/students/print-view.mdx`
- changed `docs.json`, `hflow/students.mdx`, `hflow/students/roles-and-permissions.mdx`, `hflow/changelog.mdx`, `HELP_PAGE_LOG.md`

### DOC-0050 (2026-06-02): Reporting issues and suggestions (dedicated page)

**Summary:** New Support page for in-app bug reports and suggestions (FAB, sheet, impact chips, point-at, Look on the page, student ID, receipt email, owner **Reported issues** / withdraw). Troubleshooting shortened with link to the new page. Nav: Support group lists the page before Troubleshooting.

**Open doc backlog:** Screenshot of ladybug FAB + report sheet → `images/support/` (optional Reference figure).

**Files (this repo):**

- added `hflow/reporting-issues-and-suggestions.mdx`
- changed `docs.json`, `hflow/troubleshooting.mdx`, `HELP_PAGE_LOG.md`

### DOC-0049 (2026-06-02): Report a problem (H-182)

**Summary:** Added **Report a problem or suggest an idea** to Troubleshooting: FAB, four impact chips (including **Suggest an improvement**), screenshot, point-at-spot, Look on the page, student ID, receipt email, owner **Reported issues** withdraw flow.

**Files (this repo):**

- changed `hflow/troubleshooting.mdx`, `HELP_PAGE_LOG.md`

### DOC-0048 (2026-06-01): In-page logos: Welcome only

**Summary:** Removed inline brand images from Getting started, Languages, and Troubleshooting. Lockups remain on the Welcome page (`index.mdx`) and in the site header (`docs.json`) on all pages.

**Files (this repo):**

- changed `hflow/getting-started.mdx`, `hflow/languages.mdx`, `hflow/troubleshooting.mdx`, `AUTHORING.md`, `HELP_PAGE_LOG.md`

### DOC-0047 (2026-06-01): Light lockup: restore dark wordmark

**Summary:** Re-exported `hflow-lockup.png` from **`D_lockup_flat`** instead of `Light/lockup-flat-h512` (white wordmark invisible on light UI). Navbar and hero lockups show **hFlow** text again in light mode.

**Files (this repo):**

- changed `images/brand/hflow-lockup.png`, `hflow-lockup-sm.png`, `scripts/export-brand-assets.py`, `AUTHORING.md`, `HELP_PAGE_LOG.md`

### DOC-0046 (2026-06-01): Brand icons: flat light, framed dark

**Summary:** Re-exported help brand PNGs from **`Assets/hFlow Logos/`** (flat lockup/chart for light, framed lockup/chart for dark). **Languages** and **Troubleshooting** page marks now swap by theme. Favicon uses flat chart mark. Added **`scripts/export-brand-assets.py`** for future regenerations.

**Files (this repo):**

- changed `images/brand/*.png`, `docs.json`, `AUTHORING.md`, `hflow/languages.mdx`, `hflow/troubleshooting.mdx`, `scripts/export-brand-assets.py`, `HELP_PAGE_LOG.md`

### DOC-0045 (2026-06-01): Communications: template when switching students

**Summary:** Documented how the focus drafter picks a template when moving between students in a session (sent vs draft, last-used template, first-time default). Matches app behavior: draft students get the last template chosen in Communications Hub; sent students keep their sent template.

**Files (this repo):**

- changed `hflow/communications.mdx`, `HELP_PAGE_LOG.md`

### DOC-0044 (2026-06-01): Dark logo transparent background fix

**Summary:** Removed the full-width navy card baked into the Dark framed export and rebuilt `hflow-lockup-dark.png` on a transparent **1548×512** canvas (matching the light lockup). Keeps the framed icon stroke, dots, and white wordmark; frame fill and outer margins are transparent so the navbar/page background shows through.

**Files (this repo):**

- changed `images/brand/hflow-lockup-dark.png`, `AUTHORING.md`, `HELP_PAGE_LOG.md`

### DOC-0043 (2026-06-01): Dark navbar logo size fix

**Summary:** Rebuilt `hflow-lockup-dark.png` on a **1548×512** canvas (matching the light navbar lockup) by cropping the framed artwork to its icon/wordmark bounds and scaling up. The prior dark asset was **1645×820**, so Mintlify shrank the mark in the top-left navbar.

**Files (this repo):**

- changed `images/brand/hflow-lockup-dark.png`, `HELP_PAGE_LOG.md`

### DOC-0042 (2026-06-01): Dark mode lockup-framed logo

**Summary:** Replaced dark-theme help logo (`hflow-lockup-dark.png`) with **`Assets/hFlow Logos/Dark/lockup-framed-flat-h512.png`** (horizontal framed lockup for dark UI). Help home and Getting started dark hero images now use the same `280px` max width as the light lockup. Site header `docs.json` `logo.dark` path unchanged.

**Files (this repo):**

- changed `images/brand/hflow-lockup-dark.png`, `index.mdx`, `hflow/getting-started.mdx`, `AUTHORING.md`, `HELP_PAGE_LOG.md`

### DOC-0041 (2026-06-01): Sample CSV downloads via Google Drive

**Summary:** Getting started example student and assessment CSV links now point to Google Drive (Mintlify does not serve `.csv` on the current plan). Notes mention opening Drive and using **Download** to save the file.

**Files (this repo):**

- changed `hflow/getting-started.mdx`, `HELP_PAGE_LOG.md`

### DOC-0040 (2026-05-31): Dark theme logo: C_deep_3d (white wordmark)

**Summary:** Replaced dark-theme help logo (`hflow-lockup-dark.png`) with **`Assets/hFlow Logos/C_deep_3d/hFlow-512.png`** (square mark, white **hFlow** text on deep background). Light lockup unchanged. Prior dark asset was horizontal **`D_lockup_3d`** lockup with dark navy wordmark, which was hard to read on dark UI.

**Files (this repo):**

- changed `images/brand/hflow-lockup-dark.png`, `index.mdx`, `hflow/getting-started.mdx`, `AUTHORING.md`, `HELP_PAGE_LOG.md`

### DOC-0039 (2026-05-31): Dark mode lockup on help home and Getting started

**Summary:** Help home and Getting started now show the 3D dark lockup (`hflow-lockup-dark.png`) in dark mode at the same `280px` max width as the flat light lockup. Site header already used `docs.json` `logo.light` / `logo.dark` at matching navbar height.

**Files (this repo):**

- changed `index.mdx`, `hflow/getting-started.mdx`, `HELP_PAGE_LOG.md`

### DOC-0038 (2026-05-31): Data exports: delete is final

**Summary:** Note under delete section: deletion is final, cannot be undone, no restore, download first if needed.

**Files (this repo):**

- changed `hflow/configuration/data-exports.mdx`, `HELP_PAGE_LOG.md`

### DOC-0037 (2026-05-31): Data exports: server retention vs manual download

**Summary:** Under download steps, clarified completed exports stay in hFlow but are **not automatically downloaded**.

**Files (this repo):**

- changed `hflow/configuration/data-exports.mdx`, `HELP_PAGE_LOG.md`

### DOC-0036 (2026-05-31): Data exports help expanded

**Summary:** Expanded [Data exports](/hflow/configuration/data-exports): periodic backup recommendation, all school years per ZIP, 10 completed retention cap and storage-limit modal, download/delete/cancel, one job at a time, deleted students included. Removed outdated school-year checkbox steps.

**Files (this repo):**

- changed `hflow/configuration/data-exports.mdx`, `HELP_PAGE_LOG.md`

### DOC-0035 (2026-05-31): Benchmarks help under Languages nav

**Summary:** Moved **Benchmarks** from Configuration to **Languages** sidebar (order: Languages → Benchmarks → Tiers). Link from Languages page to benchmarks guide.

**Files (this repo):**

- changed `docs.json`, `hflow/languages.mdx`, `HELP_PAGE_LOG.md`

### DOC-0034 (2026-05-31): Benchmarks and tier rules help aligned with Languages

**Summary:** Rewrote [Benchmarks](/hflow/configuration/benchmarks) and [Tier rules](/hflow/configuration/tier-rules) to match the product: benchmarks derive from Tier 1 on **Languages**, read-only optional Configuration summary, no manual save-on-benchmarks flow. Clarified read-only **Benchmarks** table on Languages.

**Files (this repo):**

- changed `hflow/configuration/benchmarks.mdx`, `hflow/configuration/tier-rules.mdx`, `hflow/languages.mdx`, `HELP_PAGE_LOG.md`

### DOC-0033 (2026-05-31): Help nav restructure and student home page

**Summary:** Renamed sidebar **Shortcuts** → **Navigation**; moved **Tiers** under **Languages**; flattened **Students** (removed Guides subgroup). Replaced drawer doc with **[Student home page](/hflow/students/student-home-page)** (360° intro, header, Summary / Reading / Language tabs, assessments, checkpoints, notes, goals). Permanent redirect from `/hflow/students/view-student-data`. Updated cross-links across Students, Assessments, Getting started, roles, staff.

**Open doc backlog (screenshots):** Student home header, Summary tab (goals/notes/assessments/checkpoints), Reading and Language progress tabs.

**Files (this repo):**

- added `hflow/students/student-home-page.mdx`
- deleted `hflow/students/view-student-data.mdx`
- changed `docs.json`, `hflow/students.mdx`, `hflow/students/roles-and-permissions.mdx`, `hflow/students/student-progress-charts.mdx`, `hflow/assessments.mdx`, `hflow/getting-started.mdx`, `hflow/shortcuts.mdx`, `hflow/configuration/staff.mdx`, `hflow/tiers.mdx`, `index.mdx`, `hflow/changelog.mdx`, `HELP_PAGE_LOG.md`

### DOC-0032 (2026-05-31): Shortcuts help page

**Summary:** New standalone **[Shortcuts](/hflow/shortcuts)** guide: saved views / filter states, Tier 3 example, shortcuts vs [student groups](/hflow/students/groups), multi-screen reuse (Students, Assessments, reports), admin vs teacher, create/pin/rename/reorder/delete. Sidebar group **Shortcuts**; links from Students hub, Assessments, Reports.

**Open doc backlog (screenshots):** Shortcut chip (unsaved, saved, modified), Save shortcut dialog, Manage shortcuts with drag reorder, Pinned section in menu.

**Files (this repo):**

- added `hflow/shortcuts.mdx`
- changed `docs.json`, `hflow/students.mdx`, `hflow/assessments.mdx`, `hflow/reports.mdx`, `hflow/changelog.mdx`, `HELP_PAGE_LOG.md`

### DOC-0031 (2026-05-31): Getting started sample CSV downloads

**Summary:** Added **`samples/csv/hflow-sample-students.csv`** and **`hflow-sample-assessments.csv`** (fictitious data; reference only). **[Getting started](/hflow/getting-started)** explains CSV format, links downloads on steps 3 and 4 with **do not import as-is** guidance.

**Files (this repo):**

- added `samples/csv/hflow-sample-students.csv`, `samples/csv/hflow-sample-assessments.csv`
- changed `hflow/getting-started.mdx`, `hflow/changelog.mdx`, `HELP_PAGE_LOG.md`

### DOC-0030 (2026-05-31): Staff roles and permissions help

**Summary:** Rewrote **[Staff](/hflow/configuration/staff)** with Owner / Admin / Teacher definitions, navigation scope, assessment access, classroom assignments, and owner-only staff workflows. Updated **[Students: Admin vs Teacher](/hflow/students/roles-and-permissions)** to distinguish owners from admins and link to Staff. **Troubleshooting** sign-in section links to Staff for menu questions.

**Open doc backlog (screenshots):** Staff list (role groups), Add Staff modal (role + assessments checkbox), staff detail (role, Active, Assessments, assignments table).

**Files (this repo):**

- changed `hflow/configuration/staff.mdx`, `hflow/students/roles-and-permissions.mdx`, `hflow/troubleshooting.mdx`, `HELP_PAGE_LOG.md`

### DOC-0029 (2026-05-31): Ship hFlow brand logos to production

**Summary:** Added **`images/brand/`** PNG lockups (light + dark) and pushed **`docs.json`** `logo.light` / `logo.dark` paths so help.hflow.pro navbar matches local. Prior pushes only included the video commit without these assets.

**Files (this repo):**

- added `images/brand/hflow-lockup.png`, `hflow-lockup-sm.png`, `hflow-lockup-dark.png`, `hflow-mark.png`, `hflow-mark-sm.png`
- changed `docs.json`, `index.mdx`, and remaining unpublished help MDX from the May help refresh

### DOC-0028 (2026-05-31): Getting started video embed

**Summary:** Embedded setup walkthrough on **[Getting started](/hflow/getting-started)** (`<video>` + `<source>`, no `Frame`). **`videos/hflow-getting-started-guide.mp4`** re-encoded for web (H.264 + faststart); later prepended **hflow logo night** intro (~10 s) before the tutorial body. **Must be committed and pushed** to `hFlowDocs` for playback on help.hflow.pro.

**Files (this repo):**

- added `videos/hflow-getting-started-guide.mp4`
- changed `hflow/getting-started.mdx`, `AUTHORING.md`

### DOC-0027 (2026-05-31): Correct app / website / help URLs

**Summary:** Staff-facing links now use **app.hflow.pro** (app), **www.hflow.pro** (website), and **help.hflow.pro** (help). Updated **`docs.json`** navbar, **`index.mdx`**, **`getting-started.mdx`**, and **`AUTHORING.md`** domain table.

**Files (this repo):**

- changed `docs.json`, `index.mdx`, `hflow/getting-started.mdx`, `AUTHORING.md`

### DOC-0026 (2026-05-31): Getting started, brand logos, troubleshooting, assessment CSV

**Summary:** Rebuilt **[Getting started](/hflow/getting-started)** from the setup and data-import tutorial (org profile → languages/tiers → student CSV → assessment CSV). Added **`images/brand/`** lockup and mark PNGs from `Assets/hFlow Logos` (flat lockup for light theme, 3d lockup for dark); updated **`docs.json`** site logo paths. Expanded **Languages**, **Assessments** (CSV import section), and **Troubleshooting** (staff FAQs). Refreshed **`index.mdx`** with lockup and getting-started cards. Removed broken screenshot references (files were never in repo). **Org profile** save button label aligned to **Save Changes**.

**Open doc backlog (screenshots):** Students roster header, Add Student modal, student drawer (re-add under `images/students/` when captured).

**Files (this repo):**

- added `images/brand/hflow-lockup.png`, `hflow-lockup-sm.png`, `hflow-lockup-dark.png`, `hflow-mark.png`, `hflow-mark-sm.png`
- changed `docs.json`, `index.mdx`, `hflow/getting-started.mdx`, `hflow/languages.mdx`, `hflow/assessments.mdx`, `hflow/troubleshooting.mdx`, `hflow/changelog.mdx`, `hflow/configuration/org-profile.mdx`, `hflow/students.mdx`, `hflow/students/add-students.mdx`, `hflow/students/view-student-data.mdx`, `hflow/students/roles-and-permissions.mdx`

### DOC-0025 (2026-05-28): Communications sessions, groups, email template tokens

**Summary:** Replaced outdated Communications campaign guide with session-based hub workflow (groups, sessions, roster filters, focus drafter, Reset Template, Copy/Mark Sent). Added **Student groups** guide (Manage Groups, builder pool/roster, admin vs teacher filters). Updated **Email templates** for dropdown UI, template filters, and token panel (**Show for period**, **Filter tokens…**, categories).

**Open doc backlog (screenshots):** Communications hub (group/session, roster filters, donut); draft screen (Reset Template, preview, Copy/Mark Sent); Email Templates token panel; Groups builder (pool/roster transfer).

**Files (this repo):**

- changed `hflow/communications.mdx`, `hflow/configuration/email-templates.mdx`, `hflow/students.mdx`, `docs.json`
- added `hflow/students/groups.mdx`

### DOC-0024 (2026-05-26): H-188 Reading-only assessment card layouts

**Summary:** Documented roster period cells and Assessments gradebook cards when only reading is reported (no L/S/W), including “not reported” footers and return to full layout after L/S/W entry.

**Files (this repo):**

- changed `hflow/students.mdx`, `hflow/assessments.mdx`

### DOC-0023 (2026-05-25): Email templates auto-save

**Summary:** Updated **Email templates** help: custom templates auto-save with inline **Saving…** / **Saved** next to the name; removed manual Save and unsaved-changes dialog from the guide.

**Files (this repo):**

- changed `hflow/configuration/email-templates.mdx`

### DOC-0022 (2026-05-18): ACTFL proficiency scale reference page

**Summary:** Published **`hflow/actfl-proficiency-scale.mdx`** (intro from public ACTFL summaries, links to **[Language Testing International](https://www.languagetesting.com/actfl-proficiency-scale)** and **[ACTFL](https://www.actfl.org/)**, distinction versus **reading tiers**, where hFlow uses **1–9** domain levels / composite). Nav: **Assessments** group adds this page after **Assessments**. Cross-linked from **Assessments**, **Tiers**, **Student progress charts**; changelog entry.

**Files (this repo):**

- added `hflow/actfl-proficiency-scale.mdx`
- changed `docs.json`, `hflow/assessments.mdx`, `hflow/tiers.mdx`, `hflow/students/student-progress-charts.mdx`, `hflow/changelog.mdx`

### DOC-0021 (2026-05-18): Authoring guideline: mandatory every edit + Voice and phrasing

**Summary:** Made **`AUTHORING.md`** explicitly **mandatory** for every **`hflow/`** and **`index.mdx`** edit; added **Voice and phrasing** (forbid Expected outcome/result scaffolding; examples table), **Audience and honesty**, and tightened cross-references from **`CONTRIBUTING.md`**, **`README.md`**, **`AGENTS.md`**, Gilat **`help-pages-implications.mdc`**, and **`MAINTENANCE.md`** so contributors and agents re-read authoring rules on each help touch.

**Files (this repo):**

- changed `AUTHORING.md`, `README.md`, `CONTRIBUTING.md`, `AGENTS.md`

**Related (Gilat app repo):** `.cursor/rules/help-pages-implications.mdc`, `docs/llm/MAINTENANCE.md`

### DOC-0020 (2026-05-18): Plain-language outcomes (drop “Expected outcome”)

**Summary:** Removed **Expected outcome / Expected result** labels across **`hflow/**/*.mdx`**, rewriting follow-up sentences (“After saving…”, “You should see…”); updated **`AUTHORING.md`** and **`.cursor/rules/help-pages-implications.mdc`** to instruct plain prose instead of that pattern.

**Files (this repo):**

- changed `AUTHORING.md`
- changed many `hflow/**/*.mdx` pages (students, assessments, reports, languages, communications, configuration, getting-started)

**Related (Gilat app):** `.cursor/rules/help-pages-implications.mdc`

### DOC-0019 (2026-05-18): Help IA, audience split, Reports + Configuration guides

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

### DOC-0018 (2026-05-12): Reports menu + Copy Charts

**Summary:** Published **Org reports (Reports menu)**: how to open each header report, what each summarizes, **Copy Charts** on Growth, Language Progress, and Grade Language Distribution (including two-panel stitched PNG), clipboard vs download behavior, and that Reading Tier Distribution has no Copy Charts. Linked student progress charts to org reports for shared export behavior.

**Files (this repo):**

- added `hflow/reports.mdx`
- changed `docs.json` (nav order)
- changed `index.mdx` (Org reports card)
- changed `hflow/students/student-progress-charts.mdx` (**Copy Charts** label + cross-link)

**Related (Gilat app):** `AppShell` Reports dropdown; `grade-progress/page.tsx`, `grade-language-distribution/page.tsx`, `growth/page.tsx`, `StudentTrendReport.tsx`, `exportChart.ts`.

### DOC-0017 (2026-05-09): ACTFL chart: band abbrev inside bars

**Summary:** Documented that the ACTFL-by-skill bars show the proficiency band abbreviation (NL–AH) under the level digit inside each bar when space allows.

**Files (this repo):**

- changed `hflow/students/student-progress-charts.mdx`

**Related (Gilat app):** `LanguageProgressSection.tsx`.

### DOC-0016 (2026-05-09): Checkpoint drag order persistence

**Summary:** Added task steps for drag-and-drop checkpoint reordering, default date-based ordering behavior, and persistence scope (per student enrollment year + language) in the student profile help page.

**Files (this repo):**

- changed `hflow/students/view-student-data.mdx`

**Related (Gilat app):** `StudentProfileSummaryPanel.tsx`, `StudentProfileDrawer.tsx`, `src/app/api/student-years/[studentYearId]/checkpoint-order/route.ts`.

### DOC-0015 (2026-05-09): Students: IDs in drawer only; drawer above header

**Summary:** Roster rows no longer list ID/Ext ID on the table; copy controls for those values live in the profile drawer header. Documented z-order fix so the drawer is not covered by the app header.

**Files (this repo):**

- changed `hflow/students.mdx` (roster vs drawer IDs)
- changed `hflow/students/view-student-data.mdx` (drawer top summary)

**Related (Gilat app):** `src/app/students/page.tsx`, `StudentProfileDrawer.tsx`.

### DOC-0014 (2026-05-09): ACTFL overall display: hide trailing .0

**Summary:** User-facing composite string shows whole numbers without a decimal (e.g. `3 - NH` instead of `3.0 - NH`); fractional values still show one decimal.

**Files (this repo):**

- changed `hflow/assessments.mdx` (ACTFL overall bullet)

**Related (Gilat app):** `formatActflOverallDisplay` in `actflProficiencyLevels.ts`.

### DOC-0013 (2026-05-09): H-172: overall language, ACTFL composite, roster compact cards

**Summary:** Documented **grade-level overall** (auto + manual override rules), read-only **ACTFL overall**, bulk gradebook **G. overall** / **ACTFL Σ**, and Students roster **compact** layout with **Show Reading Only**. Noted that CSV/print/org export contracts are unchanged.

**Files (this repo):**

- changed `hflow/assessments.mdx` (replaced placeholder with task-oriented guide)
- changed `hflow/students.mdx` (roster period cells + Show Reading Only)

**Related (Gilat app):** `AssessmentFormModal`, `GradebookGrid` / `GradebookRow`, `StudentsPeriodCompactCard`, `overallLanguageScore.ts`.

### DOC-0012 (2026-05-08): Tier tooltip: worst-of accuracy vs fluency

**Summary:** Hover card for tier pills notes that placement uses the **more conservative** of the accuracy-based and fluency-based tier (each score matched to bands independently).

**Files (this repo):**

- changed `hflow/tiers.mdx` (median summary vs passage tiers)

**Related (Gilat app):** `TierPeriodHoverCard.tsx`, `assessmentMba.ts`.

### DOC-0011 (2026-05-08): Tiers: per-assessment vs overall (MBA roll-up)

**Summary:** Published help replaces the tiers placeholder with user-facing copy: per-row tiers use that enrollment year’s rules; multiple passages in one period roll up to the **worst** tier for overall placement. App migration `20260508231244_fix_student_tier_rollup_mba_passages.sql` implements that roll-up in `calculate_student_tier`.

**Files (this repo):**

- changed `hflow/tiers.mdx`

**Related (Gilat app):** `rollup_scheduled_tier_for_period`, `DATA_MODEL.md` tier section.

### DOC-0010 (2026-05-07): Language charts: BOY/MOY/EOY under each bar

**Summary:** Period abbreviations render **under every bar**; footer **BOY/MOY/EOY legend row removed**; extra bottom margin and x-axis offset reduce cramped labels.

**Files (this repo):**

- changed `hflow/students/student-progress-charts.mdx`

**Related (Gilat app):** `LanguageProgressSection`.

### DOC-0009 (2026-05-07): Language charts: no cohort toggles, unified ACTFL color, in-bar labels

**Summary:** Language progress bars drop **grade cohort** UI; ACTFL uses **one periwinkle** for all skills; labels **inside** bars with improved contrast; help updated.

**Files (this repo):**

- changed `hflow/students/student-progress-charts.mdx`

**Related (Gilat app):** `LanguageProgressSection`; student trend page no longer requests language cohort aggregates for charts.

### DOC-0008 (2026-05-07): Language charts: full-width footers, comprehension R/Y/G, always Listening

**Summary:** Language chart cards put period + grade-avg **below** the plot for width; comprehension chart uses **red/yellow/green** by level, always shows **four** skills, and adds a level **legend**.

**Files (this repo):**

- changed `hflow/students/student-progress-charts.mdx`

**Related (Gilat app):** `LanguageProgressSection`.

### DOC-0007 (2026-05-07): Language tab: bar charts for ACTFL and comprehension

**Summary:** Language progress uses **grouped bar charts** (skills on the x-axis, periods as bars); cohort averages as lighter companion bars; help text updated from line charts.

**Files (this repo):**

- changed `hflow/students/student-progress-charts.mdx`

**Related (Gilat app):** `LanguageProgressSection` bar charts.

### DOC-0006 (2026-05-07): Language charts: skill wording, overlap visibility, numeric comp labels

**Summary:** Student progress language tab copy uses **skill** (not domain); charts use dash patterns and colliding-point offsets; right chart point labels are **1 / 2 / 3** only.

**Files (this repo):**

- changed `hflow/students/student-progress-charts.mdx`

**Related (Gilat app):** Student trend `LanguageProgressSection`.

### DOC-0005 (2026-05-07): Language tab: comprehension chart L/S/W levels

**Summary:** Help text for the right-hand chart: reading comp plus listening/speaking/writing domain levels (1–3), shared colors with ACTFL chart.

**Files (this repo):**

- changed `hflow/students/student-progress-charts.mdx`

**Related (Gilat app):** H-168 follow-up.

### DOC-0004 (2026-05-07): Student progress charts (Reading vs Language tabs)

**Summary:** Documented the student trend report: folder tabs, language progress (ACTFL by domain, reading comprehension 1–3), org-wide grade cohort averages, `?tab=language`, and copy/export behavior.

**Files (this repo):**

- added `hflow/students/student-progress-charts.mdx`
- changed `docs.json`
- changed `hflow/students/view-student-data.mdx`

**Related (Gilat app):** Linear H-168.

### DOC-0003 (2026-05-07): Multi-select roster filters (admin vs teacher)

**Summary:** Documented admin multi-select for grade, class, and reading tier on Students (language single-select). Clarified teacher roster as the union of one or more selected assignments.

**Files (this repo):**

- changed `hflow/students/roles-and-permissions.mdx`

**Related (Gilat app):** Linear H-166 (filters across Students, Assessments, reports, Communications, Enrollment).

### DOC-0002 (2026-04-30): Maintainer log and no internal backlog on published pages

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

### DOC-0001 (2026-04-29): Students help pilot and Mintlify site

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
