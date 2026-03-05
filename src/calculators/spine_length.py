from src.configuration import DiagramConfig


class SpineLengthCalculator:
    """Calculates diagram spine length based on category widths."""

    def calculate(self, x_lens_categories: list[float],
                  config: DiagramConfig) -> float:
        """
        Calculates the main spine length.

        Args:
            x_lens_categories: List of grouped category widths
            config: Diagram configuration

        Returns:
            Calculated spine length
        """
        return sum(x_lens_categories) + 0.5
