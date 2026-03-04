from matplotlib.axes import Axes

from src.configuration import DiagramConfig
from src.domain.problem import Problem
from src.render.render import Renderer


class SpineRenderer(Renderer):
    """Diagram spine renderer."""

    def __init__(self, spine_length: float, problem: Problem):
        self._spine_length = spine_length
        self._problem = problem

    def render(self, ax: Axes, config: DiagramConfig) -> None:
        """Renders spine and problem."""
        # Draw spine arrow
        ax.annotate(
            '',
            xy=(self._spine_length, 0),
            xytext=(0, 0),
            arrowprops=config.spine_arrow.to_dict()
        )

        # Draw problem
        ax.text(
            self._spine_length + 0.1,
            0,
            f"  {self._problem.description}",
            fontsize=config.problem_style.fontsize,
            fontweight=config.problem_style.fontweight,
            bbox=dict(boxstyle="round,pad=0.5", fc="white", ec="black"),
            va='center',
            ha=config.problem_style.ha
        )
