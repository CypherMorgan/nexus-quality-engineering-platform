from pathlib import Path

import pytest

from nexus_qe.ui.visual import (
    VisualValidator,
)


@pytest.mark.regression
def test_dashboard_visual(
    page,
):
    page.goto(
        "http://localhost:8000/dashboard"
    )

    current = (
        Path(
            "reports/current_dashboard.png"
        )
    )

    page.screenshot(
        path=str(current)
    )

    baseline = (
        Path(
            "tests/resources/baselines/dashboard.png"
        )
    )

    assert (
        VisualValidator.compare(
            str(baseline),
            str(current),
        )
    )