from src.configuration import DiagramConfig


class SpineLengthCalculator:
    """Calculates diagram spine length."""

    def calculate(self, x_lens_categories: list[float],
                  config: DiagramConfig) -> float:
        """Calculates the main spine length."""
        return sum(x_lens_categories) + 0.5
        # return (num_categories // 2) * config.dimensions.x_step + 0.5
