from abc import ABC, abstractmethod

from matplotlib.axes import Axes

from src.configuration import DiagramConfig


class Renderer(ABC):
    """Abstract renderer (Open/Closed, Dependency Inversion)."""

    @abstractmethod
    def render(self, ax: Axes, config: DiagramConfig) -> None:
        """Renders element on axes."""
        pass
