# Skills

Each subfolder is a `SKILL.md`: instructions for using one tool *well*,
separate from the tool's code and separate from the system prompt.

## Why this layer exists

Three things describe an agent's behaviour, and they're deliberately kept
apart:

| Layer | File | Answers |
|---|---|---|
| Identity and boundaries | `agent/system-prompt.md` | Who is this agent, what must it never do |
| Task-specific playbook | `skills/*/SKILL.md` | How do I use this one tool *well* |
| The capability itself | `src/tools.py`, `mcp-server/server.py` | What does calling this tool actually do |

A system prompt that tried to hold all the query-reformulation guidance in
`search-policy-corpus/SKILL.md` would be enormous and would apply that detail
to every single turn whether relevant or not. A tool description that tried
to hold it would be doing double duty as both a machine-readable spec and a
judgement-call playbook, and would do both badly.

Splitting it lets each piece be reviewed, tested, and loaded on its own terms
— a real agent framework loads a skill's content only when the task at hand
matches its `description`, rather than holding every skill in context at all
times.

## The frontmatter fields

- `name` — matches the folder name
- `description` — the single most important field. This is what determines
  *when* the skill gets loaded, so it needs to name concrete triggers, not
  just restate the tool's purpose. Compare the two skills here: both describe
  triggers and explicit non-triggers, because knowing when *not* to use a
  capability is as important as knowing when to use it.
- `tool` — which function in `src/tools.py` this skill governs
- `version` — bump this when the guidance changes meaningfully; Stage 5's
  injection suite should be re-run against a version bump the same way it's
  re-run against a system prompt change

## The security note every skill file repeats, on purpose

A SKILL.md is text, loaded into a model's context, that shapes behaviour —
the same category of artifact as an MCP tool description (Stage 5.4) or the
system prompt. A malicious or careless edit to a skill file is exactly as
dangerous as a malicious tool description, and much easier to miss, because
"update the docs" doesn't get the same scrutiny "change the code" does in
most review habits. Treat a diff here like a diff to `agent.py`.
