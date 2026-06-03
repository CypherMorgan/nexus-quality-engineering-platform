from pathlib import Path

from PIL import Image
from PIL import ImageChops


class VisualValidator:

    @staticmethod
    def compare(
        baseline: str,
        current: str,
    ) -> bool:

        baseline_file = Path(
            baseline
        )

        if not baseline_file.exists():

            baseline_file.parent.mkdir(
                parents=True,
                exist_ok=True,
            )

            Image.open(
                current
            ).save(
                baseline_file
            )

            return True

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