import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from data_managementfix import load_data, save_history, load_history
from user_authfix import load_akun, save_akun
import os
from data_managementfix import save_history


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

        self.root.config(bg="#282c66")
        tk.Label(self.root, text="Pace&Stride", font=("Rockwell Extra Bold", 30, "bold", "italic"), bg="#282c66", fg="#ccf73b",).pack(pady=10)
        tk.Button(self.root, text="Panduan Tipe Kaki", command=self.show_panduan, font=("Segoe UI Semibold", 14), width=20, padx=7, pady=5, bg="#ccf73b", fg="#323774",).pack(pady=5, anchor="center")
        tk.Button(self.root, text="Cari Sepatu", command=self.show_cari_sepatu_menu, font=("Segoe UI Semibold", 14), width=20, padx=7, pady=5, bg="#ccf73b", fg="#323774",).pack(pady=5, anchor="center")
        tk.Button(self.root, text="Lihat Keranjang", command=self.show_keranjang, font=("Segoe UI Semibold", 14), width=20, padx=7, pady=5, bg="#ccf73b", fg="#323774",).pack(pady=5, anchor="center")
        tk.Button(self.root, text="Riwayat Pembelian", command=self.show_riwayat_pembelian, font=("Segoe UI Semibold", 14), width=20, padx=7, pady=5, bg="#ccf73b", fg="#323774",).pack(pady=5, anchor="center")
        tk.Button(self.root, text="Keluar", command=self.root.quit, font=("Segoe UI Semibold", 14), width=20, padx=7, pady=5, bg="#ccf73b", fg="#323774",).pack(pady=5, anchor="center")
    
    
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
            tk.Radiobutton(self.root, text=tipe, variable=self.tipe_kaki_var, value=tipe, font=("Segoe UI Semibold", 14),  indicatoron=1,  width=20, bg="#ccf73b", fg="#323774",anchor="center"  ).pack(pady=5)

        tk.Button(self.root,text="Lanjut",bg="#ccf73b", fg="#323774",command=self.show_jarak_lari_menu,padx=10,pady=5).pack(pady=10)


    def show_jarak_lari_menu(self):
        tipe_kaki = self.tipe_kaki_var.get()
        self.clear_screen()

        tk.Label(self.root, text=f"Pilih Jarak Lari untuk Kaki {tipe_kaki}", bg="#282c66", fg="#ccf73b", font=("Rockwell Extra Bold", 16)).pack(pady=10)

        self.jarak_var = tk.StringVar(value="Jarak Pendek")
        for jarak in self.sepatu_lari[tipe_kaki].keys():
            tk.Radiobutton(self.root, text=jarak, variable=self.jarak_var, value=jarak, font=("Segoe UI Semibold", 14), bg="#ccf73b", fg="#323774",width=20,  anchor="center").pack(pady=5)  

        tk.Button(self.root, text="Lihat Rekomendasi", bg="#ccf73b", fg="#323774", command=lambda: self.show_rekomendasi(tipe_kaki)).pack(pady=10)


    def show_rekomendasi(self, tipe_kaki):
        jarak = self.jarak_var.get()
        rekomendasi = self.sepatu_lari[tipe_kaki].get(jarak, [])
        self.clear_screen()

        tk.Label(self.root, text=f"Rekomendasi Sepatu ({tipe_kaki} - {jarak})", bg="#282c66", fg="#ccf73b", font=("Rockwell Extra Bold", 14)).pack(pady=10)

        for sepatu in rekomendasi:
            button = tk.Button(self.root,text=f"{sepatu['nama']} - Rp {sepatu['harga']:,}", font=("Segoe UI Semibold", 16),bg="#ccf73b", fg="#323774",anchor="center",width=30,command=lambda s=sepatu: self.show_ukuran_menu(s))
            button.pack (pady=5)

        tk.Button(self.root, text="Kembali ke Menu Utama", bg="#ccf73b", fg="#323774",command=self.show_main_menu).pack(pady=10)
      
        
    def show_ukuran_menu(self, sepatu):
        self.clear_screen()

        tk.Label(self.root, text=f"Pilih Ukuran untuk {sepatu['nama']}", bg="#282c66", fg="#ccf73b", font=("Rockwell Extra Bold", 16)).pack(pady=10)

        for ukuran in sepatu['ukuran']:
            tk.Button(self.root,text=f"Ukuran {ukuran}",font=("Segoe UI Semibold", 16),bg="#ccf73b", fg="#323774",command=lambda u=ukuran, s=sepatu: self.add_to_cart_with_size(s, u)).pack(pady=5)

        tk.Button(self.root, text="Kembali", font=("Segoe UI Semibold", 16), bg="#ccf73b", fg="#323774",command=self.show_main_menu).pack(pady=10)


    def add_to_cart_with_size(self, sepatu, ukuran):
        sepatu_terpilih = sepatu.copy()
        sepatu_terpilih['ukuran'] = ukuran  
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
                command=lambda b=barang: self.add_to_cart(b),  
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
    
            frame = tk.Frame(self.root, bg="#282c66")
            frame.pack(pady=5, fill=tk.X)

            tk.Label(frame,text=f"{item['nama']} - Rp {item['harga']:,}",bg="#282c66",fg="#ccf73b",font=("Segoe UI Semibold", 14)).pack(side=tk.LEFT, padx=10)

            tk.Button(frame,text="Hapus",bg="#ccf73b",fg="#323774",command=lambda i=item: self.hapus_item_dari_keranjang(i)).pack(side=tk.RIGHT, padx=10)

        tk.Label(self.root, text=f"\nTotal Harga: Rp {self.total_harga:,}", bg="#282c66", fg="#ccf73b", font=("Segoe UI Semibold", 12)).pack(pady=10)

        tk.Button(self.root,text="Checkout",bg="#ccf73b", fg="#323774",command=self.checkout,padx=10,pady=5).pack(pady=5)
        tk.Button(self.root,text="Tambah Pilihan Sepatu",bg="#ccf73b", fg="#323774",command=self.show_cari_sepatu_menu,padx=10,pady=5).pack(pady=5)
        tk.Button(self.root,text="Tambah Pilihan Produk",bg="#ccf73b", fg="#323774",command=self.show_tambah_barang,padx=10,pady=5).pack(pady=5)
        tk.Button(self.root,text="Kembali ke Menu Utama",bg="#ccf73b", fg="#323774",command=self.show_main_menu,padx=10,pady=5).pack(pady=5)
        
        
    def hapus_item_dari_keranjang(self, item):
        if item in self.keranjang:
            self.keranjang.remove(item)
            self.total_harga -= item['harga']
            messagebox.showinfo("Keranjang", f"{item['nama']} berhasil dihapus dari keranjang.")
            self.show_keranjang()  
        else:
            messagebox.showerror("Error", "Item tidak ditemukan di keranjang.")


    def checkout(self):
        self.clear_screen()
        tk.Label(self.root, text="Checkout", bg="#282c66", fg="#ccf73b", font=("Segoe UI Semibold", 20, "bold")).pack(pady=10)
        tk.Label(self.root,text=f"Total Harga: Rp {self.total_harga:,}",font=("Segoe UI Semibold", 12),bg="#282c66", fg="#ccf73b",).pack(pady=10)
        
        tk.Label(self.root,text="Masukkan Alamat Pengiriman:",font=("Segoe UI Semibold", 12),bg="#282c66", fg="#ccf73b",).pack()
        
        self.alamat_entry = tk.Entry(self.root, width=50)
        self.alamat_entry.pack(pady=5)

        tk.Label(self.root, text="Pilih Metode Pembayaran:", font=("Segoe UI Semibold", 12), bg="#282c66", fg="#ccf73b").pack(pady=10)

        self.metode_var = tk.StringVar(value="COD")
        metode_pembayaran = ["COD", "Virtual Account"]
        for metode in metode_pembayaran:
            tk.Radiobutton(self.root,text=metode,variable=self.metode_var,value=metode,font=("Segoe UI Semibold", 14),width=20,bg="#ccf73b", fg="#323774",  anchor="center"  ).pack(pady=5)  

        tk.Button(self.root, text="Konfirmasi Pembayaran", bg="#ccf73b", fg="#323774", command=self.konfirmasi_pembayaran).pack(pady=10)


    def konfirmasi_pembayaran(self):
        alamat = self.alamat_entry.get()
        metode = self.metode_var.get()
        if not alamat:
            messagebox.showerror("Error", "Alamat pengiriman tidak boleh kosong.")
            return

        riwayat_baru = {
            "produk": self.keranjang,
            "total_harga": self.total_harga,
            "metode_pembayaran": metode,
            "tanggal": "2024-12-27",
            "alamat": alamat
        }

        username = self.current_user
        if username not in self.history:
            self.history[username] = []
        self.history[username].append(riwayat_baru)
        save_history(self.history)

        self.keranjang.clear()
        total_harga = self.total_harga
        
        if metode == "COD":
            messagebox.showinfo(
                "Konfirmasi COD",
                    f"Terima kasih telah berbelanja.\n"
            f"Harap siapkan uang tunai sebesar Rp {total_harga} saat paket sampai."
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
            tk.Radiobutton(self.root,text=bank,variable=self.bank_var,value=bank,font=("Segoe UI Semibold", 14),width=20,bg="#ccf73b", fg="#323774",  anchor="center").pack(pady=5)  

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
        

    def show_riwayat_pembelian(self):
        self.clear_screen()  

        if not self.current_user:  
            messagebox.showerror("Error", "Anda belum login.")
            self.show_login_screen()
            return

        tk.Label(self.root, text="Riwayat Pembelian", bg="#282c66", fg="#ccf73b", font=("Segoe UI Semibold", 20, "bold")).pack(pady=10)

        if self.current_user not in self.history or not self.history[self.current_user]:
            tk.Label(self.root, text="Tidak ada riwayat pembelian.", bg="#282c66", fg="#ccf73b", font=("Segoe UI Semibold", 14)).pack(pady=10)
            tk.Button(self.root, text="Kembali", bg="#ccf73b", fg="#323774", command=self.show_main_menu).pack(pady=10)
            return

        frame_canvas = tk.Frame(self.root)
        frame_canvas.pack(fill="both", expand=True, padx=10, pady=10)

        canvas = tk.Canvas(frame_canvas, bg="#282c66")
        scrollbar = tk.Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="#282c66")

        canvas.create_window((canvas.winfo_width() // 2, 0), window=scrollable_frame, anchor="n")
        canvas.bind("<Configure>", lambda e: canvas.create_window((e.width // 2, 0), window=scrollable_frame, anchor="n"))

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        for transaksi in self.history[self.current_user]:
            transaksi_frame = tk.Frame(scrollable_frame, bg="#282c66", bd=1, relief="solid")
            transaksi_frame.pack(pady=10, padx=10, fill="x") 
            
            tk.Label(scrollable_frame, text=f"Tanggal: {transaksi['tanggal']}", bg="#282c66", fg="#ccf73b", font=("Segoe UI", 12)).pack(pady=2)
            tk.Label(scrollable_frame, text=f"Total Harga: Rp {transaksi['total_harga']:,}", bg="#282c66", fg="#ccf73b", font=("Segoe UI", 12)).pack(pady=2)
            tk.Label(scrollable_frame, text=f"Metode Pembayaran: {transaksi['metode_pembayaran']}", bg="#282c66", fg="#ccf73b", font=("Segoe UI", 12)).pack(pady=2)
            tk.Label(scrollable_frame, text=f"Alamat: {transaksi['alamat']}", bg="#282c66", fg="#ccf73b", font=("Segoe UI", 12)).pack(pady=2)
        
            tk.Label(scrollable_frame, text="Produk yang dibeli:", bg="#282c66", fg="#ccf73b", font=("Segoe UI", 12)).pack(pady=5)
            for produk in transaksi.get("produk", []):
                tk.Label(scrollable_frame, text=f"- {produk['nama']} (Rp {produk['harga']:,})", bg="#282c66", fg="#ccf73b", font=("Segoe UI", 12)).pack(pady=2)

        tk.Button(self.root, text="Kembali", bg="#ccf73b", fg="#323774", command=self.show_main_menu).pack(pady=10)


    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
