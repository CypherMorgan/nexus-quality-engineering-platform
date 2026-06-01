import allure
import pytest
from playwright.sync_api import Page

from nexus_qe.reporting.allure import AllureManager
from nexus_qe.reporting.attachments import AttachmentManager
from nexus_qe.reporting.environment import EnvironmentWriter
from nexus_qe.ui.browser import BrowserManager


def pytest_addoption(parser) -> None:
    """
    Register custom pytest command-line options.
    """
    parser.addoption(
        "--browser",
        action="store",
        default=None,
        help="Browser to execute tests against "
             "(chromium, firefox, webkit)",
    )


def pytest_sessionstart(session) -> None:
    """
    Generate Allure environment metadata before test execution.
    """
    EnvironmentWriter.write()


@pytest.fixture(scope="function")
def page(request) -> Page:
    """
    Provides a Playwright page instance for tests.
    Supports browser override through:
        pytest --browser chromium
        pytest --browser firefox
        pytest --browser webkit
    """
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


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Capture failure diagnostics and attach them to Allure.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when != "call":
        return

    if not report.failed:
        return

    page = item.funcargs.get("page")

    if not page:
        return

    screenshot_path = (
        AttachmentManager
        .screenshot_path(item.name)
    )

    screenshot_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    page.screenshot(
        path=str(screenshot_path),
        full_page=True,
    )

    AllureManager.attach_file(
        file_path=str(screenshot_path),
        name=f"{item.name}_failure_screenshot",
        attachment_type=allure.attachment_type.PNG,
    )