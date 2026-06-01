import os

from dotenv import load_dotenv

load_dotenv()


class SecretsManager:
    """Provides access to secrets stored in environment variables."""

    @staticmethod
    def get(secret_name: str) -> str:
        value = os.getenv(secret_name)

        if value is None:
            raise ValueError(
                f"Missing required secret: {secret_name}"
            )

        return value