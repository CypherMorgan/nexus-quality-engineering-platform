from nexus_qe.api.client import ApiClient


class AuthClient(ApiClient):
    """Authentication API abstraction."""

    def login(
        self,
        username: str,
        password: str,
    ):
        return self.post(
            "/auth/login",
            {
                "username": username,
                "password": password,
            },
        )