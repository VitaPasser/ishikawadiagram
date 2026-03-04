"""Example usage of Ishikawa diagram."""

from main import draw_dynamic_ishikawa


def main():
    """Run example with diagram."""
    problem_name = "THREAD BREAK"

    data_set = {
        "Machines": [
            "Bearing wear\nBearing wear\nBearing wear\nBearing wear\nBearing wear\nBearing wear",
            "Vibration",
            "Old needle\nOld needle",
            "Overheating"
        ],
        "People": ["Fatigue"],
        "Methods": ["Speed above normal", "No lubrication"],
        "Materials": ["Thin thread", "Raw material defect", "Humidity"],
        "Environment": ["Dust"],
        "Measurements": ["Sensor error", "Calibration"]
    }

    draw_dynamic_ishikawa(problem_name, data_set)


if __name__ == "__main__":
    main()

