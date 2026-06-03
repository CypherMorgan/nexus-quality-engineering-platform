from playwright.sync_api import (
    Browser,
    BrowserContext,
    Page,
    Playwright,
    sync_playwright,
)
from nexus_qe.core.constants import (
    FrameworkConstants,
)
from nexus_qe.core.config import Settings
from nexus_qe.observability.logging import LoggerManager
from nexus_qe.reporting.artifacts import ArtifactManager


class BrowserManager:
    """Manages Playwright browser lifecycle."""

    def __init__(self) -> None:
        self.settings = Settings().config
        self.logger = LoggerManager.get_logger()

        ArtifactManager.ensure_directories()

    def launch(self) -> tuple[
        Playwright,
        Browser,
        BrowserContext,
        Page,
    ]:
        playwright = sync_playwright().start()

        browser_name = self.settings.browser.browser_name

        browser_factory = getattr(
            playwright,
            browser_name,
        )

        browser = browser_factory.launch(
            headless=self.settings.browser.headless,
        )

        context = browser.new_context(
            record_video_dir=str(
                FrameworkConstants.VIDEOS_DIR
            )
        )

        page = context.new_page()

        self.logger.info(
            f"Browser launched: {browser_name}"
        )

        return playwright, browser, context, page

    @staticmethod
    def close(
        playwright: Playwright,
        browser: Browser,
    ) -> None:
        browser.close()
        playwright.stop()