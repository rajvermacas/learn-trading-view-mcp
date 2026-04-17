# Capabilities

## What This Skill Covers

- Price history retrieval from Yahoo Finance
- Technical indicator calculation with `stockstats`
- Single-indicator and multi-indicator bundle retrieval
- Fundamental company metrics from Yahoo Finance
- Company-specific news retrieval
- Macro or global-news retrieval through curated Yahoo Finance search queries
- Deterministic markdown report assembly written to `docs/market-analysis/`
- Codex-driven final synthesis and recommendation

## What This Skill Does Not Cover

- TradingAgents graph execution
- Multi-agent debates or autonomous role orchestration
- Provider-backed OpenAI, Anthropic, Google, xAI, or OpenRouter runtime
- Upstream TradingAgents CLI behavior
- Persistent reflection-and-memory loops

## Data Source Notes

- `yfinance` can be incomplete or sparse for some tickers, especially on news and fundamentals.
- Fundamental statement filtering by date is best-effort and depends on source timestamps.
- Indicator output can return `null` for warm-up periods, non-trading days, or ticker-specific source alignment issues.
- News payload fields such as `summary` and `published_at` can be `null` even when an article is otherwise valid.

## Output Conventions

- Scripts write machine-readable JSON to stdout unless the script is the markdown report generator.
- Logs go to stderr.
- Do not combine stderr with stdout when saving JSON files.
- Input validation errors raise immediately.
- External-data gaps are surfaced explicitly through availability metadata and empty result sets.
- Do not infer missing company news or missing statement data as positive or negative signals by default.
- `generate_market_report.py` accepts file paths to existing JSON payloads, not inline JSON text.
- The generated markdown file is a draft scaffold that still requires Codex-written synthesis.
- Read the exact payload keys from `references/output-schemas.md`; do not assume alternative keys such as `history`.
