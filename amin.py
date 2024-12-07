import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import json

# Inisialisasi data pengguna
users_data = {}

# Fungsi untuk menyimpan data ke file JSON
def save_users_to_json():
    with open("users.json", "w") as file:
        json.dump(users_data, file)

# Fungsi untuk memuat data dari file JSON
def load_users_from_json():
    global users_data
    try:
        with open("users.json", "r") as file:
            users_data = json.load(file)
    except FileNotFoundError:
        users_data = {}

# Fungsi untuk halaman belanja
def open_shopping_page():
    for widget in root.winfo_children():
        widget.destroy()
    setup_shopping_page()

# Fungsi untuk Sign Up
def signup():
    def submit_signup():
        username = username_entry.get()
        email = email_entry.get()
        password = password_entry.get()
        if username and email and password:
            if email in users_data:
                messagebox.showerror("Error", "Email sudah terdaftar!")
            else:
                users_data[email] = {"username": username, "password": password}
                save_users_to_json()
                messagebox.showinfo("Berhasil", "Akun berhasil dibuat! Silakan login.")
                signup_window.destroy()
        else:
            messagebox.showwarning("Peringatan", "Harap isi semua kolom!")

    signup_window = tk.Toplevel(root)
    signup_window.title("Sign Up")
    tk.Label(signup_window, text="Username").pack()
    username_entry = ttk.Entry(signup_window)
    username_entry.pack()
    tk.Label(signup_window, text="Email").pack()
    email_entry = ttk.Entry(signup_window)
    email_entry.pack()
    tk.Label(signup_window, text="Password").pack()
    password_entry = ttk.Entry(signup_window, show="*")
    password_entry.pack()
    ttk.Button(signup_window, text="Sign Up", command=submit_signup).pack()

# Fungsi untuk Login
def login():
    def submit_login():
        email = email_entry.get()
        password = password_entry.get()
        if email in users_data and users_data[email]["password"] == password:
            messagebox.showinfo("Berhasil", f"Selamat datang, {users_data[email]['username']}!")
            login_window.destroy()
            open_shopping_page()
        else:
            messagebox.showerror("Error", "Email atau password salah!")

    login_window = tk.Toplevel(root)
    login_window.title("Login")
    tk.Label(login_window, text="Email").pack()
    email_entry = ttk.Entry(login_window)
    email_entry.pack()
    tk.Label(login_window, text="Password").pack()
    password_entry = ttk.Entry(login_window, show="*")
    password_entry.pack()
    ttk.Button(login_window, text="Login", command=submit_login).pack()

# Halaman awal aplikasi
def setup_home_page():
    tk.Label(root, text="Selamat Datang di Pace&Stride", font=("Arial", 18, "bold")).pack(pady=20)
    ttk.Button(root, text="Sign Up", command=signup).pack(pady=5)
    ttk.Button(root, text="Login", command=login).pack(pady=5)

# Fungsi untuk halaman belanja
def setup_shopping_page():
    tk.Label(root, text="Halaman Belanja", font=("Arial", 18, "bold")).pack(pady=20)

    # Frame untuk katalog produk
    katalog_frame = ttk.Frame(root)
    katalog_frame.pack(fill="both", expand=True)

    # Katalog sepatu
    for category, sepatu_list in sepatu_data.items():
        for produk in sepatu_list:
            frame_produk = ttk.Frame(katalog_frame, relief="ridge", padding=10)
            frame_produk.pack(fill="x", padx=5, pady=5)

            # Nama produk
            label_nama = ttk.Label(frame_produk, text=produk["nama"], font=("Segoe UI Semibold", 12, "bold"))
            label_nama.pack(anchor="w")

            # Harga produk
            label_harga = ttk.Label(frame_produk, text=f"Rp {produk['harga']:,}", font=("Segoe UI Semibold", 10))
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
        label_nama = ttk.Label(frame_produk, text=produk["nama"], font=("Segoe UI Semibold", 12, "bold"))
        label_nama.pack(anchor="w")

        # Harga produk
        label_harga = ttk.Label(frame_produk, text=f"Rp {produk['harga']:,}", font=("Segoe UI Semibold", 10))
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

# Ganti warna background aplikasi
root.configure(bg="#323774")

# Atur style untuk tombol
style = ttk.Style()
style.configure("Custom.TButton", background="#ccf73b", foreground="#ccf73b", font=("Segoe UI Semibold", 10))
style.configure("Custom.TFrame", background="#ccf73b")

# Nama aplikasi di bagian atas
nama_aplikasi = tk.Label(root, text="Pace&Stride", font=("Rockwell Extra Bold", 22, "bold"), bg="#323774", fg="#ccf73b")
nama_aplikasi.pack(pady=10)

# Variabel
keranjang = []
tipe_kaki_var = tk.StringVar()
ukuran_var = tk.StringVar()
tipe_jarak_var = tk.StringVar()

# Panduan tipe kaki
ttk.Button(root, text="Panduan Tipe Kaki", style="Custom.TButton", command=tampilkan_panduan_kaki).pack(pady=5)

# Panduan tipe jarak
ttk.Button(root, text="Panduan Tipe Jarak", style="Custom.TButton", command=tampilkan_panduan_jarak).pack(pady=5)

# Atur tampilan awal halaman login/signup
setup_home_page()

# Mulai aplikasi
root.mainloop()
