from database import load_data, save_data
import os

class UserManagement:
    def __init__(self):
        self.file_path = os.path.join(os.path.dirname(__file__), "akun.json")
        self.akun = load_data(self.file_path)

    def login(self, username, password):
        """Memeriksa kredensial login pengguna."""
        return self.akun.get(username) == password

    def register(self, username, password):
        """Mendaftarkan pengguna baru."""
        if username in self.akun:
            return False  # Username sudah ada
        self.akun[username] = password
        save_data(self.file_path, self.akun)
        return True
