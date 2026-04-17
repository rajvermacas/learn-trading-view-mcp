#!/usr/bin/env python3
"""Indicator metadata for the standalone market-analysis skill."""

INDICATOR_DESCRIPTIONS = {
    "close_50_sma": "50 SMA: medium-term trend indicator and dynamic support or resistance.",
    "close_200_sma": "200 SMA: long-term trend benchmark for major direction and regime.",
    "close_10_ema": "10 EMA: short-term trend indicator for faster directional shifts.",
    "macd": "MACD: momentum via moving-average convergence and divergence.",
    "macds": "MACD signal line: smoothing line used with MACD crossovers.",
    "macdh": "MACD histogram: distance between MACD and signal line.",
    "rsi": "RSI: momentum gauge for overbought, oversold, and divergence context.",
    "boll": "Bollinger middle line: baseline moving average for Bollinger Bands.",
    "boll_ub": "Bollinger upper band: upper volatility boundary for extension pressure.",
    "boll_lb": "Bollinger lower band: lower volatility boundary for exhaustion pressure.",
    "atr": "ATR: average true range for volatility and stop-width context.",
    "vwma": "VWMA: moving average weighted by traded volume.",
    "mfi": "MFI: money flow index using price and volume to assess buying pressure.",
}


def require_supported_indicator(indicator_name: str) -> str:
    """Validate an indicator name and return the normalized identifier."""
    normalized_name = indicator_name.strip().lower()
    if normalized_name not in INDICATOR_DESCRIPTIONS:
        supported_names = ", ".join(sorted(INDICATOR_DESCRIPTIONS))
        raise ValueError(f"Unsupported indicator '{indicator_name}'. Supported indicators: {supported_names}")
    return normalized_name
