#!/usr/bin/env python3
"""Fundamentals helpers for the standalone skill."""

from __future__ import annotations

import pandas as pd
import yfinance as yf

from common import LOGGER, parse_iso_date, run_with_retry

SUMMARY_FIELDS = [
    "longName",
    "sector",
    "industry",
    "marketCap",
    "trailingPE",
    "forwardPE",
    "priceToBook",
    "trailingEps",
    "forwardEps",
    "dividendYield",
    "beta",
    "fiftyTwoWeekHigh",
    "fiftyTwoWeekLow",
    "fiftyDayAverage",
    "twoHundredDayAverage",
    "totalRevenue",
    "grossProfits",
    "ebitda",
    "netIncomeToCommon",
    "profitMargins",
    "operatingMargins",
    "returnOnEquity",
    "returnOnAssets",
    "debtToEquity",
    "currentRatio",
    "bookValue",
    "freeCashflow",
]


def fetch_fundamentals_payload(ticker: str, current_date_raw: str) -> dict:
    """Fetch company fundamentals and statement snapshots."""
    parse_iso_date(current_date_raw, "current_date")
    ticker_object = yf.Ticker(ticker)
    info = run_with_retry("fetch_company_info", lambda: ticker_object.info)
    if not info:
        raise RuntimeError(f"No company information found for {ticker}")
    balance_sheet = collect_statement_section(
        run_with_retry("fetch_balance_sheet", lambda: ticker_object.quarterly_balance_sheet),
        current_date_raw,
    )
    cashflow = collect_statement_section(
        run_with_retry("fetch_cashflow", lambda: ticker_object.quarterly_cashflow),
        current_date_raw,
    )
    income_statement = collect_statement_section(
        run_with_retry("fetch_income_statement", lambda: ticker_object.quarterly_income_stmt),
        current_date_raw,
    )
    insider_transactions = collect_insider_section(
        run_with_retry("fetch_insider_transactions", lambda: ticker_object.insider_transactions),
    )
    return {
        "ticker": ticker,
        "current_date": current_date_raw,
        "company_summary": extract_company_summary(info),
        "balance_sheet": balance_sheet["records"],
        "cashflow": cashflow["records"],
        "income_statement": income_statement["records"],
        "insider_transactions": insider_transactions["records"],
        "availability": {
            "balance_sheet": balance_sheet["availability"],
            "cashflow": cashflow["availability"],
            "income_statement": income_statement["availability"],
            "insider_transactions": insider_transactions["availability"],
        },
    }


def extract_company_summary(info: dict) -> dict:
    """Select the subset of company metrics exposed by the skill."""
    summary = {field: info.get(field) for field in SUMMARY_FIELDS if info.get(field) is not None}
    LOGGER.info("Collected %s summary fields", len(summary))
    return summary


def collect_statement_section(frame: pd.DataFrame, current_date_raw: str) -> dict:
    """Collect a financial statement section with availability metadata."""
    if frame is None or frame.empty:
        return unavailable_section("empty statement data")
    cutoff = pd.Timestamp(current_date_raw)
    eligible_columns = [column for column in frame.columns if pd.to_datetime(column, errors="coerce") <= cutoff]
    if not eligible_columns:
        return unavailable_section(f"no statement columns on or before {current_date_raw}")
    filtered_frame = frame.loc[:, eligible_columns].copy().reset_index(names="line_item")
    filtered_frame.columns = [
        column.isoformat() if hasattr(column, "isoformat") else str(column)
        for column in filtered_frame.columns
    ]
    return available_section(filtered_frame.to_dict(orient="records"))


def collect_insider_section(frame: pd.DataFrame) -> dict:
    """Collect insider transactions with availability metadata."""
    if frame is None or frame.empty:
        return unavailable_section("no insider transactions available")
    normalized_frame = frame.reset_index(drop=True).copy()
    return available_section(normalized_frame.to_dict(orient="records"))


def available_section(records: list[dict]) -> dict:
    """Wrap available section records."""
    return {
        "records": records,
        "availability": {"status": "available", "reason": None},
    }


def unavailable_section(reason: str) -> dict:
    """Wrap unavailable section records."""
    LOGGER.info("Returning unavailable fundamentals section: %s", reason)
    return {
        "records": [],
        "availability": {"status": "unavailable", "reason": reason},
    }
