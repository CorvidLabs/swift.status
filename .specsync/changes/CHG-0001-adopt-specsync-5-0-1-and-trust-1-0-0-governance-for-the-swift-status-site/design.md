---
change: CHG-0001-adopt-specsync-5-0-1-and-trust-1-0-0-governance-for-the-swift-status-site
artifact: design
---

# Design

SpecSync 5.0.1 records governance state in `.specsync/` and treats all four authored Jekyll inputs plus governance configuration as meaningful paths. Trust 1.0.0 invokes the repository's `verify` lane, enforces contract and risk policy, keeps provenance progressive, and leaves Atlas publication disabled. The pull-request job retains the required name `trust` and uses the immutable Trust release commit.
