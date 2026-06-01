from sqlalchemy import text

from nexus_qe.database.connections import (
    DatabaseManager,
)


class QueryExecutor:
    """Executes SQL queries."""

    def __init__(self) -> None:
        self.database = DatabaseManager()

    def fetch_one(
        self,
        query: str,
        parameters: dict | None = None,
    ):
        with (
            self.database.get_engine()
            .connect()
            as connection
        ):
            result = connection.execute(
                text(query),
                parameters or {},
            )

            return result.fetchone()

    def fetch_all(
        self,
        query: str,
        parameters: dict | None = None,
    ):
        with (
            self.database.get_engine()
            .connect()
            as connection
        ):
            result = connection.execute(
                text(query),
                parameters or {},
            )

            return result.fetchall()