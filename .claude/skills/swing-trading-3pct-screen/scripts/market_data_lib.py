#!/usr/bin/env python3
"""Market data and indicator helpers for the standalone skill."""

from __future__ import annotations

import logging
from datetime import datetime, timedelta

import pandas as pd
import yfinance as yf
from stockstats import wrap

from common import LOGGER, parse_iso_date, run_with_retry, validate_date_order
from indicator_catalog import INDICATOR_DESCRIPTIONS, require_supported_indicator

SUPPORTED_INTERVALS = ("15m", "30m", "60m", "1d", "1wk")


def fetch_stock_history_payload(
    ticker: str,
    start_date_raw: str,
    end_date_raw: str,
    interval_raw: str,
) -> dict:
    """Fetch OHLCV history and return a normalized JSON payload."""
    start_date = parse_iso_date(start_date_raw, "start_date")
    end_date = parse_iso_date(end_date_raw, "end_date")
    interval = require_supported_interval(interval_raw)
    validate_date_order(start_date, end_date)
    ticker_object = yf.Ticker(ticker)
    history_frame = run_with_retry(
        "fetch_stock_history",
        lambda: ticker_object.history(
            start=start_date_raw,
            end=end_date_raw,
            interval=interval,
        ),
    )
    normalized_frame = normalize_history_frame(history_frame, ticker, start_date_raw, end_date_raw)
    return build_stock_history_payload(ticker, start_date_raw, end_date_raw, interval, normalized_frame)


def normalize_history_frame(frame: pd.DataFrame, ticker: str, start_date_raw: str, end_date_raw: str) -> pd.DataFrame:
    """Normalize a stock history frame."""
    if frame.empty:
        raise RuntimeError(f"No price history found for {ticker} between {start_date_raw} and {end_date_raw}")
    normalized_frame = frame.reset_index()
    if "Datetime" in normalized_frame.columns and "Date" not in normalized_frame.columns:
        normalized_frame.rename(columns={"Datetime": "Date"}, inplace=True)
    normalized_frame["Date"] = pd.to_datetime(normalized_frame["Date"], errors="raise").dt.tz_localize(None)
    numeric_columns = [name for name in ("Open", "High", "Low", "Close", "Adj Close", "Volume") if name in normalized_frame]
    normalized_frame[numeric_columns] = normalized_frame[numeric_columns].apply(pd.to_numeric, errors="raise")
    return normalized_frame


def build_stock_history_payload(
    ticker: str,
    start_date_raw: str,
    end_date_raw: str,
    interval: str,
    frame: pd.DataFrame,
) -> dict:
    """Convert a normalized stock history frame into a payload."""
    LOGGER.info("Normalized %s %s stock-history rows for %s", len(frame), interval, ticker)
    records = frame.to_dict(orient="records")
    return {
        "ticker": ticker,
        "start_date": start_date_raw,
        "end_date": end_date_raw,
        "interval": interval,
        "record_count": len(records),
        "columns": list(frame.columns),
        "records": records,
    }


def fetch_indicator_payload(
    ticker: str,
    indicator_name_raw: str,
    current_date_raw: str,
    look_back_days_raw: str,
    interval_raw: str,
) -> dict:
    """Compute a single indicator series for a look-back window."""
    indicator_name = require_supported_indicator(indicator_name_raw)
    current_date = parse_iso_date(current_date_raw, "current_date")
    look_back_days = parse_look_back_days(look_back_days_raw)
    interval = require_supported_interval(interval_raw)
    history_frame = load_indicator_history_frame(ticker, current_date, interval)
    indicator_frame = compute_indicator_frame(history_frame, indicator_name)
    series = select_indicator_window(indicator_frame, indicator_name, current_date, look_back_days)
    return {
        "ticker": ticker,
        "indicator": indicator_name,
        "interval": interval,
        "current_date": current_date_raw,
        "look_back_days": look_back_days,
        "description": INDICATOR_DESCRIPTIONS[indicator_name],
        "series": series,
    }


def parse_look_back_days(look_back_days_raw: str) -> int:
    """Validate the requested look-back window."""
    look_back_days = int(look_back_days_raw)
    if look_back_days <= 0:
        raise ValueError("look_back_days must be a positive integer")
    return look_back_days


def require_supported_interval(interval_raw: str) -> str:
    """Validate the requested yfinance interval."""
    if not interval_raw or not interval_raw.strip():
        raise ValueError("interval is required")
    interval = interval_raw.strip()
    if interval not in SUPPORTED_INTERVALS:
        supported = ", ".join(SUPPORTED_INTERVALS)
        raise ValueError(f"Unsupported interval '{interval_raw}'. Supported intervals: {supported}")
    return interval


def load_indicator_history_frame(ticker: str, current_date: datetime, interval: str) -> pd.DataFrame:
    """Download the history frame used by stockstats indicators."""
    intraday_max_days = {"15m": 55, "30m": 55, "60m": 500}
    lookback_days = intraday_max_days.get(interval, 365 * 5)
    start_date = (current_date - timedelta(days=lookback_days)).strftime("%Y-%m-%d")
    end_date = (current_date + timedelta(days=1)).strftime("%Y-%m-%d")
    LOGGER.info(
        "Downloading %s indicator history for %s from %s to %s",
        interval,
        ticker,
        start_date,
        end_date,
    )
    history_frame = download_indicator_history_frame(ticker, start_date, end_date, interval)
    if history_frame.empty:
        raise RuntimeError(f"No indicator history found for {ticker} up to {current_date.strftime('%Y-%m-%d')}")
    normalized_frame = history_frame.reset_index()
    if "Datetime" in normalized_frame.columns and "Date" not in normalized_frame.columns:
        normalized_frame.rename(columns={"Datetime": "Date"}, inplace=True)
    normalized_frame["Date"] = pd.to_datetime(normalized_frame["Date"], errors="raise").dt.tz_localize(None)
    end_cutoff = current_date + timedelta(days=1)
    return normalized_frame[normalized_frame["Date"] < end_cutoff]


def download_indicator_history_frame(ticker: str, start_date: str, end_date: str, interval: str) -> pd.DataFrame:
    """Download indicator history, falling back to Ticker.history if needed."""
    history_frame = run_with_retry(
        "fetch_indicator_history",
        lambda: yf.download(
            ticker,
            start=start_date,
            end=end_date,
            interval=interval,
            progress=False,
            auto_adjust=True,
            multi_level_index=False,
        ),
    )
    if not history_frame.empty:
        return history_frame
    LOGGER.warning("yf.download returned no %s history for %s; trying Ticker.history", interval, ticker)
    ticker_object = yf.Ticker(ticker)
    return run_with_retry(
        "fetch_indicator_history_fallback",
        lambda: ticker_object.history(
            start=start_date,
            end=end_date,
            interval=interval,
            auto_adjust=True,
        ),
    )


def compute_indicator_frame(history_frame: pd.DataFrame, indicator_name: str) -> pd.DataFrame:
    """Compute an indicator column on a stockstats frame."""
    wrapped_frame = wrap(history_frame.copy())
    wrapped_frame["Date"] = pd.to_datetime(wrapped_frame["Date"], errors="raise").dt.tz_localize(None)
    wrapped_frame[indicator_name]
    return wrapped_frame


def select_indicator_window(
    indicator_frame: pd.DataFrame,
    indicator_name: str,
    current_date: datetime,
    look_back_days: int,
) -> list[dict]:
    """Select the requested indicator window."""
    start_date = current_date - timedelta(days=look_back_days)
    filtered_frame = indicator_frame[indicator_frame["Date"] >= start_date].copy()
    if filtered_frame.empty:
        raise RuntimeError("No indicator rows available for the requested look-back window")
    filtered_frame["Date"] = filtered_frame["Date"].dt.strftime("%Y-%m-%dT%H:%M:%S")
    series = []
    for _, row in filtered_frame.iterrows():
        value = row[indicator_name]
        series.append({"date": row["Date"], "value": None if pd.isna(value) else float(value)})
    return series
