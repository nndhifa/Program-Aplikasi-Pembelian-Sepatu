import tkinter as tk
from tkinter import messagebox
import json


class TokoSepatuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pace and Stride")

        # Load data dari file JSON
        self.akun = self.load_data("account.json", default={})
        self.sepatu_lari = self.load_data("sepatu.json", default={})
        self.barang_tambahan = self.load_data("barang_tambahan.json", default=[])

        self.keranjang = []
        self.total_harga = 0

        # Tampilkan halaman login awal
        self.show_login_screen()

    def load_data(self, filename, default):
        """Membaca data dari file JSON atau mengembalikan nilai default."""
        try:
            with open(filename, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return default

    def save_data(self, filename, data):
        """Menyimpan data ke file JSON."""
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

    def show_login_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="Login", font=("Arial", 20, "bold")).pack(pady=10)

        tk.Label(self.root, text="Username:").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()

        tk.Label(self.root, text="Password:").pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()

        tk.Button(self.root, text="Login", command=self.login).pack(pady=5)
        tk.Button(self.root, text="Sign Up", command=self.show_signup_screen).pack(pady=5)

    def show_signup_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="Sign Up", font=("Arial", 20, "bold")).pack(pady=10)

        tk.Label(self.root, text="Username:").pack()
        self.new_username_entry = tk.Entry(self.root)
        self.new_username_entry.pack()

        tk.Label(self.root, text="Password:").pack()
        self.new_password_entry = tk.Entry(self.root, show="*")
        self.new_password_entry.pack()

        tk.Button(self.root, text="Register", command=self.register).pack(pady=5)
        tk.Button(self.root, text="Back to Login", command=self.show_login_screen).pack(pady=5)

    def show_main_menu(self):
        self.clear_screen()

        tk.Label(self.root, text="Pace and Stride", font=("Arial", 24, "bold")).pack(pady=10)

        tk.Button(self.root, text="Panduan Tipe Kaki", command=self.show_panduan).pack(fill="x", pady=5)
        tk.Button(self.root, text="Cari Sepatu", command=self.show_cari_sepatu_menu).pack(fill="x", pady=5)
        tk.Button(self.root, text="Lihat Keranjang", command=self.show_keranjang).pack(fill="x", pady=5)
        tk.Button(self.root, text="Keluar", command=self.root.quit).pack(fill="x", pady=5)

    def show_panduan(self):
        messagebox.showinfo(
            "Panduan Tipe Kaki",
            "1. Kaki Normal: Lebar kaki seimbang.\n"
            "2. Kaki Sempit: Jari-jari kaki berdempetan.\n"
            "3. Kaki Lebar: Jari-jari membutuhkan ruang ekstra."
        )
        
    def show_panduan_jarak(self):
        messagebox.showinfo(
            "1. Pendek: Kurang dari 5 km.\n"
            "2. Menengah: 5 km hingga 10 km.\n"
            "3. Jauh: Lebih dari 10 km.\n"
        )

    def show_cari_sepatu_menu(self):
        self.clear_screen()

        tk.Label(self.root, text="Pilih Tipe Kaki", font=("Arial", 16)).pack(pady=10)

        self.tipe_kaki_var = tk.StringVar(value="Normal")
        for tipe in ["Normal", "Sempit", "Lebar"]:
            tk.Radiobutton(self.root, text=tipe, variable=self.tipe_kaki_var, value=tipe).pack(anchor="w")

        tk.Button(self.root, text="Lanjut", command=self.show_jarak_lari_menu).pack(pady=10)

    def show_jarak_lari_menu(self):
        tipe_kaki = self.tipe_kaki_var.get()
        self.clear_screen()

        tk.Label(self.root, text=f"Pilih Jarak Lari untuk Kaki {tipe_kaki}", font=("Arial", 16)).pack(pady=10)

        self.jarak_var = tk.StringVar(value="Jarak Pendek")
        for jarak in ["Jarak Pendek", "Jarak Menengah", "Jarak Jauh"]:
            tk.Radiobutton(self.root, text=jarak, variable=self.jarak_var, value=jarak).pack(anchor="w")

        tk.Button(self.root, text="Lihat Rekomendasi", command=lambda: self.show_rekomendasi(tipe_kaki)).pack(pady=10)

    def show_rekomendasi(self, tipe_kaki):
        jarak = self.jarak_var.get()
        rekomendasi = self.sepatu_lari[tipe_kaki].get(jarak, [])
        self.clear_screen()

        tk.Label(self.root, text=f"Rekomendasi Sepatu ({tipe_kaki} - {jarak})", font=("Arial", 16)).pack(pady=10)

        for sepatu in rekomendasi:
            tk.Button(
                self.root,
                text=f"{sepatu['nama']} - Rp {sepatu['harga']:,}",
                command=lambda s=sepatu: self.add_to_cart(s)
            ).pack(fill="x", pady=5)

        tk.Button(self.root, text="Kembali ke Menu Utama", command=self.show_main_menu).pack(pady=10)

    def add_to_cart(self, sepatu):
        self.keranjang.append(sepatu)
        self.total_harga += sepatu['harga']
        messagebox.showinfo("Keranjang", f"{sepatu['nama']} berhasil ditambahkan ke keranjang.")
        
        # Menampilkan pilihan untuk melanjutkan menambah aksesoris
        self.show_tambah_barang()

    def show_tambah_barang(self):
        self.clear_screen()

        tk.Label(self.root, text="Tambahkan Barang Lain?", font=("Arial", 16)).pack(pady=10)
        for barang in self.barang_tambahan:
            tk.Button(
                self.root,
                text=f"{barang['nama']} - Rp {barang['harga']:,}",
                command=lambda b=barang: self.add_to_cart(b)
            ).pack(fill="x", pady=5)

        tk.Button(self.root, text="Lihat Keranjang", command=self.show_keranjang).pack(pady=10)

    def show_keranjang(self):
        self.clear_screen()

        tk.Label(self.root, text="Keranjang Belanja", font=("Arial", 20, "bold")).pack(pady=10)
        for item in self.keranjang:
            tk.Label(self.root, text=f"{item['nama']} - Rp {item['harga']:,}").pack()

        tk.Label(self.root, text=f"\nTotal Harga: Rp {self.total_harga:,}", font=("Arial", 16)).pack(pady=10)
        tk.Button(self.root, text="Checkout", command=self.checkout).pack(pady=5)
        tk.Button(self.root, text="Kembali ke Menu Utama", command=self.show_main_menu).pack(pady=5)

    def checkout(self):
        self.clear_screen()

        tk.Label(self.root, text="Pembayaran", font=("Arial", 20, "bold")).pack(pady=10)
        tk.Label(self.root, text=f"Total Harga: Rp {self.total_harga:,}").pack(pady=10)

        tk.Label(self.root, text="Masukkan jumlah uang pembayaran:").pack()
        self.bayar_entry = tk.Entry(self.root)
        self.bayar_entry.pack()

        tk.Button(self.root, text="Bayar", command=self.proses_pembayaran).pack(pady=10)

    def proses_pembayaran(self):
        try:
            bayar = int(self.bayar_entry.get())
            if bayar >= self.total_harga:
                kembalian = bayar - self.total_harga
                messagebox.showinfo("Pembayaran Berhasil", f"Pembayaran berhasil!\nKembalian: Rp {kembalian:,}")
                self.keranjang.clear()
                self.total_harga = 0
                self.show_main_menu()
            else:
                messagebox.showerror("Pembayaran Gagal", "Jumlah uang tidak cukup.")
        except ValueError:
            messagebox.showerror("Error", "Masukkan jumlah uang yang valid.")

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username in self.akun and self.akun[username] == password:
            self.show_main_menu()
        else:
            messagebox.showerror("Login Gagal", "Username atau password salah.")

    def register(self):
        username = self.new_username_entry.get()
        password = self.new_password_entry.get()

        if username in self.akun:
            messagebox.showerror("Error", "Username sudah terdaftar.")
        else:
            self.akun[username] = password
            self.save_data("account.json", self.akun)
            messagebox.showinfo("Sukses", "Pendaftaran berhasil!")
            self.show_login_screen()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()


# Jalankan aplikasi
if __name__ == "__main__":
    root = tk.Tk()
    app = TokoSepatuApp(root)
    root.mainloop()
