from datetime import datetime
from pathlib import Path

from nexus_qe.core.constants import (
    FrameworkConstants,
)


class AttachmentManager:
    """Manages reporting artifacts."""

    @staticmethod
    def screenshot_path(
        test_name: str,
    ) -> Path:
        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        return (
            FrameworkConstants.SCREENSHOTS_DIR
            / f"{test_name}_{timestamp}.png"
        )