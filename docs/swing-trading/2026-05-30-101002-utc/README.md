# Swing Trading 3% Screen Run

Generated: 2026-05-30 10:10:02 UTC

Screen: https://www.screener.in/screens/3615928/3-month-return-50/

## Screen Thesis

The visible filter is `Return over 3months > 50 AND Market Capitalization > 3000`.
This run looks for liquid-enough Indian momentum names whose recent business
evidence can sponsor a 1-8 week swing, then tests whether a practical 2%-4%
downside band around the usual 3% reference has structural support.

## Coverage

| Item | Count |
|---|---:|
| Parsed HTML pages | 2 |
| Parsed and deduplicated stocks | 49 |
| User-specified pre-rank cap | 20 |
| Fundamental dossiers ranked | 20 |
| User-specified technical coverage | 15 |
| Technically reviewed | 15 |
| Selected for immediate entry | 0 |
| Watchlist after confirmation | 10 |
| Technical rejects | 4 |
| Technical review not run due to coverage limit | 5 |

## Data Mode

`technical_data_mode=api_fallback` was used for every reviewed name because the
TradingView browser endpoint remained unreachable after `ensure_socat.sh`.
Each technical worker fetched its own `15m`, `30m`, `60m`, `1d`, and `1wk`
OHLCV and indicator bundles with EMA 10/20/50/100/200 into a unique transient
directory. The raw API files were validated and then removed because their
pretty-printed payloads exceed this repository's 800-line file limit.

## Previews

Fundamental top five: `CPPLUS`, `ATLANTAELE`, `WEBELSOLAR`, `EMMVEE`, `CUPID`.

Technical top five by stop safety: `ATLANTAELE`, `CUPID`, `GVPIL`, `TIMEX`,
`SASKEN`.

Combined top five: `ATLANTAELE`, `CUPID`, `CPPLUS`, `EMMVEE`, `GVPIL`.

## Files

- `screen-universe.md`: full HTML coverage, schema, pre-rank scoring, penalties,
  and the top-20 cut.
- `3pct-selected-and-watchlist.md`: reviewed names that deserve trade-level
  monitoring and their confirmation conditions.
- `3pct-rejected.md`: technical rejects and the five names not reviewed because
  technical coverage was capped at 15.
- `3pct-ranked-by-stop-safety.md`: fundamental top ten, technical top ten, and
  the default combined ranking.
- `technical-dossiers/`: one crisp audit dossier for every technically reviewed
  stock. Use these to inspect timeframe evidence, support inventory, entry
  condition, and failure risk.
