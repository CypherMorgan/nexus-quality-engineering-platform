import pytest

from nexus_qe.api.auth import AuthClient
from nexus_qe.api.validators import (
    ResponseValidator,
)


@pytest.mark.api
def test_authentication_endpoint():
    client = AuthClient()

    response = client.login(
        "demo",
        "password",
    )

    ResponseValidator.status_code(
        response.status_code,
        200,
    )

    assert (
        "token"
        in response.body
    )