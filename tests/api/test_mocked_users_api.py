import pytest

from nexus_qe.ui.network import (
    NetworkMock,
)


@pytest.mark.api
def test_mocked_users_response(
    page,
):
    NetworkMock.mock_users(
        page
    )

    response = page.evaluate(
        """
        async () => {
            const response =
                await fetch(
                    'http://localhost:8000/users/1'
                );

            return await response.json();
        }
        """
    )

    assert (
        response["username"]
        == "mock-user"
    )