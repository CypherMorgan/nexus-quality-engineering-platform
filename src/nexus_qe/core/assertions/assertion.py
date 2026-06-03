class Assertion:
    """Reusable framework assertions."""

    @staticmethod
    def equal(
        actual,
        expected,
        message: str | None = None,
    ) -> None:
        if actual != expected:
            raise AssertionError(
                message
                or f"Expected {expected}, got {actual}"
            )

    @staticmethod
    def true(
        value,
        message: str | None = None,
    ) -> None:
        if not value:
            raise AssertionError(
                message
                or "Expected value to be True"
            )

    @staticmethod
    def not_none(
        value,
        message: str | None = None,
    ) -> None:
        if value is None:
            raise AssertionError(
                message
                or "Expected value not to be None"
            )