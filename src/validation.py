"""Data validation utilities for diagram inputs."""

from typing import Dict, List


class DiagramDataValidator:
    """Validates diagram data for correctness."""

    @staticmethod
    def validate_problem_name(problem: str) -> bool:
        """
        Validates problem name.

        Args:
            problem: Problem description

        Returns:
            True if valid

        Raises:
            ValueError: If invalid
        """
        if not problem or not isinstance(problem, str):
            raise ValueError("Problem must be a non-empty string")
        if len(problem.strip()) == 0:
            raise ValueError("Problem cannot be empty or whitespace")
        return True

    @staticmethod
    def validate_causes(causes: List[str]) -> bool:
        """
        Validates causes list.

        Args:
            causes: List of cause descriptions

        Returns:
            True if valid

        Raises:
            ValueError: If invalid
        """
        if not isinstance(causes, list):
            raise ValueError("Causes must be a list")
        if len(causes) == 0:
            raise ValueError("Causes list cannot be empty")
        for cause in causes:
            if not isinstance(cause, str) or len(cause.strip()) == 0:
                raise ValueError("Each cause must be a non-empty string")
        return True

    @staticmethod
    def validate_categories(categories: Dict[str, List[str]]) -> bool:
        """
        Validates categories dictionary.

        Args:
            categories: Dictionary of category names to causes

        Returns:
            True if valid

        Raises:
            ValueError: If invalid
        """
        if not isinstance(categories, dict):
            raise ValueError("Categories must be a dictionary")
        if len(categories) == 0:
            raise ValueError("Categories cannot be empty")

        for category_name, causes in categories.items():
            if not isinstance(category_name, str) or len(category_name.strip()) == 0:
                raise ValueError("Category name must be a non-empty string")
            DiagramDataValidator.validate_causes(causes)

        return True

    @staticmethod
    def validate_diagram_data(problem: str, categories: Dict[str, List[str]]) -> bool:
        """
        Validates complete diagram data.

        Args:
            problem: Problem description
            categories: Dictionary of categories and causes

        Returns:
            True if valid

        Raises:
            ValueError: If invalid
        """
        DiagramDataValidator.validate_problem_name(problem)
        DiagramDataValidator.validate_categories(categories)
        return True

