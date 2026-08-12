import json
from pathlib import Path


# __file__ is the location of this utils.py file.
# .parent gives us the ecommerce_engine directory.
#
# So this works regardless of where we run:
# python main.py
#
# data.json will always be looked for beside utils.py.
BASE_DIR = Path(__file__).resolve().parent

DATA_FILE = BASE_DIR / "data.json"


def load_data():
    """Load data from data.json."""

    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        # If the file doesn't exist yet, return
        # an empty data structure.
        return {
            "products": []
        }

    except json.JSONDecodeError:
        raise ValueError("data.json contains invalid JSON.")


def save_data(data):
    """Save data to data.json."""

    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)
