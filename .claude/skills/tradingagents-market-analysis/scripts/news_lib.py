#!/usr/bin/env python3
"""News helpers for the standalone skill."""

from __future__ import annotations

from datetime import datetime, timedelta

import yfinance as yf

from common import LOGGER, parse_iso_date, run_with_retry, validate_date_order

GLOBAL_NEWS_QUERIES = [
    "stock market economy",
    "Federal Reserve interest rates",
    "inflation economic outlook",
    "global markets trading",
]


def fetch_company_news_payload(ticker: str, start_date_raw: str, end_date_raw: str) -> dict:
    """Fetch company news within a date range."""
    start_date = parse_iso_date(start_date_raw, "start_date")
    end_date = parse_iso_date(end_date_raw, "end_date")
    validate_date_order(start_date, end_date)
    ticker_object = yf.Ticker(ticker)
    articles = run_with_retry("fetch_company_news", lambda: ticker_object.get_news(count=20))
    normalized_articles = filter_company_articles(articles or [], start_date, end_date)
    return build_company_news_payload(ticker, start_date_raw, end_date_raw, normalized_articles)


def filter_company_articles(articles: list[dict], start_date: datetime, end_date: datetime) -> list[dict]:
    """Normalize and filter company articles."""
    normalized_articles = []
    for article in articles:
        normalized_article = normalize_article(article)
        publish_date = normalized_article["published_at"]
        if publish_date and not (start_date <= datetime.fromisoformat(publish_date) <= end_date + timedelta(days=1)):
            continue
        normalized_articles.append(normalized_article)
    LOGGER.info("Filtered %s company-news articles", len(normalized_articles))
    return normalized_articles


def build_company_news_payload(
    ticker: str,
    start_date_raw: str,
    end_date_raw: str,
    normalized_articles: list[dict],
) -> dict:
    """Build a company-news payload with availability metadata."""
    if normalized_articles:
        availability = {"status": "available", "reason": None}
    else:
        availability = {
            "status": "unavailable",
            "reason": f"No company news found for {ticker} between {start_date_raw} and {end_date_raw}",
        }
    return {
        "ticker": ticker,
        "start_date": start_date_raw,
        "end_date": end_date_raw,
        "articles": normalized_articles,
        "availability": availability,
    }


def fetch_global_news_payload(current_date_raw: str, look_back_days_raw: str, limit_raw: str) -> dict:
    """Fetch macro/global news through curated Yahoo Finance searches."""
    current_date = parse_iso_date(current_date_raw, "current_date")
    look_back_days = parse_positive_int(look_back_days_raw, "look_back_days")
    limit = parse_positive_int(limit_raw, "limit")
    deduplicated_articles = collect_global_articles(limit)
    filtered_articles = filter_global_articles(deduplicated_articles, current_date, look_back_days, limit)
    if not filtered_articles:
        raise RuntimeError(f"No global news found for {current_date_raw}")
    return {
        "current_date": current_date_raw,
        "look_back_days": look_back_days,
        "limit": limit,
        "articles": filtered_articles,
    }


def parse_positive_int(raw_value: str, field_name: str) -> int:
    """Parse and validate a positive integer."""
    value = int(raw_value)
    if value <= 0:
        raise ValueError(f"{field_name} must be a positive integer")
    return value


def collect_global_articles(limit: int) -> list[dict]:
    """Collect and deduplicate global-news search results."""
    articles = []
    seen_titles: set[str] = set()
    for query in GLOBAL_NEWS_QUERIES:
        search = run_with_retry("fetch_global_news_search", lambda query=query: yf.Search(query=query, news_count=limit, enable_fuzzy_query=True))
        for article in search.news:
            title = extract_title(article)
            if title in seen_titles:
                continue
            seen_titles.add(title)
            articles.append(article)
        if len(articles) >= limit:
            break
    LOGGER.info("Collected %s deduplicated global-news articles", len(articles))
    return articles


def filter_global_articles(
    articles: list[dict],
    current_date: datetime,
    look_back_days: int,
    limit: int,
) -> list[dict]:
    """Filter global articles to the requested date window."""
    earliest_date = current_date - timedelta(days=look_back_days)
    filtered_articles = []
    for article in articles:
        normalized_article = normalize_article(article)
        publish_date = normalized_article["published_at"]
        if publish_date is None:
            filtered_articles.append(normalized_article)
        else:
            published_at = datetime.fromisoformat(publish_date)
            if earliest_date <= published_at <= current_date + timedelta(days=1):
                filtered_articles.append(normalized_article)
        if len(filtered_articles) == limit:
            break
    return filtered_articles


def normalize_article(article: dict) -> dict:
    """Normalize both nested and flat Yahoo Finance news shapes."""
    if "content" in article:
        content = article["content"]
        publisher = content.get("provider", {}).get("displayName")
        link = extract_link(content)
        published_at = extract_publish_time(content.get("pubDate"))
        title = content.get("title")
        summary = content.get("summary")
    else:
        publisher = article.get("publisher")
        link = article.get("link")
        published_at = extract_publish_time(article.get("providerPublishTime"))
        title = article.get("title")
        summary = article.get("summary")
    if not title:
        raise RuntimeError("Encountered a news article without a title")
    return {
        "title": title,
        "summary": summary,
        "publisher": publisher,
        "link": link,
        "published_at": published_at,
    }


def extract_title(article: dict) -> str:
    """Extract the comparable article title for deduplication."""
    return normalize_article(article)["title"]


def extract_link(content: dict) -> str | None:
    """Extract an article URL from nested content payloads."""
    canonical = content.get("canonicalUrl")
    clickthrough = content.get("clickThroughUrl")
    url_object = canonical or clickthrough
    if url_object is None:
        return None
    return url_object.get("url")


def extract_publish_time(raw_value: object) -> str | None:
    """Normalize a publish timestamp into ISO format."""
    if raw_value is None:
        return None
    if isinstance(raw_value, str):
        return datetime.fromisoformat(raw_value.replace("Z", "+00:00")).replace(tzinfo=None).isoformat()
    if isinstance(raw_value, (int, float)):
        return datetime.utcfromtimestamp(raw_value).isoformat()
    raise RuntimeError(f"Unsupported publish-time value: {raw_value!r}")
