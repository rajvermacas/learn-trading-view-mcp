# Swing Trading 3% Stop Report - 2026-04-12

## What Changed Versus The Earlier Analysis

- Re-scored all 42 stocks using your updated rule that stoploss must be at or inside 3% below CMP.
- Kept only the setups where the chart shows multiple support layers inside that 3% band.
- Verified the TradingView chart contains the `10 in 1 Different Moving Averages` study and that `MA 1-5` are `EMA 10/20/50/100/200` on `Close`.
- Created a repo report in `docs/swing-trading/` instead of leaving the analysis only in terminal output.

## Screen Coverage

- Checked the Screener HTML pages directly and did not use the JSON endpoint.
- Page 1 contains 25 names and page 2 contains 17 names.
- `?page=3` repeats page 2, so the report uses 42 unique companies after de-duplication by company slug.
- Full 42-stock HTML screen universe is listed in [screen-universe.md](/workspaces/learn-trading-view-mcp/docs/swing-trading/screen-universe.md).

## How To Read The Numbers

- `CMP`: current TradingView price used in the scan.
- `3% Floor`: `CMP x 0.97`. Anything below that breaks your risk rule.
- `Entry`: current-price entry only when support is already directly underneath CMP.
- `Stoploss`: placed below the lowest support that still stays inside the 3% band.
- `First Trouble Area`: nearest resistance where price may stall.
- `Swing Target`: a broader exit objective using at least a 2R framework, cross-checked with resistance.
- `Support Layers Inside 3%`: the key metric for your trading mindset. More layers mean more technical reasons for price to hold above the stop.

## Result Summary

- Selected for 3% stop swing: 2
- Watch only if price tightens: 3
- Reject for 3% stop rule: 37

| Stock | Verdict | CMP | Stoploss | Risk % | First Trouble Area | Swing Target | Support Layers Inside 3% |
|---|---|---:|---:|---:|---:|---:|---:|
| Acutaas Chemical | Selected for 3% stop swing | 2362.20 | 2291.33 | 3.00% | 2394.00 | 2503.94 | 5 |
| Aditya Infotech | Selected for 3% stop swing | 1894.40 | 1840.95 | 2.82% | 1903.80 | 2001.30 | 3 |
| Volt.Transform. | Watch only if price tightens | 9311.50 | 9032.16 | 3.00% | 9581.00 | 9870.18 | 2 |
| Kirloskar Oil | Watch only if price tightens | 1473.20 | 1429.00 | 3.00% | 1495.00 | 1561.60 | 2 |
| SEAMEC Ltd | Watch only if price tightens | 1525.20 | 1488.71 | 2.39% | 1537.80 | 1598.18 | 3 |

## Short Conclusion

Under the old wider-stop swing framework, several more names looked attractive. Under your actual rule, only two names currently make sense: `Acutaas Chemical` and `Aditya Infotech`. Three more names are close, but they still need either a tighter entry or one more visible support layer inside the 3% band.

- Detailed selected and watchlist names: [3pct-selected-and-watchlist.md](/workspaces/learn-trading-view-mcp/docs/swing-trading/3pct-selected-and-watchlist.md)
- Rejected names under the 3% rule: [3pct-rejected.md](/workspaces/learn-trading-view-mcp/docs/swing-trading/3pct-rejected.md)
