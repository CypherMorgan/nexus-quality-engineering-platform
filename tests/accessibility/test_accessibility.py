import pytest

from nexus_qe.ui.accessibility import (
    AccessibilityScanner,
)


@pytest.mark.regression
def test_login_page_accessibility(
    page,
):
    page.goto(
        "http://localhost:8000/login"
    )

    violations = (
        AccessibilityScanner
        .scan(page)
    )

    assert (
        len(violations)
        == 0
    )