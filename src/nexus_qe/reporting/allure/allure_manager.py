from pathlib import Path

import allure


class AllureManager:
    """Centralized Allure attachment handling."""

    @staticmethod
    def attach_file(
        file_path: str,
        name: str,
        attachment_type,
    ) -> None:
        path = Path(file_path)

        if not path.exists():
            return

        allure.attach.file(
            str(path),
            name=name,
            attachment_type=attachment_type,
        )