import tkinter as tk
from tkinter import messagebox

def checkout(root, keranjang, total_harga, bayar_entry, clear_screen, show_main_menu):
    clear_screen()

    tk.Label(root, text="Pembayaran", font=("Arial", 20, "bold")).pack(pady=10)
    tk.Label(root, text=f"Total Harga: Rp {total_harga:,}").pack(pady=10)

    tk.Label(root, text="Masukkan jumlah uang pembayaran:").pack()
    bayar_entry = tk.Entry(root)
    bayar_entry.pack()

    tk.Button(root, text="Bayar", command=lambda: proses_pembayaran(bayar_entry, total_harga, keranjang, root, show_main_menu)).pack(pady=10)

def proses_pembayaran(bayar_entry, total_harga, keranjang, root, show_main_menu):
    try:
        bayar = int(bayar_entry.get())
        if bayar >= total_harga:
            kembalian = bayar - total_harga
            messagebox.showinfo("Pembayaran Berhasil", f"Pembayaran berhasil!\nKembalian: Rp {kembalian:,}")
            keranjang.clear()
            total_harga = 0
            show_main_menu()
        else:
            messagebox.showerror("Pembayaran Gagal", "Jumlah uang tidak cukup.")
    except ValueError:
        messagebox.showerror("Error", "Masukkan jumlah uang yang valid.")
