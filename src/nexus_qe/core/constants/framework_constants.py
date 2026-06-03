from pathlib import Path


class FrameworkConstants:
    """Framework-wide constants."""

    PROJECT_ROOT = Path(__file__).resolve().parents[4]

    CONFIG_DIR = PROJECT_ROOT / "config"
    ENVIRONMENTS_DIR = CONFIG_DIR / "environments"

    REPORTS_DIR = PROJECT_ROOT / "reports"

    SCREENSHOTS_DIR = REPORTS_DIR / "screenshots"
    VIDEOS_DIR = REPORTS_DIR / "videos"
    TRACES_DIR = REPORTS_DIR / "traces"
    LOGS_DIR = REPORTS_DIR / "logs"

    DEFAULT_ENV = "qa"

    SUPPORTED_BROWSERS = [
        "chromium",
        "firefox",
        "webkit",
    ]