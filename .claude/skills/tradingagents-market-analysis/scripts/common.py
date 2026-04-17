#!/usr/bin/env python3
"""Shared helpers for the standalone market-analysis skill."""

from __future__ import annotations

import json
import logging
import time
from datetime import datetime
from pathlib import Path
from typing import Any, Callable

import numpy as np
import pandas as pd
from yfinance.exceptions import YFRateLimitError

LOGGER = logging.getLogger("tradingagents_market_analysis")


def configure_logging() -> None:
    """Configure stderr logging once for all scripts."""
    if LOGGER.handlers:
        return
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )


def parse_iso_date(raw_value: str, field_name: str) -> datetime:
    """Parse and validate an ISO date."""
    if not raw_value:
        raise ValueError(f"{field_name} is required")
    try:
        return datetime.strptime(raw_value, "%Y-%m-%d")
    except ValueError as exc:
        raise ValueError(f"{field_name} must be in YYYY-MM-DD format") from exc


def validate_date_order(start_date: datetime, end_date: datetime) -> None:
    """Ensure the date range is valid."""
    if start_date > end_date:
        raise ValueError("start_date must be on or before end_date")


def require_text(value: str, field_name: str) -> str:
    """Validate a required text field."""
    if not value or not value.strip():
        raise ValueError(f"{field_name} is required")
    return value.strip().upper()


def run_with_retry(operation_name: str, operation: Callable[[], Any]) -> Any:
    """Retry yfinance rate-limit errors with a fixed policy."""
    max_retries = 3
    base_delay_seconds = 2.0
    for attempt in range(max_retries + 1):
        try:
            LOGGER.info("Starting %s attempt %s", operation_name, attempt + 1)
            return operation()
        except YFRateLimitError:
            if attempt == max_retries:
                raise RuntimeError(f"{operation_name} failed after {max_retries + 1} attempts")
            delay_seconds = base_delay_seconds * (2**attempt)
            LOGGER.warning("%s rate-limited, retrying in %.1fs", operation_name, delay_seconds)
            time.sleep(delay_seconds)


def write_json(payload: dict[str, Any]) -> None:
    """Write a JSON payload to stdout."""
    print(json.dumps(payload, indent=2, default=_json_default))


def _json_default(value: Any) -> Any:
    """Convert pandas and numpy values into JSON-safe types."""
    if isinstance(value, (datetime, pd.Timestamp)):
        return value.isoformat()
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, np.generic):
        return value.item()
    if pd.isna(value):
        return None
    raise TypeError(f"Unsupported JSON value type: {type(value)!r}")
