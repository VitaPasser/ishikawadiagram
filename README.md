# Ishikawa Diagram

A library for creating dynamic Ishikawa diagrams (fishbone diagrams) in Python.

## Description

The Ishikawa diagram is a tool for analyzing cause-and-effect relationships, used in quality management and problem-solving. The diagram visualizes various causes of a problem by grouping them into categories.

## Installation

Requires installed uv

```bash
uv sync
```

## Usage

### Method 1: Python Code

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

### Method 2: YAML File (Recommended)

Create a YAML file `diagram.yaml`:

```yaml
problem: "THREAD BREAK"

categories:
  Machines:
    - Bearing wear
    - Vibration
    - Old needle
  
  People:
    - Fatigue
  
  Methods:
    - Speed above normal
    - No lubrication
  
  Materials:
    - Thin thread
    - Raw material defect
```

Load and display:

```python
from src.loaders import YamlLoader
from main import draw_dynamic_ishikawa

# Load YAML and convert to dict format
problem_name, data = YamlLoader.load('diagram.yaml')

# Display diagram using facade function
draw_dynamic_ishikawa(problem_name, data)
```

Alternative YAML format with explicit structure:

```yaml
problem: "THREAD BREAK"

categories:
  - name: Machines
    causes:
      - Bearing wear
      - Vibration
  
  - name: People
    causes:
      - Fatigue
```

## License

MIT

