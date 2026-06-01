import pytest

from nexus_qe.database.assertions import (
    DatabaseAssertions,
)
from nexus_qe.database.queries import (
    QueryExecutor,
)


@pytest.mark.database
def test_user_exists():
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