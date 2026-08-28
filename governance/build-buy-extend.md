---
document: Build / buy / extend analysis
system: Policy Buddy
decision: Build (pilot), on existing platform
date: 2026-__-__
revisit: At pilot exit
---

# Build, buy, or extend — Policy Buddy

> Worked example. The purpose of this document is not to justify building.
> It is to make the reasoning inspectable so that a reviewer can disagree with
> a specific step rather than with the conclusion as a whole.

## The options, honestly stated

### Option A — Do nothing

**Cost:** $0 direct. **Not** zero in effect.

Employees are already pasting policy questions into consumer AI tools.
"Do nothing" preserves an unmanaged data-egress path. This option is often
scored as the safe baseline and it is frequently not.

Rejected — but it is the correct comparison point for every other option.

### Option B — Improve intranet search

**Cost:** low. **Risk:** very low. **Fabrication risk:** none.

If most questions are "I could not find it," this solves them for a fraction
of the cost with no new failure modes. See business case section 7.

**Not rejected on merit.** Deferred, and explicitly re-tested if M1 improves by
less than 20%. This is the strongest competing option and the document says so
rather than dismissing it, because a build-vs-buy analysis that eliminates the
cheapest option in one line is not analysis.

### Option C — Use Microsoft 365 Copilot as-is

Licences already exist. Zero build effort. Genuinely tempting.

**Rejected for this use case, for one specific reason:** Copilot answers from
whatever the *signed-in user* can already reach. That is correct behaviour for
a general assistant and wrong for a policy service, because:

- Answers vary by who asks. Two employees get different answers to the same
  policy question depending on their permissions. For a *policy* service,
  inconsistency is the original problem restated.
- It cannot be scoped to the authoritative corpus. It will happily answer from
  a stale draft in someone's OneDrive.
- Stage 8 demonstrates the failure directly: as admin, Copilot will surface
  `HR-Confidential` compensation bands. That is not a Copilot defect — it is
  Copilot working exactly as designed on a permission structure that was never
  audited for it.

**This rejection is scoped, not general.** Copilot remains the right tool for
open-ended assistance. It is the wrong tool when you need one authoritative
answer regardless of who asks.

### Option D — Buy a vendor HR assistant

**Cost:** typically $10k–50k/year at this scale.

Rejected on cost relative to pilot value, but note the *hidden* cost that
usually decides these: each vendor requires a third-party assessment covering
data residency, retention, training use, subprocessors, and incident
notification (see `foundry-assessment.md` for what that involves). At pilot
scale that review effort can exceed the build effort.

Revisit if the pilot succeeds and scaling to multiple domains is on the table —
buy economics improve with breadth, build economics do not.

### Option E — Build on Azure AI Foundry  ← **selected**

**Cost:** $5–15/month at pilot scale, plus build effort.

Chosen because it is the only option that satisfies **S1 and S2**: retrieval
scoped to one library, identical answers regardless of who asks, and a hard
boundary against restricted content. Everything else follows from that.

Secondary factor, stated honestly: this is a learning project, and building
develops organisational capability that buying does not. That is a legitimate
input but it must be **named** rather than smuggled in as a technical argument.
Architects routinely dress up "we wanted to build it" as a requirements
conclusion.

### Option F — Build in Copilot Studio

Deferred rather than rejected. Evaluated head-to-head in Stage 9 with the same
MCP tool server, which turns it into a controlled comparison rather than an
opinion.

Early expectation, recorded now so it can be checked later: Copilot Studio will
be dramatically faster to build and materially harder to inspect. Writing the
prediction down before running the experiment is what makes the result
informative.

## Decision

**Build (Option E) for the pilot**, with Option B held as the fallback
hypothesis and Option F evaluated as a comparison.

## What would change this decision

- M1 improves less than 20% → Option B was probably right; re-test search.
- Scaling to 3+ domains → Option D economics improve; re-run this analysis.
- Copilot gains scoped, corpus-restricted grounding → Option C becomes viable
  and this build becomes redundant. **This is the most likely reason this
  decision expires**, and it could happen within a year.

That last bullet matters. A build decision made against a fast-moving
platform has a shelf life, and saying so protects you from defending it past
its expiry out of sunk-cost attachment.
