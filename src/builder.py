from typing import List

from src.main import IshikawaDiagram
from src.configuration import DiagramConfig
from src.domain.category import Category
from src.domain.cause import Cause
from src.domain.problem import Problem


class DiagramBuilder:
    """
    Строитель диаграммы (Builder Pattern).
    Упрощает создание сложных объектов.
    """

    def __init__(self, problem: Problem, config: DiagramConfig = None):
        self._problem = problem
        self._config = config or DiagramConfig()
        self._categories: List[Category] = []

    def add_category(self, name: str, causes: List[str]) -> 'DiagramBuilder':
        """Добавляет категорию с причинами."""
        cause_objects = [Cause(text) for text in causes]
        category = Category(name, cause_objects)
        self._categories.append(category)
        return self

    def build(self) -> 'IshikawaDiagram':
        """Строит диаграмму."""
        return IshikawaDiagram(self._problem, self._categories, self._config)
