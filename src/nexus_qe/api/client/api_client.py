from typing import Any

import requests

from nexus_qe.api.models import ApiResponse
from nexus_qe.core.base import BaseService
from nexus_qe.core.config import Settings


class ApiClient(BaseService):
    """Reusable REST client."""

    def __init__(self) -> None:
        super().__init__()

        self.settings = Settings().config

        self.base_url = self.settings.api.base_url
        self.timeout = self.settings.api.timeout

    def get(
        self,
        endpoint: str,
        headers: dict | None = None,
    ) -> ApiResponse:
        response = requests.get(
            f"{self.base_url}{endpoint}",
            headers=headers,
            timeout=self.timeout,
        )

        return ApiResponse(
            status_code=response.status_code,
            body=response.json(),
        )

    def post(
        self,
        endpoint: str,
        payload: dict[str, Any],
        headers: dict | None = None,
    ) -> ApiResponse:
        response = requests.post(
            f"{self.base_url}{endpoint}",
            json=payload,
            headers=headers,
            timeout=self.timeout,
        )

        return ApiResponse(
            status_code=response.status_code,
            body=response.json(),
        )