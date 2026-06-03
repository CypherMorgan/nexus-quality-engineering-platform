class NetworkMock:
    """Playwright network interception utility."""

    @staticmethod
    def mock_users(
        page,
    ):
        page.route(
            "**/users/*",
            lambda route: route.fulfill(
                status=200,
                content_type="application/json",
                body="""
                {
                    "id": 999,
                    "username": "mock-user"
                }
                """,
            ),
        )