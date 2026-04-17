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


def fetch_stock_history_payload(ticker: str, start_date_raw: str, end_date_raw: str) -> dict:
    """Fetch OHLCV history and return a normalized JSON payload."""
    start_date = parse_iso_date(start_date_raw, "start_date")
    end_date = parse_iso_date(end_date_raw, "end_date")
    validate_date_order(start_date, end_date)
    ticker_object = yf.Ticker(ticker)
    history_frame = run_with_retry(
        "fetch_stock_history",
        lambda: ticker_object.history(start=start_date_raw, end=end_date_raw),
    )
    normalized_frame = normalize_history_frame(history_frame, ticker, start_date_raw, end_date_raw)
    return build_stock_history_payload(ticker, start_date_raw, end_date_raw, normalized_frame)


def normalize_history_frame(frame: pd.DataFrame, ticker: str, start_date_raw: str, end_date_raw: str) -> pd.DataFrame:
    """Normalize a stock history frame."""
    if frame.empty:
        raise RuntimeError(f"No price history found for {ticker} between {start_date_raw} and {end_date_raw}")
    normalized_frame = frame.reset_index()
    normalized_frame["Date"] = pd.to_datetime(normalized_frame["Date"], errors="raise").dt.tz_localize(None)
    numeric_columns = [name for name in ("Open", "High", "Low", "Close", "Adj Close", "Volume") if name in normalized_frame]
    normalized_frame[numeric_columns] = normalized_frame[numeric_columns].apply(pd.to_numeric, errors="raise")
    return normalized_frame


def build_stock_history_payload(ticker: str, start_date_raw: str, end_date_raw: str, frame: pd.DataFrame) -> dict:
    """Convert a normalized stock history frame into a payload."""
    LOGGER.info("Normalized %s stock-history rows for %s", len(frame), ticker)
    records = frame.to_dict(orient="records")
    return {
        "ticker": ticker,
        "start_date": start_date_raw,
        "end_date": end_date_raw,
        "record_count": len(records),
        "columns": list(frame.columns),
        "records": records,
    }


def fetch_indicator_payload(
    ticker: str,
    indicator_name_raw: str,
    current_date_raw: str,
    look_back_days_raw: str,
) -> dict:
    """Compute a single indicator series for a look-back window."""
    indicator_name = require_supported_indicator(indicator_name_raw)
    current_date = parse_iso_date(current_date_raw, "current_date")
    look_back_days = parse_look_back_days(look_back_days_raw)
    history_frame = load_indicator_history_frame(ticker, current_date)
    indicator_frame = compute_indicator_frame(history_frame, indicator_name)
    series = select_indicator_window(indicator_frame, indicator_name, current_date, look_back_days)
    return {
        "ticker": ticker,
        "indicator": indicator_name,
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


def load_indicator_history_frame(ticker: str, current_date: datetime) -> pd.DataFrame:
    """Download the history frame used by stockstats indicators."""
    start_date = (current_date - timedelta(days=365 * 5)).strftime("%Y-%m-%d")
    end_date = (current_date + timedelta(days=1)).strftime("%Y-%m-%d")
    LOGGER.info("Downloading indicator history for %s from %s to %s", ticker, start_date, end_date)
    history_frame = run_with_retry(
        "fetch_indicator_history",
        lambda: yf.download(
            ticker,
            start=start_date,
            end=end_date,
            progress=False,
            auto_adjust=True,
            multi_level_index=False,
        ),
    )
    if history_frame.empty:
        raise RuntimeError(f"No indicator history found for {ticker} up to {current_date.strftime('%Y-%m-%d')}")
    normalized_frame = history_frame.reset_index()
    normalized_frame["Date"] = pd.to_datetime(normalized_frame["Date"], errors="raise").dt.tz_localize(None)
    return normalized_frame[normalized_frame["Date"] <= current_date]


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
    filtered_frame["Date"] = filtered_frame["Date"].dt.strftime("%Y-%m-%d")
    series = []
    for _, row in filtered_frame.iterrows():
        value = row[indicator_name]
        series.append({"date": row["Date"], "value": None if pd.isna(value) else float(value)})
    return series
