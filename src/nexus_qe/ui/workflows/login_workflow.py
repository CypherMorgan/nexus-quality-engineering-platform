from nexus_qe.data.models import User
from nexus_qe.ui.pages.dashboard_page import (
    DashboardPage,
)
from nexus_qe.ui.pages.login_page import LoginPage


class LoginWorkflow:
    """Business-level login workflow."""

    def __init__(
        self,
        login_page: LoginPage,
    ):
        self.login_page = login_page

    def login(
        self,
        user: User,
    ) -> DashboardPage:
        self.login_page.enter_username(
            user.username
        )

        self.login_page.enter_password(
            user.password
        )

        self.login_page.click_login()

        return DashboardPage(
            self.login_page.page
        )