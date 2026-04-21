import logging
import re
import unittest
from pathlib import Path


LOGGER = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

METHODOLOGY_PATH = Path(
    ".claude/skills/swing-trading-3pct-screen/references/methodology.md"
)


def read_methodology() -> str:
    LOGGER.info("Reading methodology file from %s", METHODOLOGY_PATH)
    if not METHODOLOGY_PATH.exists():
        raise FileNotFoundError(f"Missing methodology file: {METHODOLOGY_PATH}")
    return METHODOLOGY_PATH.read_text(encoding="utf-8")


def extract_base_weights(text: str) -> list[float]:
    LOGGER.info("Extracting documented base weights")
    pattern = re.compile(r"- `[^`]+`: `([0-9.]+)`")
    weights = [float(match) for match in pattern.findall(text)]
    if not weights:
        raise ValueError("No documented base weights found in methodology")
    return weights


class SwingTradingMethodologyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.methodology = read_methodology()

    def test_uses_fixed_schema_headings(self) -> None:
        LOGGER.info("Checking fixed schema headings")
        self.assertIn("### Fixed Screener Columns", self.methodology)
        self.assertIn("### Pre-Rank Scoring Columns", self.methodology)
        self.assertIn("### Context-Only Visible Columns", self.methodology)

    def test_removes_broader_adaptive_language(self) -> None:
        LOGGER.info("Checking broader adaptive language is gone")
        self.assertNotIn("### Recognized Screener Columns", self.methodology)
        self.assertNotIn("### Minimum Viable Pre-Rank Coverage", self.methodology)
        self.assertNotIn(
            "minimum viable pre-rank coverage",
            self.methodology,
        )

    def test_documents_exact_screen_schema(self) -> None:
        LOGGER.info("Checking exact screen schema")
        self.assertIn(
            "- `CMP Rs.`\n- `P/E`\n- `Mar Cap Rs.Cr.`\n- `Div Yld %`\n"
            "- `NP Qtr Rs.Cr.`\n- `Qtr Profit Var %`\n- `Sales Qtr Rs.Cr.`\n"
            "- `Qtr Sales Var %`\n- `ROCE %`\n- `3mth return %`",
            self.methodology,
        )

    def test_documents_exact_scoring_formula(self) -> None:
        LOGGER.info("Checking exact scoring formula")
        self.assertIn(
            "`PreRankScore = 0.35 * rank(Qtr Profit Var %) + 0.35 * "
            "rank(Qtr Sales Var %) + 0.20 * rank(ROCE %) + 0.10 * "
            "rank(3mth return %)`",
            self.methodology,
        )

    def test_documented_base_weights_sum_to_one(self) -> None:
        LOGGER.info("Checking base weights sum to 1.0")
        weights = extract_base_weights(self.methodology)
        self.assertAlmostEqual(sum(weights), 1.0, places=6)


if __name__ == "__main__":
    unittest.main()
