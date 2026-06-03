import pytest

from nexus_qe.ui.accessibility import (
    AccessibilityScanner,
)

from nexus_qe.core.config.settings import (
    Settings,
)

settings = Settings().config


@pytest.mark.regression
def test_login_page_accessibility(
    page,
):
    page.goto(
        f"{settings.application.base_url}/login"
    )

    violations = (
        AccessibilityScanner
        .scan(page)
    )

    assert (
        len(violations)
        == 0
    )