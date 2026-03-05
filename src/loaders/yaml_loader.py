"""YAML file loader for Ishikawa diagrams."""

from pathlib import Path
from typing import Dict, List, Tuple, Union

import yaml

from src.loaders.yaml_parser import YamlDataParser


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

        return YamlDataParser.parse_yaml_data(data)

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
        return YamlDataParser.parse_yaml_data(data)

