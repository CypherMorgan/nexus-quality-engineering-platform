from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

from nexus_qe.core.base import BaseService
from nexus_qe.core.config import Settings


class DatabaseManager(BaseService):
    """Database connection manager."""

    def __init__(self) -> None:
        super().__init__()

        self.connection_string = (
            Settings()
            .config
            .database
            .connection_string
        )

        self.engine: Engine = create_engine(
            self.connection_string
        )

    def get_engine(self) -> Engine:
        return self.engine