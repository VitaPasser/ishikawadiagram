from typing import Dict, List

from src.builder import DiagramBuilder
from src.domain.problem import Problem
from src.validation import DiagramDataValidator


def draw_dynamic_ishikawa(problem: str, data: Dict[str, List[str]]) -> None:
    """
    Facade function for quick diagram creation.
    Maintains backward compatibility with previous API.

    Args:
        problem: Problem name for analysis
        data: Dictionary {category: [list of causes]}

    Raises:
        ValueError: If input data is invalid
    """
    # Validate input data
    DiagramDataValidator.validate_diagram_data(problem, data)

    builder = DiagramBuilder(Problem(problem))

    for category_name, causes in data.items():
        builder.add_category(category_name, causes)

    diagram = builder.build()
    diagram.show()


