# TradingAgents Market Analysis Skill Design

## Goal

Build a standalone skill at `.claude/skills/tradingagents-market-analysis/` that gives Codex a reusable, no-extra-key market-analysis workflow. The skill must not depend on `refs/TradingAgents` at runtime. Codex will be the reasoning/orchestration layer; bundled scripts will handle network calls and deterministic computation.

## User-Facing Outcome

The skill should let a user ask for market analysis on a ticker and receive:

- Technical analysis using supported indicators
- Fundamental analysis from public company data
- Company news summary
- Global or macro news summary
- A structured final report with recommendation and risk framing

The skill does not need to preserve TradingAgents' multi-agent runtime, CLI, or provider-backed graph behavior. The user accepts Codex as the orchestrator as long as the core analysis outcome remains covered.

## Scope

In scope:

- Standalone skill checked into this repo under `.claude/skills/`
- Skill-owned scripts for:
  - stock history retrieval
  - indicator retrieval
  - fundamentals retrieval
  - company news retrieval
  - global news retrieval
  - report generation from fetched data
- Skill references documenting:
  - supported indicators
  - script entry points
  - workflow and limits
  - analyst-style interpretation heuristics adapted from TradingAgents
- `agents/openai.yaml`
- Basic validation of script behavior and skill structure

Out of scope:

- Runtime imports from `refs/TradingAgents`
- LangGraph graph execution
- Multi-agent debate orchestration
- Provider-backed LLM clients
- Upstream CLI parity
- Reflection/memory parity in this first version

## Architecture

### Skill Layout

The skill should use this structure:

```text
.claude/skills/tradingagents-market-analysis/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── scripts/
│   ├── fetch_stock_data.py
│   ├── fetch_indicator.py
│   ├── fetch_fundamentals.py
│   ├── fetch_company_news.py
│   ├── fetch_global_news.py
│   └── generate_market_report.py
└── references/
    ├── capabilities.md
    ├── indicators.md
    └── workflow.md
```

### Runtime Boundary

The skill scripts must be self-contained and import only normal Python dependencies available through the repo environment. They may be adapted from `refs/TradingAgents` during implementation, but after implementation the skill should not import or execute code from that tree.

### Data Sources

Use the no-key public data path:

- `yfinance` for stock history, fundamentals, company news, and search-backed macro/global news
- `stockstats` for indicator computation
- `pandas` for data shaping

If required inputs are missing, scripts must fail fast with clear exceptions. No fallback to hidden alternate providers.

## Script Responsibilities

### `fetch_stock_data.py`

Inputs:

- ticker
- start date
- end date

Behavior:

- fetch OHLCV history
- validate dates
- return structured JSON or CSV-safe JSON payload

### `fetch_indicator.py`

Inputs:

- ticker
- indicator name
- current date
- look-back days

Behavior:

- support only a curated set of indicators
- compute one indicator per invocation
- return date/value series plus metadata

### `fetch_fundamentals.py`

Inputs:

- ticker
- current date

Behavior:

- fetch company overview and statement-derived metrics
- include only data available up to the requested date where possible
- return normalized JSON

### `fetch_company_news.py`

Inputs:

- ticker
- start date
- end date

Behavior:

- return filtered articles with title, publisher, summary, link, and publish date

### `fetch_global_news.py`

Inputs:

- current date
- look-back days
- limit

Behavior:

- run a small curated set of macro queries
- deduplicate articles
- return normalized JSON

### `generate_market_report.py`

Inputs:

- ticker
- assembled outputs from the fetch scripts

Behavior:

- generate a deterministic markdown report skeleton from fetched data
- avoid making the investment decision itself
- leave final synthesis to Codex

## Codex Workflow

When the skill triggers:

1. Identify ticker and analysis date requirements.
2. Call the relevant fetch scripts.
3. Use the references for indicator interpretation and report structure.
4. Produce:
   - executive summary
   - technical section
   - fundamentals section
   - news and sentiment section
   - recommendation with confidence and risk framing

Codex should emulate TradingAgents' analyst-style synthesis in a single orchestrated flow rather than invoking separate agent runtimes.

## Supported Indicators

Initial supported set:

- `close_50_sma`
- `close_200_sma`
- `close_10_ema`
- `macd`
- `macds`
- `macdh`
- `rsi`
- `boll`
- `boll_ub`
- `boll_lb`
- `atr`
- `vwma`
- `mfi`

This set is small enough to validate and broad enough to cover trend, momentum, volatility, and volume.

## Error Handling

The skill must fail fast with explicit errors for:

- missing ticker
- invalid date formats
- unsupported indicators
- empty data results
- network or provider errors after retry budget is exhausted

Do not silently substitute providers or invent values.

## Validation

Validation should be lightweight and practical:

- confirm the skill folder passes structural validation
- run a representative sample of scripts against a known ticker
- confirm the report-generation flow works with script outputs

Do not attempt exhaustive TDD for every market-data path in this first pass.

## Risks

- `yfinance` availability and response shape can drift
- news coverage can be sparse for some tickers
- historical fundamentals filtered by date may be approximate depending on source availability
- copied/adapted logic creates maintenance responsibility inside the skill

## Recommendation

Implement the skill as a standalone Codex-native package and use `refs/TradingAgents` only as a one-time source for adaptation. This gives the cleanest long-term reuse boundary and aligns with the user's stated goal.
