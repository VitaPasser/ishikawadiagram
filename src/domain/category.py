from typing import List

from src.configuration import DiagramConfig
from src.domain.cause import Cause


class Category:
    """Category of causes (Domain Model)."""

    def __init__(self, name: str, causes: List[Cause]):
        self._name = name
        self._causes = causes

    @property
    def name(self) -> str:
        """Returns category name."""
        return self._name

    @property
    def causes(self) -> List[Cause]:
        """Returns list of causes."""
        return self._causes

    def calculate_total_height(self, config: DiagramConfig) -> float:
        """Calculates total height of all causes."""
        heights = [cause.calculate_height(config) for cause in self._causes]
        return sum(heights) + config.dimensions.y_unit

    def calculate_max_width(self, config: DiagramConfig) -> float:
        """Calculates maximum width of cause text."""
        dims = config.dimensions
        widths = [
            cause.max_line_length * dims.text_width_factor * dims.x_step
            for cause in self._causes
        ]
        return max(widths) if widths else 0
