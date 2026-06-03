from pathlib import Path

from nexus_qe.core.config import Settings


class EnvironmentWriter:
    """Writes environment details into Allure."""

    @staticmethod
    def write() -> None:
        config = Settings().config

        output = Path(
            "allure-results/environment.properties"
        )

        output.parent.mkdir(
            exist_ok=True,
            parents=True,
        )

        output.write_text(
            (
                f"environment={config.environment}\n"
                f"browser={config.browser.browser_name}\n"
                f"base_url={config.application.base_url}\n"
            ),
            encoding="utf-8",
        )