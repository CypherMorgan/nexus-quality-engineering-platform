import pytest

from nexus_qe.ui.pages.dashboard_page import (
    DashboardPage,
)


@pytest.mark.regression
def test_dashboard_title_exists(page):
    dashboard = DashboardPage(page)

    title = dashboard.title()

    assert isinstance(
        title,
        str,
    )