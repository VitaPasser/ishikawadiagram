from matplotlib.axes import Axes

from src.calculators.cause_position import CausePositionCalculator
from src.configuration import DiagramConfig
from src.domain.cause import Cause
from src.dto.point import Point
from src.render.render import Renderer


class CauseRenderer(Renderer):
    """Рендерер причины."""

    def __init__(
        self,
        cause: Cause,
        position: Point,
        bone_start: Point,
        bone_end: Point
    ):
        self._cause = cause
        self._position = position
        self._bone_start = bone_start
        self._bone_end = bone_end
        self._position_calculator = CausePositionCalculator()

    def render(self, ax: Axes, config: DiagramConfig) -> None:
        """Отрисовывает причину."""
        contact = self._position_calculator.calculate_contact_point(
            self._position.y,
            self._bone_start,
            self._bone_end
        )

        dims = config.dimensions
        num_lines = self._cause.num_lines

        # Вычисляем позицию текста
        x_text_start = contact.x - 1.0
        x_text = x_text_start + 0.6 - num_lines * 0.05
        y_text = self._position.y + 0.2

        # Рисуем текст
        ax.text(
            x_text,
            y_text,
            self._cause.text,
            fontsize=config.cause_style.fontsize,
            ha=config.cause_style.ha,
            va=config.cause_style.va
        )

        # Рисуем стрелку
        max_length = self._cause.max_line_length
        x_len_text = max_length * dims.text_length_factor
        x_arrow_start = x_text_start - x_len_text - num_lines * 0.05

        ax.annotate(
            '',
            xy=(contact.x, contact.y),
            xytext=(x_arrow_start, self._position.y),
            arrowprops=config.cause_arrow.to_dict()
        )
