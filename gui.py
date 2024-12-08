import tkinter as tk
from tkinter import messagebox
from user_management import UserManagement
from cart_management import CartManagement
from database import load_data

class TokoSepatuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pace and Stride")
        self.user_manager = UserManagement()
        self.cart_manager = CartManagement()
        self.sepatu_lari = load_data("sepatu_lari_daniel.json")
        self.barang_tambahan = load_data("barang_tambahan_daniel.json")
        self.show_login_screen()

    def show_login_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Login", font=("Arial", 20)).pack(pady=10)
        tk.Label(self.root, text="Username").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(pady=5)
        tk.Label(self.root, text="Password").pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack(pady=5)
        tk.Button(self.root, text="Login", command=self.login).pack(pady=10)
        tk.Button(self.root, text="Sign Up", command=self.show_signup_screen).pack(pady=5)

    def show_signup_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Sign Up", font=("Arial", 20)).pack(pady=10)
        tk.Label(self.root, text="Username").pack()
        self.new_username_entry = tk.Entry(self.root)
        self.new_username_entry.pack(pady=5)
        tk.Label(self.root, text="Password").pack()
        self.new_password_entry = tk.Entry(self.root, show="*")
        self.new_password_entry.pack(pady=5)
        tk.Button(self.root, text="Register", command=self.register).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.show_login_screen).pack(pady=5)

    def show_main_menu(self):
        self.clear_screen()
        tk.Label(self.root, text="Main Menu", font=("Arial", 20)).pack(pady=10)
        tk.Button(self.root, text="Cari Sepatu", command=self.show_cari_sepatu_menu).pack(pady=10)
        tk.Button(self.root, text="Lihat Keranjang", command=self.show_keranjang).pack(pady=10)
        tk.Button(self.root, text="Keluar", command=self.root.quit).pack(pady=10)

    def show_cari_sepatu_menu(self):
        self.clear_screen()
        tk.Label(self.root, text="Pilih Tipe Kaki").pack(pady=10)
        self.tipe_kaki_var = tk.StringVar(value="Normal")
        for tipe in self.sepatu_lari.keys():
            tk.Radiobutton(self.root, text=tipe, variable=self.tipe_kaki_var, value=tipe).pack()
        tk.Button(self.root, text="Lanjut", command=self.show_jarak_lari_menu).pack(pady=10)

    def show_keranjang(self):
        self.clear_screen()
        tk.Label(self.root, text="Keranjang").pack(pady=10)
        for item in self.cart_manager.keranjang:
            tk.Label(self.root, text=f"{item['nama']} - Rp {item['harga']:,}").pack()
        tk.Label(self.root, text=f"Total: Rp {self.cart_manager.get_total():,}").pack(pady=10)
        tk.Button(self.root, text="Checkout", command=self.checkout).pack(pady=10)

    def checkout(self):
        messagebox.showinfo("Checkout", f"Total: Rp {self.cart_manager.get_total():,}")
        self.cart_manager.clear_cart()
        self.show_main_menu()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if self.user_manager.login(username, password):
            self.show_main_menu()
        else:
            messagebox.showerror("Error", "Login Gagal!")

    def register(self):
        username = self.new_username_entry.get()
        password = self.new_password_entry.get()
        if self.user_manager.register(username, password):
            messagebox.showinfo("Info", "Pendaftaran Berhasil!")
            self.show_login_screen()
        else:
            messagebox.showerror("Error", "Username sudah terdaftar.")

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
