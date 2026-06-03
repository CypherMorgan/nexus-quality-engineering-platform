import pytest

from nexus_qe.api.client import ApiClient
from nexus_qe.api.validators import (
    ResponseValidator,
    SchemaValidator,
)


@pytest.mark.api
def test_get_user():
    client = ApiClient()

    response = client.get(
        "/users/1"
    )

    ResponseValidator.status_code(
        response.status_code,
        200,
    )

    assert (
        response.body["username"]
        == "demo"
    )

    SchemaValidator.validate_response(
        "user_schema.json",
        response.body,
    )