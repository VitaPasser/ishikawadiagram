from src.configuration import DiagramConfig


class SpineLengthCalculator:
    """Calculates diagram spine length."""

    def calculate(self, num_categories: int, config: DiagramConfig) -> float:
        """Calculates the main spine length."""
        return (num_categories // 2) * config.dimensions.x_step + 0.5
