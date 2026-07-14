---
module: status-site
version: 2
status: active
files:
  - README.md
  - index.md
  - _config.yml
  - _layouts/default.html

db_tables: []
depends_on: []
---

# Swift Status Site

## Purpose

Publish a static, read-only catalog of CI, release, documentation, issue, and pull-request status links for CorvidLabs Swift repositories. The README presents the catalog on GitHub; Jekyll publishes the same table through `index.md`, `_config.yml`, and `_layouts/default.html`.

## Public API

The public interface is the rendered GitHub Pages site at `https://corvidlabs.github.io/swift.status/` and the repository catalog in `README.md`. Each package row identifies one CorvidLabs repository and exposes version, macOS, non-macOS, documentation, issue, and pull-request links or an explicit platform limitation badge.

### Exported Configuration

| Export | Contract |
|--------|----------|
| `title` | Human-readable site title used by the layout. |
| `description` | Site purpose rendered in metadata and the page header. |
| `url` | Canonical GitHub Pages origin. |
| `baseurl` | Repository-specific `/swift.status` publication path. |
| `markdown` | Kramdown is the selected Markdown renderer. |
| `kramdown` | Nested renderer configuration selects GitHub-Flavored Markdown input. |

## Invariants

1. `README.md` and `index.md` contain the same seven-column package table.
2. Every package name matches its `https://github.com/CorvidLabs/<package>` target and appears only once.
3. `index.md` selects the `default` layout, and the layout renders `{{ content }}` with an English document language, viewport metadata, site title, and site description.
4. `_config.yml` keeps the canonical GitHub Pages origin and `/swift.status` base path.
5. The authored inputs contain no TODO, FIXME, TBD, placeholder, lorem-ipsum, dummy, or changeme markers.
6. The site is static and read-only; badges and links may fetch remote status, but the repository does not synthesize CI results or embed fake status data.

## Behavioral Examples

- Given a package row in `index.md`, when Jekyll renders the page, then a visitor can follow the package, release, CI, docs, issues, and pull-request links represented by that row.
- Given a maintainer updates the package catalog, when `fledge lanes run verify` runs, then mismatched README/site tables, duplicate repositories, inconsistent repository links, or malformed columns fail verification.

## Error Cases

| Error | Behavior |
|-------|----------|
| Missing or empty authored input | Verification fails before Trust accepts the change. |
| README and site tables diverge | Verification reports the mismatch and exits non-zero. |
| Duplicate or malformed package row | Verification identifies the invalid catalog condition and exits non-zero. |
| Required Jekyll metadata or Liquid content slot is absent | Verification reports the missing contract token and exits non-zero. |
| Placeholder marker is committed | Verification names the marker and input and exits non-zero. |

## Dependencies

- GitHub Pages and Jekyll with Kramdown/GFM render the committed site inputs.
- Shields.io, GitHub Actions badges, NES.css, and Google Fonts are remote presentation/status dependencies; their availability does not alter the committed catalog.
- `scripts/verify-site.py` uses only Python 3 standard-library modules and is the blocking native verification command.

## Change Log

| Version | Date | Changes |
|---------|------|---------|
| 1 | 2026-07-14 | Added the canonical status-site contract for SpecSync 5 / Trust 1 adoption. |
| 2 | 2026-07-14 | CHG-0002-define-and-verify-the-canonical-swift-status-site-contract-at-100-percent-covera: Define and verify the canonical Swift status site contract at 100 percent coverage |
