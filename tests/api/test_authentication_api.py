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

    assert response is not None