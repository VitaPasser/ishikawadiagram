from dataclasses import dataclass


@dataclass(frozen=True)
class DiagramDimensions:
    """Размеры диаграммы."""
    x_step: float
    y_unit: float
    angle_offset: float
    line_height_factor: float
    text_width_factor: float
    text_length_factor: float
