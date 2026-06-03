import json
from pathlib import Path

from jsonschema import validate

from nexus_qe.core.constants import (
    FrameworkConstants,
)


class SchemaValidator:
    """JSON schema validator."""

    @staticmethod
    def validate_response(
        schema_name: str,
        payload: dict,
    ) -> None:
        schema_file: Path = (
            Path(__file__).parent.parent
            / "contracts"
            / schema_name
        )

        with open(
            schema_file,
            encoding="utf-8",
        ) as file:
            schema = json.load(file)

        validate(
            instance=payload,
            schema=schema,
        )