from src.dto.diagram_dimensions import DiagramDimensions
from src.dto.text_style import TextStyle
from src.dto.arrow_style import ArrowStyle


class DiagramConfig:
    """
    Diagram configuration (Single Responsibility).
    Responsible only for storing settings.
    """

    def __init__(
        self,
        dimensions: DiagramDimensions = None,
        spine_arrow: ArrowStyle = None,
        bone_arrow: ArrowStyle = None,
        cause_arrow: ArrowStyle = None,
        title_style: TextStyle = None,
        problem_style: TextStyle = None,
        category_style: TextStyle = None,
        cause_style: TextStyle = None
    ):
        self.dimensions = dimensions or DiagramDimensions(
            x_step=3.0,
            y_unit=0.8,
            angle_offset=1.0,
            line_height_factor=0.2,
            text_width_factor=0.0625,
            text_length_factor=0.08
        )

        self.spine_arrow = spine_arrow or ArrowStyle(
            arrowstyle='->',
            linewidth=2,
            color='black'
        )

        self.bone_arrow = bone_arrow or ArrowStyle(
            arrowstyle='->',
            linewidth=2,
            color='navy'
        )

        self.cause_arrow = cause_arrow or ArrowStyle(
            arrowstyle='->',
            linewidth=1,
            color='gray'
        )

        self.title_style = title_style or TextStyle(fontsize=16, fontweight='bold')
        self.problem_style = problem_style or TextStyle(fontsize=14, fontweight='bold', ha='left')
        self.category_style = category_style or TextStyle(fontsize=12, fontweight='bold')
        self.cause_style = cause_style or TextStyle(fontsize=10, ha='right', va='bottom')
