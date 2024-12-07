import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, StringVar, Frame

# Inisialisasi root
root = tk.Tk()
root.title("Aplikasi Pembelian Sepatu")
root.geometry("800x600")  

# Data pengguna
users = {}

# Data sepatu dan produk lainnya
sepatu_data = {
    "Sepatu Normal": [
        {"nama": "Nike Speed Racer", "harga": 1200000, "ukuran" : [36, 37, 38, 39, 40, 41, 42, 43, 44, 45]},
        {"nama": "Adidas Dash Pro", "harga": 1350000, "ukuran" : [36, 37, 38, 39, 40, 41, 42, 43, 44, 45]},
        {"nama": "Puma Velocity Nitro", "harga": 1250000, "ukuran" : [36, 37, 38, 39, 40, 41, 42, 43, 44, 45]},
        {"nama": "Reebok Floatride Energy", "harga": 1400000, "ukuran" : [36, 37, 38, 39, 40, 41, 42, 43, 44, 45]},
        {"nama": "Hoka Clifton 8", "harga": 1500000, "ukuran" : [36, 37, 38, 39, 40, 41, 42, 43, 44, 45]},
        {"nama": "Under Armour Sonic", "harga": 1450000, "ukuran" : [36, 37, 38, 39, 40, 41, 42, 43, 44, 45]},
        {"nama": "Saucony Endurance", "harga": 1300000, "ukuran" : [36, 37, 38, 39, 40, 41, 42, 43, 44, 45]},
        {"nama": "New Balance Fresh Foam", "harga": 1400000, "ukuran" : [36, 37, 38, 39, 40, 41, 42, 43, 44, 45]},
        {"nama": "Brooks Marathon Master", "harga": 1600000, "ukuran" : [36, 37, 38, 39, 40, 41, 42, 43, 44, 45]},
        {"nama": "Altra Torin 5", "harga": 1500000, "ukuran" : [36, 37, 38, 39, 40, 41, 42, 43, 44, 45]},
    ],
    "Sepatu Sempit": [
        {"nama": "Puma Slim Runner", "harga": 1100000, "ukuran" : [36, 37, 38, 39, 40, 41, 42, 43, 44, 45]},
        {"nama": "Under Armour Narrow", "harga": 1250000, "ukuran" : [36, 37, 38, 39, 40, 41, 42, 43, 44, 45]},
        {"nama": "Nike Slim Racer", "harga": 1200000, "ukuran" : [36, 37, 38, 39, 40, 41, 42, 43, 44, 45]},
        {"nama": "ASICS Fit", "harga": 1300000, "ukuran" : [36, 37, 38, 39, 40, 41, 42, 43, 44, 45]},
        {"nama": "Adidas Narrow Glide", "harga": 1350000, "ukuran" : [36, 37, 38, 39, 40, 41, 42, 43, 44, 45]},
        {"nama": "Brooks Slim Line", "harga": 1400000, "ukuran" : [36, 37, 38, 39, 40, 41, 42, 43, 44, 45]},
        {"nama": "Hoka Thin Glide", "harga": 1500000, "ukuran" : [36, 37, 38, 39, 40, 41, 42, 43, 44, 45]},
        {"nama": "Mizuno Light Sempit", "harga": 1450000, "ukuran" : [36, 37, 38, 39, 40, 41, 42, 43, 44, 45]},
        {"nama": "New Balance Sempit Max", "harga": 1400000, "ukuran" : [36, 37, 38, 39, 40, 41, 42, 43, 44, 45]},
        {"nama": "Altra Slim Focus", "harga": 1350000, "ukuran" : [36, 37, 38, 39, 40, 41, 42, 43, 44, 45]},
    ],
    "Sepatu Lebar": [
        {"nama": "Hoka Wide Glide", "harga": 1500000, "ukuran": [36, 37, 38, 39, 40, 41, 42, 43, 44, 45]},
        {"nama": "New Balance Extra Wide", "harga": 1450000, "ukuran": [36, 37, 38, 39, 40, 41, 42, 43, 44, 45]},
        {"nama": "Brooks Wide Fit", "harga": 1600000, "ukuran": [36, 37, 38, 39, 40, 41, 42, 43, 44, 45]},
        {"nama": "Nike Wide Marathon", "harga": 1550000, "ukuran": [36, 37, 38, 39, 40, 41, 42, 43, 44, 45]},
        {"nama": "Adidas Wide Boost", "harga": 1650000, "ukuran": [36, 37, 38, 39, 40, 41, 42, 43, 44, 45]},
        {"nama": "Under Armour Wide Runner", "harga": 1500000, "ukuran": [36, 37, 38, 39, 40, 41, 42, 43, 44, 45]},
        {"nama": "Mizuno Wave Wide", "harga": 1550000, "ukuran": [36, 37, 38, 39, 40, 41, 42, 43, 44, 45]},
        {"nama": "Saucony Wide Stream", "harga": 1400000, "ukuran": [36, 37, 38, 39, 40, 41, 42, 43, 44, 45]},
        {"nama": "Puma Large Fit", "harga": 1450000, "ukuran": [36, 37, 38, 39, 40, 41, 42, 43, 44, 45]},
        {"nama": "ASICS Wide Comfort", "harga": 1600000, "ukuran": [36, 37, 38, 39, 40, 41, 42, 43, 44, 45]},
    ],
}

produk_lain = [
    {"nama": "Baju Nike Dri-Fit", "harga": 350000},
    {"nama": "Baju Adidas Coolmax", "harga": 400000},
    {"nama": "Baju Puma Active", "harga": 380000},
    {"nama": "Baju Under Armour Tech", "harga": 420000},
    {"nama": "Baju Reebok Training", "harga": 360000},
    {"nama": "Baju Mizuno Sport", "harga": 390000},
    {"nama": "Baju Hoka Motion", "harga": 410000},
    {"nama": "Baju Saucony Swift", "harga": 400000},
    {"nama": "Baju ASICS ProFit", "harga": 430000},
    {"nama": "Baju Altra Cool", "harga": 370000},
    {"nama": "Celana Nike Flex", "harga": 300000},
    {"nama": "Celana Adidas Run", "harga": 350000},
    {"nama": "Celana Hoka Freedom", "harga": 320000},
    {"nama": "Celana Reebok Endurance", "harga": 330000},
    {"nama": "Celana ASICS Comfort", "harga": 340000},
    {"nama": "Celana Mizuno Sprint", "harga": 360000},
    {"nama": "Celana Saucony Aero", "harga": 370000},
    {"nama": "Celana Brooks Swift", "harga": 390000},
    {"nama": "Celana Under Armour Glide", "harga": 400000},
    {"nama": "Celana Puma Velocity", "harga": 380000},
    {"nama": "Kaos Kaki Compression", "harga": 50000},
    {"nama": "Kaos Kaki Sport", "harga": 75000},
    {"nama": "Kaos Kaki Anti-Bakteri", "harga": 60000},
    {"nama": "Kaos Kaki Running Pro", "harga": 80000},
    {"nama": "Kaos Kaki Breathable", "harga": 70000},
    {"nama": "Kaos Kaki Soft Comfort", "harga": 55000},
    {"nama": "Kaos Kaki Ultra Thin", "harga": 65000},
    {"nama": "Kaos Kaki No-Slip Grip", "harga": 75000},
    {"nama": "Kaos Kaki Thermal Fit", "harga": 85000},
    {"nama": "Kaos Kaki Shock Absorb", "harga": 90000},
    {"nama": "Garmin Forerunner", "harga": 2000000},
    {"nama": "Polar Vantage", "harga": 1800000},
    {"nama": "Coros Pace 2", "harga": 1700000},
    {"nama": "Suunto 9 Peak", "harga": 2500000},
    {"nama": "Fitbit Charge 5", "harga": 1600000},
    {"nama": "Amazfit T-Rex", "harga": 1900000},
    {"nama": "Samsung Galaxy Watch", "harga": 2100000},
    {"nama": "Apple Watch SE", "harga": 2300000},
    {"nama": "Garmin Fenix 6", "harga": 3000000},
    {"nama": "Suunto Spartan Trainer", "harga": 2200000},
    {"nama": "Botol Minum Hydro Flask", "harga": 250000},
    {"nama": "Botol Minum CamelBak", "harga": 200000},
    {"nama": "Botol Minum Nike Squeeze", "harga": 180000},
    {"nama": "Botol Minum Adidas Runner", "harga": 210000},
    {"nama": "Botol Minum Decathlon Sport", "harga": 190000},
    {"nama": "Botol Minum Thermos Active", "harga": 240000},
    {"nama": "Botol Minum Sigg Sport", "harga": 230000},
    {"nama": "Botol Minum Klean Kanteen", "harga": 260000},
    {"nama": "Botol Minum Zojirushi Slim", "harga": 220000},
    {"nama": "Botol Minum Nalgene Wide", "harga": 210000},
]

# Variabel global
current_user = None
keranjang = []
tipe_kaki_var = StringVar()
ukuran_var = StringVar()

# Fungsi untuk membersihkan layar
def clear_screen():
    for widget in root.winfo_children():
        if isinstance(widget, ttk.Frame):
            widget.pack_forget()

def tampilkan_sign_up_form():
    clear_screen()
    sign_up_form_frame.pack(fill="both", expand=True)

def tampilkan_home():
    clear_screen()
    home_frame.pack(fill="both", expand=True)

def tampilkan_login_form():
    login_email_label.pack(pady=5)
    login_email_entry.pack(pady=5)
    login_password_label.pack(pady=5)
    login_password_entry.pack(pady=5)
    submit_login_button.pack(pady=5)

def sign_up():
    clear_screen()
    nama_lengkap = nama_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if not nama_lengkap or not email or not password:
        messagebox.showwarning("Peringatan", "Semua kolom harus diisi!")
        return

    if email in users:
        messagebox.showwarning("Peringatan", "Email sudah terdaftar!")
        return

    users[email] = {"nama": nama_lengkap, "password": password}
    messagebox.showinfo("Sukses", "Pendaftaran berhasil! Silakan login.")
    tampilkan_home()

def login():
    clear_screen()
    global current_user
    email = login_email_entry.get()
    password = login_password_entry.get()

    if email not in users or users[email]["password"] != password:
        messagebox.showwarning("Gagal Login", "Email atau password salah!")
        return

    current_user = email
    messagebox.showinfo("Sukses", f"Selamat datang, {users[email]['nama']}!")
    tampilkan_toko()  
    
def tampilkan_toko():
    clear_screen()
    toko_frame.pack(fill="both", expand=True)

# Fungsi untuk menampilkan panduan tipe kaki
def tampilkan_panduan():
    panduan_text = (
        "1. Normal: Bentuk kaki standar.\n"
        "2. Sempit: Kaki dengan lebar kecil.\n"
        "3. Lebar: Kaki dengan lebar besar.\n"
    )
    messagebox.showinfo("Panduan Tipe Kaki", panduan_text)

# Fungsi untuk menampilkan sepatu rekomendasi berdasarkan tipe dan ukuran kaki
def tampilkan_rekomendasi():
    clear_screen()
    tipe_kaki = tipe_kaki_var.get()
    ukuran_kaki = ukuran_var.get()

    if not tipe_kaki or not ukuran_kaki:
        messagebox.showwarning("Peringatan", "Pilih tipe dan ukuran kaki terlebih dahulu!")
        return

    ukuran = int(ukuran_kaki)
    daftar_sepatu = sepatu_data.get(f"Sepatu {tipe_kaki}", [])  # Mendapatkan daftar sepatu berdasarkan tipe kaki

    # Filter sepatu berdasarkan ukuran
    rekomendasi = [sepatu for sepatu in daftar_sepatu if ukuran in sepatu["ukuran"]]

    # Tampilkan pesan jika tidak ada rekomendasi
    if not rekomendasi:
        messagebox.showinfo("Informasi", f"Tidak ada sepatu yang tersedia untuk ukuran {ukuran} pada tipe kaki {tipe_kaki}.")
        return

    # Bersihkan frame katalog sebelum menampilkan rekomendasi baru
    for widget in katalog_frame.winfo_children():
        widget.destroy()

    # Tampilkan produk yang sesuai
    for produk in rekomendasi:
        frame_produk = ttk.Frame(katalog_frame, relief="ridge", padding=10)
        frame_produk.pack(fill="x", padx=5, pady=5)

        # Nama produk
        label_nama = ttk.Label(frame_produk, text=produk["nama"], font=("Arial", 12, "bold"))
        label_nama.pack(anchor="w")

        # Harga produk
        label_harga = ttk.Label(frame_produk, text=f"Rp {produk['harga']:,}", font=("Arial", 10))
        label_harga.pack(anchor="w")

        # Tombol tambah ke keranjang
        tombol_tambah = ttk.Button(
            frame_produk,
            text="Pilih Sepatu Ini",
            command=lambda p=produk: tambah_ke_keranjang(p)
        )
        tombol_tambah.pack(anchor="e")
    
def tampilkan_katalog():
    clear_screen()
    global katalog_frame
    katalog_frame = Frame(root)
    katalog_frame.pack(fill="both", expand=True)

# Fungsi untuk menambahkan sepatu atau produk lain ke keranjang
def tambah_ke_keranjang(produk):
    clear_screen()
    keranjang.append(produk)
    keranjang_listbox.insert(tk.END, f"{produk['nama']} - Rp {produk['harga']:,}")
    if produk in produk_lain:
        return

    # Tanyakan apakah ingin menambah barang lain
    tambah_lagi = messagebox.askyesno("Konfirmasi", "Apakah Anda ingin menambah barang lain?")
    if tambah_lagi:
        tambah_produk_lain()

# Halaman utama aplikasi
def main_page():
    clear_screen()
    for widget in root.winfo_children():
        widget.destroy()

    nama_aplikasi = ttk.Label(root, text="Shoes Center", font=("Rockwell Extra Bold", 16, "bold"), anchor="center")
    nama_aplikasi.pack(pady=10)

    ttk.Button(root, text="Panduan Tipe Kaki", command=tampilkan_panduan).pack(pady=5)

    frame_pilihan = ttk.LabelFrame(root, text="Pilih Tipe dan Ukuran Kaki")
    frame_pilihan.pack(fill="x", padx=10, pady=10)

    ttk.Label(frame_pilihan, text="Pilih Tipe Kaki:").pack(side="left", padx=5)
    for tipe in ["Normal", "Sempit", "Lebar"]:
        ttk.Radiobutton(frame_pilihan, text=tipe, variable=tipe_kaki_var, value=tipe).pack(side="left")

    ttk.Label(frame_pilihan, text="Pilih Ukuran Kaki:").pack(side="left", padx=5)
    ukuran_dropdown = ttk.Combobox(frame_pilihan, textvariable=ukuran_var, values=list(range(36, 46)), state="readonly")
    ukuran_dropdown.pack(side="left", padx=5)

    ttk.Button(frame_pilihan, text="Tampilkan Sepatu", command=tampilkan_rekomendasi).pack(side="left", padx=5)

    frame_katalog = ttk.LabelFrame(root, text="Katalog Produk")
    frame_katalog.pack(fill="both", expand=True, padx=10, pady=10)

    canvas = tk.Canvas(frame_katalog)
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = ttk.Scrollbar(frame_katalog, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)
    global katalog_frame
    katalog_frame = ttk.Frame(canvas)
    canvas.create_window((0, 0), window=katalog_frame, anchor="nw")

    frame_keranjang = ttk.LabelFrame(root, text="Keranjang Belanja")
    frame_keranjang.pack(fill="x", padx=10, pady=10)

    global keranjang_listbox
    keranjang_listbox = tk.Listbox(frame_keranjang, height=8)
    keranjang_listbox.pack(fill="x", padx=5, pady=5)

    frame_aksi = tk.Frame(root)
    frame_aksi.pack(fill="x", padx=40, pady=40)

def checkout():
    clear_screen()
    if not keranjang:
        messagebox.showwarning("Peringatan", "Keranjang belanja Anda kosong!")
        return

    alamat_pengiriman = simpledialog.askstring("Checkout", "Masukkan alamat pengiriman Anda:")
    if not alamat_pengiriman:
        messagebox.showwarning("Peringatan", "Alamat pengiriman tidak boleh kosong!")
        return

    total_harga = sum(item["harga"] for item in keranjang)
    uang_bayar = simpledialog.askinteger("Checkout", f"Total belanja Anda Rp {total_harga:,}\nMasukkan jumlah uang Anda:")

    if uang_bayar is None or uang_bayar < total_harga:
        messagebox.showwarning("Peringatan", "Uang Anda tidak mencukupi!")
        return

    kembalian = uang_bayar - total_harga
    messagebox.showinfo(
        "Terima Kasih",
        f"Terima kasih telah berbelanja, {users[current_user]['nama']}!\nKembalian Anda: Rp {kembalian:,}\nAlamat Pengiriman: {alamat_pengiriman}"
    )
    keranjang.clear()
    keranjang_listbox.delete(0, tk.END)
    logout()

def logout():
    clear_screen()
    global current_user
    current_user = None
    keranjang.clear()
    keranjang_listbox.delete(0, tk.END)
    tampilkan_home()


def clear_screen():
    for widget in root.winfo_children():
        if isinstance(widget, ttk.Frame):
            widget.pack_forget()

# Setup aplikasi
root = tk.Tk()
root.title("Aplikasi Pembelian Produk")
root.geometry("800x600")

# Frame untuk Home
home_frame = ttk.Frame(root)
home_frame.pack(fill="both", expand=True)

welcome_label = ttk.Label(home_frame, text="Selamat Datang di Aplikasi Kami!")
welcome_label.pack(pady=10)

signup_button = ttk.Button(home_frame, text="Sign Up", command=tampilkan_sign_up_form)
signup_button.pack(pady=5)

login_button = ttk.Button(home_frame, text="Login", command=tampilkan_login_form)
login_button.pack(pady=5)

# Input login (disembunyikan awalnya)
login_email_label = ttk.Label(home_frame, text="Email:")
login_email_entry = ttk.Entry(home_frame)
login_password_label = ttk.Label(home_frame, text="Password:")
login_password_entry = ttk.Entry(home_frame, show="*")
submit_login_button = ttk.Button(home_frame, text="Submit Login", command=login)

# Frame untuk Form Sign Up
sign_up_form_frame = ttk.Frame(root)

nama_label = ttk.Label(sign_up_form_frame, text="Nama Lengkap:")
nama_label.pack()
nama_entry = ttk.Entry(sign_up_form_frame)
nama_entry.pack()

email_label = ttk.Label(sign_up_form_frame, text="Email:")
email_label.pack()
email_entry = ttk.Entry(sign_up_form_frame)
email_entry.pack()

password_label = ttk.Label(sign_up_form_frame, text="Password:")
password_label.pack()
password_entry = ttk.Entry(sign_up_form_frame, show="*")
password_entry.pack()

submit_signup_button = ttk.Button(sign_up_form_frame, text="Submit Sign Up", command=sign_up)
submit_signup_button.pack(pady=5)

# Frame untuk Toko
toko_frame = ttk.Frame(root)

keranjang_frame = ttk.LabelFrame(toko_frame, text="Keranjang Belanja")
keranjang_frame.pack(fill="x", padx=10, pady=10)

keranjang_listbox = tk.Listbox(keranjang_frame, height=8)
keranjang_listbox.pack(fill="x", padx=5, pady=5)

checkout_button = ttk.Button(toko_frame, text="Checkout", command=checkout)
checkout_button.pack(pady=10)

logout_button = ttk.Button(toko_frame, text="Logout", command=logout)
logout_button.pack(pady=10)

# Tampilkan frame awal
tampilkan_home()

# Jalankan aplikasi
root.mainloop()