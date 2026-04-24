import contextlib
import importlib
import io
import logging
import sys
import unittest
from pathlib import Path

import pandas as pd


LOGGER = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

SKILL_DIR = Path(".claude/skills/swing-trading-3pct-screen")
SCRIPTS_DIR = SKILL_DIR / "scripts"
REFERENCES_DIR = SKILL_DIR / "references"
TRADINGVIEW_EMA_INDICATORS = {
    "close_10_ema",
    "close_20_ema",
    "close_50_ema",
    "close_100_ema",
    "close_200_ema",
}
TRADINGVIEW_INTERVALS = {"15m", "30m", "60m", "1d", "1wk"}

sys.path.insert(0, str(SCRIPTS_DIR.resolve()))


class SwingTradingApiFallbackTest(unittest.TestCase):
    def test_indicator_catalog_contains_tradingview_ema_set(self) -> None:
        LOGGER.info("Checking API fallback EMA indicator parity")
        indicator_catalog = importlib.import_module("indicator_catalog")
        supported = set(indicator_catalog.INDICATOR_DESCRIPTIONS)
        self.assertTrue(
            TRADINGVIEW_EMA_INDICATORS.issubset(supported),
            f"Missing EMA indicators: {sorted(TRADINGVIEW_EMA_INDICATORS - supported)}",
        )

    def test_stockstats_can_compute_required_emas(self) -> None:
        LOGGER.info("Checking required EMAs compute on OHLCV input")
        market_data_lib = importlib.import_module("market_data_lib")
        frame = pd.DataFrame(
            {
                "Date": pd.date_range("2026-01-01", periods=240, freq="D"),
                "Open": range(240),
                "High": range(1, 241),
                "Low": range(240),
                "Close": range(1, 241),
                "Volume": [1000] * 240,
            }
        )
        for indicator_name in TRADINGVIEW_EMA_INDICATORS:
            computed_frame = market_data_lib.compute_indicator_frame(frame, indicator_name)
            self.assertIn(indicator_name, computed_frame.columns)

    def test_market_data_lib_contains_tradingview_intervals(self) -> None:
        LOGGER.info("Checking API fallback timeframe parity")
        market_data_lib = importlib.import_module("market_data_lib")
        supported = set(market_data_lib.SUPPORTED_INTERVALS)
        self.assertTrue(
            TRADINGVIEW_INTERVALS.issubset(supported),
            f"Missing intervals: {sorted(TRADINGVIEW_INTERVALS - supported)}",
        )

    def test_cli_requires_interval_arguments(self) -> None:
        LOGGER.info("Checking API fallback CLI interval arguments")
        fetch_stock_data = importlib.import_module("fetch_stock_data")
        fetch_indicator_bundle = importlib.import_module("fetch_indicator_bundle")
        self.assertIsInstance(fetch_stock_data.build_parser().parse_args, object)
        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr), self.assertRaises(SystemExit):
            fetch_stock_data.build_parser().parse_args(
                ["--ticker", "ABC.NS", "--start-date", "2026-01-01", "--end-date", "2026-01-31"]
            )
        with contextlib.redirect_stderr(stderr), self.assertRaises(SystemExit):
            fetch_indicator_bundle.build_parser().parse_args(
                [
                    "--ticker",
                    "ABC.NS",
                    "--current-date",
                    "2026-01-31",
                    "--look-back-days",
                    "30",
                    "--indicators",
                    "close_10_ema",
                ]
            )

    def test_api_references_document_full_parity_surface(self) -> None:
        LOGGER.info("Checking API reference documents TradingView parity")
        combined_text = "\n".join(
            [
                (REFERENCES_DIR / "api-workflow.md").read_text(encoding="utf-8"),
                (REFERENCES_DIR / "api-indicators.md").read_text(encoding="utf-8"),
                (REFERENCES_DIR / "methodology.md").read_text(encoding="utf-8"),
            ]
        )
        for indicator_name in TRADINGVIEW_EMA_INDICATORS:
            self.assertIn(indicator_name, combined_text)
        for interval_name in TRADINGVIEW_INTERVALS:
            self.assertIn(interval_name, combined_text)


if __name__ == "__main__":
    unittest.main()
