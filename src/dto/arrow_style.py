from dataclasses import dataclass
from typing import Dict


@dataclass(frozen=True)
class ArrowStyle:
    """Стиль стрелки."""
    arrowstyle: str
    linewidth: float
    color: str
    shrink_a: int = 0
    shrink_b: int = 0

    def to_dict(self) -> Dict:
        """Преобразует в словарь для matplotlib."""
        return {
            'arrowstyle': self.arrowstyle,
            'lw': self.linewidth,
            'color': self.color,
            'shrinkA': self.shrink_a,
            'shrinkB': self.shrink_b
        }
