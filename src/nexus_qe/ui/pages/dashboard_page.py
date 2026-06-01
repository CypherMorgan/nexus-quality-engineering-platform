from nexus_qe.ui.locators import LocatorStrategy
from nexus_qe.ui.pages import BasePage


class DashboardPage(BasePage):

    PAGE_TITLE = LocatorStrategy.by_test_id(
        "dashboard-title"
    )

    def title(self) -> str:
        return self.text(
            self.PAGE_TITLE
        )