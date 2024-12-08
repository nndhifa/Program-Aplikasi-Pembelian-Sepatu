import json
import os

def load_data(file_name):
    """Memuat data dari file JSON."""
    try:
        full_path = os.path.join(os.path.dirname(__file__), file_name)
        with open(full_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_data(file_name, data):
    """Menyimpan data ke file JSON."""
    full_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(full_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
