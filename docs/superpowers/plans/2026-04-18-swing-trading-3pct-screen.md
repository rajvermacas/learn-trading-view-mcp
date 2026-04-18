# Swing Trading 3pct Screen Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Redesign the `swing-trading-3pct-screen` skill so it evaluates practical `2%` to `4%` stop survivability, requires multi-timeframe structural reasoning, analyzes each stock through its own sequential sub-agent, and outputs a five-file report set including a structured ranked-universe file.

**Architecture:** The change is documentation-driven and limited to the skill entrypoint, its methodology reference, and the agent prompt metadata. The skill file will describe the workflow, sequential sub-agent orchestration, and required output artifacts. The methodology file will define the decision model, ranking logic, rejection discipline, and concise reporting format. The agent prompt metadata will reinforce the same execution contract.

**Tech Stack:** Markdown skill files, existing TradingView MCP workflow, existing Screener HTML workflow, git verification commands

---

### Task 1: Rewrite The Skill Contract

**Files:**
- Modify: `.claude/skills/swing-trading-3pct-screen/SKILL.md`
- Test: `rg -n "2%|4%|3pct-ranked-by-stop-safety|single-indicator|sub-agent|sequential|parallel" .claude/skills/swing-trading-3pct-screen/SKILL.md`

- [ ] **Step 1: Write the failing expectation list**

Create a local checklist for the missing contract items:

```text
- hard 3% wording still present as a binary rule
- report output still lists 4 files
- no ranked-universe file requirement
- no explicit ban on single-indicator rejection logic
- no explicit sequential per-stock sub-agent contract
- no requirement for concise but complete reasoning
```

- [ ] **Step 2: Run grep to verify the old contract is still present**

Run: `rg -n "hard 3%|four files|3% rule|3pct-ranked-by-stop-safety|extended by pattern|sub-agent|parallel" .claude/skills/swing-trading-3pct-screen/SKILL.md`
Expected: matches show the old binary framing and missing ranked file references

- [ ] **Step 3: Rewrite the skill file**

Replace the old wording with content shaped like:

```md
## Overview

Use this skill for screening Indian stocks from Screener.in and ranking them by multi-timeframe stop survivability. Keep `3%` as the central reference, but evaluate a practical `2%` to `4%` downside zone instead of using a rigid binary cutoff.

## Workflow

7. Dispatch one isolated sub-agent per stock after universe fetch and setup verification.
8. Run those stock-analysis sub-agents sequentially, never in parallel, because TradingView MCP chart state is shared.
9. Require each stock sub-agent to analyze weekly, daily, `60`, `30`, and `15` for its assigned ticker only.
10. Build a market-structure map using both structural support and EMA support.
11. Rank the full universe from least likely to most likely to break the practical stop zone.
12. Write the five-file markdown report set inside the timestamped directory.

## TradingView Rules

- Do not reject a name from one indicator or one timeframe alone.
- Do not use blanket extrapolation such as "extended by pattern" without minimum direct chart evidence.
- Never run stock-analysis sub-agents in parallel against TradingView MCP.
- Treat supports slightly above or slightly below the exact `3% Floor` as valid context when the broader `2%` to `4%` stop zone is structurally defendable.
```

- [ ] **Step 4: Run grep to verify the new contract exists**

Run: `rg -n "2%|4%|3pct-ranked-by-stop-safety|Do not reject a name from one indicator|sub-agent|sequential|parallel" .claude/skills/swing-trading-3pct-screen/SKILL.md`
Expected: matches confirm the new stop-band framing, ranked file requirement, ban on one-indicator rejection, and sequential sub-agent contract

- [ ] **Step 5: Commit**

```bash
git add .claude/skills/swing-trading-3pct-screen/SKILL.md
git commit -m "docs: redesign swing trading skill contract"
```

### Task 2: Rewrite The Methodology Reference

**Files:**
- Modify: `.claude/skills/swing-trading-3pct-screen/references/methodology.md`
- Test: `rg -n "2%|4%|Overall Combined Ranking|Fundamentally Strongest Top Ten|Technically Strongest Top Ten|Reject|sub-agent|sequential|parallel" .claude/skills/swing-trading-3pct-screen/references/methodology.md`

- [ ] **Step 1: Write the failing expectation list**

Create a local checklist for the methodology gaps:

```text
- ranking logic still keyed to exact 3% floor only
- output structure still lists 4 files
- no three-section definition for the ranked file
- rejection criteria allow over-reliance on moving averages
- writing style does not force concise, information-dense output
- no execution contract forcing sequential one-stock-per-sub-agent analysis
```

- [ ] **Step 2: Run grep to verify the old methodology wording**

Run: `rg -n "inside 3%|Produce four files|Explain why each chosen setup is less likely than peers to break 3%|Reject:|sub-agent|parallel" .claude/skills/swing-trading-3pct-screen/references/methodology.md`
Expected: matches confirm the old strict-floor phrasing and four-file output contract

- [ ] **Step 3: Rewrite the methodology file**

Replace the old methodology with content shaped like:

```md
## Goal

Find the stocks in a Screener.in universe that are fundamentally strong and least likely to break a practical `2%` to `4%` stop zone around the usual `3%` reference.

## Execution Model

- Main agent fetches the universe and verifies chart setup once.
- Each stock gets its own analysis sub-agent.
- Stock-analysis sub-agents run strictly sequentially, never in parallel.
- TradingView MCP chart state is shared, so parallel workers are invalid.

## Technical Filter

Selected now:
- structure is defendable around the stop zone now
- support case includes structural references plus EMA references

Watch only:
- support is close, but entry or confirmation is not clean enough yet

Reject for now:
- no credible support map near the stop zone
- support depends mostly on duplicate EMAs
- lower timeframes show an air pocket into the stop area
- rejection must cite the failing timeframe or structure issue

## Output Structure

Produce five files inside the timestamped directory:
- `README.md`
- `3pct-selected-and-watchlist.md`
- `3pct-rejected.md`
- `screen-universe.md`
- `3pct-ranked-by-stop-safety.md`

The ranked file must contain:
1. `Fundamentally Strongest Top Ten`
2. `Technically Strongest Top Ten`
3. `Overall Combined Ranking`
```

- [ ] **Step 4: Run grep to verify the new methodology exists**

Run: `rg -n "2%|4%|Produce five files|Fundamentally Strongest Top Ten|Technically Strongest Top Ten|Overall Combined Ranking|Reject for now|sub-agent|sequential|parallel" .claude/skills/swing-trading-3pct-screen/references/methodology.md`
Expected: matches confirm the practical stop-zone model, structured ranked-file contract, and sequential sub-agent execution model

- [ ] **Step 5: Commit**

```bash
git add .claude/skills/swing-trading-3pct-screen/references/methodology.md
git commit -m "docs: update swing trading methodology"
```

### Task 3: Update Agent Prompt Metadata

**Files:**
- Modify: `.claude/skills/swing-trading-3pct-screen/agents/openai.yaml`
- Test: `rg -n "hard 3%|2% to 4%|sub-agent|sequential|parallel|five-file" .claude/skills/swing-trading-3pct-screen/agents/openai.yaml`

- [ ] **Step 1: Rewrite the prompt metadata**

Update the display metadata so it no longer advertises a hard `3%` stop and instead reinforces:

- practical `2%` to `4%` stop-zone evaluation
- per-stock sub-agent analysis
- sequential execution only
- final five-file report synthesis

- [ ] **Step 2: Verify the prompt metadata**

Run: `rg -n "2% to 4%|sub-agent|sequential|parallel|five-file" .claude/skills/swing-trading-3pct-screen/agents/openai.yaml`
Expected: the agent prompt metadata matches the redesigned workflow

- [ ] **Step 3: Commit**

```bash
git add .claude/skills/swing-trading-3pct-screen/agents/openai.yaml
git commit -m "docs: align swing trading agent prompt"
```

### Task 4: Verify Consistency And Repo Constraints

**Files:**
- Modify: `docs/superpowers/plans/2026-04-18-swing-trading-3pct-screen.md`
- Test: `.claude/skills/swing-trading-3pct-screen/SKILL.md`
- Test: `.claude/skills/swing-trading-3pct-screen/references/methodology.md`
- Test: `.claude/skills/swing-trading-3pct-screen/agents/openai.yaml`

- [ ] **Step 1: Check file sizes**

Run: `wc -l .claude/skills/swing-trading-3pct-screen/SKILL.md .claude/skills/swing-trading-3pct-screen/references/methodology.md .claude/skills/swing-trading-3pct-screen/agents/openai.yaml`
Expected: all files remain below `800` lines

- [ ] **Step 2: Check required deliverables are aligned**

Run: `rg -n "3pct-ranked-by-stop-safety|Fundamentally Strongest Top Ten|Technically Strongest Top Ten|Overall Combined Ranking|sub-agent|sequential|parallel" .claude/skills/swing-trading-3pct-screen/SKILL.md .claude/skills/swing-trading-3pct-screen/references/methodology.md .claude/skills/swing-trading-3pct-screen/agents/openai.yaml`
Expected: all files reference the same ranking contract and sequential sub-agent model

- [ ] **Step 3: Check for old binary-rule leftovers**

Run: `rg -n "hard 3% stop|Produce four files|extended by pattern|inside 3% below CMP|parallel workers are valid" .claude/skills/swing-trading-3pct-screen/SKILL.md .claude/skills/swing-trading-3pct-screen/references/methodology.md .claude/skills/swing-trading-3pct-screen/agents/openai.yaml`
Expected: no misleading old-rule leftovers that conflict with the redesign

- [ ] **Step 4: Review git diff**

Run: `git diff -- .claude/skills/swing-trading-3pct-screen/SKILL.md .claude/skills/swing-trading-3pct-screen/references/methodology.md .claude/skills/swing-trading-3pct-screen/agents/openai.yaml docs/superpowers/plans/2026-04-18-swing-trading-3pct-screen.md`
Expected: diff shows only the intended redesign of skill behavior, sequential delegation contract, and reporting rules

- [ ] **Step 5: Commit**

```bash
git add .claude/skills/swing-trading-3pct-screen/SKILL.md .claude/skills/swing-trading-3pct-screen/references/methodology.md .claude/skills/swing-trading-3pct-screen/agents/openai.yaml docs/superpowers/plans/2026-04-18-swing-trading-3pct-screen.md
git commit -m "docs: finalize swing trading skill redesign"
```
