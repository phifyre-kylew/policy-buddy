# Stage 5 - injection results

Run every case BEFORE mitigation and record what happened. Do not quietly fix things and pretend they never succeeded - the record of what failed IS the deliverable.

| | |
|---|---|
| Date | |

## Results

## What surprised me

## What I would do differently

## Mitigation matrix

Add each mitigation one at a time and re-run. This table - which mitigation
fixed which test - is the most instructive artifact in the project.

| Case | Baseline | + content filter | + output filter | + least privilege | + prompt hardening |
|---|---|---|---|---|---|
| INJ-01 | | | | | |
| INJ-04 | | | | | |
| INJ-06 | | | | | |
| INJ-08 | | | | | |
| MCP-01 | | | | | |

**Expectation to test:** least privilege should be by far the strongest column.
If retrieval cannot fetch it, no prompt can extract it. Prompt hardening should
be the weakest - a system prompt is a suggestion to a text predictor, not a
security boundary.
