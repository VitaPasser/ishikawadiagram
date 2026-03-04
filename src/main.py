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
    Главный класс диаграммы Исикавы.
    Координирует работу всех компонентов (Facade Pattern).
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
        Отрисовывает диаграмму.

        Returns:
            Кортеж из Figure и Axes
        """
        spine_length = self._spine_calculator.calculate(
            len(self._categories),
            self._config
        )

        fig, ax = plt.subplots(figsize=(spine_length + 4, 8))

        # Рисуем хребет
        spine_renderer = SpineRenderer(spine_length, self._problem)
        spine_renderer.render(ax, self._config)

        # Рисуем категории
        max_y_reach = self._render_categories(ax)

        # Настраиваем оси
        self._configure_axes(ax, spine_length, max_y_reach)

        return fig, ax

    def _render_categories(self, ax: Axes) -> float:
        """Отрисовывает все категории и их причины."""
        max_y_reach = 0
        x_attach = 0

        for i, category in enumerate(self._categories):
            side = 1 if i % 2 == 0 else -1

            # Обновляем позицию крепления
            x_attach += category.calculate_max_width(self._config) * ((i + 1) % 2)

            # Вычисляем позиции ребра
            bone_start, bone_end = self._bone_calculator.calculate(
                category,
                x_attach,
                side,
                self._config
            )

            max_y_reach = max(max_y_reach, abs(bone_start.y))

            # Рисуем ребро категории
            bone_renderer = BoneRenderer(category, bone_start, bone_end, side)
            bone_renderer.render(ax, self._config)

            # Рисуем причины
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
        """Отрисовывает причины категории."""
        dims = self._config.dimensions
        y_cause = (-dims.y_unit - dims.y_unit * side) / 4 + (dims.y_unit * side)

        for cause in category.causes:
            position = Point(0, y_cause)  # x не используется

            cause_renderer = CauseRenderer(cause, position, bone_start, bone_end)
            cause_renderer.render(ax, self._config)

            y_cause += cause.calculate_height(self._config) * side

    def _configure_axes(self, ax: Axes, spine_length: float, max_y_reach: float) -> None:
        """Настраивает оси и отображение."""
        ax.set_xlim(-1, spine_length + 5)
        ax.set_ylim(-max_y_reach - 2, max_y_reach + 2)
        ax.axis('off')

        plt.title(
            "Динамическая диаграмма Исикавы",
            fontsize=self._config.title_style.fontsize,
            fontweight=self._config.title_style.fontweight,
            pad=20
        )
        plt.tight_layout()

    def show(self) -> None:
        """Отображает диаграмму."""
        self.render()
        plt.show()

    def save(self, filename: str, dpi: int = 300) -> None:
        """
        Сохраняет диаграмму в файл.

        Args:
            filename: Имя файла для сохранения
            dpi: Разрешение изображения
        """
        fig, _ = self.render()
        fig.savefig(filename, dpi=dpi, bbox_inches='tight')
        plt.close(fig)
