from src.dto.point import Point


class CausePositionCalculator:
    """Calculates cause position on the bone."""

    def calculate_contact_point(
        self,
        y_cause: float,
        bone_start: Point,
        bone_end: Point
    ) -> Point:
        """
        Calculates contact point of cause with category bone.

        Args:
            y_cause: Y-coordinate of the cause
            bone_start: Start point of the bone
            bone_end: End point of the bone

        Returns:
            Contact point
        """
        if bone_start.y == 0:
            t = 0
        else:
            t = y_cause / bone_start.y

        x_contact = bone_start.x + (bone_end.x - bone_start.x) * (1 - t)
        return Point(x_contact, y_cause)
