"""Example of using YAML loader for Ishikawa diagrams."""

from src.loaders import YamlLoader
from main import draw_dynamic_ishikawa


def example_load_yaml():
    """Example: Load diagram from YAML file and display."""
    print("Loading diagram from YAML file...")

    # Load YAML and convert to (problem_name, data_dict)
    problem_name, data_set = YamlLoader.load('example_data.yaml')

    # Use the facade function
    draw_dynamic_ishikawa(problem_name, data_set)


def example_load_yaml_list_format():
    """Example: Load diagram from YAML with list format."""
    print("Loading diagram from YAML file (list format)...")

    problem_name, data_set = YamlLoader.load('example_data_list.yaml')
    draw_dynamic_ishikawa(problem_name, data_set)


def example_load_yaml_from_string():
    """Example: Load diagram from YAML string."""
    yaml_content = """
problem: "Low Product Quality"

categories:
  Materials:
    - Poor raw materials
    - Inconsistent supply
  
  Process:
    - Inadequate quality control
    - Equipment malfunction
  
  Personnel:
    - Lack of training
    - High turnover
    
  Materials2:
    - Poor raw materials
    - Inconsistent supply
  
  Process2:
    - Inadequate quality control
    - Equipment malfunction
  
  Personnel2:
    - Lack of training
    - High turnover
  
  Process2:
    - Inadequate quality control
    - Equipment malfunction
  
  Personnel2:
    - Lack of training
    - High turnover
    
  Materials22:
    - Poor raw materials
    - Inconsistent supply
  
  Process22:
    - Inadequate quality control
    - Equipment malfunction
  
  Personnel22:
    - Lack of training
    - High turnover
    
  Materials222:
    - Poor raw materials
    - Inconsistent supply
"""

    print("Loading diagram from YAML string...")
    problem_name, data_set = YamlLoader.load_from_string(yaml_content)

    draw_dynamic_ishikawa(problem_name, data_set)


def example_print_data():
    """Example: Print loaded data structure."""
    problem_name, data_set = YamlLoader.load('example_data.yaml')

    print(f"\nProblem: {problem_name}")
    print(f"Data structure:")
    for category, causes in data_set.items():
        print(f"  {category}: {causes}")


if __name__ == "__main__":
    # Run example
    example_load_yaml()

    # Uncomment to try other examples:
    # example_load_yaml_list_format()
    # example_load_yaml_from_string()
    # example_print_data()


