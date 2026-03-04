from typing import Dict, List

from src.builder import DiagramBuilder
from src.domain.problem import Problem


def draw_dynamic_ishikawa(problem: str, data: Dict[str, List[str]]) -> None:
    """
    Функция-фасад для быстрого создания диаграммы.
    Сохраняет обратную совместимость с предыдущим API.

    Args:
        problem: Название проблемы для анализа
        data: Словарь {категория: [список причин]}
    """
    builder = DiagramBuilder(Problem(problem))

    for category_name, causes in data.items():
        builder.add_category(category_name, causes)

    diagram = builder.build()
    diagram.show()


