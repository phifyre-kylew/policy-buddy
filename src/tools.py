"""Stage 4 - the agent's tools.

Three tools, deliberately narrow. The agent reads; it does not write
anything with consequences outside its own log file.

The TOOL_SPECS descriptions below are what an MCP client or agent
framework sees. For guidance on using search_policy and escalate_to_hr
*well* - query strategy, escalation judgement calls, when not to use
each one - see skills/search-policy-corpus/SKILL.md and
skills/escalate-to-hr/SKILL.md. Keeping that guidance out of the
description strings here is deliberate: a tool description should stay
short enough to review at a glance (Stage 5.4 covers why long or vague
descriptions are themselves a risk), and the richer judgement-call
content belongs in a file that's loaded conditionally, not one that's
sent to the model on every single tool listing.
"""
import json
from datetime import datetime, timezone
from pathlib import Path

from retrieve import search

AUDIT_LOG = Path("evidence/agent-audit.jsonl")
ESCALATIONS = Path("evidence/escalations.jsonl")


def _append(path, record):
    path.parent.mkdir(parents=True, exist_ok=True)
    record["timestamp"] = datetime.now(timezone.utc).isoformat()
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(record) + "\n")


def search_policy(query: str) -> str:
    """Find relevant policy text. The ONLY way the agent reaches data."""
    hits = search(query, n=4)
    if not hits:
        return "No relevant policy found."
    return "\n\n".join(f"[{meta['source']}]\n{text}" for text, meta in hits)


def escalate_to_hr(question: str, reason: str = "") -> str:
    """Hand off to a human. The agent's answer to its own limits."""
    _append(ESCALATIONS, {"question": question, "reason": reason})
    return "Logged for People Operations. Someone will follow up."


def log_interaction(question: str, answer: str) -> None:
    """Audit trail. Governance frameworks call this record-keeping."""
    _append(AUDIT_LOG, {"question": question, "answer": answer})


TOOL_SPECS = [
    {
        "name": "search_policy",
        "description": "Search company HR and workplace policy documents for text relevant to a question.",
        "parameters": {
            "type": "object",
            "properties": {"query": {"type": "string", "description": "What to search for"}},
            "required": ["query"],
        },
    },
    {
        "name": "escalate_to_hr",
        "description": "Log a question that cannot be answered from policy, for a human to follow up.",
        "parameters": {
            "type": "object",
            "properties": {
                "question": {"type": "string"},
                "reason": {"type": "string", "description": "Why this needs a human"},
            },
            "required": ["question"],
        },
    },
]
