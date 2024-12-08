# data_loader.py
import json
import os
from tkinter import messagebox

def load_data(file_name):
    try:
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        messagebox.showerror("Error", f"File {file_name} tidak valid atau tidak ditemukan. Error: {str(e)}")
        return {}
