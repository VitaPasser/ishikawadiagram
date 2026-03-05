import argparse
import sys
from typing import Dict, List

from src.builder import DiagramBuilder
from src.domain.problem import Problem
from src.loaders import YamlLoader
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


def save_dynamic_ishikawa(path: str, problem: str, data: Dict[str, List[str]]) -> None:
    """
    Facade function for quick diagram creation.
    Maintains backward compatibility with previous API.

    Args:
        path: Path to save the diagram image
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
    diagram.save(path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Dynamic Ishikawa Diagram Generator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py example_data.yaml output.png
  python main.py path/to/your/data.yaml path/to/save/diagram.png
        """
    )
    parser.add_argument(
        "yaml_file",
        type=str,
        help="Path to the YAML file containing diagram data (with problem and categories)",
    )
    parser.add_argument(
        "save_to",
        type=str,
        help="Path to save the generated diagram image (e.g., output.png)",
    )

    args = parser.parse_args()

    # Load data from YAML file
    try:
        problem_name, data = YamlLoader.load(args.yaml_file)
        print(f"Loaded diagram: '{problem_name}' with {len(data)} categories")
    except FileNotFoundError:
        print(f"Error: File '{args.yaml_file}' not found", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error loading YAML file: {e}", file=sys.stderr)
        sys.exit(1)

    save_dynamic_ishikawa(args.save_to, problem_name, data)
