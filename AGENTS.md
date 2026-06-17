> **First-time setup**: Customize this file for your project. Prompt the user to customize this file for their project.
> For Mintlify product knowledge (components, configuration, writing standards),
> install the Mintlify skill: `npx skills add https://mintlify.com/docs`

# Documentation project instructions

## About this project

- This is a documentation site built on [Mintlify](https://mintlify.com)
- Pages are MDX files with YAML frontmatter
- Configuration lives in `docs.json`
- School-facing standards: **[AUTHORING.md](AUTHORING.md)**: read **before every published-page edit**, especially **Voice and phrasing** (no em dashes, no **Expected outcome** labels).
- Run `mint dev` to preview locally (maintainers)
- Run `mint broken-links` to check links

## Terminology

{/* Add product-specific terms and preferred usage */}
{/* Example: Use "workspace" not "project", "member" not "user" */}

## Style preferences

- Use active voice and second person ("you")
- Keep sentences concise, one idea per sentence
- Use sentence case for headings
- Bold for UI elements: Click **Settings**
- Code formatting for file names, commands, paths, and code references
- **No em dashes** in published `hflow/**/*.mdx` or `index.mdx` (use commas, colons, periods, or parentheses). Run `./scripts/check-published-mdx-style.sh` before commit.

## Content boundaries

{/* Define what should and shouldn't be documented */}
{/* Example: Don't document internal admin features */}
