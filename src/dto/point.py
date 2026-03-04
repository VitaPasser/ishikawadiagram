from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    """Неизменяемая точка на координатной плоскости."""
    x: float
    y: float
