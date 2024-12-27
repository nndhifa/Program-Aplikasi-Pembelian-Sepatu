import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from data_management import load_data, save_history, load_history
from user_auth import load_akun, save_akun
import os

class TokoSepatuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pace and Stride")
        self.akun = load_akun()
        self.sepatu_lari = load_data("sepatu_lari_daniel.json")
        self.barang_tambahan = load_data("barang_tambahan_daniel.json")
        self.keranjang = []
        self.total_harga = 0
        self.history = load_history()
        self.current_user = None
        self.show_login_screen()

    def show_login_screen(self):
        self.clear_screen()

        bg_image = Image.open("background_login.jpg")
        bg_image = bg_image.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(bg_image)

        bg_label = tk.Label(self.root, image=self.bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        tk.Label(self.root, text="Login", font=("Segoe UI Semibold", 20, "bold", "italic"), bg="#282c66", fg="#ccf73b").pack(pady=10)

        tk.Label(self.root, text="Username:", bg="#ccf73b", fg="#323774").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(pady=5)

        tk.Label(self.root, text="Password:", bg="#ccf73b", fg="#323774").pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack(pady=5)

        tk.Button(self.root, text="Login", bg="#ccf73b", fg="#323774", command=self.login).pack(pady=10)
        tk.Button(self.root, text="Sign Up", bg="#ccf73b", fg="#323774", command=self.show_signup_screen).pack(pady=5)

    def show_signup_screen(self):
        self.clear_screen()

        bg_image = Image.open("background_signup.jpg")
        bg_image = bg_image.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()), Image.Resampling.LANCZOS)
        self.bg_photo_signup = ImageTk.PhotoImage(bg_image)

        bg_label = tk.Label(self.root, image=self.bg_photo_signup)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        tk.Label(self.root, text="Sign Up", font=("Segoe UI Semibold", 20, "bold", "italic"), bg="#282c66", fg="#ccf73b").pack(pady=10)

        tk.Label(self.root, text="Username:", bg="#ccf73b", fg="#323774").pack()
        self.new_username_entry = tk.Entry(self.root)
        self.new_username_entry.pack(pady=5)

        tk.Label(self.root, text="Password:", bg="#ccf73b", fg="#323774").pack()
        self.new_password_entry = tk.Entry(self.root, show="*")
        self.new_password_entry.pack(pady=5)

        tk.Button(self.root, text="Register", bg="#ccf73b", fg="#323774", command=self.register).pack(pady=10)
        tk.Button(self.root, text="Back to Login", bg="#ccf73b", fg="#323774", command=self.show_login_screen).pack(pady=5)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username in self.akun and self.akun[username] == password:
            self.current_user = username
            self.show_main_menu()
        else:
            messagebox.showerror("Login Gagal", "Username atau password salah.")

    def register(self):
        username = self.new_username_entry.get()
        password = self.new_password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "Username dan password tidak boleh kosong.")
            return

        if username in self.akun:
            messagebox.showerror("Error", "Username sudah terdaftar.")
        else:
            self.akun[username] = password
            save_akun(self.akun)
            messagebox.showinfo("Sukses", "Pendaftaran berhasil!")
            self.show_login_screen()

    def show_main_menu(self):
        self.clear_screen()

        tk.Label(self.root, text="Pace&Stride", font=("Rockwell Extra Bold", 30, "bold", "italic"), bg="#282c66", fg="#ccf73b").pack(pady=10)
        tk.Button(self.root, text="Panduan Tipe Kaki", command=self.show_panduan, font=("Segoe UI Semibold", 14), width=20, padx=7, pady=5, bg="#ccf73b", fg="#323774").pack(pady=5)
        tk.Button(self.root, text="Cari Sepatu", command=self.show_cari_sepatu_menu, font=("Segoe UI Semibold", 14), width=20, padx=7, pady=5, bg="#ccf73b", fg="#323774").pack(pady=5)
        tk.Button(self.root, text="Lihat Keranjang", command=self.show_keranjang, font=("Segoe UI Semibold", 14), width=20, padx=7, pady=5, bg="#ccf73b", fg="#323774").pack(pady=5)
        tk.Button(self.root, text="Riwayat Pembelian", command=self.show_riwayat_pembelian, font=("Segoe UI Semibold", 14), width=20, padx=7, pady=5, bg="#ccf73b", fg="#323774").pack(pady=5)
        tk.Button(self.root, text="Keluar", command=self.root.quit, font=("Segoe UI Semibold", 14), width=20, padx=7, pady=5, bg="#ccf73b", fg="#323774").pack(pady=5)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
