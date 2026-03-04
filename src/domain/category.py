from typing import List

from src.configuration import DiagramConfig
from src.domain.cause import Cause


class Category:
    """Категория причин (Domain Model)."""

    def __init__(self, name: str, causes: List[Cause]):
        self._name = name
        self._causes = causes

    @property
    def name(self) -> str:
        """Возвращает название категории."""
        return self._name

    @property
    def causes(self) -> List[Cause]:
        """Возвращает список причин."""
        return self._causes

    def calculate_total_height(self, config: DiagramConfig) -> float:
        """Вычисляет общую высоту всех причин."""
        heights = [cause.calculate_height(config) for cause in self._causes]
        return sum(heights) + config.dimensions.y_unit

    def calculate_max_width(self, config: DiagramConfig) -> float:
        """Вычисляет максимальную ширину текста причин."""
        dims = config.dimensions
        widths = [
            cause.max_line_length * dims.text_width_factor * dims.x_step
            for cause in self._causes
        ]
        return max(widths) if widths else 0
