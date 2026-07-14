---
change: CHG-0002-define-and-verify-the-canonical-swift-status-site-contract-at-100-percent-covera
artifact: testing
---

# Testing

The blocking command is `fledge lanes run verify`, which executes
`python3 scripts/verify-site.py` without network access.

| Requirement | Deterministic evidence |
|-------------|------------------------|
| REQ-status-site-001 | The verifier compares every status-table row in `README.md` and `index.md`. |
| REQ-status-site-002 | The verifier extracts each package/link pair and rejects mismatches or duplicate package names. |
| REQ-status-site-003 | The verifier requires exactly seven columns in each package row. |
| REQ-status-site-004 | The verifier requires `layout: default` and the Liquid content slot. |
| REQ-status-site-005 | The verifier requires the canonical GitHub Pages origin and `/swift.status` base path. |
| REQ-status-site-006 | The verifier requires the English language, viewport, title, description, and CorvidLabs footer tokens. |
| REQ-status-site-007 | The verifier rejects missing, empty, inconsistent, duplicate, and malformed inputs. |
| REQ-status-site-008 | The verifier scans only the four authored site inputs for incomplete-work and sample-content markers. |
| REQ-status-site-009 | The verifier and spec confirm the authored inputs use remote links/badges and contain no hard-coded passing-status claims. |

Strict SpecSync verification additionally enforces four-of-four file and line coverage and six-of-six documented Jekyll configuration exports.
