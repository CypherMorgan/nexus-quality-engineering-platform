from nexus_qe.ui.locators import LocatorStrategy
from nexus_qe.ui.pages import BasePage


class NavigationComponent(BasePage):

    LOGOUT_BUTTON = LocatorStrategy.by_test_id(
        "logout-button"
    )

    def logout(self) -> None:
        self.click(
            self.LOGOUT_BUTTON
        )