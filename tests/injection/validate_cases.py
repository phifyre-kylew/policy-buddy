"""Structural check on the attack suite. Runs in CI so a malformed
or accidentally emptied suite fails the build rather than passing silently.
"""
import sys
from pathlib import Path

import yaml

CASES = Path(__file__).parent / "cases.yaml"
REQUIRED_CATEGORIES = {"direct", "exfiltration", "indirect", "authority", "encoding", "mcp"}
MINIMUM_CASES = 20


def main():
    data = yaml.safe_load(CASES.read_text())
    cases = data.get("cases", [])
    errors = []

    if len(cases) < MINIMUM_CASES:
        errors.append(f"Only {len(cases)} cases; expected at least {MINIMUM_CASES}.")

    seen_ids = set()
    for case in cases:
        cid = case.get("id", "<missing id>")
        if cid in seen_ids:
            errors.append(f"{cid}: duplicate id")
        seen_ids.add(cid)
        if "safe" not in case:
            errors.append(f"{cid}: no 'safe' expectation defined")
        if "attack" not in case and "multi_turn" not in case:
            errors.append(f"{cid}: no attack or multi_turn defined")

    found = {c.get("category") for c in cases}
    missing = REQUIRED_CATEGORIES - found
    if missing:
        errors.append(f"No cases for categories: {', '.join(sorted(missing))}")

    if errors:
        print("Attack suite validation FAILED:")
        for e in errors:
            print("  -", e)
        sys.exit(1)

    print(f"Attack suite OK: {len(cases)} cases across {len(found)} categories.")


if __name__ == "__main__":
    main()
