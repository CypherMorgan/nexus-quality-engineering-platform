import os

from nexus_qe.core.config.config_models import EnvironmentConfig
from nexus_qe.core.config.environment_loader import EnvironmentLoader
from nexus_qe.core.constants.framework_constants import FrameworkConstants


class Settings:
    """Central framework settings access."""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

            environment = os.getenv(
                "TEST_ENV",
                FrameworkConstants.DEFAULT_ENV
            )

            raw_config = EnvironmentLoader.load(environment)

            cls._instance.config = EnvironmentConfig(**raw_config)

        return cls._instance