import tkinter as tk
from tkinter import messagebox
import json
from PIL import Image, ImageTk
import os

class TokoSepatuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pace and Stride")

        # Data akun permanen
        self.accounts = self.load_accounts()

        # Keranjang belanja
        self.keranjang = []
        self.total_harga = 0

        # Tampilkan halaman login awal
        self.show_login_screen()

    def load_accounts(self, file_name="accounts.json"):
        try:
            with open(file_name, "r", encoding="utf-8") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_accounts(self, accounts, file_name="accounts.json"):
        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(accounts, file, indent=4)

    def show_login_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="Login", font=("Segoe UI", 20, "bold")).pack(pady=10)

        tk.Label(self.root, text="Username:").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(pady=5)

        tk.Label(self.root, text="Password:").pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack(pady=5)

        tk.Button(self.root, text="Login", command=self.login).pack(pady=10)
        tk.Button(self.root, text="Sign Up", command=self.show_signup_screen).pack(pady=5)
        tk.Button(self.root, text="Forgot Password", command=self.show_reset_password_screen).pack(pady=5)

    def show_signup_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="Sign Up", font=("Segoe UI", 20, "bold")).pack(pady=10)

        tk.Label(self.root, text="Email:").pack()
        self.new_email_entry = tk.Entry(self.root)
        self.new_email_entry.pack(pady=5)

        tk.Label(self.root, text="Username:").pack()
        self.new_username_entry = tk.Entry(self.root)
        self.new_username_entry.pack(pady=5)

        tk.Label(self.root, text="Password:").pack()
        self.new_password_entry = tk.Entry(self.root, show="*")
        self.new_password_entry.pack(pady=5)

        tk.Button(self.root, text="Register", command=self.register).pack(pady=10)
        tk.Button(self.root, text="Back to Login", command=self.show_login_screen).pack(pady=5)

    def show_reset_password_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="Reset Password", font=("Segoe UI", 20, "bold")).pack(pady=10)

        tk.Label(self.root, text="Enter your registered email:").pack()
        self.reset_email_entry = tk.Entry(self.root)
        self.reset_email_entry.pack(pady=5)

        tk.Button(self.root, text="Reset Password", command=self.reset_password).pack(pady=10)
        tk.Button(self.root, text="Back to Login", command=self.show_login_screen).pack(pady=5)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username in self.accounts and self.accounts[username]["password"] == password:
            self.show_main_menu()
        else:
            messagebox.showerror("Login Failed", "Incorrect username or password.")

    def register(self):
        email = self.new_email_entry.get()
        username = self.new_username_entry.get()
        password = self.new_password_entry.get()

        if username in self.accounts:
            messagebox.showerror("Error", "Username already exists.")
        else:
            self.accounts[username] = {"password": password, "email": email}
            self.save_accounts(self.accounts)
            messagebox.showinfo("Success", "Registration successful!")
            self.show_login_screen()

    def reset_password(self):
        email = self.reset_email_entry.get()
        username = next((user for user, data in self.accounts.items() if data["email"] == email), None)

        if username:
            new_password = "newpassword123"  # Generate a secure password in a real application
            self.accounts[username]["password"] = new_password
            self.save_accounts(self.accounts)
            messagebox.showinfo("Success", f"Your new password is: {new_password}")
        else:
            messagebox.showerror("Error", "Email not found.")

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_main_menu(self):
        self.clear_screen()
        tk.Label(self.root, text="Main Menu", font=("Segoe UI", 20, "bold")).pack(pady=10)
        tk.Button(self.root, text="Logout", command=self.show_login_screen).pack(pady=10)
        
        def show_main_menu(self):
            self.clear_screen()

        self.root.config(bg="#282c66")
        tk.Label(
            self.root,
            text="Pace&Stride",
            font=("Rockwell Extra Bold", 30, "bold", "italic"),
            bg="#282c66", 
            fg="#ccf73b",
        ).pack(pady=10)
        
        tk.Button(
            self.root,
            text="Panduan Tipe Kaki",
            command=self.show_panduan,
            font=("Segoe UI Semibold", 14),
            width=20,
            padx=7,
            pady=5,
            bg="#ccf73b",
            fg="#323774",
        ).pack(pady=5, anchor="center")

        tk.Button(
            self.root,
            text="Cari Sepatu",
            command=self.show_cari_sepatu_menu,
            font=("Segoe UI Semibold", 14),
            width=20,
            padx=7,
            pady=5,
            bg="#ccf73b",
            fg="#323774",
        ).pack(pady=5, anchor="center")

        tk.Button(
            self.root,
            text="Lihat Keranjang",
            command=self.show_keranjang,
            font=("Segoe UI Semibold", 14),
            width=20,
            padx=7,
            pady=5,
            bg="#ccf73b",
            fg="#323774",
        ).pack(pady=5, anchor="center")

        tk.Button(
            self.root,
            text="Keluar",
            command=self.root.quit,
                font=("Segoe UI Semibold", 14),
            width=20,
            padx=7,
            pady=5,
            bg="#ccf73b",
            fg="#323774",
        ).pack(pady=5, anchor="center")

    def show_panduan(self):
        messagebox.showinfo(
            "Panduan Tipe Kaki",
            "1. Kaki Normal: Lebar kaki seimbang.\n"
            "2. Kaki Sempit: Jari-jari kaki berdempetan.\n"
            "3. Kaki Lebar: Jari-jari membutuhkan ruang ekstra."
        )

    def show_cari_sepatu_menu(self):
        self.clear_screen()

        tk.Label(self.root, text="Pilih Tipe Kaki", bg="#282c66", fg="#ccf73b", font=("Rockwell Extra Bold", 16)).pack(pady=10)

        self.tipe_kaki_var = tk.StringVar(value="Normal")
        for tipe in self.sepatu_lari.keys():
            tk.Radiobutton(
                self.root, 
                text=tipe, 
                variable=self.tipe_kaki_var, 
                value=tipe, 
                font=("Segoe UI Semibold", 14),  
                indicatoron=1,  
                width=20, 
                bg="#ccf73b", 
                fg="#323774",
                anchor="center"  
            ).pack(pady=5)

        tk.Button(
            self.root,
            text="Lanjut",
            bg="#ccf73b", 
            fg="#323774",
            command=self.show_jarak_lari_menu,
            padx=10,  
            pady=5    
        ).pack(pady=10)

    def show_jarak_lari_menu(self):
        tipe_kaki = self.tipe_kaki_var.get()
        self.clear_screen()

        tk.Label(self.root, text=f"Pilih Jarak Lari untuk Kaki {tipe_kaki}", bg="#282c66", fg="#ccf73b", font=("Rockwell Extra Bold", 16)).pack(pady=10)

        self.jarak_var = tk.StringVar(value="Jarak Pendek")
        for jarak in self.sepatu_lari[tipe_kaki].keys():
            tk.Radiobutton(
                self.root, 
                text=jarak, 
                variable=self.jarak_var, 
                value=jarak, 
                font=("Segoe UI Semibold", 14), 
                bg="#ccf73b", 
                fg="#323774",
                width=20,  
                anchor="center"  
            ).pack(pady=5)  

        tk.Button(self.root, text="Lihat Rekomendasi", bg="#ccf73b", fg="#323774", command=lambda: self.show_rekomendasi(tipe_kaki)).pack(pady=10)

    def show_rekomendasi(self, tipe_kaki):
        jarak = self.jarak_var.get()
        rekomendasi = self.sepatu_lari[tipe_kaki].get(jarak, [])
        self.clear_screen()

        tk.Label(self.root, text=f"Rekomendasi Sepatu ({tipe_kaki} - {jarak})", bg="#282c66", fg="#ccf73b", font=("Rockwell Extra Bold", 14)).pack(pady=10)

        for sepatu in rekomendasi:
        # Menampilkan tombol untuk memilih sepatu
            button = tk.Button(
                self.root,
                text=f"{sepatu['nama']} - Rp {sepatu['harga']:,}", 
                font=("Segoe UI Semibold", 16),
                bg="#ccf73b", 
                fg="#323774",
               command=lambda s=sepatu: self.show_ukuran_menu(s)
        )
            button.pack (pady=5)

        tk.Button(self.root, text="Kembali ke Menu Utama", bg="#ccf73b", fg="#323774",command=self.show_main_menu).pack(pady=10)
        
    def show_ukuran_menu(self, sepatu):
        self.clear_screen()

        tk.Label(self.root, text=f"Pilih Ukuran untuk {sepatu['nama']}", bg="#282c66", fg="#ccf73b", font=("Rockwell Extra Bold", 16)).pack(pady=10)

    # Menampilkan ukuran sepatu yang tersedia
        for ukuran in sepatu['ukuran']:
            tk.Button(
                self.root,
                text=f"Ukuran {ukuran}",
                font=("Segoe UI Semibold", 16),
                bg="#ccf73b", 
                fg="#323774",
                command=lambda u=ukuran, s=sepatu: self.add_to_cart_with_size(s, u)
            ).pack(pady=5)

        tk.Button(self.root, text="Kembali", font=("Segoe UI Semibold", 16), bg="#ccf73b", fg="#323774",command=self.show_rekomendasi).pack(pady=10)

    def add_to_cart_with_size(self, sepatu, ukuran):
        sepatu_terpilih = sepatu.copy()
        sepatu_terpilih['ukuran'] = ukuran  # Menambahkan ukuran sepatu yang dipilih
        self.keranjang.append(sepatu_terpilih)
        self.total_harga += sepatu['harga']
        messagebox.showinfo("Keranjang", f"{sepatu_terpilih['nama']} (Ukuran {ukuran}) berhasil ditambahkan ke keranjang.")
        self.show_tambah_barang()

    def show_tambah_barang(self):
        self.clear_screen()

        tk.Label(self.root, text="Tambahkan Barang Lain?", bg="#282c66", fg="#ccf73b", font=("Rockwell Extra Bold", 16)).pack(pady=10)
        for barang in self.barang_tambahan:
            tk.Button(
                self.root,
                text=f"{barang['nama']} - Rp {barang['harga']:,}",
                font=("Segoe UI Semibold", 12),
                bg="#ccf73b",
                fg="#323774",
                command=lambda b=barang: self.add_to_cart(b),  # Make sure the correct 'barang' is passed
                width=40
            ).pack(pady=5)


        tk.Button(self.root, text="Lihat Keranjang", bg="#ccf73b", fg="#323774", command=self.show_keranjang).pack(pady=10)
        
    def add_to_cart(self, barang):
        print(f"Barang ditambahkan ke keranjang: {barang}")
        self.keranjang.append(barang)
        self.total_harga += barang['harga']
        messagebox.showinfo("Keranjang", f"{barang['nama']} berhasil ditambahkan ke keranjang.")

    def show_keranjang(self):
        self.clear_screen()

        tk.Label(self.root, text="Keranjang Belanja", bg="#282c66", fg="#ccf73b", font=("Rockwell Extra Bold", 20, "bold")).pack(pady=10)

        for item in self.keranjang:
            tk.Label(self.root, text=f"{item['nama']} - Rp {item['harga']:,}", bg="#282c66", fg="#ccf73b", font=("Segoe UI Semibold", 14)).pack()

        tk.Label(self.root, text=f"\nTotal Harga: Rp {self.total_harga:,}", bg="#282c66", fg="#ccf73b", font=("Segoe UI Semibold", 12)).pack(pady=10)

        tk.Button(
            self.root,
            text="Checkout",
            bg="#ccf73b", 
            fg="#323774",
            command=self.checkout,
            padx=10,
            pady=5
        ).pack(pady=5)

        tk.Button(
            self.root,
            text="Kembali ke Menu Utama",
            bg="#ccf73b", 
            fg="#323774",
            command=self.show_main_menu,
            padx=10,
            pady=5
        ).pack(pady=5)


    def checkout(self):
        self.clear_screen()
        tk.Label(self.root, text="Checkout", bg="#282c66", fg="#ccf73b", font=("Segoe UI Semibold", 20, "bold")).pack(pady=10)
        tk.Label(
            self.root,
            text=f"Total Harga: Rp {self.total_harga:,}",
            font=("Segoe UI Semibold", 12),
            bg="#282c66", 
            fg="#ccf73b",
        ).pack(pady=10)
        
        tk.Label(
            self.root,
            text="Masukkan Alamat Pengiriman:",
            font=("Segoe UI Semibold", 12),
            bg="#282c66", 
            fg="#ccf73b",
        ).pack()
        
        self.alamat_entry = tk.Entry(self.root, width=50)
        self.alamat_entry.pack(pady=5)

        tk.Label(
            self.root, 
            text="Pilih Metode Pembayaran:", 
            font=("Segoe UI Semibold", 12), 
            bg="#282c66", 
            fg="#ccf73b"
        ).pack(pady=10)

        self.metode_var = tk.StringVar(value="COD")
        metode_pembayaran = ["COD", "Virtual Account"]
        for metode in metode_pembayaran:
            tk.Radiobutton(
                self.root,
                text=metode,
                variable=self.metode_var,
                value=metode,
                font=("Segoe UI Semibold", 14),  
                width=20,
                bg="#ccf73b", 
                fg="#323774",  
                anchor="center"  
            ).pack(pady=5)  

        tk.Button(self.root, text="Konfirmasi Pembayaran", bg="#ccf73b", fg="#323774", command=self.konfirmasi_pembayaran).pack(pady=10)


    def konfirmasi_pembayaran(self):
        metode = self.metode_var.get()
        if metode == "COD":
            messagebox.showinfo(
                "Konfirmasi COD",
                    f"Terima kasih telah berbelanja.\n"
            f"Harap siapkan uang tunai sebesar Rp {self.total_harga:,} saat paket sampai."
            )
            self.keranjang.clear()
            self.total_harga = 0
            self.show_main_menu()
        else:
            self.show_virtual_account()

    def show_virtual_account(self):
        self.clear_screen()
        tk.Label(self.root, text="Pilih Bank untuk Virtual Account", bg="#282c66", fg="#ccf73b", font=("Segoe UI Semibold", 20, "bold")).pack(pady=10)

        self.bank_var = tk.StringVar(value="Mandiri")
        daftar_bank = ["Mandiri", "BNI", "BCA", "BRI"]
        for bank in daftar_bank:
            tk.Radiobutton(
                self.root,
                    text=bank,
                variable=self.bank_var,
                value=bank,
                font=("Segoe UI Semibold", 14),  
                width=20,
                bg="#ccf73b", 
                fg="#323774",  
                anchor="center" 
            ).pack(pady=5)  

        tk.Button(self.root, text="Lanjutkan", bg="#ccf73b", fg="#323774",command=self.show_va_rekening).pack(pady=10)

    def show_va_rekening(self):
        bank = self.bank_var.get()
        rekening = {
            "Mandiri": "1234567890",
            "BNI": "0987654321",
            "BCA": "1122334455",
            "BRI": "5566778899"
        }
        nomor_rekening = rekening.get(bank, "Tidak tersedia")
        messagebox.showinfo(
            "Konfirmasi Virtual Account",
            f"Bank: {bank}\n"
            f"Silakan lakukan pembayaran ke nomor rekening berikut:\n{nomor_rekening}\n\n"
            "Pembayaran akan diperiksa sistem. Jika transaksi sukses, paket akan segera dikirimkan."
        )
        self.keranjang.clear()
        self.total_harga = 0
        self.show_main_menu()

# Jalankan aplikasi
if __name__ == "__main__":
    root = tk.Tk()
    app = TokoSepatuApp(root)
    root.mainloop()
