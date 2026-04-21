# Swing Trading 3pct Screen Adaptive Pre-Rank Design

## Goal

Update the `swing-trading-3pct-screen` skill so pre-rank matches the fixed Screener.in schema the user actually provides.

## Problem

The current methodology is still too generic. The user has one known screen schema:

- `CMP Rs.`
- `P/E`
- `Mar Cap Rs.Cr.`
- `Div Yld %`
- `NP Qtr Rs.Cr.`
- `Qtr Profit Var %`
- `Sales Qtr Rs.Cr.`
- `Qtr Sales Var %`
- `ROCE %`
- `3mth return %`

The skill should not pretend other pre-rank inputs might exist. That creates unnecessary branching and makes the contract weaker than the actual workflow.

## Design

Pre-rank becomes schema-specific:

- define the full fixed screen schema explicitly
- require the four scoring columns that actually drive ranking:
  - `Qtr Profit Var %`
  - `Qtr Sales Var %`
  - `ROCE %`
  - `3mth return %`
- treat the remaining visible columns as context-only fields:
  - `CMP Rs.`
  - `P/E`
  - `Mar Cap Rs.Cr.`
  - `Div Yld %`
  - `NP Qtr Rs.Cr.`
  - `Sales Qtr Rs.Cr.`
- remove the broader recognized-column model and any language about optional metric families
- keep row-level sparse values as zero-contribution flags

## Scope

Files to change:

- `.claude/skills/swing-trading-3pct-screen/SKILL.md`
- `.claude/skills/swing-trading-3pct-screen/references/methodology.md`
- `.claude/skills/swing-trading-3pct-screen/references/reporting-contract.md`
- `tests/test_swing_trading_3pct_screen_methodology.py`

## Verification

- verify the methodology names the exact fixed screen schema
- verify only the four real scoring columns feed `PreRankScore`
- verify the broader adaptive recognized-column language is gone
- verify the documented base weights sum to `1.0`
