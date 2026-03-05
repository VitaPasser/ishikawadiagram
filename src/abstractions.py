"""Abstract interfaces and protocols for extensibility."""

from abc import ABC, abstractmethod
from typing import Protocol, List, Dict, Tuple

from src.domain.category import Category
from src.domain.problem import Problem


class DiagramRenderer(ABC):
    """Abstract base class for diagram renderers."""

    @abstractmethod
    def render(self):
        """Render the diagram."""
        pass


class DataLoader(ABC):
    """Abstract base class for data loaders."""

    @abstractmethod
    def load(self, source) -> Tuple[str, Dict[str, List[str]]]:
        """Load diagram data from source."""
        pass


class PositionCalculator(ABC):
    """Abstract base class for position calculations."""

    @abstractmethod
    def calculate(self, *args, **kwargs):
        """Calculate position based on input parameters."""
        pass

