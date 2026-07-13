---
change: CHG-0001-adopt-specsync-5-0-1-and-trust-1-0-0-governance-for-the-swift-status-site
artifact: testing
---

# Testing

Run `fledge lanes run verify` to require all four committed Jekyll inputs to exist and be non-empty. Confirm all four agent integrations with `specsync agents status`, run `specsync check --strict --force`, then run `fledge trust doctor` and `fledge trust verify`. Hosted pull-request validation must independently complete the same immutable Trust gate before merge.
