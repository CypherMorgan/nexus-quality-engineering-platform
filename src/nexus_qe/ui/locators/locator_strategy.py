class LocatorStrategy:
    """Centralized locator strategy definitions."""

    DATA_TEST_ID = "[data-testid='{}']"

    @staticmethod
    def by_test_id(
        value: str,
    ) -> str:
        return LocatorStrategy.DATA_TEST_ID.format(
            value
        )