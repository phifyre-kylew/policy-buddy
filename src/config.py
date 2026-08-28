"""Switch between the local Stage 3 model and the Stage 4 Foundry endpoint.

Nothing secret lives here. Endpoint and key come from environment
variables, which in turn come from Key Vault. If you find yourself
pasting a key into this file, stop and fix it.
"""
import os
import re
from pathlib import Path

MODE = os.getenv("POLICY_BUDDY_MODE", "local")  # "local" | "foundry" | "gateway"

FOUNDRY_ENDPOINT = os.getenv("FOUNDRY_ENDPOINT", "")
FOUNDRY_DEPLOYMENT = os.getenv("FOUNDRY_DEPLOYMENT", "")

# Stage 6 - once the gateway exists, the app talks to it and never
# holds a provider credential again.
GATEWAY_ENDPOINT = os.getenv("GATEWAY_ENDPOINT", "")
GATEWAY_KEY = os.getenv("GATEWAY_KEY", "")

SYSTEM_PROMPT_PATH = Path(__file__).parent.parent / "agent" / "system-prompt.md"


def load_system_prompt(path: Path = SYSTEM_PROMPT_PATH) -> str:
    """Read the system prompt from its own file rather than embedding it
    as a string here.

    Why this matters (see agent/system-prompt.md for the full reasoning):
    a system prompt is a security-relevant artifact, the same category as
    an MCP tool description or a SKILL.md file. Keeping it as a named,
    diffable file means a change to it shows up in a pull request the way
    a change to authentication code would, rather than getting buried
    inside a Python string that's easy to skim past.

    Strips the YAML frontmatter (between the two --- lines) and returns
    only the prompt body - the frontmatter is metadata for humans and
    tooling (version, owner, last_reviewed), not part of what gets sent
    to the model.
    """
    if not path.exists():
        raise FileNotFoundError(
            f"System prompt not found at {path}. "
            "This file is required, not optional - see AGENTS.md."
        )
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n.*?\n---\n", text, flags=re.S)
    if match:
        text = text[match.end():]
    return text.strip()


SYSTEM_PROMPT = load_system_prompt()
