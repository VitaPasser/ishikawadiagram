# Ishikawa Diagram

A library for creating dynamic Ishikawa diagrams (fishbone diagrams) in Python.

## Description

The Ishikawa diagram is a tool for analyzing cause-and-effect relationships, used in quality management and problem-solving. The diagram visualizes various causes of a problem by grouping them into categories.

## Installation

Requires Python 3.7+ and the matplotlib library:

```bash
pip install matplotlib
```

## Usage

```python
from main import draw_dynamic_ishikawa

# Define the problem
problem = "THREAD BREAK"

# Define categories and causes
data = {
    "Machines": [
        "Bearing wear",
        "Vibration",
        "Old needle"
    ],
    "People": [
        "Fatigue"
    ],
    "Methods": [
        "Speed above normal",
        "No lubrication"
    ],
    "Materials": [
        "Thin thread",
        "Raw material defect"
    ]
}

# Draw the diagram
draw_dynamic_ishikawa(problem, data)
```

## Code Structure

### Classes

#### `IshikawaDiagramConfig`
Configuration class containing all diagram parameters:
- Sizes and distances
- Arrow styles
- Font sizes
- Scaling factors

#### `CategoryMetrics`
Class for calculating category metrics:
- Cause height
- Text width

### Functions

- `calculate_spine_length()` - calculates main spine length
- `draw_spine()` - draws the main spine of the diagram
- `calculate_bone_position()` - calculates category bone position
- `draw_category_bone()` - draws bone and category name
- `draw_cause()` - draws individual cause
- `draw_category_causes()` - draws all causes for a category
- `draw_dynamic_ishikawa()` - main function for creating the diagram

## Features

- **Dynamic scaling**: bone length adapts to the number of causes
- **Multi-line text**: support for multi-line causes using `\n`
- **Flexible configuration**: easily change styles and sizes through the configuration class
- **Automatic placement**: categories are automatically placed on both sides of the spine

## Examples

Run the `example.py` file to see an example usage:

```bash
python example.py
```

## License

MIT

