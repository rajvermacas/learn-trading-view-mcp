# Swing Trading 3% Screen — Run Report

**Run Date:** 2026-04-23
**Screen URL:** https://www.screener.in/screens/3474384/return-over-3-months
**Screen Thesis:** "Return over 3 months" — stocks with 3-month return > 30% AND market cap > ₹3,000 Cr. Surfaces momentum credibly backed by recent business evidence, filtering for companies where price strength is sponsored by operating improvement, catalyst events, or structural inflections rather than pure speculation.

---

## Universe Summary

| Metric | Count |
|--------|-------|
| Parsed universe size | 136 stocks |
| Pre-rank cap (user-specified) | 20 |
| Working universe (after pre-rank) | 20 |
| Fundamentally analyzed | 20 (all cached fresh) |
| Technically reviewed | 15 (user-specified limit) |
| Pending technical review | 5 |
| Technical dossiers written | 15 |

## Coverage Mode

User requested top 20 for fundamental analysis and top 15 for technical review. Technical review started at fundamental rank #1 and proceeded downward through #15. Stocks ranked #16–20 (SKYGOLD, PRECWIRE, RUBICON, WAAREEENER, KRISHANA) have fundamental analysis only — no technical review was run.

---

## Pre-Rank Step

Pre-rank computed `PreRankScore` from four scoring columns:
- **Qtr Profit Var %** (weight 0.35)
- **Qtr Sales Var %** (weight 0.35)
- **ROCE %** (weight 0.20)
- **3mth return %** (weight 0.10)

Soft penalties applied:
- Qtr Profit Var % ≤ 0: subtract 12
- Qtr Sales Var % ≤ 0: subtract 12
- ROCE % < 15: subtract 8
- ROCE % < 0: treat as 0 + subtract 12
- 3mth return % ≤ 0: subtract 8

Top 20 by adjusted PreRankScore kept as working universe. See `screen-universe.md` for full 136-stock table.

---

## Top 5 Fundamentally Strongest

| Rank | Symbol | Sponsorship | Confidence |
|------|--------|-------------|------------|
| 1 | LLOYDSME | Strongly Sponsored | High |
| 2 | ATLANTAELE | Strongly Sponsored | High |
| 3 | GVT&D | Strongly Sponsored | High |
| 4 | SHARDACROP | Strong | High |
| 5 | QPOWER | Strongly Sponsored | Medium |

## Top 5 Technically Strongest (among reviewed)

| Rank | Symbol | Technical Verdict | Stop Survivability |
|------|--------|-------------------|-------------------|
| 1 | CPPLUS | Near-Valid | Moderate-High |
| 2 | ENGINERSIN | Near-Valid | Moderate-Strong |
| 3 | SHARDACROP | Near-Valid | Moderate |
| 4 | MANORAMA | Near-Valid | Moderate (at 4%) |
| 5 | BAJAJCON | Near-Valid | Moderate |

## Top 5 Overall Combined

| Rank | Symbol | Fund Rank | Tech Verdict | Stop Surv | Key Reason |
|------|--------|-----------|--------------|-----------|------------|
| 1 | SHARDACROP | #4 | Near-Valid | Moderate | Best value (P/E 17.7x), zero debt, stop has 3-layer structural support |
| 2 | CPPLUS | #11 | Near-Valid | Mod-High | Strongest tested stop zone (₹2,170 demand-confirmed), Chinese ban catalyst |
| 3 | ENGINERSIN | #14 | Near-Valid | Mod-Strong | Tested stop at ₹236.71, zero debt PSU, record order book |
| 4 | BAJAJCON | #7 | Near-Valid | Moderate | Clean stop anchor at ₹452.5 (tested twice), near-zero debt |
| 5 | LLOYDSME | #1 | Near-Valid | Moderate | #1 fundamental, powerful trend but stop in untested air |

---

## How to Read the Ranking File

The `3pct-ranked-by-stop-safety.md` file contains three sections:
1. **Fundamentally Strongest Top Ten** — ranked by business sponsorship quality
2. **Technically Strongest Top Ten** — ranked by stop-zone defensibility among reviewed names only
3. **Overall Combined Ranking** — master ranking combining both, with technical review status explicit

Names marked "pending technical review" were not charted due to the user-imposed coverage limit of 15.

## Technical Dossier Directory

`technical-dossiers/` contains 15 verbose markdown dossiers, one per technically reviewed stock. Filename format: `<RANK>-<SYMBOL>.md` where RANK is the fundamental rank. Each dossier includes: core fields, 5 timeframe notes (weekly through 15-min), support/resistance inventories, trade parameters, verdict fields, and summary rationale. The 30-minute note is the primary execution frame with the most detail.
