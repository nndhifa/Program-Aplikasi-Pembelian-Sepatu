import tkinter as tk
from tkinter import messagebox


class TokoSepatuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pace and Stride")

        # Database sementara untuk akun dan produk
        self.akun = {}
        self.sepatu_lari = {
            "Normal": {
                "Jarak Pendek": [
                    {"nama": "Nike Speed Racer", "harga": 1200000, "deskripsi": "Ringan untuk lari sprint"},
                    {"nama": "Adidas Dash Pro", "harga": 1350000, "deskripsi": "Responsif untuk lari cepat"}
                ],
                "Jarak Menengah": [
                    {"nama": "ASICS Midrun Comfort", "harga": 1500000, "deskripsi": "Nyaman untuk lari jarak menengah"},
                    {"nama": "Saucony Endurance", "harga": 1300000, "deskripsi": "Dukungan optimal untuk lari stabil"}
                ],
                "Jarak Jauh": [
                    {"nama": "Brooks Marathon Master", "harga": 1800000, "deskripsi": "Desain khusus untuk marathon"},
                    {"nama": "Hoka Long Distance", "harga": 2000000, "deskripsi": "Maksimal peredam kejut untuk ultra run"}
                ]
            },
            "Sempit": {
                "Jarak Pendek": [
                    {"nama": "Nike Slim Race", "harga": 1100000, "deskripsi": "Desain khusus untuk kaki sempit"},
                    {"nama": "Mizuno Narrow Fit", "harga": 1250000, "deskripsi": "Pas untuk kaki langsing"}
                ],
                "Jarak Menengah": [
                    {"nama": "New Balance Slim Runner", "harga": 1400000, "deskripsi": "Dukungan optimal untuk kaki sempit"},
                    {"nama": "Skechers Narrow Path", "harga": 1150000, "deskripsi": "Ringan dan pas"}
                ],
                "Jarak Jauh": [
                    {"nama": "ASICS Precision Long", "harga": 1700000, "deskripsi": "Ultra marathon untuk kaki sempit"},
                    {"nama": "Altra Slim Distance", "harga": 1900000, "deskripsi": "Teknologi zero drop untuk kaki sempit"}
                ]
            },
            "Lebar": {
                "Jarak Pendek": [
                    {"nama": "Nike Wide Sprint", "harga": 1250000, "deskripsi": "Desain khusus untuk kaki lebar"},
                    {"nama": "Adidas Comfort Wide", "harga": 1300000, "deskripsi": "Ruang ekstra untuk jari kaki"}
                ],
                "Jarak Menengah": [
                    {"nama": "ASICS Wide Support", "harga": 1550000, "deskripsi": "Stabilitas maksimal untuk kaki lebar"},
                    {"nama": "Brooks Extra Room", "harga": 1450000, "deskripsi": "Desain ergonomis untuk kaki lebar"}
                ],
                "Jarak Jauh": [
                    {"nama": "Hoka Wide Marathon", "harga": 2100000, "deskripsi": "Ultra support untuk kaki lebar"},
                    {"nama": "Saucony Comfort Extreme", "harga": 1950000, "deskripsi": "Maksimal kenyamanan untuk kaki lebar"}
                ]
            }
        }

        self.barang_tambahan = [
            {"nama": "Kaos Lari Nike", "harga": 300000},
            {"nama": "Botol Minum", "harga": 50000},
            {"nama": "Topi Olahraga", "harga": 150000},
            {"nama": "Jam Tangan Lari", "harga": 800000},
            {"nama": "Kaos Kaki Lari", "harga": 100000},
            {"nama": "Celana Lari", "harga": 250000},
            {"nama": "Celana Lari2", "harga": 150000}
        ]
        
        self.keranjang = []
        self.total_harga = 0

        # Tampilkan halaman login awal
        self.show_login_screen()

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
