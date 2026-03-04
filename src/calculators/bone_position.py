from src.configuration import DiagramConfig
from src.domain.category import Category
from src.dto.point import Point


class BonePositionCalculator:
    """Calculates positions of bones (ribs) for categories."""

    def calculate(
        self,
        category: Category,
        x_attach: float,
        side: int,
        config: DiagramConfig
    ) -> tuple[Point, Point]:
        """
        Calculates start and end points of the bone.

        Args:
            category: Category for calculation
            x_attach: Attachment point to the spine
            side: Side (1 or -1)
            config: Diagram configuration

        Returns:
            Tuple of start and end points
        """
        dims = config.dimensions
        y_end = category.calculate_total_height(config) * side
        x_end = x_attach - dims.angle_offset

        start_point = Point(x_end, y_end)
        end_point = Point(x_attach, 0)

        return start_point, end_point
