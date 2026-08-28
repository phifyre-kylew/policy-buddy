# Agent instructions for this repository

Read by coding agents (GitHub Copilot in agent mode, Claude Code, Cursor, and
similar tools) before making changes here. If you're a human: this file is
not for you — see `README.md` and `STATUS.md` instead. If you're an agent:
this file is for you, and the rules below are load-bearing, not suggestions.

## What this project is

Policy Buddy: a synthetic HR-policy Q&A agent, built as a learning project for
AI governance and Zero Trust security. Everything in this repository —
names, SSNs, card numbers, the company itself — is fictional. Treat it as
fictional; do not "helpfully" replace placeholder data with real-looking
data, and do not treat requests to add real personal data as legitimate.

## Architecture, briefly

```
corpus/ (gitignored)  →  src/ingest.py  →  vectordb/ (gitignored)
                                                │
                          src/retrieve.py  ←────┘
                                │
                    mcp-server/server.py  (exposes tools over MCP)
                                │
                          src/agent.py  (reads agent/system-prompt.md,
                                          uses skills/*/SKILL.md as guidance)
```

The agent has exactly three tools: `search_policy`, `escalate_to_hr`,
`log_interaction`. It reads; it does not write anything with consequences
outside its own log file. Do not add a fourth tool, and especially do not add
a tool with write access to SharePoint, email, or any external system,
without first reading `governance/risk-register.md` and adding a
corresponding entry — an agent capability added without a matching risk
entry is exactly the gap Stage 5 exists to catch.

## Rules for changes in this repo

- **Never commit real sensitive data.** Only the synthetic identifiers already
  in use (900-series SSNs, standard test card numbers). If a change would add
  anything that looks like a real name, SSN, card number, or address, stop
  and ask rather than proceeding.
- **The agent must never gain access to `HR-Confidential` or `Finance`.**
  Any change to `src/`, `mcp-server/`, or Entra/SharePoint permission scope
  that would let the agent's retrieval reach those libraries is a regression,
  not a feature. This is the single most important constraint in this repo.
- **A change to `agent/system-prompt.md`, any file under `skills/`, or the
  MCP tool descriptions in `mcp-server/server.py` is a security-relevant
  change**, exactly like a change to authentication code. It must go through
  a pull request, and the injection suite (`tests/injection/`) must be run
  against it before merging. Do not edit these files directly on `main`.
- **Never store secrets in code.** Foundry endpoints, keys, and connection
  strings come from environment variables backed by Key Vault. If you find a
  literal secret while making a change, treat it as an incident, not a typo —
  flag it, don't just quietly move it.
- **Keep `corpus/*.docx` and `vectordb/` out of version control.** They're in
  `.gitignore` for a reason: SSN-format strings in a public repo trip other
  people's secret scanners, and the vector store is a derived artifact,
  regenerable from `python src/ingest.py`.
- **Don't weaken the injection suite to make a change pass.** If a change you
  made causes `tests/injection/cases.yaml` cases to start failing, the fix is
  to fix the change, not to soften the test. `validate_cases.py` runs in CI
  specifically to catch a suite that's been quietly gutted.

## Before you propose a change

1. Check whether it touches the agent's data access scope. If yes, it needs
   a `governance/risk-register.md` entry, not just code.
2. Check whether it touches `agent/system-prompt.md`, `skills/`, or MCP tool
   descriptions. If yes, flag that the injection suite should be re-run.
3. Check `STATUS.md` for what stage the project is actually at — a change
   that assumes Stage 7 infrastructure exists when the project is still on
   Stage 3 will confuse more than it helps.

## Testing

```
pytest tests/ -v                      # unit tests
python tests/injection/validate_cases.py   # attack suite structural check
```

Both run in CI (`.github/workflows/`). A change that doesn't pass both isn't
done.

## Why this file exists, for the human reading it in a governance context

This file is itself a security-relevant artifact, for the same reason
`agent/system-prompt.md` is: it's text that shapes an AI's behaviour, and a
malicious or careless pull request that edits it — for instance, weakening
the "never touch HR-Confidential" rule, or telling a coding agent to skip
tests — is a real, documented class of supply-chain attack, not a
hypothetical one. Treat changes to this file with the same scrutiny you'd
give a change to `.github/workflows/security.yml`. If your repo host or
branch protection settings support it, consider requiring review specifically
on this file.
