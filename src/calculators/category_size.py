"""Calculator for category sizes in the diagram."""

from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from src.configuration import DiagramConfig
    from src.domain.category import Category


class CategorySizeCalculator:
    """Calculates category widths and groups them appropriately."""

    @staticmethod
    def calculate_widths(categories: List['Category'], config: 'DiagramConfig') -> List[float]:
        """
        Calculates widths for categories.

        Args:
            categories: List of categories
            config: Diagram configuration

        Returns:
            List of widths for each category
        """
        return [category.calculate_max_width(config) for category in categories]

    @staticmethod
    def group_widths(widths: List[float]) -> List[float]:
        """
        Groups widths into pairs, taking maximum of each pair.
        This ensures symmetry in the diagram.

        Args:
            widths: List of original widths

        Returns:
            List of grouped widths
        """
        if len(widths) <= 1:
            return widths

        grouped = []
        for i in range(0, len(widths), 2):
            current = widths[i]
            next_width = widths[i + 1] if i + 1 < len(widths) else 0
            grouped.append(max(current, next_width))

        return grouped


