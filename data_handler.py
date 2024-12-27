import os
import json
from tkinter import messagebox

def load_data(file_name):
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(base_dir, file_name)
        with open(full_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        messagebox.showerror("Error", f"File {file_name} tidak ditemukan.")
        return {}
    except json.JSONDecodeError:
        messagebox.showerror("Error", f"Format file {file_name} tidak valid.")
        return {}

def save_data(data, file_name):
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(base_dir, file_name)
        with open(full_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        messagebox.showerror("Error", f"Gagal menyimpan file {file_name}: {e}")
