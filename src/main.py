from typing import List

from matplotlib import pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure

from src.calculators.bone_position import BonePositionCalculator
from src.calculators.spine_length import SpineLengthCalculator
from src.configuration import DiagramConfig
from src.domain.category import Category
from src.domain.problem import Problem
from src.dto.point import Point
from src.render.bone import BoneRenderer
from src.render.cause import CauseRenderer
from src.render.spine import SpineRenderer


class IshikawaDiagram:
    """
    Main Ishikawa diagram class.
    Coordinates the work of all components (Facade Pattern).
    """

    def __init__(
            self,
            problem: Problem,
            categories: List[Category],
            config: DiagramConfig
    ):
        self._problem = problem
        self._categories = categories
        self._config = config
        self._spine_calculator = SpineLengthCalculator()
        self._bone_calculator = BonePositionCalculator()

    def render(self) -> tuple[Figure, Axes]:
        """
        Renders the diagram.

        Returns:
            Tuple of Figure and Axes
        """
        spine_length = self._spine_calculator.calculate(
            len(self._categories),
            self._config
        )

        fig, ax = plt.subplots(figsize=(spine_length + 4, 8))

        # Draw spine
        spine_renderer = SpineRenderer(spine_length, self._problem)
        spine_renderer.render(ax, self._config)

        # Draw categories
        max_y_reach = self._render_categories(ax)

        # Configure axes
        self._configure_axes(ax, spine_length, max_y_reach)

        return fig, ax

    def _render_categories(self, ax: Axes) -> float:
        """Renders all categories and their causes."""
        max_y_reach = 0
        x_attach = 0

        categories_max_widths = [category.calculate_max_width(self._config) for category in self._categories]
        if len(categories_max_widths) > 1:
            categories_max_widths = [max(categories_max_widths[i - 1], categories_max_widths[i])
                                     for i in range(1, len(categories_max_widths), 2)]

        for i, category in enumerate(self._categories):
            side = 1 if i % 2 == 0 else -1

            # Update attachment position
            x_attach += categories_max_widths[i // 2] * ((i + 1) % 2)

            # Calculate bone positions
            bone_start, bone_end = self._bone_calculator.calculate(
                category,
                x_attach,
                side,
                self._config
            )

            max_y_reach = max(max_y_reach, abs(bone_start.y))

            # Draw category bone
            bone_renderer = BoneRenderer(category, bone_start, bone_end, side)
            bone_renderer.render(ax, self._config)

            # Draw causes
            self._render_causes(ax, category, bone_start, bone_end, side)

        return max_y_reach

    def _render_causes(
            self,
            ax: Axes,
            category: Category,
            bone_start: Point,
            bone_end: Point,
            side: int
    ) -> None:
        """Renders category causes."""
        dims = self._config.dimensions
        y_cause = (-dims.y_unit - dims.y_unit * side) / 4 + (dims.y_unit * side)

        for cause in category.causes:
            position = Point(0, y_cause)  # x is not used

            cause_renderer = CauseRenderer(cause, position, bone_start, bone_end)
            cause_renderer.render(ax, self._config)

            y_cause += cause.calculate_height(self._config) * side

    def _configure_axes(self, ax: Axes, spine_length: float, max_y_reach: float) -> None:
        """Configures axes and display."""
        ax.set_xlim(-1, spine_length + 1)
        ax.set_ylim(-max_y_reach + 5, max_y_reach + 1)
        ax.axis('off')
        plt.tight_layout()

    def show(self) -> None:
        """Displays the diagram."""
        self.render()
        plt.show()

    def save(self, filename: str, dpi: int = 300) -> None:
        """
        Saves the diagram to a file.

        Args:
            filename: Filename for saving
            dpi: Image resolution
        """
        fig, _ = self.render()
        fig.savefig(filename, dpi=dpi, bbox_inches='tight')
        plt.close(fig)
