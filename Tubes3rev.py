import tkinter as tk
from tkinter import messagebox
from login_signup_module import LoginSignupModule
import json
import checkout_module # Import the checkout module

class TokoSepatuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pace and Stride")

        self.login_signup = LoginSignupModule()

        # Memuat data sepatu dan barang tambahan
        self.sepatu_lari = self.load_data(r"D:\\projectA\\TUBES\\sepatu_lari.json")
        self.barang_tambahan = self.load_data(r"D:\\projectA\\TUBES\\barang_tambahan.json")

        self.keranjang = []
        self.total_harga = 0

        self.login_signup.show_login_screen(
            self.root,
            on_login_success=self.show_main_menu,
            on_show_signup=self.show_signup_screen
        )

    def load_data(self, file_name):
        try:
            with open(file_name, "r", encoding="utf-8") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            messagebox.showerror("Error", str(e))
            return {}

    def show_main_menu(self):
        self.login_signup.clear_screen(self.root)
        tk.Label(self.root, text="Pace and Stride", font=("Arial", 24, "bold")).pack(pady=10)
        tk.Button(self.root, text="Panduan Tipe Kaki", command=self.show_panduan).pack(fill="x", pady=5)
        tk.Button(self.root, text="Cari Sepatu", command=self.show_cari_sepatu_menu).pack(fill="x", pady=5)
        tk.Button(self.root, text="Lihat Keranjang", command=self.show_keranjang).pack(fill="x", pady=5)
        tk.Button(self.root, text="Keluar", command=self.root.quit).pack(fill="x", pady=5)

    def show_signup_screen(self):
        self.login_signup.show_signup_screen(self.root, on_back_to_login=lambda: self.login_signup.show_login_screen(
            self.root,
            on_login_success=self.show_main_menu,
            on_show_signup=self.show_signup_screen
        ))



    def show_panduan(self):
        messagebox.showinfo(
            "Panduan Tipe Kaki",
            "1. Kaki Normal: Lebar kaki seimbang.\n"
            "2. Kaki Sempit: Jari-jari kaki berdempetan.\n"
            "3. Kaki Lebar: Jari-jari membutuhkan ruang ekstra."
        )

    def show_cari_sepatu_menu(self):
        self.clear_screen()

        tk.Label(self.root, text="Pilih Tipe Kaki", font=("Arial", 16)).pack(pady=10)

        self.tipe_kaki_var = tk.StringVar(value="Normal")
        for tipe in self.sepatu_lari.keys():
            tk.Radiobutton(self.root, text=tipe, variable=self.tipe_kaki_var, value=tipe).pack(anchor="w")

        tk.Button(self.root, text="Lanjut", command=self.show_jarak_lari_menu).pack(pady=10)

    def show_jarak_lari_menu(self):
        tipe_kaki = self.tipe_kaki_var.get()
        self.clear_screen()

        tk.Label(self.root, text=f"Pilih Jarak Lari untuk Kaki {tipe_kaki}", font=("Arial", 16)).pack(pady=10)

        self.jarak_var = tk.StringVar(value="Jarak Pendek")
        for jarak in self.sepatu_lari[tipe_kaki].keys():
            tk.Radiobutton(self.root, text=jarak, variable=self.jarak_var, value=jarak).pack(anchor="w")

        tk.Button(self.root, text="Lihat Rekomendasi", command=lambda: self.show_rekomendasi(tipe_kaki)).pack(pady=10)

    def show_rekomendasi(self, tipe_kaki):
        jarak = self.jarak_var.get()
        rekomendasi = self.sepatu_lari[tipe_kaki].get(jarak, [])
        self.clear_screen()

        tk.Label(self.root, text=f"Rekomendasi Sepatu ({tipe_kaki} - {jarak})", font=("Arial", 16)).pack(pady=10)

        for sepatu in rekomendasi:
        # Menampilkan tombol untuk memilih sepatu
            button = tk.Button(
                self.root,
                text=f"{sepatu['nama']} - Rp {sepatu['harga']:,}",
                command=lambda s=sepatu: self.show_ukuran_menu(s)
        )
            button.pack(fill="x", pady=5)

        tk.Button(self.root, text="Kembali ke Menu Utama", command=self.show_main_menu).pack(pady=10)
        
    def show_ukuran_menu(self, sepatu):
        self.clear_screen()

        tk.Label(self.root, text=f"Pilih Ukuran untuk {sepatu['nama']}", font=("Arial", 16)).pack(pady=10)

    # Menampilkan ukuran sepatu yang tersedia
        for ukuran in sepatu['ukuran']:
            tk.Button(
                self.root,
                text=f"Ukuran {ukuran}",
                command=lambda u=ukuran, s=sepatu: self.add_to_cart_with_size(s, u)
            ).pack(fill="x", pady=5)

        tk.Button(self.root, text="Kembali", command=self.show_rekomendasi).pack(pady=10)

    def add_to_cart_with_size(self, sepatu, ukuran):
        sepatu_terpilih = sepatu.copy()
        sepatu_terpilih['ukuran'] = ukuran  # Menambahkan ukuran sepatu yang dipilih
        self.keranjang.append(sepatu_terpilih)
        self.total_harga += sepatu['harga']
        messagebox.showinfo("Keranjang", f"{sepatu_terpilih['nama']} (Ukuran {ukuran}) berhasil ditambahkan ke keranjang.")
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
     # Menggunakan modul checkout untuk menampilkan layar checkout
        self.bayar_entry = tk.Entry(self.root)
        checkout_module.checkout(self.root, self.keranjang, self.total_harga, self.bayar_entry, self.clear_screen, self.show_main_menu)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()


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
