import pytest

from nexus_qe.data.factories import UserFactory
from nexus_qe.ui.pages.dashboard_page import (
    DashboardPage,
)
from nexus_qe.ui.pages.login_page import LoginPage
from nexus_qe.ui.workflows import LoginWorkflow


@pytest.mark.smoke
def test_login_flow(
    page,
):
    login_page = LoginPage(page)

    user = UserFactory.build()

    workflow = LoginWorkflow(
        login_page
    )

    dashboard_page: DashboardPage = (
        workflow.login(user)
    )

    assert dashboard_page is not None