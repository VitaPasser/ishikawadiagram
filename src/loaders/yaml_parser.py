"""YAML data parser for Ishikawa diagrams."""

from typing import Dict, List, Tuple

import yaml


class YamlDataParser:
    """Parses YAML data and converts to diagram format."""

    @staticmethod
    def parse_yaml_data(data: dict) -> Tuple[str, Dict[str, List[str]]]:
        """
        Parses YAML data and converts to (problem_name, data_dict) format.

        Args:
            data: Parsed YAML data

        Returns:
            Tuple of (problem_name, data_dict)

        Raises:
            ValueError: If required fields are missing or invalid format
        """
        if not data:
            raise ValueError("Empty YAML data")

        if 'problem' not in data:
            raise ValueError("Missing required field: 'problem'")

        if 'categories' not in data:
            raise ValueError("Missing required field: 'categories'")

        problem_name = data['problem']
        categories = data['categories']

        data_dict = YamlDataParser._convert_categories(categories)
        return problem_name, data_dict

    @staticmethod
    def _convert_categories(categories) -> Dict[str, List[str]]:
        """
        Converts categories from various formats to standard dict format.

        Args:
            categories: Categories in dict or list format

        Returns:
            Dictionary {category_name: [causes]}

        Raises:
            ValueError: If format is invalid
        """
        if isinstance(categories, dict):
            return YamlDataParser._convert_dict_format(categories)
        elif isinstance(categories, list):
            return YamlDataParser._convert_list_format(categories)
        else:
            raise ValueError("'categories' must be a dict or list")

    @staticmethod
    def _convert_dict_format(categories_dict: dict) -> Dict[str, List[str]]:
        """
        Converts dict format: {"Category Name": ["cause1", "cause2"]}

        Args:
            categories_dict: Categories in dict format

        Returns:
            Converted dictionary
        """
        return {k: v if isinstance(v, list) else [v]
                for k, v in categories_dict.items()}

    @staticmethod
    def _convert_list_format(categories_list: list) -> Dict[str, List[str]]:
        """
        Converts list format: [{"name": "Category", "causes": ["cause1"]}]

        Args:
            categories_list: Categories in list format

        Returns:
            Converted dictionary

        Raises:
            ValueError: If category format is invalid
        """
        data_dict = {}
        for category in categories_list:
            if not isinstance(category, dict):
                raise ValueError(f"Invalid category format: {category}")

            if 'name' not in category:
                raise ValueError("Category missing 'name' field")

            causes = category.get('causes', [])
            if not isinstance(causes, list):
                causes = [causes]

            data_dict[category['name']] = causes

        return data_dict

