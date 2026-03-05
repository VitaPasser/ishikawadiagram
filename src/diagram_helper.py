"""Helper utilities for diagram operations."""

from typing import Dict, List, TYPE_CHECKING
from pathlib import Path

from src.builder import DiagramBuilder
from src.domain.problem import Problem
from src.validation import DiagramDataValidator

if TYPE_CHECKING:
    from src.main import IshikawaDiagram


class DiagramHelper:
    """Helper class for common diagram operations."""

    @staticmethod
    def create_diagram_from_data(
        problem: str,
        categories: Dict[str, List[str]]
    ) -> 'IshikawaDiagram':
        """
        Creates a diagram from problem and categories data.

        Args:
            problem: Problem description
            categories: Dictionary of categories and causes

        Returns:
            IshikawaDiagram instance

        Raises:
            ValueError: If data is invalid
        """
        DiagramDataValidator.validate_diagram_data(problem, categories)

        builder = DiagramBuilder(Problem(problem))
        for category_name, causes in categories.items():
            builder.add_category(category_name, causes)

        return builder.build()

    @staticmethod
    def save_diagram_to_file(
        problem: str,
        categories: Dict[str, List[str]],
        filename: str,
        dpi: int = 300
    ) -> Path:
        """
        Creates and saves a diagram to file.

        Args:
            problem: Problem description
            categories: Dictionary of categories and causes
            filename: Output filename
            dpi: Image resolution

        Returns:
            Path to saved file

        Raises:
            ValueError: If data is invalid
        """
        diagram = DiagramHelper.create_diagram_from_data(problem, categories)
        diagram.save(filename, dpi=dpi)
        return Path(filename)


