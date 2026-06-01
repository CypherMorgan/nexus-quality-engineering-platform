import pytest
from playwright.sync_api import Page

from nexus_qe.ui.browser import BrowserManager


@pytest.fixture(scope="function")
def page(request):
    browser_override = request.config.getoption(
        "--browser"
    )

    manager = BrowserManager()

    if browser_override:
        manager.settings.browser.browser_name = (
            browser_override
        )

    playwright, browser, context, page = (
        manager.launch()
    )

    yield page

    context.close()

    manager.close(
        playwright=playwright,
        browser=browser,
    )