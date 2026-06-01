from pathlib import Path

from nexus_qe.core.constants import FrameworkConstants


class ArtifactManager:
    """Provides report artifact paths."""

    @staticmethod
    def ensure_directories() -> None:
        directories = [
            FrameworkConstants.SCREENSHOTS_DIR,
            FrameworkConstants.VIDEOS_DIR,
            FrameworkConstants.TRACES_DIR,
            FrameworkConstants.LOGS_DIR,
        ]

        for directory in directories:
            Path(directory).mkdir(
                parents=True,
                exist_ok=True,
            )