import pytest

from nexus_qe.database.assertions import (
    DatabaseAssertions,
)
from nexus_qe.database.queries import (
    QueryExecutor,
)


@pytest.mark.database
def test_user_count():
    executor = QueryExecutor()

    records = executor.fetch_all(
        """
        SELECT *
        FROM users
        """
    )

    DatabaseAssertions.expected_count(
        len(records),
        1,
    )