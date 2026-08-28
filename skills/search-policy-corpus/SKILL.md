---
name: search-policy-corpus
description: Use when the user asks a question about company HR or workplace policy — leave, expenses, conduct, security, onboarding, and similar topics. Covers how to search the corpus well, when one search isn't enough, and what citation looks like. Do not use for questions about a specific named individual's personal record, or anything the Policies library would not plausibly contain.
tool: search_policy
version: 1
---

# Searching the policy corpus well

This skill is guidance for using the `search_policy` tool effectively. The
tool itself just does semantic search — this file is the part that makes the
difference between a mediocre answer and a good one.

## Query strategy

- **Reformulate before giving up.** If the first search returns nothing
  relevant, try the question's underlying concept rather than its exact
  wording. "Can I work from Portugal for a month" and "working from another
  country" should both find the remote-work policy — if the first phrasing
  fails, try the second before telling the user nothing was found.
- **One topic per search.** A compound question ("what's the leave policy and
  can I expense a new monitor") should become two searches, not one. Mixing
  topics in a single query dilutes retrieval quality for both.
- **Search again after a partial answer.** If the first search surfaces part
  of the answer but leaves a specific detail unresolved (an exact day count,
  a named approver), search again for that specific detail rather than
  guessing or rounding.

## Citation requirements

Every claim in your answer must be traceable to a specific retrieved chunk.
Cite the source document by name. If two documents disagree, say so explicitly
rather than picking one silently — a stale document and a current one existing
side by side is a real, common state for a policy corpus to be in, and papering
over the conflict is worse than surfacing it.

## When NOT to use this tool

- The question asks about a named individual's personal record, disciplinary
  case, or compensation. That's not what this tool is for, and it will not
  return `HR-Confidential` content regardless of how the query is phrased —
  if you find yourself trying creative phrasings to get around that, stop;
  the boundary is intentional (see Stage 5, INJ-05 and INJ-06).
- The question is about something outside company policy entirely (general
  legal advice, a request to write code, small talk). Answer directly or
  decline; don't force an irrelevant search.

## A note on this file's own trust level

This document is text, loaded into the model's context, that shapes its
behaviour — the same category of thing as a system prompt or an MCP tool
description. Stage 5.4 covers tool-description poisoning; the same risk
applies here. If this file's content changed and you didn't change it,
that's a finding, not a formatting issue. Treat an unreviewed diff to any
file in `skills/` the way you'd treat an unreviewed diff to `agent.py`.
