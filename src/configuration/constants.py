"""Default constants for diagram configuration."""


class DiagramDefaults:
    """Default values for Ishikawa diagram configuration."""

    # Dimensions
    X_STEP = 3.0
    Y_UNIT = 0.8
    ANGLE_OFFSET = 1.0
    LINE_HEIGHT_FACTOR = 0.2
    TEXT_WIDTH_FACTOR = 0.0625
    TEXT_LENGTH_FACTOR = 0.08

    # Arrow styles
    SPINE_ARROW_STYLE = '->'
    BONE_ARROW_STYLE = '->'
    CAUSE_ARROW_STYLE = '->'

    SPINE_LINEWIDTH = 2
    BONE_LINEWIDTH = 2
    CAUSE_LINEWIDTH = 1

    SPINE_COLOR = 'black'
    BONE_COLOR = 'black'
    CAUSE_COLOR = 'black'

    # Text styles
    TITLE_FONTSIZE = 16
    PROBLEM_FONTSIZE = 14
    CATEGORY_FONTSIZE = 12
    CAUSE_FONTSIZE = 10

    FONTWEIGHT_BOLD = 'bold'
    FONTWEIGHT_NORMAL = 'normal'

    # Text alignment
    TEXT_HA_CENTER = 'center'
    TEXT_HA_RIGHT = 'right'
    TEXT_HA_LEFT = 'left'

    TEXT_VA_CENTER = 'center'
    TEXT_VA_TOP = 'top'
    TEXT_VA_BOTTOM = 'bottom'

