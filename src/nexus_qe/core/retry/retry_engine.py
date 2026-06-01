import time
from collections.abc import Callable
from typing import Any

from nexus_qe.core.exceptions import RetryExceededError
from nexus_qe.observability.logging import LoggerManager


class RetryEngine:
    """Simple retry engine for flaky operations."""

    @staticmethod
    def execute(
        operation: Callable[..., Any],
        retries: int = 3,
        delay: int = 2,
        *args,
        **kwargs,
    ) -> Any:
        logger = LoggerManager.get_logger()

        last_exception = None

        for attempt in range(1, retries + 1):
            try:
                return operation(*args, **kwargs)

            except Exception as exception:
                last_exception = exception

                logger.warning(
                    f"Attempt {attempt}/{retries} failed: {exception}"
                )

                if attempt < retries:
                    time.sleep(delay)

        raise RetryExceededError(
            f"Operation failed after {retries} attempts"
        ) from last_exception