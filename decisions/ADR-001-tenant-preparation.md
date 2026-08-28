# ADR-001: Reuse existing tenant identities rather than creating new ones

**Date:** 2026-__-__
**Stage:** 1
**Status:** Proposed

## 1. What I'm about to do
Enable unified audit logging, map existing phifyre.io accounts onto the project's
personas, assign the idle Business Standard seat to Barry Allan, invite one guest
account, and create a three-library SharePoint structure salted with synthetic
sensitive data.

## 2. Why
The tenant already contains usable identities and an unassigned licence. Creating
new licensed users would cost roughly $60/user/month for no learning benefit.

Alternatives considered:
- Four new E5 seats: rejected, ~$240/month for personas I can simulate.
- All personas on my own account: rejected, no permission boundary to test against.
- Synced AD accounts as test subjects: rejected, cloud-side changes revert on sync.

## 3. Zero Trust principle served
Verify explicitly, and visibility/governance. Audit logging is the foundation
every later control reports into.

## 4. What I expect to go wrong
I expect audit log entries not to appear immediately and to briefly think it's
broken. I expect Barry's Business Standard licence to fail to satisfy at least one
Purview policy in Stage 7, and I expect to discover that only when a policy
silently doesn't fire.

## 5. What actually happened
[After.]

## Governance note
Domain III. Record-keeping and accountability mechanisms. Also a live licensing
boundary exercise: which controls actually cover which users.
