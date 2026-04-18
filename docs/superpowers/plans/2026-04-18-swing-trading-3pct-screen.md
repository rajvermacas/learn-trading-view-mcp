# Swing Trading 3pct Screen Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Update the `swing-trading-3pct-screen` skill so it uses a markdown-only fundamental cache, ranks only from full stock dossiers, refreshes cache entries deterministically, and then runs sequential multi-timeframe technical review.

**Architecture:** Keep `SKILL.md` lean and orchestration-focused. Move cache rules, dossier schema, and worker contracts into focused reference files. Preserve a markdown-only design: `index.md` is a registry, per-stock markdown files are authoritative dossiers, and no helper parsing script or JSON sidecar is introduced.

**Tech Stack:** Markdown skill files, YAML skill metadata, existing Screener HTML workflow, existing TradingView MCP workflow, `skill-creator` guidance, repo verification via `rg`, `sed`, `wc`, and `scripts/quick_validate.py`

---

### Task 1: Refresh The Top-Level Skill Workflow

**Files:**
- Modify: `.claude/skills/swing-trading-3pct-screen/SKILL.md`
- Test: `.claude/skills/swing-trading-3pct-screen/SKILL.md`

- [ ] **Step 1: Inspect the current skill workflow for stale guidance**

Run: `sed -n '1,220p' .claude/skills/swing-trading-3pct-screen/SKILL.md`
Expected: the file still lacks the markdown-only cache workflow, the `index.md` registry role, and the explicit rule that ranking authority comes from stock dossiers rather than the index.

- [ ] **Step 2: Rewrite the workflow section to include cache-first fundamentals**

Replace the workflow portion with content shaped like:

```md
## Workflow

1. Fetch the user-provided Screener URL as HTML across all pages.
2. Extract a compact screen thesis from the visible title, filters, and user intent.
3. Build the full stock universe and deduplicate it.
4. Read `docs/swing-trading/fundamentals/index.md`.
5. Derive which current-universe names are runtime `missing`, `fresh`, `review_due`, and `hard_stale`.
6. Dispatch fundamental sub-agents for all runtime `missing`, all `hard_stale`, and exactly top `3` `review_due`.
7. Reuse cached dossiers for all `fresh` and remaining `review_due`.
8. Build the full-universe fundamental ranking from authoritative stock dossiers only.
9. Run `scripts/ensure_socat.sh` and verify TradingView plus the EMA study setup before chart work begins.
10. Dispatch technical sub-agents only after the ranking exists.
11. Run technical sub-agents strictly one at a time because TradingView MCP is shared mutable state.
12. Respect a user-provided technical coverage count such as `analyze 12 stocks`; otherwise continue through the full universe.
13. Overwrite refreshed stock dossiers, update `index.md`, and write the five-file report set.
```

- [ ] **Step 3: Add the ranking-authority and canonical-write rules**

Add text shaped like:

```md
## Cache Rules

- `index.md` is a registry only.
- The main agent must never rank from `index.md`.
- The main agent must treat a reused cached stock dossier as equivalent to a previously accepted fundamental sub-agent response.
- The main agent must write refreshed stock dossiers in the exact canonical markdown structure defined in `references/fundamental-dossier-contract.md`.
```

- [ ] **Step 4: Update the reference list in the reporting section**

Ensure `SKILL.md` points to these references:

```md
- `references/fundamental-cache-contract.md`
- `references/fundamental-dossier-contract.md`
- `references/fundamental-worker-contract.md`
- `references/technical-worker-contract.md`
- `references/delegation-examples.md`
- `references/reporting-contract.md`
- `references/methodology.md`
```

- [ ] **Step 5: Verify the new workflow language is present**

Run: `rg -n "index.md|review_due|hard_stale|must never rank from `index.md`|canonical markdown" .claude/skills/swing-trading-3pct-screen/SKILL.md`
Expected: matches confirm cache-first workflow, deterministic refresh states, and the dossier-versus-index ranking boundary.

- [ ] **Step 6: Commit**

```bash
git add .claude/skills/swing-trading-3pct-screen/SKILL.md
git commit -m "docs: add cache-first workflow to swing trading skill"
```

### Task 2: Add The Cache And Dossier Contracts

**Files:**
- Create: `.claude/skills/swing-trading-3pct-screen/references/fundamental-cache-contract.md`
- Create: `.claude/skills/swing-trading-3pct-screen/references/fundamental-dossier-contract.md`
- Test: `.claude/skills/swing-trading-3pct-screen/references/fundamental-cache-contract.md`
- Test: `.claude/skills/swing-trading-3pct-screen/references/fundamental-dossier-contract.md`

- [ ] **Step 1: Create the cache contract reference**

Create `.claude/skills/swing-trading-3pct-screen/references/fundamental-cache-contract.md` with sections shaped like:

```md
# Fundamental Cache Contract

## Cache Layout

- `docs/swing-trading/fundamentals/index.md`
- `docs/swing-trading/fundamentals/by-symbol/<SYMBOL>.md`

## Registry Format

| Symbol | Company | Cache File | Last Analyzed On | Next Review On | Hard Stale On |
|---|---|---|---|---|---|

## Runtime Derivation

- no index row -> runtime `missing`
- `today <= Next Review On` -> `fresh`
- `Next Review On < today <= Hard Stale On` -> `review_due`
- `today > Hard Stale On` -> `hard_stale`

## Refresh Rule

- refresh all runtime `missing`
- refresh all `hard_stale`
- refresh exactly top `3` `review_due`

## Review-Due Tie Breaker

1. earlier `Next Review On`
2. earlier `Hard Stale On`
3. lexicographically smaller `Symbol`
```

- [ ] **Step 2: Create the dossier contract reference**

Create `.claude/skills/swing-trading-3pct-screen/references/fundamental-dossier-contract.md` with sections shaped like:

```md
# Fundamental Dossier Contract

## Canonical Shape

1. `Ranking Packet`
2. `Sponsorship Reasoning`

## Ranking Packet

- Symbol
- Company
- Analysis Date
- Screen Thesis Fit
- Sponsorship Verdict
- Confidence

### Comparison Dimensions
- Recent Trigger
- Operating Evidence
- Earnings Quality
- Balance Sheet Comfort
- Catalyst Credibility
- Evidence-to-Price Alignment
- Near-Term Fragility

### Ranking Summary
- Why It Ranks Here
- What Keeps It From Ranking Higher
- What Kind Of Peer Should Rank Above It
- What Kind Of Peer Should Rank Below It

### Refresh Timing
- Next Review On
- Hard Stale On

## Sponsorship Reasoning
- Why Sponsorship Is Present Or Not
- Recent Trigger And What Likely Drove The Move
- Business And Financial Evidence
- Catalyst Context
- Why The Rally Looks Legit Or Fragile For 1-8 Weeks
- Contradictions, Weaknesses, And Open Risks
- Peer Placement Notes
```

- [ ] **Step 3: Add the accept-versus-redo contract to the dossier reference**

Append content shaped like:

```md
## Main-Agent Acceptance

- `accepted`: output follows the canonical structure, covers required dimensions, and is usable for peer ranking
- `redo`: output is malformed, contradictory, too shallow, wrong-stock, or otherwise unusable

No third state is allowed.
```

- [ ] **Step 4: Verify the new references exist and carry the required terms**

Run: `rg -n "review_due|Hard Stale On|Ranking Packet|Sponsorship Reasoning|redo" .claude/skills/swing-trading-3pct-screen/references/fundamental-*.md`
Expected: matches show the date-driven refresh logic and the exact two-section dossier schema.

- [ ] **Step 5: Commit**

```bash
git add .claude/skills/swing-trading-3pct-screen/references/fundamental-cache-contract.md \
  .claude/skills/swing-trading-3pct-screen/references/fundamental-dossier-contract.md
git commit -m "docs: define swing trading cache and dossier contracts"
```

### Task 3: Update Worker Contracts And Few-Shot Guidance

**Files:**
- Modify: `.claude/skills/swing-trading-3pct-screen/references/fundamental-worker-contract.md`
- Modify: `.claude/skills/swing-trading-3pct-screen/references/technical-worker-contract.md`
- Modify: `.claude/skills/swing-trading-3pct-screen/references/delegation-examples.md`
- Test: `.claude/skills/swing-trading-3pct-screen/references/fundamental-worker-contract.md`
- Test: `.claude/skills/swing-trading-3pct-screen/references/technical-worker-contract.md`
- Test: `.claude/skills/swing-trading-3pct-screen/references/delegation-examples.md`

- [ ] **Step 1: Re-read the current worker contracts for mismatch against the new cache design**

Run: `sed -n '1,260p' .claude/skills/swing-trading-3pct-screen/references/fundamental-worker-contract.md && sed -n '1,260p' .claude/skills/swing-trading-3pct-screen/references/technical-worker-contract.md && sed -n '1,260p' .claude/skills/swing-trading-3pct-screen/references/delegation-examples.md`
Expected: the current files still need explicit cache context, canonical dossier output language, and stronger anti-shortcut technical discipline.

- [ ] **Step 2: Rewrite the fundamental worker contract around one-stock dossier output**

Ensure the file includes:

```md
## Context Required From Main Agent

- screen title
- visible filters
- screen thesis
- why the stock is in this universe
- whether this is a first-time analysis or a refresh
- prior analysis date and cached dossier path when this is a refresh

## Output Requirement

Return one canonical stock dossier candidate using the exact structure from `fundamental-dossier-contract.md`.
```

- [ ] **Step 3: Tighten the technical worker contract against EMA-only shortcuts**

Ensure the file includes:

```md
## Decision Discipline

- do not accept or reject from EMA distance alone
- do not accept or reject from one timeframe alone
- do not count clustered EMAs as separate support reasons unless structure confirms them
- do not ignore lower-timeframe breakage when evaluating stop survivability
```

- [ ] **Step 4: Expand few-shot examples to match the final model**

Ensure `delegation-examples.md` includes concise examples for:

```md
- `Strongly Sponsored`
- `Mixed`
- `Weakly Sponsored`
- `News escalation needed`
- `Best Aligned`
- `Near-Valid`
- `Likely To Break`
- `Bad EMA-only analysis`
```

- [ ] **Step 5: Verify the contracts mention goal, context, few-shots, and output schema**

Run: `rg -n "Goal|Context|Few-shot|Output|refresh|EMA-only|Likely To Break" .claude/skills/swing-trading-3pct-screen/references/fundamental-worker-contract.md .claude/skills/swing-trading-3pct-screen/references/technical-worker-contract.md .claude/skills/swing-trading-3pct-screen/references/delegation-examples.md`
Expected: matches confirm that both worker handoffs remain fully specified and aligned with the approved cache-aware flow.

- [ ] **Step 6: Commit**

```bash
git add .claude/skills/swing-trading-3pct-screen/references/fundamental-worker-contract.md \
  .claude/skills/swing-trading-3pct-screen/references/technical-worker-contract.md \
  .claude/skills/swing-trading-3pct-screen/references/delegation-examples.md
git commit -m "docs: align swing trading worker contracts with cache design"
```

### Task 4: Rewrite The Methodology And Reporting References

**Files:**
- Modify: `.claude/skills/swing-trading-3pct-screen/references/methodology.md`
- Modify: `.claude/skills/swing-trading-3pct-screen/references/reporting-contract.md`
- Test: `.claude/skills/swing-trading-3pct-screen/references/methodology.md`
- Test: `.claude/skills/swing-trading-3pct-screen/references/reporting-contract.md`

- [ ] **Step 1: Replace the methodology execution order**

Rewrite the top of `methodology.md` with content shaped like:

```md
## Execution Order

1. Fetch the full Screener universe.
2. Extract the screen thesis.
3. Read `docs/swing-trading/fundamentals/index.md`.
4. Refresh all runtime `missing` and all `hard_stale`.
5. Refresh exactly top `3` `review_due`.
6. Reuse all `fresh` and remaining `review_due`.
7. Build the full-universe fundamental ranking from dossiers only.
8. Run technical review only after the ranking exists.
9. Run technical workers strictly one at a time.
```

- [ ] **Step 2: Add the dossier and cache references to methodology**

Add wording shaped like:

```md
- `index.md` is a registry and freshness surface only
- per-stock markdown dossiers are the authoritative ranking inputs
- the main agent must never rank from index rows alone
```

- [ ] **Step 3: Update the reporting contract for cache-aware but concise outputs**

Ensure `reporting-contract.md` keeps the five-file report set and includes:

```md
## 3pct-ranked-by-stop-safety.md

- Fundamentally Strongest Top Ten
- Technically Strongest Top Ten
- Overall Combined Ranking
- rows must distinguish technically reviewed from pending names

## 3pct-rejected.md

- best support found
- why it was insufficient
- re-check or hard reject
- `technical review not run in this execution` when applicable
```

- [ ] **Step 4: Verify the methodology now reflects the final cache rules**

Run: `rg -n "index.md|review_due|hard_stale|must never rank from index|dossier" .claude/skills/swing-trading-3pct-screen/references/methodology.md .claude/skills/swing-trading-3pct-screen/references/reporting-contract.md`
Expected: matches confirm the refresh workflow, ranking authority, and report semantics are aligned with the final design.

- [ ] **Step 5: Commit**

```bash
git add .claude/skills/swing-trading-3pct-screen/references/methodology.md \
  .claude/skills/swing-trading-3pct-screen/references/reporting-contract.md
git commit -m "docs: update swing trading methodology and reporting"
```

### Task 5: Refresh Skill Metadata And Validate The Skill

**Files:**
- Modify: `.claude/skills/swing-trading-3pct-screen/agents/openai.yaml`
- Test: `.claude/skills/swing-trading-3pct-screen/agents/openai.yaml`
- Test: `.claude/skills/swing-trading-3pct-screen`

- [ ] **Step 1: Update the UI metadata to match the new behavior**

Adjust `.claude/skills/swing-trading-3pct-screen/agents/openai.yaml` so its short description and default prompt mention:

```yaml
display_name: Swing Trading 3pct Screen
short_description: Cache-aware momentum screen analysis with fundamental dossiers first and sequential technical review second.
default_prompt: Screen a Screener.in universe by reusing or refreshing markdown fundamental dossiers, rank the full universe fundamentally, then run sequential multi-timeframe technical review around a practical 2% to 4% stop zone.
```

- [ ] **Step 2: Run quick skill validation**

Run: `scripts/quick_validate.py .claude/skills/swing-trading-3pct-screen`
Expected: validation succeeds with no frontmatter, naming, or YAML errors.

- [ ] **Step 3: Check file sizes stay within the repo constraints**

Run: `wc -l .claude/skills/swing-trading-3pct-screen/SKILL.md .claude/skills/swing-trading-3pct-screen/references/*.md .claude/skills/swing-trading-3pct-screen/agents/openai.yaml`
Expected: every file remains below `800` lines.

- [ ] **Step 4: Spot-check the final surface for stale references**

Run: `rg -n "JSON|index.json|parser script|optional refresh budget|accepted with caution|rank from index" .claude/skills/swing-trading-3pct-screen`
Expected: no stale guidance remains except approved wording such as `must never rank from index`.

- [ ] **Step 5: Commit**

```bash
git add .claude/skills/swing-trading-3pct-screen/agents/openai.yaml \
  .claude/skills/swing-trading-3pct-screen/SKILL.md \
  .claude/skills/swing-trading-3pct-screen/references
git commit -m "docs: finalize swing trading cache-aware skill redesign"
```

## Self-Review

### Spec Coverage

- cache-first fundamental phase: Task 1 and Task 4
- markdown-only cache registry and dossiers: Task 2
- deterministic `review_due` refresh rule with top `3`: Task 2 and Task 4
- main-agent ranking from dossiers only: Task 1, Task 2, and Task 4
- two-section fundamental dossier schema: Task 2 and Task 3
- full-universe fundamental ranking before technicals: Task 1 and Task 4
- sequential multi-timeframe technical review: Task 3 and Task 4
- five-file report contract with reviewed versus pending status: Task 4
- refreshed skill metadata and validation: Task 5

### Placeholder Scan

- No `TBD`, `TODO`, or deferred implementation placeholders remain.
- Each task lists exact files, exact verification commands, and concrete content to write.

### Type Consistency

- refresh states are consistently `fresh`, `review_due`, and `hard_stale`, with runtime `missing`
- ranking authority is consistently `stock dossier`, never `index.md`
- dossier sections are consistently `Ranking Packet` and `Sponsorship Reasoning`
- refresh cadence is consistently `all missing`, `all hard_stale`, and exactly top `3` `review_due`
