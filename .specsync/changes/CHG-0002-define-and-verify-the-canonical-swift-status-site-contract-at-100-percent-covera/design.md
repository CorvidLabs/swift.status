---
change: CHG-0002-define-and-verify-the-canonical-swift-status-site-contract-at-100-percent-covera
artifact: design
---

# Design

SpecSync scans Markdown, YAML, and HTML from the repository root while excluding generated governance and agent-integration directories. One active `status-site` spec maps all four authored Jekyll inputs, producing a four-of-four file and line coverage denominator.

`scripts/verify-site.py` uses only the Python 3 standard library. It fails on missing or empty inputs, placeholder markers, README/index table drift, malformed columns, duplicate packages, inconsistent CorvidLabs repository links, missing Jekyll deployment configuration, or missing layout contract tokens. The script reads committed files only and performs no network requests, so results are deterministic on local and hosted runners.
