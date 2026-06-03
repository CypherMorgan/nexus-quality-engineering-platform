import pytest

from nexus_qe.api.client import ApiClient
from nexus_qe.database.assertions import (
    DatabaseAssertions,
)
from nexus_qe.database.queries import (
    QueryExecutor,
)


@pytest.mark.e2e
def test_user_lifecycle():
    api_client = ApiClient()

    response = api_client.get(
        "/users/1"
    )

    assert (
        response.status_code
        == 200
    )

    executor = QueryExecutor()

    record = executor.fetch_one(
        """
        SELECT *
        FROM users
        WHERE id = :id
        """,
        {"id": 1},
    )

    DatabaseAssertions.record_exists(
        record
    )

    assert (
        response.body["id"]
        == record.id
    )