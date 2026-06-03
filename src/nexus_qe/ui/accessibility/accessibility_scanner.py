from playwright.sync_api import Page


class AccessibilityScanner:
    """Basic accessibility validation."""

    @staticmethod
    def scan(
        page: Page,
    ) -> list[str]:

        violations = []

        images = page.locator("img")

        count = images.count()

        for index in range(count):

            alt = (
                images
                .nth(index)
                .get_attribute("alt")
            )

            if not alt:
                violations.append(
                    "Image missing alt text"
                )

        return violations