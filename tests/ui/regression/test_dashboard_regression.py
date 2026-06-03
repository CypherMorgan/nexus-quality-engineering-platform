import pytest

from nexus_qe.ui.pages.dashboard_page import (
    DashboardPage,
)


@pytest.mark.regression
def test_dashboard_title_exists(page):
    dashboard = DashboardPage(page)

    dashboard.navigate(
        "http://localhost:8000/dashboard"
    )

    assert (
        dashboard.title()
        == "Nexus Dashboard"
    )