import tkinter as tk
from tkinter import ttk, messagebox

# Database sepatu lari
sepatu = {
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
            {"nama": "Brooks Marathon Master", "harga": 1800000, "deskripsi": "Desain khusus untuk marathon"}
        ]
    },
    "Sempit": {
        "Jarak Pendek": [
            {"nama": "Nike Slim Race", "harga": 1100000, "deskripsi": "Desain khusus untuk kaki sempit"}
        ],
        "Jarak Menengah": [
            {"nama": "New Balance Slim Runner", "harga": 1400000, "deskripsi": "Dukungan optimal untuk kaki sempit"}
        ],
        "Jarak Jauh": [
            {"nama": "ASICS Precision Long", "harga": 1700000, "deskripsi": "Ultra marathon untuk kaki sempit"}
        ]
    },
    "Lebar": {
        "Jarak Pendek": [
            {"nama": "Nike Wide Sprint", "harga": 1250000, "deskripsi": "Desain khusus untuk kaki lebar"}
        ],
        "Jarak Menengah": [
            {"nama": "ASICS Wide Support", "harga": 1550000, "deskripsi": "Stabilitas maksimal untuk kaki lebar"}
        ],
        "Jarak Jauh": [
            {"nama": "Hoka Wide Marathon", "harga": 2100000, "deskripsi": "Ultra support untuk kaki lebar"}
        ]
    }
}

# Barang tambahan
barang_lain = {
    "Kaos Lari": 350000,
    "Celana Lari": 450000,
    "Aksesoris Lari": 500000
}

# Data akun (Sementara menggunakan dictionary)
akun_data = {}

# Fungsi untuk menampilkan rekomendasi sepatu
def tampilkan_rekomendasi():
    tipe = tipe_kaki_var.get()
    ukuran = ukuran_sepatu_var.get()
    if not tipe or not ukuran:
        messagebox.showwarning("Peringatan", "Pilih tipe kaki dan ukuran sepatu terlebih dahulu!")
        return

    rekomendasi_listbox.delete(0, tk.END)  # Bersihkan listbox

    tipe_sepatu = sepatu.get(tipe)
    if tipe_sepatu:
        for kategori, produk_list in tipe_sepatu.items():
            rekomendasi_listbox.insert(tk.END, f"-- {kategori} (Ukuran {ukuran}) --")
            for produk in produk_list:
                rekomendasi_listbox.insert(tk.END, f"{produk['nama']} - Rp {produk['harga']:,}")

# Fungsi untuk menambahkan item ke keranjang
def tambah_ke_keranjang():
    selected_sepatu = rekomendasi_listbox.get(tk.ACTIVE)
    if selected_sepatu and not selected_sepatu.startswith("--"):
        keranjang_listbox.insert(tk.END, selected_sepatu)

    for barang, var in barang_var.items():
        if var.get():
            keranjang_listbox.insert(tk.END, f"{barang} - Rp {barang_lain[barang]:,}")

# Fungsi untuk menyelesaikan transaksi
def checkout():
    items = keranjang_listbox.get(0, tk.END)
    if not items:
        messagebox.showwarning("Peringatan", "Keranjang belanja kosong!")
        return

    total = 0
    for item in items:
        if "Rp" in item:
            harga = int(item.split("Rp")[1].replace(".", "").replace(",", "").strip())
            total += harga

    uang_bayar = uang_bayar_var.get()
    if uang_bayar < total:
        messagebox.showwarning("Peringatan", "Uang yang Anda bayar kurang!")
        return

    kembalian = uang_bayar - total
    messagebox.showinfo("Checkout", f"Total belanja Anda: Rp {total:,}\nUang yang dibayar: Rp {uang_bayar:,}\nKembalian: Rp {kembalian:,}")
    keranjang_listbox.delete(0, tk.END)  # Kosongkan keranjang setelah checkout
    uang_bayar_var.set(0)  # Reset input uang bayar

    # Menampilkan ucapan terima kasih
    messagebox.showinfo("Terima Kasih", "Terima kasih telah berbelanja!")

# Fungsi untuk halaman login
def halaman_login():
    def login():
        email = entry_email.get()
        password = entry_password.get()
        if email in akun_data and akun_data[email]['password'] == password:
            halaman_produk()
        else:
            messagebox.showerror("Login Gagal", "Email atau password salah")

    def sign_up():
        # Menampilkan form registrasi
        frame_login.pack_forget()
        frame_sign_up.pack(padx=10, pady=10)

    frame_login = tk.Frame(root)
    frame_login.pack(padx=10, pady=10)

    tk.Label(frame_login, text="Email:").grid(row=0, column=0, pady=5)
    entry_email = tk.Entry(frame_login)
    entry_email.grid(row=0, column=1, pady=5)

    tk.Label(frame_login, text="Password:").grid(row=1, column=0, pady=5)
    entry_password = tk.Entry(frame_login, show="*")
    entry_password.grid(row=1, column=1, pady=5)

    login_button = tk.Button(frame_login, text="Login", command=login)
    login_button.grid(row=2, column=0, columnspan=2, pady=10)

    sign_up_button = tk.Button(frame_login, text="Sign Up", command=sign_up)
    sign_up_button.grid(row=3, column=0, columnspan=2, pady=5)

# Fungsi halaman sign up
def halaman_sign_up():
    def register():
        nama = entry_nama_signup.get()
        email = entry_email_signup.get()
        password = entry_password_signup.get()
        confirm_password = entry_confirm_password_signup.get()

        if email in akun_data:
            messagebox.showerror("Error", "Akun dengan email ini sudah ada.")
        elif password != confirm_password:
            messagebox.showerror("Error", "Password dan konfirmasi password tidak cocok.")
        else:
            akun_data[email] = {"nama": nama, "password": password}
            messagebox.showinfo("Berhasil", "Akun berhasil dibuat! Silakan login.")
            frame_sign_up.pack_forget()
            halaman_login()

    frame_sign_up = tk.Frame(root)

    tk.Label(frame_sign_up, text="Nama Lengkap:").grid(row=0, column=0, pady=5)
    entry_nama_signup = tk.Entry(frame_sign_up)
    entry_nama_signup.grid(row=0, column=1, pady=5)

    tk.Label(frame_sign_up, text="Email:").grid(row=1, column=0, pady=5)
    entry_email_signup = tk.Entry(frame_sign_up)
    entry_email_signup.grid(row=1, column=1, pady=5)

    tk.Label(frame_sign_up, text="Password:").grid(row=2, column=0, pady=5)
    entry_password_signup = tk.Entry(frame_sign_up, show="*")
    entry_password_signup.grid(row=2, column=1, pady=5)

    tk.Label(frame_sign_up, text="Confirm Password:").grid(row=3, column=0, pady=5)
    entry_confirm_password_signup = tk.Entry(frame_sign_up, show="*")
    entry_confirm_password_signup.grid(row=3, column=1, pady=5)

    register_button = tk.Button(frame_sign_up, text="Register", command=register)
    register_button.grid(row=4, column=0, columnspan=2, pady=10)

# Fungsi halaman produk
def halaman_produk():
    frame_produk = tk.Frame(root)
    frame_produk.pack(padx=10, pady=10)

    tk.Label(frame_produk, text="Tipe Kaki:").grid(row=0, column=0, pady=5)
    tipe_kaki_var = ttk.Combobox(frame_produk, values=["Normal", "Sempit", "Lebar"])
    tipe_kaki_var.grid(row=0, column=1, pady=5)

    tk.Label(frame_produk, text="Ukuran Sepatu:").grid(row=1, column=0, pady=5)
    ukuran_sepatu_var = ttk.Combobox(frame_produk, values=["39", "40", "41", "42", "43"])
    ukuran_sepatu_var.grid(row=1, column=1, pady=5)

    rekomendasi_button = tk.Button(frame_produk, text="Tampilkan Rekomendasi", command=tampilkan_rekomendasi)
    rekomendasi_button.grid(row=2, column=0, columnspan=2, pady=10)

    rekomendasi_listbox = tk.Listbox(frame_produk, height=10, width=50)
    rekomendasi_listbox.grid(row=3, column=0, columnspan=2)

    barang_var = {
        "Kaos Lari": tk.BooleanVar(),
        "Celana Lari": tk.BooleanVar(),
        "Aksesoris Lari": tk.BooleanVar()
    }

    for idx, (barang, var) in enumerate(barang_var.items()):
        tk.Checkbutton(frame_produk, text=barang, variable=var).grid(row=4 + idx, column=0, columnspan=2)

    keranjang_button = tk.Button(frame_produk, text="Tambah ke Keranjang", command=tambah_ke_keranjang)
    keranjang_button.grid(row=7, column=0, columnspan=2, pady=5)

    keranjang_listbox = tk.Listbox(frame_produk, height=5, width=50)
    keranjang_listbox.grid(row=8, column=0, columnspan=2)

    tk.Label(frame_produk, text="Uang Bayar:").grid(row=9, column=0, pady=5)
    uang_bayar_var = tk.DoubleVar()
    entry_uang_bayar = tk.Entry(frame_produk, textvariable=uang_bayar_var)
    entry_uang_bayar.grid(row=9, column=1, pady=5)

    checkout_button = tk.Button(frame_produk, text="Checkout", command=checkout)
    checkout_button.grid(row=10, column=0, columnspan=2, pady=10)

# Fungsi utama aplikasi
root = tk.Tk()
root.title("Aplikasi Pembelian Sepatu")

halaman_login()

root.mainloop()
