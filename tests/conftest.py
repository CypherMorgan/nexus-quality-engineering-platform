import pytest
from playwright.sync_api import Page

from nexus_qe.ui.browser import BrowserManager


@pytest.fixture(scope="function")
def page() -> Page:
    manager = BrowserManager()

    playwright, browser, context, page = (
        manager.launch()
    )

    yield page

    context.close()
    manager.close(
        playwright=playwright,
        browser=browser,
    )