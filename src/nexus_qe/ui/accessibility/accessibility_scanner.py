from axe_playwright_python.sync_playwright import Axe

class AccessibilityScanner:
    """Accessibility validation utility."""

    @staticmethod
    def scan(page):
        results = Axe().scan(page)

        violations = results.get(
            "violations",
            []
        )

        return violations