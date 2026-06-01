from nexus_qe.ui.locators import LocatorStrategy
from nexus_qe.ui.pages import BasePage


class LoginPage(BasePage):

    USERNAME_INPUT = LocatorStrategy.by_test_id(
        "username"
    )

    PASSWORD_INPUT = LocatorStrategy.by_test_id(
        "password"
    )

    LOGIN_BUTTON = LocatorStrategy.by_test_id(
        "login-button"
    )

    def enter_username(
        self,
        username: str,
    ) -> None:
        self.fill(
            self.USERNAME_INPUT,
            username,
        )

    def enter_password(
        self,
        password: str,
    ) -> None:
        self.fill(
            self.PASSWORD_INPUT,
            password,
        )

    def click_login(self) -> None:
        self.click(
            self.LOGIN_BUTTON
        )