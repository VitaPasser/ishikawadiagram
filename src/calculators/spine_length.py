from src.configuration import DiagramConfig


class SpineLengthCalculator:
    """Вычисляет длину хребта диаграммы."""

    def calculate(self, num_categories: int, config: DiagramConfig) -> float:
        """Вычисляет длину главного хребта."""
        return (num_categories // 2) * config.dimensions.x_step + 0.5
