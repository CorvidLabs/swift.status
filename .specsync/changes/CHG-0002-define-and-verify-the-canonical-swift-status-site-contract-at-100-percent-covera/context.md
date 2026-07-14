---
change: CHG-0002-define-and-verify-the-canonical-swift-status-site-contract-at-100-percent-covera
artifact: context
---

# Context

`swift.status` is a four-input Jekyll status catalog: `README.md` is the GitHub view, `index.md` is the published page body, `_config.yml` selects the GitHub Pages target, and `_layouts/default.html` supplies the page shell. The first migration draft treated the repository as having no canonical product surface and therefore enforced zero SpecSync coverage.

The rollout requires truthful full SDD coverage. This change defines the existing catalog contract without changing its rows, presentation, or deployment behavior. It also replaces existence-only verification with deterministic checks of the relationships the site depends on.
