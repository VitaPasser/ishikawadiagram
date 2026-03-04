class Problem:
    """Problem for analysis (Domain Model)."""

    def __init__(self, description: str):
        self._description = description

    @property
    def description(self) -> str:
        """Returns problem description."""
        return self._description
