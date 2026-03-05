from typing import List

from src.main import IshikawaDiagram
from src.configuration import DiagramConfig
from src.domain.category import Category
from src.domain.cause import Cause
from src.domain.problem import Problem
from src.validation import DiagramDataValidator


class DiagramBuilder:
    """
    Diagram builder (Builder Pattern).
    Simplifies creation of complex objects.
    """

    def __init__(self, problem: Problem, config: DiagramConfig = None):
        self._problem = problem
        self._config = config or DiagramConfig()
        self._categories: List[Category] = []

    def add_category(self, name: str, causes: List[str]) -> 'DiagramBuilder':
        """
        Adds category with causes.

        Args:
            name: Category name
            causes: List of cause descriptions

        Returns:
            Self for method chaining

        Raises:
            ValueError: If data is invalid
        """
        DiagramDataValidator.validate_causes(causes)
        cause_objects = [Cause(text) for text in causes]
        category = Category(name, cause_objects)
        self._categories.append(category)
        return self

    def build(self) -> 'IshikawaDiagram':
        """
        Builds the diagram.

        Returns:
            Constructed IshikawaDiagram instance
        """
        return IshikawaDiagram(self._problem, self._categories, self._config)
