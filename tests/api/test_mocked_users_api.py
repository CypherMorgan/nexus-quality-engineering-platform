import pytest

from nexus_qe.ui.network import (
    NetworkMock,
)
from nexus_qe.core.config.settings import (
    Settings,
)

settings = Settings().config


@pytest.mark.api
def test_mocked_users_response(
    page,
):
    NetworkMock.mock_users(
        page
    )

    response = page.evaluate(
        f"""
        async () => {{
            const response =
                await fetch(
                    '{settings.api.base_url}/users/1'
                );

            return await response.json();
        }}
        """
    )

    assert (
        response["username"]
        == "mock-user"
    )