from pathlib import Path

from PIL import Image
from PIL import ImageChops


class VisualValidator:
    """Simple screenshot comparison utility."""

    @staticmethod
    def compare(
        baseline: str,
        current: str,
    ) -> bool:

        baseline_img = Image.open(
            baseline
        )

        current_img = Image.open(
            current
        )

        diff = ImageChops.difference(
            baseline_img,
            current_img,
        )

        return (
            diff.getbbox()
            is None
        )