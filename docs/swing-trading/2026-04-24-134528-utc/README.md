# Swing Trading 3% Screen — Run 2026-04-24

## Run Metadata

- **Run Date**: 2026-04-24
- **Screen URL**: https://www.screener.in/screens/3474384/return-over-3-months
- **Screen Thesis**: "Return over 3 months > 30 AND Market Capitalization > 3000" — surface mid-to-large-cap names with momentum-confirmed sponsorship (price leadership backed by market-cap floor to avoid micro-cap noise).
- **Page Coverage**: Page 1 only (per user instruction)
- **Parsed Universe Size**: 25 stocks
- **User-Specified Pre-Rank Cap**: 3
- **Working Universe After Pre-Rank**: 3 stocks (ATLANTAELE, LLOYDSME, GVT&D)
- **Coverage Mode**: Full — user requested technical review for all 3 fundamentally analyzed names ("top 3 for technical analysis")
- **Technical Data Mode**: `api_fallback` (TradingView MCP disconnected — CDP connection failed; yfinance + stockstats used for OHLCV/indicators)

## Counts

- Fundamentally analyzed: 3 (all reused from fresh cache; Next Review dates 2026-04-27 and 2026-04-28 ≥ today 2026-04-24)
- Technically reviewed: 3
- Selected: 0
- Watchlist: 3 (LLOYDSME, GVT&D, ATLANTAELE)
- Rejected: 0 (of the 3 analyzed)
- Pending technical review: 0
- Technical dossiers written: 3

## Top 5 Fundamentally Strongest (of 3 analyzed)

| Rank | Symbol | Sponsorship | Key Evidence |
|---|---|---|---|
| 1 | LLOYDSME | Strongly Sponsored | 120% YoY iron ore volume (SEBI filing), OPM 33% × 4 quarters, TTM EPS step-up, ~25x TTM P/E |
| 2 | GVT&D | Strongly Sponsored | Q3 FY26 revenue +58% YoY, OPM 27%, zero net debt, ₹14,380 Cr backlog, major HVDC wins |
| 3 | ATLANTAELE | Strongly Sponsored | Fresh PGCIL EHV vendor approval, OPM 14%→20%, ROCE 50%; thin float & unconfirmed orders |

## Top 5 Technically Strongest Among Reviewed

| Rank | Symbol | Technical Verdict | Key Reason |
|---|---|---|---|
| 1 | LLOYDSME | Watchlist (Medium confidence) | Structural swing-low shelf at 1,628–1,665 inside 2–4% stop zone; 30m cluster at 1,666–1,672 |
| 2 | GVT&D | Watchlist (Medium confidence) | Apr-23 breakout on 4× volume; Apr-23 close (4,480–4,496) provides structural stop at 2.2–2.6% |
| 3 | ATLANTAELE | Watchlist / No-entry at CMP (Low confidence) | 10% gap-up into all-time high; 2–4% stop zone is untraded gap air |

## Top 5 Overall Combined

| Combined Rank | Symbol | Fundamental | Technical | Verdict |
|---|---|---|---|---|
| 1 | LLOYDSME | #1 | #1 | Watchlist — clearest structural stop defense + strongest sponsorship |
| 2 | GVT&D | #2 | #2 | Watchlist — breakout valid, awaits 30m MACD re-cross |
| 3 | ATLANTAELE | #3 | #3 | Watchlist but No-entry at CMP — wait for gap consolidation |

## How to Read the Fifth File (`3pct-ranked-by-stop-safety.md`)

- Section 1: `Fundamentally Strongest` ranked by evidence-quality first.
- Section 2: `Technically Strongest` ranked by stop-survivability.
- Section 3: `Overall Combined Ranking` — default master view. Top row is least likely to break the 2–4% stop zone; bottom row is most likely.

## Technical Dossier Directory

One verbose dossier per reviewed stock lives at `technical-dossiers/<RANK>-<SYMBOL>.md`. Rank reflects the full-universe fundamental rank. Three dossiers written this run: `1-LLOYDSME.md`, `2-GVTD.md`, `3-ATLANTAELE.md`.

## Pre-Rank Method (Summary)

- Scoring columns used: `Qtr Profit Var %`, `Qtr Sales Var %`, `ROCE %`, `3mth return %` with weights 0.35 / 0.35 / 0.20 / 0.10 applied to percentile ranks within the 25-row universe.
- Soft penalties: `Qtr Profit Var% <= 0` → -12; `Qtr Sales Var% <= 0` → -12; `ROCE < 15` → -8; `3mth return% <= 0` → -8.
- Distortion rule: `ROCE < 0` → ROCE contribution zero and -12 penalty.
- All 25 rows had valid values in the four scoring columns — no rows lost metric contribution to invalid cells.
- Top 3 adjusted PreRankScores: ATLANTAELE 88.54, LLOYDSME 86.88, GVT&D 83.33 (full table in `screen-universe.md`).

## Fundamental Cache Reuse

All three top-ranked stocks had Next Review On ≥ 2026-04-24 in `docs/swing-trading/fundamentals/index.md`, classifying them as `fresh`. Per the cache contract, their existing dossiers were reused without dispatching fundamental sub-agents. No cache files were updated on this run.
