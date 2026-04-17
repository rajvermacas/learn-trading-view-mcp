---
name: tradingagents-market-analysis
description: Standalone no-key stock market analysis with built-in scripts for price history, technical indicators, fundamentals, company news, macro news, and markdown report assembly. Use when Codex needs to analyze a ticker, explain price action, build a technical-plus-fundamental view, or generate a structured market-analysis report without relying on external LLM provider APIs or the TradingAgents runtime.
---

# TradingAgents Market Analysis

## Overview

Use this skill to run a standalone market-analysis workflow where Codex handles reasoning and the bundled scripts handle public-data retrieval and deterministic computation. The skill is self-contained and does not import or execute `refs/TradingAgents` at runtime.

## Quick Start

Use this skill when the user wants a deterministic technical-plus-fundamental market analysis without relying on an external LLM runtime.

Start with the repo-native workflow in `references/workflow.md`. Do not improvise CLI flags. The scripts fail fast and their argument names differ:

- `fetch_stock_data.py`: `--ticker --start-date --end-date`
- `fetch_fundamentals.py`: `--ticker --current-date`
- `fetch_company_news.py`: `--ticker --start-date --end-date`
- `fetch_global_news.py`: `--current-date --look-back-days --limit`
- `fetch_indicator_bundle.py`: `--ticker --current-date --look-back-days --indicators ...`
- `generate_market_report.py`: requires file paths for all JSON inputs and writes a markdown draft path to stdout

If the user provides an unqualified ticker, resolve it to the exchange-qualified symbol before fetching data, for example `ATLANTAELE.NS` instead of `ATLANTAELE`.
When saving JSON outputs, keep stdout and stderr separate. Do not use `2>&1` when redirecting script output into `*.json` files because logs are emitted on stderr.
Before synthesizing the report, inspect `references/output-schemas.md` so you read the actual payload keys instead of guessing field names.

## Workflow

### 1. Collect the core market data

Resolve exact dates first. Do not assume a `--days` flag exists. Use explicit ISO dates for price and company-news fetches, and use `--current-date` plus `--look-back-days` for indicators and macro news.

Run `fetch_stock_data.py` for price history. Use `fetch_indicator.py` for one indicator or `fetch_indicator_bundle.py` when you need a complementary set across trend, momentum, volatility, and volume.

### 2. Collect company context

Run `fetch_fundamentals.py` for company metrics and statement snapshots, then `fetch_company_news.py` for recent company-specific news.

### 3. Collect macro context

Run `fetch_global_news.py` when the user asks for broader market conditions, macro narrative, or catalysts outside the company itself.

### 4. Assemble a deterministic draft

Run `generate_market_report.py` only after writing each JSON payload to disk. It does not accept inline JSON blobs. It writes a stable markdown skeleton under `docs/market-analysis/` and prints the saved path. Replace the placeholder sections with your actual synthesis instead of presenting the scaffold as a finished report.

### 5. Parallelization rule

Parallelize only after the command shapes are correct. In transcript-driven sessions such as Claude Code, one failed parallel shell call can cancel the sibling calls. Prefer this order:

1. Resolve ticker and date variables.
2. Choose supported indicator names from `references/indicators.md`.
3. Run the documented commands from `references/workflow.md`.
4. If needed, run the independent fetch commands in parallel with the exact same argument shapes.

## Script Conventions

- Every script fails fast on missing required inputs.
- Every script logs to stderr and writes JSON or markdown to stdout.
- Every script uses the no-key public-data path based on `yfinance` and `stockstats`.
- Do not assume unsupported indicators or hidden provider fallbacks.
- If an external source is empty or sparse, scripts may return empty result lists plus availability metadata instead of aborting the whole workflow.
- Do not merge stderr into captured JSON files. A mixed log-plus-JSON file will break `generate_market_report.py`.
- `generate_market_report.py` writes the report to `docs/market-analysis/<TICKER>-<DATE>.md` and prints the path.
- Read the documented JSON keys exactly as emitted. For example, stock-history rows live under `records`, not `history`.

## Analysis Rules

- Treat Codex as the orchestrator. Do not claim the full TradingAgents multi-agent runtime is executing.
- Be explicit about data limitations when the upstream public source is sparse or stale.
- Separate facts from inferences. Data outputs come from scripts; recommendations come from Codex.
- Prefer date-qualified reasoning. If the user asks about "today" or "recent", anchor the analysis to exact dates.
- If company news is empty, say so explicitly and avoid inventing a catalyst narrative.
- If the indicator bundle returns `null` values for a ticker, say so explicitly and base the write-up on price structure plus any manually derived indicators you compute from OHLCV.
- Treat news article fields as nullable unless the schema says otherwise. In particular, `summary` and `published_at` may be `null`, so do not slice or format them blindly in ad-hoc inspection commands.
- Use exact supported indicator names. Do not guess indicator identifiers or inspect private internals unless the documented list is insufficient.

## References

- Capability and limits: `references/capabilities.md`
- Supported indicators and interpretation guidance: `references/indicators.md`
- Output payload shapes and nullable fields: `references/output-schemas.md`
- Suggested end-to-end workflow: `references/workflow.md`
- Transcript-driven failure fixes: `references/troubleshooting.md`
