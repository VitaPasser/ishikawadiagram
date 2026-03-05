"""Factory for creating predefined diagram styles and configurations."""

from src.dto.arrow_style import ArrowStyle
from src.dto.text_style import TextStyle
from src.dto.diagram_dimensions import DiagramDimensions
from src.configuration.constants import DiagramDefaults


class DiagramStyleFactory:
    """Factory for creating predefined diagram styles."""

    @staticmethod
    def create_spine_arrow() -> ArrowStyle:
        """Creates default spine arrow style."""
        return ArrowStyle(
            arrowstyle=DiagramDefaults.SPINE_ARROW_STYLE,
            linewidth=DiagramDefaults.SPINE_LINEWIDTH,
            color=DiagramDefaults.SPINE_COLOR
        )

    @staticmethod
    def create_bone_arrow() -> ArrowStyle:
        """Creates default bone arrow style."""
        return ArrowStyle(
            arrowstyle=DiagramDefaults.BONE_ARROW_STYLE,
            linewidth=DiagramDefaults.BONE_LINEWIDTH,
            color=DiagramDefaults.BONE_COLOR
        )

    @staticmethod
    def create_cause_arrow() -> ArrowStyle:
        """Creates default cause arrow style."""
        return ArrowStyle(
            arrowstyle=DiagramDefaults.CAUSE_ARROW_STYLE,
            linewidth=DiagramDefaults.CAUSE_LINEWIDTH,
            color=DiagramDefaults.CAUSE_COLOR
        )

    @staticmethod
    def create_title_style() -> TextStyle:
        """Creates default title text style."""
        return TextStyle(
            fontsize=DiagramDefaults.TITLE_FONTSIZE,
            fontweight=DiagramDefaults.FONTWEIGHT_BOLD
        )

    @staticmethod
    def create_problem_style() -> TextStyle:
        """Creates default problem text style."""
        return TextStyle(
            fontsize=DiagramDefaults.PROBLEM_FONTSIZE,
            fontweight=DiagramDefaults.FONTWEIGHT_BOLD,
            ha=DiagramDefaults.TEXT_HA_LEFT
        )

    @staticmethod
    def create_category_style() -> TextStyle:
        """Creates default category text style."""
        return TextStyle(
            fontsize=DiagramDefaults.CATEGORY_FONTSIZE,
            fontweight=DiagramDefaults.FONTWEIGHT_BOLD
        )

    @staticmethod
    def create_cause_style() -> TextStyle:
        """Creates default cause text style."""
        return TextStyle(
            fontsize=DiagramDefaults.CAUSE_FONTSIZE,
            ha=DiagramDefaults.TEXT_HA_RIGHT,
            va=DiagramDefaults.TEXT_VA_BOTTOM
        )

    @staticmethod
    def create_default_dimensions() -> DiagramDimensions:
        """Creates default diagram dimensions."""
        return DiagramDimensions(
            x_step=DiagramDefaults.X_STEP,
            y_unit=DiagramDefaults.Y_UNIT,
            angle_offset=DiagramDefaults.ANGLE_OFFSET,
            line_height_factor=DiagramDefaults.LINE_HEIGHT_FACTOR,
            text_width_factor=DiagramDefaults.TEXT_WIDTH_FACTOR,
            text_length_factor=DiagramDefaults.TEXT_LENGTH_FACTOR
        )

