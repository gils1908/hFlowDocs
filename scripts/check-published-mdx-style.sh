#!/usr/bin/env bash
# Fail if published help MDX contains em dashes (U+2014).
# Run from hFlowDocs repo root: ./scripts/check-published-mdx-style.sh

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

if rg -n $'\u2014' index.mdx hflow 2>/dev/null; then
  echo >&2
  echo "check-published-mdx-style: em dashes are not allowed in published help." >&2
  echo "Use commas, colons, periods, or parentheses. See AUTHORING.md." >&2
  exit 1
fi

count="$(find hflow index.mdx -name '*.mdx' 2>/dev/null | wc -l | tr -d ' ')"
echo "check-published-mdx-style: OK (no em dashes in ${count} published MDX files)"
