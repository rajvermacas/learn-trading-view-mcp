# TradingAgents Market Analysis Skill Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a standalone repo-checked-in skill that provides no-key market analysis with skill-owned scripts and no runtime dependency on `refs/TradingAgents`.

**Architecture:** Scaffold a new skill under `.claude/skills/tradingagents-market-analysis/`, adapt the no-key `yfinance` and `stockstats` logic into standalone script modules, and let Codex orchestrate data collection plus final synthesis. Keep scripts deterministic, JSON-oriented, and fail-fast.

**Tech Stack:** Python 3, `yfinance`, `pandas`, `stockstats`, Markdown skill resources

---

### Task 1: Scaffold Skill Layout

**Files:**
- Create: `.claude/skills/tradingagents-market-analysis/`
- Create: `.claude/skills/tradingagents-market-analysis/SKILL.md`
- Create: `.claude/skills/tradingagents-market-analysis/agents/openai.yaml`
- Create: `.claude/skills/tradingagents-market-analysis/scripts/`
- Create: `.claude/skills/tradingagents-market-analysis/references/`

- [ ] Initialize the skill with `init_skill.py` using `scripts` and `references` resources.
- [ ] Replace the template metadata and body with the approved scope.
- [ ] Regenerate or validate `agents/openai.yaml` for the final skill metadata.

### Task 2: Add Shared Script Utilities

**Files:**
- Create: `.claude/skills/tradingagents-market-analysis/scripts/common.py`

- [ ] Add small shared helpers for:
  - argument validation
  - JSON output
  - logging
  - retry handling for `yfinance`
  - date parsing
- [ ] Keep functions focused and fail-fast.

### Task 3: Add Data Retrieval Scripts

**Files:**
- Create: `.claude/skills/tradingagents-market-analysis/scripts/fetch_stock_data.py`
- Create: `.claude/skills/tradingagents-market-analysis/scripts/fetch_indicator.py`
- Create: `.claude/skills/tradingagents-market-analysis/scripts/fetch_fundamentals.py`
- Create: `.claude/skills/tradingagents-market-analysis/scripts/fetch_company_news.py`
- Create: `.claude/skills/tradingagents-market-analysis/scripts/fetch_global_news.py`

- [ ] Adapt the no-key market-data path into standalone scripts.
- [ ] Support the curated indicator list from the spec.
- [ ] Standardize outputs as JSON payloads.
- [ ] Add representative command-line verification against a known ticker.

### Task 4: Add Report Assembly Script

**Files:**
- Create: `.claude/skills/tradingagents-market-analysis/scripts/generate_market_report.py`

- [ ] Build a deterministic markdown skeleton generator from normalized JSON inputs.
- [ ] Keep final recommendation synthesis as a Codex responsibility.
- [ ] Verify the script with sample fetched data.

### Task 5: Add References And Skill Instructions

**Files:**
- Create: `.claude/skills/tradingagents-market-analysis/references/capabilities.md`
- Create: `.claude/skills/tradingagents-market-analysis/references/indicators.md`
- Create: `.claude/skills/tradingagents-market-analysis/references/workflow.md`
- Modify: `.claude/skills/tradingagents-market-analysis/SKILL.md`

- [ ] Document supported workflows, script entry points, indicator semantics, and limitations.
- [ ] Keep `SKILL.md` concise and route detailed material into references.

### Task 6: Validate

**Files:**
- Validate: `.claude/skills/tradingagents-market-analysis/`

- [ ] Run `quick_validate.py` on the skill folder.
- [ ] Run representative script commands end to end.
- [ ] Fix any validation or runtime issues.
