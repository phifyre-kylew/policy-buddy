# FinOps for AI — Policy Buddy

Completed at Stage 6.7. This is where "keep costs low" turns from a habit into
a measured practice, using the FinOps Foundation's Inform / Optimize / Operate
lifecycle and its 2026 AI technology category.

## Why this is here

AI spend doesn't behave like ordinary cloud spend. It's consumption-based per
token rather than per provisioned hour, harder to forecast, and capable of
moving fast in ways a monthly cloud bill usually doesn't. The FinOps Foundation
treats AI as a distinct technology category for exactly this reason — it needs
enough governance to catch runaway cost without slowing down the experimentation
that makes AI worth using in the first place.

## Resource tagging

Applied in the Azure portal to every resource in `policy-buddy-rg`:

| Tag | Value |
|---|---|
| `project` | `policy-buddy` |
| `stage` | (stage number that created the resource) |
| `owner` | |
| `environment` | `learning` |

This is the allocation mechanism. In a real organisation it's what makes
chargeback or showback possible — attributing shared cloud spend back to the
team or product that caused it. One team, one product here, but the mechanism
is identical at any scale.

## Cost per interaction

```
cost per interaction = (token cost this period) / (agent interactions this period)
```

Interaction count comes from `evidence/agent-audit.jsonl` (written by
`log_interaction` since Stage 4). Token cost comes from Application Insights,
grouped by the `stage` tag.

| Date | Period | Token cost | Interactions | Cost per interaction | Notes |
|---|---|---|---|---|---|
| | | | | | |

**Recompute this after every Stage 5 mitigation.** Content filtering and output
filtering both consume tokens, so "more secure" and "more expensive per
interaction" move together. A governance decision that ignores that tradeoff is
an incomplete one — record what each mitigation cost, not just whether it
worked.

| Mitigation added | Cost per interaction before | After | Delta |
|---|---|---|---|
| Content filter | | | |
| Output filter | | | |
| Least privilege scoping | | | |
| Prompt hardening | | | |

## Forecast (deliberately naive)

Project cost-per-interaction against a made-up user count:

| Assumed users | Assumed interactions/user/month | Projected monthly cost |
|---|---|---|
| 500 | | |

**Why this forecast is almost certainly wrong** — write your own reasoning here.
Starting points: usage isn't linear with headcount, a viral internal moment
could spike volume tenfold in a day, and a prompt injection loop (Stage 5)
could in principle burn tokens without limit if rate limiting fails. The value
of doing this isn't the number — it's noticing that AI cost forecasting breaks
the assumptions traditional cloud forecasting relies on.

## The three hats

A real FinOps practice has separate Engineering, Finance, and Leadership
personas in tension with each other. You're one person — write one sentence
from each seat anyway. Holding several legitimate, competing interests in mind
at once instead of collapsing them into your own default view is most of what
governance work actually is.

**As Finance** — would you approve this spend, given what it's measured to cost?

**As Engineering** — would you accept this rate limit, given what you need to
build and test?

**As Leadership** — would you fund another quarter of this, given what you've
learned so far?

## FinOps lifecycle applied to this project

| Phase | What it looked like here |
|---|---|
| **Inform** | Budget alerts (Stage 4), licence inventory check (Stage 1), gateway telemetry (Stage 6) |
| **Optimize** | Serverless not provisioned, monthly not annual commitment, reused licences not new ones, smallest capable model |
| **Operate** | Stage 6 and Stage 10 deletion reminders, `STATUS.md` billing table, day-28 Defender disable |

## Owner

## Review date
