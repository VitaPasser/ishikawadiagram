from matplotlib.axes import Axes

from src.configuration import DiagramConfig
from src.domain.category import Category
from src.dto.point import Point
from src.render.render import Renderer


class BoneRenderer(Renderer):
    """Category bone renderer."""

    def __init__(self, category: Category, start: Point, end: Point, side: int):
        self._category = category
        self._start = start
        self._end = end
        self._side = side

    def render(self, ax: Axes, config: DiagramConfig) -> None:
        """Renders bone and category name."""
        # Draw bone
        ax.annotate(
            '',
            xy=(self._end.x, self._end.y),
            xytext=(self._start.x, self._start.y),
            arrowprops=config.bone_arrow.to_dict()
        )

        # Draw category name
        y_offset = 0.3 * self._side
        va = 'bottom' if self._side > 0 else 'top'

        ax.text(
            self._start.x,
            self._start.y + y_offset,
            self._category.name,
            fontsize=config.category_style.fontsize,
            fontweight=config.category_style.fontweight,
            ha=config.category_style.ha,
            va=va
        )
