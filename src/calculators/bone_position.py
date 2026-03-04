from src.configuration import DiagramConfig
from src.domain.category import Category
from src.dto.point import Point


class BonePositionCalculator:
    """Вычисляет позиции костей (рёбер) категорий."""

    def calculate(
        self,
        category: Category,
        x_attach: float,
        side: int,
        config: DiagramConfig
    ) -> tuple[Point, Point]:
        """
        Вычисляет начальную и конечную точки ребра.

        Args:
            category: Категория для расчёта
            x_attach: Точка крепления к хребту
            side: Сторона (1 или -1)
            config: Конфигурация диаграммы

        Returns:
            Кортеж из начальной и конечной точки
        """
        dims = config.dimensions
        y_end = category.calculate_total_height(config) * side
        x_end = x_attach - dims.angle_offset

        start_point = Point(x_end, y_end)
        end_point = Point(x_attach, 0)

        return start_point, end_point
