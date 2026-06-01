from pathlib import Path

import yaml

from nexus_qe.core.constants.framework_constants import FrameworkConstants


class EnvironmentLoader:
    """Loads environment-specific YAML configuration."""

    @staticmethod
    def load(environment: str) -> dict:
        config_file: Path = (
            FrameworkConstants.ENVIRONMENTS_DIR / f"{environment}.yaml"
        )

        if not config_file.exists():
            raise FileNotFoundError(
                f"Environment configuration not found: {config_file}"
            )

        with open(config_file, encoding="utf-8") as file:
            return yaml.safe_load(file)