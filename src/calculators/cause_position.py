from src.dto.point import Point


class CausePositionCalculator:
    """Вычисляет позицию причины на ребре."""

    def calculate_contact_point(
        self,
        y_cause: float,
        bone_start: Point,
        bone_end: Point
    ) -> Point:
        """
        Вычисляет точку касания причины с ребром категории.

        Args:
            y_cause: Y-координата причины
            bone_start: Начальная точка ребра
            bone_end: Конечная точка ребра

        Returns:
            Точка касания
        """
        if bone_start.y == 0:
            t = 0
        else:
            t = y_cause / bone_start.y

        x_contact = bone_start.x + (bone_end.x - bone_start.x) * (1 - t)
        return Point(x_contact, y_cause)
