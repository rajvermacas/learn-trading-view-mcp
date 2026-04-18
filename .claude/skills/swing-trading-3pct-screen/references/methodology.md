# Swing Trading 3% Methodology

## Goal

Find the small number of stocks in a Screener.in universe that are both fundamentally strong and technically hardest to break more than 3% below the current trade location.

## Required Inputs

- Screener.in HTML screen URL
- TradingView MCP access
- `10 in 1 Different Moving Averages` study configured as:
  - `MA 1 = EMA 10 on Close`
  - `MA 2 = EMA 20 on Close`
  - `MA 3 = EMA 50 on Close`
  - `MA 4 = EMA 100 on Close`
  - `MA 5 = EMA 200 on Close`
- Fundamental data required for each shortlisted candidate:
  - Quarterly sales growth
  - Quarterly profit growth
  - ROCE
  - Debt quality or leverage context from the screen or company page

If any required chart state or required fundamental data cannot be verified, stop or reject with a clear reason. Do not assume missing values.

## Timeframes

- Weekly: trend and major structure
- Daily: swing structure and resistance map
- Hourly: near-price support density and setup cleanliness
- `30` minute: deep lower-timeframe moving-average map, structure map, and support/resistance validation
- `15` minute: micro structure, trigger quality, and immediate downside air pockets

## Fundamental Filter

Use the screen columns first, then the Screener company page when a shortlisted name needs missing context confirmed.

Require for selected names:

- Positive quarterly profit growth
- Positive quarterly sales growth
- Acceptable or strong ROCE relative to the screen universe
- No obvious balance-sheet stress, profit collapse, or business deterioration

Allow watchlist names only when:

- The business quality is still acceptable
- One quality field is merely average rather than clearly strong
- The technical setup is close but not yet actionable

Downgrade or reject when:

- Profit growth is sharply negative
- Sales growth is sharply negative
- ROCE is weak relative to the universe
- Debt or leverage profile is clearly unsafe for a tight-stop swing
- The chart is good but fundamentals are too weak to justify a tight-stop swing

## Technical Filter

Selected now:

- Weekly trend is bullish or at least clearly constructive
- Daily trend is bullish and clean
- Hourly structure is constructive and not sloppy
- `30` minute structure confirms the hourly thesis with visible support layering and clean resistance mapping
- `15` minute structure confirms there is no obvious air pocket straight to the stop area
- Multiple support layers sit inside 3% below CMP
- The support stack includes both market-structure references and EMA references
- Price is close enough to those support layers that a real stop can stay inside the 3% rule

Watch only:

- The broader trend is good
- Support exists inside 3%
- The entry is still too extended, or the support stack is not dense enough yet, or hourly, `30` minute, or `15` minute structure is not clean enough

Reject:

- No meaningful support inside 3%
- The support case relies only on moving averages and lacks real market structure
- Daily, hourly, `30` minute, or `15` minute structure is too messy for a tight stop
- Fundamentals are too weak relative to the rest of the screen

## Support Layer Logic

Count support references inside the 3% band below CMP. Stronger cases usually have several of these clustered together:

- `30` minute EMA20
- `30` minute EMA50
- `30` minute EMA100
- `30` minute EMA200
- `30` minute swing low
- `30` minute pullback base or consolidation shelf
- `30` minute breakout retest
- `15` minute swing low
- `15` minute pullback base or consolidation shelf
- `15` minute breakout retest
- Hourly EMA20
- Hourly EMA50
- Hourly EMA100
- Hourly EMA200
- Hourly swing low
- Hourly pullback base or prior resistance turned support
- Daily EMA10
- Daily EMA20
- Recent daily swing low
- Daily breakout retest shelf
- Weekly higher low or base if it sits inside the 3% band

Do not count duplicated references at nearly the same price as separate support unless they come from clearly different timeframes or structure types.

More layers inside the band means there are more reasons for price to hold before the stop is hit.

Also judge the spacing. A support stack is stronger when the supports are distributed through the band instead of all sitting at one level with empty space above them.

## Market Structure Checks

For every shortlisted stock, read the chart from higher to lower timeframe:

- Weekly: confirm the broader trend, major higher low, and whether price is extended into resistance.
- Daily: map the active swing, nearest resistance, prior breakout zone, and the most recent meaningful higher low.
- Hourly: identify the active pullback, local demand shelf, and where the setup becomes structurally invalid.
- `30` minute: map the lower-timeframe support stack, nearest resistance shelves, EMA alignment, and the key levels that define whether price still has room to hold above the `3% Floor`.
- `15` minute: inspect the immediate path below CMP for micro higher lows, rejection candles, base building, or an air pocket straight to the stop area.

Reject the setup if lower timeframes contradict the higher-timeframe thesis near the trade location.

## Ranking Logic

Rank higher when a stock has:

- Stronger fundamentals than peers in the same screen
- Clear weekly and daily alignment
- More independently justified supports between CMP and the `3% Floor`
- Better distribution of supports across daily, hourly, `30` minute, and `15` minute charts
- Cleaner lower-timeframe structure with fewer air pockets

Rank lower when the name is extended, support depends mostly on one level, or the fundamental case is merely acceptable rather than strong.

## Number Definitions

- `CMP`: current TradingView price used for the decision
- `3% Floor`: `CMP x 0.97`
- `Entry`: current price only if support is already underneath; otherwise define a narrower pullback entry zone
- `Stoploss`: below the lowest support that still stays within the 3% rule
- `First Trouble Area`: nearest obvious resistance where a stall is likely
- `Swing Target`: broader target that still respects visible resistance and supports a roughly `2R` style payoff
- `Support Map`: the exact layers inside 3% with timeframe, support type, level, and distance below CMP

## Output Structure

Create a fresh timestamped directory on each run:

- `docs/swing-trading/YYYY-MM-DD-HHMMSS-utc/`

Produce four files inside that directory:

- `README.md`: summary and ranking table
- `3pct-selected-and-watchlist.md`: full writeups for selected and watch names
- `3pct-rejected.md`: compact table for rejected names
- `screen-universe.md`: all names scraped from all HTML pages

Do not overwrite an older run. Each analysis should keep its own timestamped folder.

Each full writeup must show:

- Fundamental quality snapshot with the exact fields used
- Weekly structure note
- Daily structure note
- Hourly structure note
- `30` minute structure note
- `15` minute structure note
- Support inventory table with timeframe and support type
- Resistance inventory table with timeframe and structure type
- Entry, stoploss, first trouble area, and swing target with reasoning

## Writing Style

- Explain why each chosen setup is less likely than peers to break 3% down from the current trade location.
- Be direct about weak setups.
- If nothing qualifies, say so clearly.
- Use exact numbers and tie each number back to structure or EMA support.
- Name the timeframe whenever citing a support or resistance level.
- Mention the date so the report is clearly point-in-time.
