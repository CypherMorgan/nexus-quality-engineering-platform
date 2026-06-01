from pathlib import Path

from loguru import logger

from nexus_qe.core.constants import FrameworkConstants


class LoggerManager:
    """Centralized framework logger."""

    _configured = False

    @classmethod
    def configure(cls) -> None:
        if cls._configured:
            return

        log_directory: Path = FrameworkConstants.LOGS_DIR
        log_directory.mkdir(parents=True, exist_ok=True)

        logger.remove()

        logger.add(
            sink=lambda msg: print(msg, end=""),
            level="INFO",
            format=(
                "{time:YYYY-MM-DD HH:mm:ss} | "
                "{level:<8} | "
                "{name}:{function}:{line} | "
                "{message}"
            ),
        )

        logger.add(
            log_directory / "execution.log",
            rotation="10 MB",
            retention="10 days",
            compression="zip",
            level="DEBUG",
        )

        cls._configured = True

    @staticmethod
    def get_logger():
        LoggerManager.configure()
        return logger