---
document: Stakeholder map
system: Policy Buddy
date: 2026-__-__
---

# Stakeholders — Policy Buddy

> Worked example. In this project you play every role. The exercise is to
> notice that these interests genuinely conflict, and that "the architect
> decides" is usually shorthand for "the architect chose whose interest to
> prioritise without saying so."

| Stakeholder | What they want | What they fear | Their veto |
|---|---|---|---|
| **People Operations** (owner) | Fewer repetitive tickets; consistent answers | Wrong answers attributed to HR | Can refuse to endorse it |
| **Employees** (users) | Fast, correct answers | Being given a wrong answer they act on; being monitored | Simply won't use it |
| **Information Security** | Controlled data access; auditability | Data leakage; prompt injection; shadow AI | Can block deployment |
| **Legal / Compliance** | Defensible records; regulatory fit | Becoming a high-risk AI system unnoticed | Can block deployment |
| **Finance** | Predictable, justified spend | Runaway token costs; unclear ROI | Controls the budget |
| **IT / Platform** | Supportable, standard architecture | One-off system nobody can maintain | Controls the platform |
| **The AI system itself** | — | — | — |

## The conflicts, named

- **Employees vs Information Security.** Employees want the agent to know
  everything; Security wants it scoped to one library. Requirement S1 resolves
  this in Security's favour, and that is a *choice with a cost* — the agent
  will sometimes be unable to answer a legitimate question.
- **Finance vs Engineering.** Rate limits protect budget and degrade user
  experience. Stage 6.5 sets them; Stage 6.7 asks you to defend the setting
  from each seat.
- **People Operations vs Employees.** HR wants fewer tickets; employees want a
  human when it matters. M6's deliberate two-sided target is where this
  tension lives.
- **Everyone vs Legal.** Every useful feature extension moves the system closer
  to the high-risk boundary in `requirements.md`.

## Why the last row is blank

The AI system is not a stakeholder. It has no interests to weigh.

This is stated explicitly because agentic language ("the agent decides,"
"the agent wants") makes it easy to slip into treating the system as a party
to the decision rather than an artifact of it. Every choice here was made by a
person, and accountability sits with people. Governance frameworks insist on
named human owners for exactly this reason.

## RACI for the pilot

| Activity | R | A | C | I |
|---|---|---|---|---|
| Requirements | Architect | People Ops | InfoSec, Legal | Employees |
| Build | Architect | Architect | IT | — |
| Security testing | Architect | InfoSec | — | Legal |
| Go/no-go at pilot exit | People Ops | People Ops | InfoSec, Legal, Finance | All |

In this project you are every letter in every row. Fill it in anyway — noticing
that **A** and **R** are the same person everywhere is itself the finding, and
it is the structural weakness of most solo or small-team AI projects.
