from src.configuration import DiagramConfig


class Cause:
    """Cause in the diagram (Domain Model)."""

    def __init__(self, text: str):
        self._text = text
        self._lines = text.split('\n')

    @property
    def text(self) -> str:
        """Returns cause text."""
        return self._text

    @property
    def num_lines(self) -> int:
        """Returns number of lines."""
        return len(self._lines)

    @property
    def max_line_length(self) -> int:
        """Returns maximum line length."""
        return max(len(line) for line in self._lines)

    def calculate_height(self, config: DiagramConfig) -> float:
        """Calculates cause height."""
        dims = config.dimensions
        return (self.num_lines * dims.line_height_factor - 0.5 + 1) * dims.y_unit
