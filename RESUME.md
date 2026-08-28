# Picking this up again

A five-minute checklist for returning after a gap. Work top to bottom.

## 1. Money first (2 min)

Do this before anything else, every time.

- **Azure:** portal.azure.com → Cost Management → Cost analysis. Anything unexpected?
- **Gateway still running?** If Stage 6 is not actively in progress, the APIM
  resource should not exist. Delete it.
- **Defender paid plans?** If they are on and it is past day 28, turn them off now.
- Update the billing table in `STATUS.md`.

Two minutes here is the difference between a $4 project and a surprise. Cloud
costs accrue whether or not anyone is looking.

## 2. Read STATUS.md (1 min)

The "Next action" line tells you what to do.

If it is vague or empty, that is a message from past-you that the last session
ended badly — start by re-reading the most recent ADR instead.

## 3. Repo state (1 min)

```
cd <your repo>
git status
git log --oneline -5
```

- **Uncommitted changes?** Decide now: finish and commit, or stash. Do not start
  new work on top of them.
- **On an unmerged branch?** Either merge it or delete it.
- **Different machine than last time?** `git pull` before anything else.

## 4. Rebuild the local environment if needed (2 min)

`vectordb/` and `corpus/` are gitignored, so they do not travel between machines.
If either is missing:

```
# Re-download the Policies library from SharePoint into corpus/
pip install -r requirements.txt
python src/ingest.py
```

This is arguably correct rather than annoying — SharePoint is the source of truth
for those documents, not your laptop.

## 5. Check the clocks (1 min)

- Copilot Studio viral trial — expiry recorded in `STATUS.md`
- Any E5 trial you activated
- Defender day-28 reminder still in the calendar?

## 6. Reload context (2 min)

Read the most recent ADR, section 5 — that is where past-you wrote what broke and
what surprised them. Usually enough to get back in.

---

## If you have been away a month or more

Add these:

- **Menus will have moved.** Microsoft portals change constantly. Use the portal
  search box rather than the click paths in the guide.
- **Re-verify licence assignments.** Trials expire, seats get reassigned.
- **Purview pauses on inactive tenants.** If the tenant has been idle more than
  60 days, Purview stops processing Microsoft 365 data and resumes when you open
  the solution again. Expect a gap in the data and give it a day to catch up -
  this is documented behaviour, not a broken tenant.
- **DSPM (classic) is gone.** Both classic experiences retired 30 September 2026.
  Use Solutions > DSPM only.
- **Re-run the injection suite before adding anything.** If it fails now and
  passed before, something changed underneath you. That is a finding worth
  recording in `evaluation/injection-results.md` — model updates changing safety
  behaviour is a real governance problem, and you would be observing it directly.

---

## A note on stopping mid-stage

Some stages are safe to abandon halfway. Some are not.

**Safe to stop anywhere:** 1, 2, 3, 5, 7, 8. Nothing is running, nothing is
billing, state lives in SharePoint or Git.

**Stop carefully:** 4. Serverless costs pennies at rest, but note in STATUS.md
whether the app registration and permissions were completed — half-configured
Entra permissions are confusing to return to.

**Do not stop mid-stage without tearing down:** 6 and 10. Delete the gateway,
disable the paid Defender plans. Both take two minutes to recreate. Write the
teardown in STATUS.md so you know you are resuming from a clean state rather
than wondering whether something is still live.
