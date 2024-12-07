import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import json
import os

# Lokasi file JSON untuk menyimpan akun
file_akun = "akun.json"

# Fungsi untuk memuat data akun dari file JSON
def muat_data_akun():
    if os.path.exists(file_akun):
        with open(file_akun, "r") as file:
            return json.load(file)
    return {}

# Fungsi untuk menyimpan data akun ke file JSON
def simpan_data_akun(data):
    with open(file_akun, "w") as file:
        json.dump(data, file, indent=4)

# Memuat data akun awal
data_akun = muat_data_akun()

# Fungsi untuk mengganti konten tampilan
def ganti_tampilan(frame):
    for widget in root.winfo_children():
        widget.destroy()
    frame()

# Tampilan Sign Up
def tampilan_signup():
    tk.Label(root, text="Sign Up", font=("Arial", 16, "bold")).pack(pady=10)

    tk.Label(root, text="Nama Lengkap:").pack(anchor="w", padx=20)
    entry_nama = tk.Entry(root)
    entry_nama.pack(fill="x", padx=20, pady=5)

    tk.Label(root, text="Email:").pack(anchor="w", padx=20)
    entry_email = tk.Entry(root)
    entry_email.pack(fill="x", padx=20, pady=5)

    tk.Label(root, text="Password:").pack(anchor="w", padx=20)
    entry_password = tk.Entry(root, show="*")
    entry_password.pack(fill="x", padx=20, pady=5)

    def proses_signup():
        nama = entry_nama.get().strip()
        email = entry_email.get().strip()
        password = entry_password.get().strip()

        if not nama or not email or not password:
            messagebox.showwarning("Peringatan", "Semua kolom harus diisi!")
            return

        if email in data_akun:
            messagebox.showwarning("Peringatan", "Email sudah terdaftar!")
            return

        data_akun[email] = {"nama": nama, "password": password}
        simpan_data_akun(data_akun)
        messagebox.showinfo("Sukses", "Akun berhasil didaftarkan! Silakan login.")
        ganti_tampilan(tampilan_login)

    tk.Button(root, text="Daftar", command=proses_signup).pack(pady=10)
    tk.Button(root, text="Sudah punya akun? Login", command=lambda: ganti_tampilan(tampilan_login)).pack()

# Tampilan Login
def tampilan_login():
    tk.Label(root, text="Login", font=("Arial", 16, "bold")).pack(pady=10)

    tk.Label(root, text="Email:").pack(anchor="w", padx=20)
    entry_email = tk.Entry(root)
    entry_email.pack(fill="x", padx=20, pady=5)

    tk.Label(root, text="Password:").pack(anchor="w", padx=20)
    entry_password = tk.Entry(root, show="*")
    entry_password.pack(fill="x", padx=20, pady=5)

    def proses_login():
        email = entry_email.get().strip()
        password = entry_password.get().strip()

        if not email or not password:
            messagebox.showwarning("Peringatan", "Email dan password harus diisi!")
            return

        if email not in data_akun or data_akun[email]["password"] != password:
            messagebox.showerror("Error", "Email atau password salah!")
            return

        messagebox.showinfo("Sukses", f"Selamat datang, {data_akun[email]['nama']}!")
        ganti_tampilan(tampilan_belanja)

    tk.Button(root, text="Masuk", command=proses_login).pack(pady=10)
    tk.Button(root, text="Belum punya akun? Sign Up", command=lambda: ganti_tampilan(tampilan_signup)).pack()

# Tampilan Belanja
def tampilan_belanja():
    tk.Label(root, text="Halaman Belanja", font=("Arial", 16, "bold")).pack(pady=10)
    tk.Label(root, text="Selamat datang di aplikasi belanja!").pack(pady=20)

    # Tambahkan tombol-tombol produk (contoh)
    produk = ["Produk 1", "Produk 2", "Produk 3"]
    for item in produk:
        tk.Button(root, text=item).pack(pady=5)

    tk.Button(root, text="Keluar", command=root.destroy).pack(pady=20)

# Inisialisasi aplikasi
root = tk.Tk()
root.title("Aplikasi Belanja")
root.geometry("400x400")

# Tampilkan halaman login sebagai tampilan awal
ganti_tampilan(tampilan_login)

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

# Fungsi untuk menampilkan panduan tipe kaki
def tampilkan_panduan_kaki():
    panduan_text = (
        "1. Normal: Bentuk kaki standar.\n"
        "2. Sempit: Kaki dengan lebar kecil.\n"
        "3. Lebar: Kaki dengan lebar besar.\n"
    )
    messagebox.showinfo("Panduan Tipe Kaki", panduan_text)
    
# Fungsi untuk menampilkan panduan jarak lari
def tampilkan_panduan_jarak():
    panduan_text = (
        "1. Pendek: Kurang dari 5 km.\n"
        "2. Menengah: 5 km hingga 10 km.\n"
        "3. Jauh: Lebih dari 10 km.\n"
    )
    messagebox.showinfo("Panduan Jarak Lari", panduan_text)

# Fungsi untuk menampilkan sepatu rekomendasi berdasarkan tipe kaki, ukuran, dan jarak lari
def tampilkan_rekomendasi():
    tipe_kaki = tipe_kaki_var.get()
    ukuran_kaki = ukuran_var.get()
    tipe_jarak = tipe_jarak_var.get()

    if not tipe_kaki or not ukuran_kaki or not tipe_jarak:
        messagebox.showwarning("Peringatan", "Pilih tipe kaki, ukuran kaki, dan jarak lari terlebih dahulu!")
        return

    ukuran = int(ukuran_kaki)
    daftar_sepatu = sepatu_data.get(f"Sepatu {tipe_kaki}", [])

    # Filter sepatu berdasarkan ukuran (dapat ditambahkan logika terkait jarak lari jika ada data tambahan)
    rekomendasi = [sepatu for sepatu in daftar_sepatu if ukuran in sepatu["ukuran"]]

    # Tampilkan pesan jika tidak ada rekomendasi
    if not rekomendasi:
        messagebox.showinfo("Informasi", f"Tidak ada sepatu yang sesuai untuk ukuran {ukuran} pada tipe kaki {tipe_kaki}.")
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

# Fungsi untuk menambahkan sepatu atau produk lain ke keranjang
def tambah_ke_keranjang(produk):
    keranjang.append(produk)
    keranjang_listbox.insert(tk.END, f"{produk['nama']} - Rp {produk['harga']:,}")
    if produk in produk_lain:
        return

    # Tanyakan apakah ingin menambah barang lain
    tambah_lagi = messagebox.askyesno("Konfirmasi", "Apakah Anda ingin menambah barang lain?")
    if tambah_lagi:
        tambah_produk_lain()

# Fungsi untuk menambahkan produk lain
def tambah_produk_lain():
    for widget in katalog_frame.winfo_children():
        widget.destroy()

    for produk in produk_lain:
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
            text="Tambah ke Keranjang",
            command=lambda p=produk: tambah_ke_keranjang(p)
        )
        tombol_tambah.pack(anchor="e")

# Fungsi untuk checkout
def checkout():
    if not keranjang:
        messagebox.showwarning("Peringatan", "Keranjang belanja Anda kosong!")
        return

    total_harga = sum(item["harga"] for item in keranjang)
    uang_bayar = simpledialog.askinteger("Checkout", f"Total belanja Anda Rp {total_harga:,}\nMasukkan jumlah uang Anda:")

    if uang_bayar is None:
        return

    if uang_bayar < total_harga:
        messagebox.showwarning("Peringatan", "Uang Anda tidak mencukupi!")
    else:
        kembalian = uang_bayar - total_harga
        messagebox.showinfo("Terima Kasih", f"Terima kasih telah berbelanja!\nKembalian Anda: Rp {kembalian:,}")
        keranjang.clear()
        keranjang_listbox.delete(0, tk.END)

# Setup aplikasi
root = tk.Tk()
root.title("Aplikasi Pembelian Produk")
root.geometry("800x600")

# Nama aplikasi di bagian atas
nama_aplikasi = ttk.Label(root, text="Pace&Stride", font=("Rockwell Extra Bold", 16, "bold"), anchor="center")
nama_aplikasi.pack(pady=10)

# Variabel
keranjang = []
tipe_kaki_var = tk.StringVar()
ukuran_var = tk.StringVar()
tipe_jarak_var = tk.StringVar()

# Panduan tipe kaki
ttk.Button(root, text="Panduan Tipe Kaki", command=tampilkan_panduan_kaki).pack(pady=5)

# Panduan tipe jarak
ttk.Button(root, text="Panduan Jarak Lari", command=tampilkan_panduan_jarak).pack(pady=5)

# Pilih tipe kaki, ukuran, dan jarak lari
frame_pilihan = ttk.LabelFrame(root, text="Pilih Tipe, Ukuran Kaki, dan Jarak Lari")
frame_pilihan.pack(fill="x", padx=10, pady=10)

# Pilihan tipe kaki
ttk.Label(frame_pilihan, text="Pilih Tipe Kaki:").pack(side="left", padx=5)
for tipe in ["Normal", "Sempit", "Lebar"]:
    ttk.Radiobutton(frame_pilihan, text=tipe, variable=tipe_kaki_var, value=tipe).pack(side="left")

# Pilihan ukuran kaki
ttk.Label(frame_pilihan, text="Pilih Ukuran Kaki:").pack(side="left", padx=5)
ukuran_dropdown = ttk.Combobox(frame_pilihan, textvariable=ukuran_var, values=list(range(36, 46)), state="readonly")
ukuran_dropdown.pack(side="left", padx=5)

# Pilihan jarak lari
ttk.Label(frame_pilihan, text="Pilih Jarak Lari:").pack(side="left", padx=5)
for jarak in ["Pendek", "Menengah", "Jauh"]:
    ttk.Radiobutton(frame_pilihan, text=jarak, variable=tipe_jarak_var, value=jarak).pack(side="left")

# Tombol tampilkan rekomendasi
ttk.Button(frame_pilihan, text="Tampilkan Sepatu", command=tampilkan_rekomendasi).pack(side="left", padx=5)

# Katalog produk
frame_katalog = ttk.LabelFrame(root, text="Katalog Produk")
frame_katalog.pack(fill="both", expand=True, padx=10, pady=10)

canvas = tk.Canvas(frame_katalog)
canvas.pack(side="left", fill="both", expand=True)

scrollbar = ttk.Scrollbar(frame_katalog, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

canvas.configure(yscrollcommand=scrollbar.set)

# Frame untuk katalog
katalog_frame = ttk.Frame(canvas)
canvas.create_window((0, 0), window=katalog_frame, anchor="nw")

# Keranjang belanja
frame_keranjang = ttk.LabelFrame(root, text="Keranjang Belanja")
frame_keranjang.pack(fill="x", padx=10, pady=10)

keranjang_listbox = tk.Listbox(frame_keranjang, height=8)
keranjang_listbox.pack(fill="x", padx=5, pady=5)

# Tombol checkout
frame_aksi = tk.Frame(root)
frame_aksi.pack(fill="x", padx=40, pady=40)

ttk.Button(frame_aksi, text="Checkout", command=checkout).pack(anchor="center", pady=5)

# Jalankan aplikasi
root.mainloop()