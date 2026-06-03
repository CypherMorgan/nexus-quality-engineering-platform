import pytest

from nexus_qe.ui.pages.dashboard_page import (
    DashboardPage,
)
from nexus_qe.core.config.settings import (
    Settings,
)

settings = Settings().config


@pytest.mark.regression
def test_dashboard_title_exists(page):
    dashboard = DashboardPage(page)

    dashboard.navigate(
        f"{settings.application.base_url}/dashboard"
    )

    assert (
        dashboard.title()
        == "Nexus Dashboard"
    )