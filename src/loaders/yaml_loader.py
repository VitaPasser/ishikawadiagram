"""YAML file loader for Ishikawa diagrams."""

from pathlib import Path
from typing import Dict, List, Tuple, Union

import yaml


class YamlLoader:
    """Loads Ishikawa diagram data from YAML files and converts to dict format."""

    @staticmethod
    def load(file_path: Union[str, Path]) -> Tuple[str, Dict[str, List[str]]]:
        """
        Loads diagram data from YAML file.

        Converts YAML to (problem_name, data_dict) format for use with draw_dynamic_ishikawa.

        Args:
            file_path: Path to YAML file

        Returns:
            Tuple of (problem_name, data_dict) where data_dict is {category: [causes]}

        Raises:
            FileNotFoundError: If file doesn't exist
            yaml.YAMLError: If YAML parsing fails
            ValueError: If required fields are missing
        """
        file_path = Path(file_path)

        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        with open(file_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)

        return YamlLoader._parse_yaml_data(data)

    @staticmethod
    def load_from_string(yaml_content: str) -> Tuple[str, Dict[str, List[str]]]:
        """
        Loads diagram data from YAML string.

        Args:
            yaml_content: YAML content as string

        Returns:
            Tuple of (problem_name, data_dict)

        Raises:
            yaml.YAMLError: If YAML parsing fails
            ValueError: If required fields are missing
        """
        data = yaml.safe_load(yaml_content)
        return YamlLoader._parse_yaml_data(data)

    @staticmethod
    def _parse_yaml_data(data: dict) -> Tuple[str, Dict[str, List[str]]]:
        """
        Parses YAML data and converts to (problem_name, data_dict) format.

        Args:
            data: Parsed YAML data

        Returns:
            Tuple of (problem_name, data_dict)
        """
        if not data:
            raise ValueError("Empty YAML data")

        if 'problem' not in data:
            raise ValueError("Missing required field: 'problem'")

        if 'categories' not in data:
            raise ValueError("Missing required field: 'categories'")

        problem_name = data['problem']
        categories = data['categories']

        # Convert to simple dict format: {category: [cause1, cause2, ...]}
        if isinstance(categories, dict):
            # Dict format: {"Category Name": ["cause1", "cause2"]}
            data_dict = {k: v if isinstance(v, list) else [v]
                        for k, v in categories.items()}
        elif isinstance(categories, list):
            # List format: [{"name": "Category", "causes": ["cause1"]}]
            data_dict = {}
            for category in categories:
                if not isinstance(category, dict):
                    raise ValueError(f"Invalid category format: {category}")

                if 'name' not in category:
                    raise ValueError("Category missing 'name' field")

                causes = category.get('causes', [])
                if not isinstance(causes, list):
                    causes = [causes]

                data_dict[category['name']] = causes
        else:
            raise ValueError("'categories' must be a dict or list")

        return problem_name, data_dict

