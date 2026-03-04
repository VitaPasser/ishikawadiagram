from dataclasses import dataclass


@dataclass(frozen=True)
class TextStyle:
    """Стиль текста."""
    fontsize: int
    fontweight: str = 'normal'
    ha: str = 'center'
    va: str = 'center'
