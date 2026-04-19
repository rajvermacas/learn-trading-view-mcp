# Swing Trading 3% Screen — Page 2 Run

**Run date:** 2026-04-19 (UTC)
**Screen URL:** https://www.screener.in/screens/3474384/return-over-3-months/?page=2
**Scope restriction:** Page 2 only (per user directive). Pages 1, 3, 4 not fetched.
**Run folder:** `docs/swing-trading/2026-04-19-055500-utc/`

---

## Screen Thesis

- **Screen title:** "Return over 3 months"
- **Visible filter rules:** `Return over 3 months > 30%` AND `Market Capitalization > ₹3,000 Cr`
- **Query definition:** `Return over 3months > 30 AND Market Capitalization > 3000`
- **Screen intent:** Surface mid-to-large-cap names delivering strong 3-month relative momentum (>30%). Thesis for swing trading is that a business-backed momentum filter (not penny-cap chase) uncovers sponsorship candidates where recent operating evidence legitimizes the move.
- **Sponsorship lens:** Prefer stocks where the 3-month rally is confirmed by recent operating/earnings evidence and a catalyst within the 1–8 week swing window, over names where price has run ahead of proof.

## Coverage Mode

- **Fundamental coverage:** Full page-2 universe (25 of 25 stocks analyzed).
- **Technical coverage:** Top 10 fundamentally ranked names only (per user directive). Ranks 11–25 are marked `pending technical review (user-limited coverage)` and are not presented as outright technical rejects.
- **Fundamental concurrency:** 6 sonnet sub-agents inflight at peak; each sub-agent owned exactly one stock and was retired after its dossier was accepted. Five waves dispatched (6+6+6+6+1).
- **Technical concurrency:** Strictly sequential (1 at a time) because TradingView MCP is shared mutable state.

## Universe Size

- 25 stocks from page 2 (S.No 26–50 of the 89-company full screen).
- 0 stocks on current cache index prior to this run; all 25 required fresh fundamental dossiers.

## Counts

| Bucket | Count |
|---|---|
| Fundamentally analyzed | 25 |
| Technically reviewed | 10 |
| Pending technical review (user-limited coverage) | 15 |
| Selected (full trade-level writeups) | 5 |
| Watchlist (reviewed but entry timing or stop-band tightness deferred) | 5 |
| Rejected (technically reviewed with likely-to-break verdict) | 0 |
| Listed as pending / not reviewed | 15 |

## Top 5 Fundamentally Strongest (from full universe of 25)

| # | Symbol | Company | Sponsorship | Confidence | Core reason |
|---|---|---|---|---|---|
| 1 | ACUTAAS | Acutaas Chemicals (fka Ami Organics) | Sponsored | High | Q3 FY26 NP +140% YoY, OPM 25%→38%, Fermion/Bayer 10-year contract to 2033+, debt-free, P/E 67x |
| 2 | IMFA | Indian Metals & Ferro Alloys | Supported | High | Q3 beat + Tata Steel Kalinganagar plant closed Feb 2026 + June 2026 KNR-1 commissioning; captive chrome/power; P/E 22.9x cheap |
| 3 | WELCORP | Welspun Corp | Sponsored | High | Record operating profit (+42% stripped of one-offs), ₹24,700 Cr orderbook thru FY28, Saudi DI commissioning H1 FY26, net-cash |
| 4 | HIRECT | Hind Rectifiers | Strong | High | Record Q3 revenue ₹277 Cr (+64% YoY), 9M +53%, ₹1,103 Cr orderbook, Vande Bharat/railway capex tailwind, 1:1 bonus |
| 5 | SHARDACROP | Sharda Cropchem | Strong | High | Three consecutive quarters of earnings acceleration, 9M FY26 PAT +259%, zero debt, ₹826 Cr cash, P/E 17.7x vs 29x sector |

## Top 5 Technically Strongest (among 10 reviewed names)

| # | Symbol | Verdict | Stop Survivability | CMP ₹ | Stop ₹ (% from CMP) | First Target | R:R |
|---|---|---|---|---|---|---|---|
| 1 | ACUTAAS | Best Aligned | Strong | 2,361.90 | 2,275 (3.7%) | 2,394–2,403 | 2.3R–2.7R |
| 2 | SHARDACROP | Best Aligned | Strong | 1,103.50 | 1,055–1,060 (4.0–4.3%) | 1,145.80 | 4.3R (swing) |
| 3 | IMFA | Best Aligned | Strong | 1,560 | 1,510–1,515 (2.9–3.2%) | 1,582.7 | 4R+ (swing) |
| 4 | WELCORP | Best Aligned | Strong | 1,075 | 1,035–1,045 (2.8–3.7%) | 1,100–1,115 | ~9R (swing) |
| 5 | SONACOMS | Bullish | High | 593 | 569–577 (2.7–4.0%) | 610–615 | 3.25R |

## Top 5 Overall Combined (master ranking, technically reviewed names only)

| # | Symbol | Combined verdict | Key reason |
|---|---|---|---|
| 1 | ACUTAAS | Best Aligned + strongest fundamentals | Highest-quality sponsorship + clean higher-low stop defense at 2280-2300 shelf |
| 2 | IMFA | Best Aligned + P/E 22.9x value | Breakout + closed M&A + June greenfield; stop 2.9–3.2% sits at breakout retest |
| 3 | WELCORP | Best Aligned + net-cash moat | Two weekly breakout candles; stop 2.8% on 30m EMA50 confluence |
| 4 | SHARDACROP | Best Aligned + P/E 17.7x | Flag consolidation at 30m EMA10/20; 4R+ swing |
| 5 | SONACOMS | Bullish + EV orderbook | Weekly breakout reclaim; 30m bull flag; 3.25R |

## Output Files in This Folder

1. `README.md` — this file.
2. `3pct-selected-and-watchlist.md` — full trade-level writeups for the 10 technically reviewed names (5 Selected + 5 Watchlist).
3. `3pct-rejected.md` — the 15 names not technically reviewed due to user-imposed coverage limit; each marked `technical review not run in this execution`.
4. `screen-universe.md` — proof of page-2 HTML coverage, pagination handling, deduplication, normalized universe used for analysis.
5. `3pct-ranked-by-stop-safety.md` — master ranking file with three sections: `Fundamentally Strongest Top Ten`, `Technically Strongest Top Ten`, `Overall Combined Ranking` (all 25 rows with explicit reviewed/pending status).

## How To Read File 5

`3pct-ranked-by-stop-safety.md` is the default master ranking. The combined section orders every stock in the analyzed universe from **least likely to break the practical 2–4% stop zone** (top) to **most likely to break** (bottom). Rows for stocks not technically reviewed carry `pending technical review (user-limited coverage)` in the Technical Review Status column and rank behind all reviewed names by default, since the combined view must not pretend equal certainty for reviewed and pending rows.
