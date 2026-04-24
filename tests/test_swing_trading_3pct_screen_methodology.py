import logging
import re
import unittest
from pathlib import Path


LOGGER = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

METHODOLOGY_PATH = Path(
    ".claude/skills/swing-trading-3pct-screen/references/methodology.md"
)
SKILL_PATH = Path(".claude/skills/swing-trading-3pct-screen/SKILL.md")
TECHNICAL_DOSSIER_CONTRACT_PATH = Path(
    ".claude/skills/swing-trading-3pct-screen/references/technical-dossier-contract.md"
)
TECHNICAL_WORKER_CONTRACT_PATH = Path(
    ".claude/skills/swing-trading-3pct-screen/references/technical-worker-contract.md"
)


def read_methodology() -> str:
    LOGGER.info("Reading methodology file from %s", METHODOLOGY_PATH)
    if not METHODOLOGY_PATH.exists():
        raise FileNotFoundError(f"Missing methodology file: {METHODOLOGY_PATH}")
    return METHODOLOGY_PATH.read_text(encoding="utf-8")


def read_skill() -> str:
    LOGGER.info("Reading skill file from %s", SKILL_PATH)
    if not SKILL_PATH.exists():
        raise FileNotFoundError(f"Missing skill file: {SKILL_PATH}")
    return SKILL_PATH.read_text(encoding="utf-8")


def read_technical_dossier_contract() -> str:
    LOGGER.info("Reading technical dossier contract from %s", TECHNICAL_DOSSIER_CONTRACT_PATH)
    if not TECHNICAL_DOSSIER_CONTRACT_PATH.exists():
        raise FileNotFoundError(f"Missing technical dossier contract: {TECHNICAL_DOSSIER_CONTRACT_PATH}")
    return TECHNICAL_DOSSIER_CONTRACT_PATH.read_text(encoding="utf-8")


def read_technical_worker_contract() -> str:
    LOGGER.info("Reading technical worker contract from %s", TECHNICAL_WORKER_CONTRACT_PATH)
    if not TECHNICAL_WORKER_CONTRACT_PATH.exists():
        raise FileNotFoundError(f"Missing technical worker contract: {TECHNICAL_WORKER_CONTRACT_PATH}")
    return TECHNICAL_WORKER_CONTRACT_PATH.read_text(encoding="utf-8")


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
        cls.skill = read_skill()
        cls.technical_dossier_contract = read_technical_dossier_contract()
        cls.technical_worker_contract = read_technical_worker_contract()

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

    def test_documents_tradingview_disconnected_api_fallback(self) -> None:
        LOGGER.info("Checking TradingView disconnected API fallback contract")
        self.assertIn("## Technical Data Source Selection", self.methodology)
        self.assertIn("technical_data_mode", self.methodology)
        self.assertIn("tradingview_mcp", self.methodology)
        self.assertIn("api_fallback", self.methodology)
        self.assertIn("fetch_stock_data.py", self.methodology)
        self.assertIn("fetch_indicator_bundle.py", self.methodology)
        self.assertIn(
            "TradingView MCP is disconnected or unreachable",
            self.methodology,
        )

    def test_api_fallback_is_self_contained_in_swing_skill(self) -> None:
        LOGGER.info("Checking API fallback is self-contained")
        combined_text = f"{self.skill}\n{self.methodology}"
        self.assertNotIn("$tradingagents-market-analysis", combined_text)
        self.assertNotIn("tradingagents-market-analysis", combined_text)
        self.assertIn("scripts/fetch_stock_data.py", combined_text)
        self.assertIn("scripts/fetch_indicator_bundle.py", combined_text)
        self.assertIn("references/api-workflow.md", combined_text)
        self.assertIn("references/api-output-schemas.md", combined_text)
        self.assertIn("references/api-indicators.md", combined_text)

        required_paths = [
            Path(".claude/skills/swing-trading-3pct-screen/scripts/fetch_stock_data.py"),
            Path(".claude/skills/swing-trading-3pct-screen/scripts/fetch_indicator_bundle.py"),
            Path(".claude/skills/swing-trading-3pct-screen/references/api-workflow.md"),
            Path(".claude/skills/swing-trading-3pct-screen/references/api-output-schemas.md"),
            Path(".claude/skills/swing-trading-3pct-screen/references/api-indicators.md"),
        ]
        for required_path in required_paths:
            self.assertTrue(required_path.exists(), f"Missing local API fallback file: {required_path}")

    def test_api_fallback_forbids_ad_hoc_scripts(self) -> None:
        LOGGER.info("Checking API fallback forbids ad hoc scripts")
        combined_text = f"{self.skill}\n{self.methodology}"
        self.assertIn("Do not write ad hoc Python scripts", combined_text)
        self.assertIn("use the bundled scripts", combined_text)

    def test_api_fallback_fetching_is_technical_worker_owned(self) -> None:
        LOGGER.info("Checking API fallback data fetch ownership")
        combined_text = f"{self.skill}\n{self.methodology}\n{self.technical_worker_contract}"
        forbidden_phrases = [
            "the main agent must fetch per-stock JSON before the handoff",
            "JSON payloads supplied by the main agent",
            "before dispatching the technical worker",
        ]
        for phrase in forbidden_phrases:
            self.assertNotIn(phrase, combined_text)
        self.assertIn("technical sub-agent must fetch", self.skill)
        self.assertIn("technical worker must fetch deterministic technical data", self.methodology)
        self.assertIn("API output directory", self.technical_worker_contract)
        self.assertIn("run `scripts/fetch_stock_data.py`", self.technical_worker_contract)
        self.assertIn("run `scripts/fetch_indicator_bundle.py`", self.technical_worker_contract)

    def test_technical_worker_concurrency_depends_on_data_mode(self) -> None:
        LOGGER.info("Checking technical worker concurrency by data mode")
        combined_text = f"{self.skill}\n{self.methodology}"
        delegation_examples = Path(
            ".claude/skills/swing-trading-3pct-screen/references/delegation-examples.md"
        ).read_text(encoding="utf-8")
        self.assertIn("TradingView MCP is shared mutable state", combined_text)
        self.assertIn("`tradingview_mcp` technical workers must run strictly one at a time", combined_text)
        self.assertIn("`api_fallback` technical workers may run in parallel", combined_text)
        self.assertIn("hard cap of `6` inflight technical workers", combined_text)
        self.assertIn("bounded parallel worker queue", delegation_examples)
        self.assertNotIn("Technical sub-agents must run one at a time", self.skill)
        self.assertNotIn("Run technical workers strictly one at a time", self.methodology)

    def test_api_fallback_parallel_workers_do_not_share_writable_resources(self) -> None:
        LOGGER.info("Checking API fallback writable-resource isolation")
        api_workflow = Path(
            ".claude/skills/swing-trading-3pct-screen/references/api-workflow.md"
        ).read_text(encoding="utf-8")
        combined_text = f"{self.skill}\n{self.methodology}\n{self.technical_worker_contract}\n{api_workflow}"
        self.assertIn("unique per-stock API output directory", combined_text)
        self.assertIn("must not share writable resources", combined_text)
        self.assertIn("Shared read-only script and reference paths are allowed", combined_text)
        self.assertIn("Do not use a shared temp directory", api_workflow)
        self.assertIn("API_OUTPUT_DIR=\"docs/swing-trading/2026-04-24-134528-utc/api/01-ATLANTAELE\"", api_workflow)
        self.assertIn("reject the handoff if the API output directory is shared", self.technical_worker_contract)

    def test_skill_documents_each_bundled_script_usage(self) -> None:
        LOGGER.info("Checking SKILL.md documents each bundled script")
        self.assertIn("## Bundled Scripts", self.skill)
        expected_scripts = [
            "scripts/ensure_socat.sh",
            "scripts/fetch_stock_data.py",
            "scripts/fetch_indicator_bundle.py",
            "scripts/common.py",
            "scripts/indicator_catalog.py",
            "scripts/market_data_lib.py",
        ]
        for script_path in expected_scripts:
            self.assertIn(script_path, self.skill)
        self.assertIn("When to use", self.skill)
        self.assertIn("How to use", self.skill)
        self.assertIn("Do not call directly", self.skill)

    def test_technical_dossiers_are_crisp_not_huge(self) -> None:
        LOGGER.info("Checking technical dossier brevity contract")
        contract = self.technical_dossier_contract
        self.assertIn("maximum `90` lines", contract)
        self.assertIn("maximum `3` bullets", contract)
        self.assertIn("Do not paste raw worker output", contract)
        self.assertIn("crisp", contract.lower())
        self.assertNotIn("verbose synthesis", contract)


if __name__ == "__main__":
    unittest.main()
