from playwright.sync_api import Locator, Page

from nexus_qe.core.base import BaseService


class BasePage(BaseService):
    """Base page object."""

    def __init__(self, page: Page):
        super().__init__()
        self.page = page

    def navigate(self, url: str) -> None:
        self.logger.info(f"Navigating to: {url}")
        self.page.goto(url)

    def click(self, locator: str) -> None:
        self.page.locator(locator).click()

    def fill(
        self,
        locator: str,
        value: str,
    ) -> None:
        self.page.locator(locator).fill(value)

    def text(
        self,
        locator: str,
    ) -> str:
        return self.page.locator(locator).text_content() or ""

    def locator(
        self,
        locator: str,
    ) -> Locator:
        return self.page.locator(locator)

    def wait_for_url(
        self,
        url: str,
    ) -> None:
        self.page.wait_for_url(url)