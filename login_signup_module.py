# login_signup_module.py
import tkinter as tk
from tkinter import messagebox

class LoginSignupModule:
    def __init__(self):
        # Database sementara untuk akun
        self.akun = {}

    def show_login_screen(self, root, on_login_success, on_show_signup):
        self.clear_screen(root)

        tk.Label(root, text="Login", font=("Arial", 20, "bold")).pack(pady=10)

        tk.Label(root, text="Username:").pack()
        username_entry = tk.Entry(root)
        username_entry.pack()

        tk.Label(root, text="Password:").pack()
        password_entry = tk.Entry(root, show="*")
        password_entry.pack()

        tk.Button(root, text="Login", command=lambda: self.login(username_entry.get(), password_entry.get(), on_login_success)).pack(pady=5)
        tk.Button(root, text="Sign Up", command=on_show_signup).pack(pady=5)

    def show_signup_screen(self, root, on_back_to_login):
        self.clear_screen(root)

        tk.Label(root, text="Sign Up", font=("Arial", 20, "bold")).pack(pady=10)

        tk.Label(root, text="Username:").pack()
        new_username_entry = tk.Entry(root)
        new_username_entry.pack()

        tk.Label(root, text="Password:").pack()
        new_password_entry = tk.Entry(root, show="*")
        new_password_entry.pack()

        tk.Button(root, text="Register", command=lambda: self.register(new_username_entry.get(), new_password_entry.get(), root, on_back_to_login)).pack(pady=5)
        tk.Button(root, text="Back to Login", command=on_back_to_login).pack(pady=5)

    def login(self, username, password, on_success):
        if username in self.akun and self.akun[username] == password:
            on_success()
        else:
            messagebox.showerror("Login Gagal", "Username atau password salah.")

    def register(self, username, password, root, on_back_to_login):
        if username in self.akun:
            messagebox.showerror("Error", "Username sudah terdaftar.")
        else:
            self.akun[username] = password
            messagebox.showinfo("Sukses", "Pendaftaran berhasil!")
            on_back_to_login()

    def clear_screen(self, root):
        for widget in root.winfo_children():
            widget.destroy()
