#!/usr/bin/env python3
"""Verify the authored inputs for the CorvidLabs Swift status site."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parent.parent
AUTHORED_INPUTS = (
    ROOT / "README.md",
    ROOT / "index.md",
    ROOT / "_config.yml",
    ROOT / "_layouts/default.html",
)
FORBIDDEN_MARKERS = re.compile(
    r"\b(?:TODO|FIXME|TBD|CHANGEME|PLACEHOLDER|LOREM\s+IPSUM|DUMMY)\b",
    re.IGNORECASE,
)


def fail(message: str) -> None:
    print(f"site verification failed: {message}", file=sys.stderr)
    raise SystemExit(1)


def read_required(path: Path) -> str:
    if not path.is_file():
        fail(f"missing {path.relative_to(ROOT)}")
    content = path.read_text(encoding="utf-8")
    if not content.strip():
        fail(f"empty {path.relative_to(ROOT)}")
    marker = FORBIDDEN_MARKERS.search(content)
    if marker:
        fail(f"placeholder marker {marker.group(0)!r} in {path.relative_to(ROOT)}")
    return content


def table_rows(markdown: str) -> list[str]:
    rows = [line.strip() for line in markdown.splitlines() if line.startswith("|")]
    if len(rows) < 3:
        fail("status table is missing its header, separator, or package rows")
    if rows[0] != "| Package | Version | macOS | Ubuntu | Docs | Issues | PRs |":
        fail("status table header changed unexpectedly")
    packages: list[str] = []
    for row in rows[2:]:
        if row.count("|") != 8:
            fail(f"status row does not contain seven columns: {row}")
        match = re.match(r"\| \[([^]]+)\]\(https://github\.com/CorvidLabs/([^)]+)\)", row)
        if not match or match.group(1) != match.group(2):
            fail(f"status row has an inconsistent CorvidLabs repository link: {row}")
        packages.append(match.group(1))
    if len(packages) != len(set(packages)):
        fail("status table contains duplicate package rows")
    return rows


def main() -> None:
    readme, index, config, layout = (read_required(path) for path in AUTHORED_INPUTS)
    if not readme.startswith("# CorvidLabs Swift Status\n\nCI status for all Swift repositories.\n"):
        fail("README title or purpose is missing")
    if not index.startswith("---\nlayout: default\n---\n"):
        fail("index.md does not select the default Jekyll layout")
    if table_rows(readme) != table_rows(index):
        fail("README.md and index.md publish different status tables")

    required_config = {
        "title: CorvidLabs Swift Status",
        "description: CI status for all Swift repositories",
        'url: "https://corvidlabs.github.io"',
        'baseurl: "/swift.status"',
        "markdown: kramdown",
        "  input: GFM",
    }
    missing_config = sorted(required_config.difference(config.splitlines()))
    if missing_config:
        fail(f"Jekyll configuration is missing: {', '.join(missing_config)}")

    required_layout = (
        '<html lang="en">',
        '<meta name="viewport"',
        "{{ page.title | default: site.title }}",
        "{{ site.description }}",
        "{{ content }}",
        "https://github.com/CorvidLabs",
    )
    missing_layout = [token for token in required_layout if token not in layout]
    if missing_layout:
        fail(f"default layout is missing: {', '.join(missing_layout)}")

    print(f"verified {len(AUTHORED_INPUTS)} authored inputs and {len(table_rows(index)) - 2} package rows")


if __name__ == "__main__":
    main()
