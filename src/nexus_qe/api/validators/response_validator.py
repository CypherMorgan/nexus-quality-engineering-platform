from nexus_qe.core.exceptions import (
    ApiValidationError,
)


class ResponseValidator:
    """API response assertions."""

    @staticmethod
    def status_code(
        actual: int,
        expected: int,
    ) -> None:
        if actual != expected:
            raise ApiValidationError(
                f"Expected {expected}, got {actual}"
            )