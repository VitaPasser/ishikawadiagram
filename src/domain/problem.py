class Problem:
    """Проблема для анализа (Domain Model)."""

    def __init__(self, description: str):
        self._description = description

    @property
    def description(self) -> str:
        """Возвращает описание проблемы."""
        return self._description
