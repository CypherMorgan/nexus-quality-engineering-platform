from nexus_qe.observability.logging import LoggerManager


class BaseService:
    """Base service class shared across framework layers."""

    def __init__(self) -> None:
        self.logger = LoggerManager.get_logger()