## ADDED

### REQUIREMENT REQ-status-site-001
The README and published index SHALL present the same seven-column Swift package status table.

Acceptance Criteria
- Deterministic verification compares the complete Markdown table rows and fails on any difference.

### REQUIREMENT REQ-status-site-002
Each catalog row SHALL name and link the same CorvidLabs repository and SHALL appear only once.

Acceptance Criteria
- Verification rejects a package/link mismatch or duplicate package name.

### REQUIREMENT REQ-status-site-003
Each catalog row SHALL expose version, macOS, non-macOS, documentation, issue, and pull-request status links or an explicit platform limitation.

Acceptance Criteria
- Every package row contains exactly seven columns.

### REQUIREMENT REQ-status-site-004
The published index SHALL use the default layout and render the committed Markdown content.

Acceptance Criteria
- `index.md` selects `layout: default` and the layout contains the Liquid `content` slot.

### REQUIREMENT REQ-status-site-005
Jekyll configuration SHALL retain the canonical `https://corvidlabs.github.io/swift.status/` deployment target.

Acceptance Criteria
- Verification requires the CorvidLabs GitHub Pages origin and `/swift.status` base path.

### REQUIREMENT REQ-status-site-006
The default layout SHALL declare English content, viewport metadata, title, description, and a visible CorvidLabs footer link.

Acceptance Criteria
- Verification requires each corresponding committed layout token.

### REQUIREMENT REQ-status-site-007
Verification SHALL reject missing, empty, inconsistent, duplicate, or malformed authored inputs.

Acceptance Criteria
- `fledge lanes run verify` exits non-zero for each invalid condition.

### REQUIREMENT REQ-status-site-008
Authored site inputs SHALL contain no incomplete-work or sample-content markers.

Acceptance Criteria
- Verification rejects TODO, FIXME, TBD, placeholder, lorem-ipsum, dummy, and changeme markers without treating the policy text itself as a site input.

### REQUIREMENT REQ-status-site-009
The committed catalog SHALL link to remote status sources without synthesizing or embedding fake CI results.

Acceptance Criteria
- Authored site inputs contain links and badges but no hard-coded claim that a remote workflow currently passes.
