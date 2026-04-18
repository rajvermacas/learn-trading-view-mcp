# Swing Trading 3pct Screen Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Redesign the `swing-trading-3pct-screen` skill so it performs full-universe fundamental sponsorship ranking first, then ranked technical review with strict sequential TradingView workers, and writes a five-file report set that stays useful under limited technical coverage.

**Architecture:** Keep orchestration rules in `SKILL.md`, move detailed worker contracts and reporting rules into focused reference files, keep the methodology centered on screen-derived sponsorship plus multi-factor stop survivability, and refresh `agents/openai.yaml` so the UI prompt matches the new workflow. The implementation is documentation-first but must still be treated like a behavior change: every touched file must align on execution order, worker handoff rules, and reporting semantics.

**Tech Stack:** Markdown skill files, YAML skill metadata, existing Screener HTML workflow, existing TradingView MCP workflow, `skill-creator` guidance, repo verification via `rg`, `sed`, `wc`, and `git diff`

---

### Task 1: Restructure The Skill Surface

**Files:**
- Modify: `.claude/skills/swing-trading-3pct-screen/SKILL.md`
- Create: `.claude/skills/swing-trading-3pct-screen/references/fundamental-worker-contract.md`
- Create: `.claude/skills/swing-trading-3pct-screen/references/technical-worker-contract.md`
- Create: `.claude/skills/swing-trading-3pct-screen/references/delegation-examples.md`
- Create: `.claude/skills/swing-trading-3pct-screen/references/reporting-contract.md`
- Test: `.claude/skills/swing-trading-3pct-screen/SKILL.md`

- [ ] **Step 1: Confirm the current skill surface is missing the new decomposition**

Run: `find .claude/skills/swing-trading-3pct-screen -maxdepth 2 -type f | sort`
Expected: the current skill has only `SKILL.md`, `agents/openai.yaml`, `references/methodology.md`, and `scripts/ensure_socat.sh`, so the worker-contract and reporting references do not yet exist.

- [ ] **Step 2: Rewrite `SKILL.md` as the orchestration contract**

Replace the top-level workflow so it explicitly says:

```md
## Workflow

1. Fetch the user-provided Screener URL as HTML across all pages.
2. Parse the screen title and visible filters into a compact `screen thesis`.
3. Build the full stock universe and deduplicate it.
4. Dispatch fundamental sub-agents for every stock using bounded parallelism.
5. Collect the full-universe fundamental sponsorship ranking.
6. Dispatch technical sub-agents only after the full ranking exists.
7. Run technical sub-agents strictly one at a time because TradingView MCP is shared mutable state.
8. Respect a user-provided technical coverage limit such as `analyze 12 stocks`; otherwise continue through the whole universe.
9. Write the five-file report set with technically reviewed versus pending status made explicit.
```

Also add a dedicated delegation rule section that says every handoff must include:

```md
- Goal
- Context
- Few-shot examples
- Output schema
```

- [ ] **Step 3: Create the fundamental worker contract reference**

Create `.claude/skills/swing-trading-3pct-screen/references/fundamental-worker-contract.md` with sections shaped like:

```md
# Fundamental Worker Contract

## Goal

Determine whether the stock's current momentum is credibly sponsored by recent business evidence.

## Context Required From Main Agent

- screen title
- visible filters
- screen thesis
- why the stock is in this universe
- phase: `fundamental-ranking`
- coverage mode

## Required Investigation

- recent trigger
- operating evidence
- earnings quality read
- balance-sheet comfort
- catalyst status
- evidence-to-price alignment
- event-risk modifier

## News Rule

Use news only when needed to resolve contradiction, validate a catalyst, or assess near-term event risk.

## Output Schema

- symbol
- screen_context
- recent_trigger
- operating_evidence
- earnings_quality_read
- balance_sheet_comfort
- catalyst_status
- news_escalation
- evidence_to_price_alignment
- sponsorship_label
- confidence
- ranking_reason
```

- [ ] **Step 4: Create the technical worker contract reference**

Create `.claude/skills/swing-trading-3pct-screen/references/technical-worker-contract.md` with sections shaped like:

```md
# Technical Worker Contract

## Goal

Determine whether the stock can defend a practical `2%` to `4%` downside zone around the usual `3%` reference.

## Context Required From Main Agent

- symbol
- screen thesis
- fundamental rank
- sponsorship label
- ranking reason
- coverage mode

## Required Timeframes

- Weekly
- Daily
- 60
- 30
- 15

## Required Factors On Each Relevant Timeframe

- EMA context
- support and resistance zones
- supply and demand zones
- chart patterns
- market structure

## Output Schema

- symbol
- cmp
- 3pct_floor
- practical_stop_zone
- weekly_note
- daily_note
- 60_note
- 30_note
- 15_note
- support_inventory
- resistance_inventory
- entry_zone
- stop_zone
- first_trouble_area
- swing_target
- technical_verdict
- stop_survivability_label
- primary_failure_risk
- ranking_reason
```

- [ ] **Step 5: Create the delegation examples reference**

Create `.claude/skills/swing-trading-3pct-screen/references/delegation-examples.md` with short calibration examples for:

```md
# Delegation Examples

## Fundamental Few-Shots

### Example: Strongly Sponsored
- Input context
- What the worker noticed
- Correct verdict
- Why

### Example: Mixed
...

## Technical Few-Shots

### Example: Best Aligned
- Input context
- What the worker noticed
- Correct verdict
- Why

### Example: Bad EMA-Only Analysis
- Why this reasoning is invalid
```

- [ ] **Step 6: Create the reporting contract reference**

Create `.claude/skills/swing-trading-3pct-screen/references/reporting-contract.md` with file-by-file requirements shaped like:

```md
# Reporting Contract

## README.md
- run date and URL
- screen thesis
- universe size
- coverage mode
- counts
- top previews

## 3pct-ranked-by-stop-safety.md
- Fundamentally Strongest Top Ten
- Technically Strongest Top Ten
- Overall Combined Ranking
- technically reviewed status on every row
```

- [ ] **Step 7: Verify the new skill surface exists**

Run: `find .claude/skills/swing-trading-3pct-screen -maxdepth 2 -type f | sort`
Expected: the new worker-contract, delegation-example, and reporting-contract references appear alongside the existing files.

- [ ] **Step 8: Commit**

```bash
git add .claude/skills/swing-trading-3pct-screen/SKILL.md \
  .claude/skills/swing-trading-3pct-screen/references/fundamental-worker-contract.md \
  .claude/skills/swing-trading-3pct-screen/references/technical-worker-contract.md \
  .claude/skills/swing-trading-3pct-screen/references/delegation-examples.md \
  .claude/skills/swing-trading-3pct-screen/references/reporting-contract.md
git commit -m "docs: restructure swing trading skill contracts"
```

### Task 2: Rewrite The Methodology Around Sponsorship First

**Files:**
- Modify: `.claude/skills/swing-trading-3pct-screen/references/methodology.md`
- Test: `.claude/skills/swing-trading-3pct-screen/references/methodology.md`

- [ ] **Step 1: Verify the old methodology does not express the approved model**

Run: `rg -n "hard 3%|Fundamental Filter|Technical Filter|Produce five files|screen thesis|Sponsorship Label|technical review" .claude/skills/swing-trading-3pct-screen/references/methodology.md`
Expected: matches show older framing and missing terms for screen-thesis extraction, sponsorship-first ranking, and reviewed-versus-pending reporting.

- [ ] **Step 2: Replace the goal and execution model**

Rewrite the top of `methodology.md` so it opens with content shaped like:

```md
## Goal

Find the stocks in a user-provided momentum-biased Screener universe that are most credibly sponsored by recent business evidence and least likely to break a practical `2%` to `4%` stop zone.

## Execution Model

- main agent fetches the screen and extracts the screen thesis
- fundamental analysis runs for the full universe first
- fundamental workers may run in parallel with bounded concurrency
- technical analysis begins only after the full fundamental ranking exists
- technical workers run strictly sequentially because TradingView MCP is shared mutable state
```

- [ ] **Step 3: Add the sponsorship model**

Add sections that define:

```md
## Fundamental Sponsorship Model

- recent trigger
- operating evidence
- earnings quality read
- balance-sheet comfort
- catalyst status
- evidence-to-price alignment
- event-risk modifier

Recommended labels:
- Strongly Sponsored
- Moderately Sponsored
- Mixed
- Weakly Sponsored
```

Also make news explicitly exception-based rather than mandatory per stock.

- [ ] **Step 4: Add the technical multi-factor model**

Replace EMA-heavy language with content shaped like:

```md
## Technical Stop-Survivability Model

Required timeframes:
- Weekly
- Daily
- 60
- 30
- 15

Required factors:
- EMA context
- support and resistance zones
- supply and demand zones
- chart patterns
- market structure

Do not:
- reject from EMA distance alone
- decide from one timeframe alone
- count clustered EMAs as multiple independent supports unless structure confirms them
```

- [ ] **Step 5: Replace the ranking and output sections**

Rewrite the ranking and output structure so they define:

```md
## Ranking Views

1. Fundamental ranking
2. Technical ranking
3. Combined ranking

## Output Structure

Produce five files:
- README.md
- 3pct-selected-and-watchlist.md
- 3pct-rejected.md
- screen-universe.md
- 3pct-ranked-by-stop-safety.md

The ranked file must contain:
1. Fundamentally Strongest Top Ten
2. Technically Strongest Top Ten
3. Overall Combined Ranking
```

Also require explicit `technical review status` when coverage is limited.

- [ ] **Step 6: Verify the methodology now contains the approved model**

Run: `rg -n "screen thesis|Sponsorship Label|Strongly Sponsored|evidence-to-price alignment|support and resistance zones|supply and demand zones|chart patterns|Overall Combined Ranking|technical review status" .claude/skills/swing-trading-3pct-screen/references/methodology.md`
Expected: matches confirm that the methodology now encodes the sponsorship-first, multi-factor, reviewed-versus-pending model.

- [ ] **Step 7: Commit**

```bash
git add .claude/skills/swing-trading-3pct-screen/references/methodology.md
git commit -m "docs: rewrite swing trading methodology"
```

### Task 3: Refresh The Agent Prompt Metadata

**Files:**
- Modify: `.claude/skills/swing-trading-3pct-screen/agents/openai.yaml`
- Test: `.claude/skills/swing-trading-3pct-screen/agents/openai.yaml`

- [ ] **Step 1: Rewrite the prompt metadata to match the new workflow**

Update `agents/openai.yaml` so the `default_prompt` advertises:

```yaml
interface:
  display_name: "Swing Trading 3% Screen"
  short_description: "Rank Screener stocks by sponsorship strength and practical stop survivability"
  default_prompt: "Use $swing-trading-3pct-screen to analyze a user-provided Screener stock screen. Fetch the full HTML universe, extract the screen thesis, run fundamental sponsorship analysis for every stock using bounded-parallel sub-agents, build the full-universe ranking, then run technical analysis in ranked order using one TradingView sub-agent at a time. Pass goal, context, few-shot examples, and output schema into every worker. Judge stop survivability with EMA context, support/resistance zones, supply/demand zones, chart patterns, and market structure across weekly, daily, 60, 30, and 15. Write the five-file report set with reviewed versus pending technical status made explicit."
```

- [ ] **Step 2: Verify the metadata matches the skill**

Run: `rg -n "screen thesis|bounded-parallel|one TradingView sub-agent at a time|goal, context, few-shot examples, and output schema|support/resistance zones|supply/demand zones|reviewed versus pending" .claude/skills/swing-trading-3pct-screen/agents/openai.yaml`
Expected: the prompt metadata now reflects the actual approved execution model.

- [ ] **Step 3: Commit**

```bash
git add .claude/skills/swing-trading-3pct-screen/agents/openai.yaml
git commit -m "docs: align swing trading agent prompt metadata"
```

### Task 4: Verify Cross-File Consistency And Repo Constraints

**Files:**
- Modify: `docs/superpowers/plans/2026-04-18-swing-trading-3pct-screen.md`
- Test: `.claude/skills/swing-trading-3pct-screen/SKILL.md`
- Test: `.claude/skills/swing-trading-3pct-screen/references/methodology.md`
- Test: `.claude/skills/swing-trading-3pct-screen/references/fundamental-worker-contract.md`
- Test: `.claude/skills/swing-trading-3pct-screen/references/technical-worker-contract.md`
- Test: `.claude/skills/swing-trading-3pct-screen/references/delegation-examples.md`
- Test: `.claude/skills/swing-trading-3pct-screen/references/reporting-contract.md`
- Test: `.claude/skills/swing-trading-3pct-screen/agents/openai.yaml`

- [ ] **Step 1: Check file size discipline**

Run: `wc -l .claude/skills/swing-trading-3pct-screen/SKILL.md .claude/skills/swing-trading-3pct-screen/references/methodology.md .claude/skills/swing-trading-3pct-screen/references/fundamental-worker-contract.md .claude/skills/swing-trading-3pct-screen/references/technical-worker-contract.md .claude/skills/swing-trading-3pct-screen/references/delegation-examples.md .claude/skills/swing-trading-3pct-screen/references/reporting-contract.md .claude/skills/swing-trading-3pct-screen/agents/openai.yaml`
Expected: every file stays below `800` lines.

- [ ] **Step 2: Verify the critical contract terms align across files**

Run: `rg -n "screen thesis|Strongly Sponsored|goal|Context|Few-shot|Output schema|support and resistance zones|supply and demand zones|chart patterns|technical review status|Overall Combined Ranking" .claude/skills/swing-trading-3pct-screen/SKILL.md .claude/skills/swing-trading-3pct-screen/references/*.md .claude/skills/swing-trading-3pct-screen/agents/openai.yaml`
Expected: the same worker contract, ranking model, and reporting semantics appear consistently across the skill surface.

- [ ] **Step 3: Verify no stale shortcuts remain**

Run: `rg -n "hard 3% stop|do not use news|EMA 10 only|four files|parallel technical|single-indicator" .claude/skills/swing-trading-3pct-screen/SKILL.md .claude/skills/swing-trading-3pct-screen/references/*.md .claude/skills/swing-trading-3pct-screen/agents/openai.yaml`
Expected: no old wording remains that contradicts the approved redesign.

- [ ] **Step 4: Review the final diff**

Run: `git diff -- .claude/skills/swing-trading-3pct-screen/SKILL.md .claude/skills/swing-trading-3pct-screen/references/methodology.md .claude/skills/swing-trading-3pct-screen/references/fundamental-worker-contract.md .claude/skills/swing-trading-3pct-screen/references/technical-worker-contract.md .claude/skills/swing-trading-3pct-screen/references/delegation-examples.md .claude/skills/swing-trading-3pct-screen/references/reporting-contract.md .claude/skills/swing-trading-3pct-screen/agents/openai.yaml docs/superpowers/plans/2026-04-18-swing-trading-3pct-screen.md`
Expected: the diff shows only the intended skill redesign and its implementation plan.

- [ ] **Step 5: Commit**

```bash
git add docs/superpowers/plans/2026-04-18-swing-trading-3pct-screen.md
git commit -m "docs: refresh swing trading implementation plan"
```
