from pathlib import Path

import pytest

from nexus_qe.ui.visual import (
    VisualValidator,
)
from nexus_qe.core.config.settings import (
    Settings,
)

settings = Settings().config

@pytest.mark.regression
def test_dashboard_visual(
    page,
):
    page.goto(
        f"{settings.application.base_url}/dashboard"
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