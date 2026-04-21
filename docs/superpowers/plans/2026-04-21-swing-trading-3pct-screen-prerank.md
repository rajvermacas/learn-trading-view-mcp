# Swing Trading 3pct Screen Adaptive Pre-Rank Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the generic pre-rank contract with a schema-specific model that matches the user’s actual Screener columns and scores only from the fields that are truly available.

**Architecture:** Keep the top-level skill concise, move the fixed screen-schema contract into `references/methodology.md`, and lock the behavior with a small unittest that validates the documented contract. The test treats the methodology file as the source of truth because this skill is documentation-driven.

**Tech Stack:** Markdown skill files, Python `unittest`, `logging`, repo verification via `python -m unittest`, `rg`, `sed`, and `wc`

---

### Task 1: Update The Skill Contract

**Files:**
- Modify: `.claude/skills/swing-trading-3pct-screen/SKILL.md`

- [ ] **Step 1: Replace the broader adaptive rule**
Add language that pre-rank depends on the fixed screen schema and fails if any of the four real scoring columns are missing.

- [ ] **Step 2: Add the context-only column rule**
Document that the remaining visible screen columns are kept for context and reporting but do not contribute to `PreRankScore`.

### Task 2: Rewrite The Methodology Pre-Rank Section

**Files:**
- Modify: `.claude/skills/swing-trading-3pct-screen/references/methodology.md`

- [ ] **Step 1: Declare the fixed screen schema**
Write one section that names all ten visible columns exactly as the user sees them.

- [ ] **Step 2: Add fixed scoring inputs and weights**
Document that only `Qtr Profit Var %`, `Qtr Sales Var %`, `ROCE %`, and `3mth return %` feed pre-rank, with explicit weights and penalties.

- [ ] **Step 3: Add context-only column guidance**
Document that `CMP Rs.`, `P/E`, `Mar Cap Rs.Cr.`, `Div Yld %`, `NP Qtr Rs.Cr.`, and `Sales Qtr Rs.Cr.` are visible context fields rather than scoring inputs.

### Task 3: Align Reporting

**Files:**
- Modify: `.claude/skills/swing-trading-3pct-screen/references/reporting-contract.md`

- [ ] **Step 1: Expand `screen-universe.md` requirements**
Require the report to show the fixed screen schema, scoring columns used, context-only columns, penalty flags, and zero-contribution flags.

### Task 4: Add Regression Coverage

**Files:**
- Create: `tests/test_swing_trading_3pct_screen_methodology.py`

- [ ] **Step 1: Write the regression test**
Assert the fixed schema is present, only the four real scoring columns are documented for pre-rank, the broader adaptive language is gone, and the base weights sum to `1.0`.

- [ ] **Step 2: Run verification**
Run `python -m unittest tests.test_swing_trading_3pct_screen_methodology -v` and confirm all assertions pass.
