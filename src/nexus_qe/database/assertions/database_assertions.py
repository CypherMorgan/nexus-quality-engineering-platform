from nexus_qe.core.exceptions import (
    DatabaseValidationError,
)


class DatabaseAssertions:
    """Database assertion utilities."""

    @staticmethod
    def record_exists(
        record,
    ) -> None:
        if record is None:
            raise DatabaseValidationError(
                "Expected database record was not found."
            )

    @staticmethod
    def expected_count(
        actual: int,
        expected: int,
    ) -> None:
        if actual != expected:
            raise DatabaseValidationError(
                f"Expected {expected}, got {actual}"
            )