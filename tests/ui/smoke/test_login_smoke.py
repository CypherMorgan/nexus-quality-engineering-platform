import pytest

from nexus_qe.data.factories.user_factory import (
    UserFactory,
)
from nexus_qe.ui.pages.login_page import (
    LoginPage,
)
from nexus_qe.ui.workflows.login_workflow import (
    LoginWorkflow,
)
from nexus_qe.core.config.settings import (
    Settings,
)

settings = Settings().config

@pytest.mark.smoke
def test_valid_login(page):
    login_page = LoginPage(page)

    login_page.navigate(
        f"{settings.application.base_url}/login"
    )

    user = UserFactory.demo_user()

    workflow = LoginWorkflow(
        login_page
    )

    dashboard = workflow.login(
        user
    )

    assert (
        dashboard.title()
        == "Nexus Dashboard"
    )