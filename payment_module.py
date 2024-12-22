from tkinter import messagebox

def konfirmasi_pembayaran(total_harga, metode, keranjang, show_main_menu_callback):
    if metode == "COD":
        messagebox.showinfo(
            "Konfirmasi COD",
            f"Terima kasih telah berbelanja.\n"
            f"Harap siapkan uang tunai sebesar Rp {total_harga:,} saat paket sampai."
        )
        keranjang.clear()
        return 0  # Total harga direset setelah pembayaran
    else:
        return show_virtual_account(total_harga, keranjang, show_main_menu_callback)

def show_virtual_account(total_harga, keranjang, show_main_menu_callback):
    rekening = {
        "Mandiri": "1234567890",
        "BNI": "0987654321",
        "BCA": "1122334455",
        "BRI": "5566778899"
    }
    
def choose_bank_and_confirm(bank):
    nomor_rekening = rekening.get(bank, "Tidak tersedia")
    messagebox.showinfo(
        "Konfirmasi Virtual Account",
        f"Bank: {bank}\n"
        f"Silakan lakukan pembayaran ke nomor rekening berikut:\n{nomor_rekening}\n\n"
        "Pembayaran akan diperiksa sistem. Jika transaksi sukses, paket akan segera dikirimkan."
    )
    keranjang.clear()
    show_main_menu_callback()
    return 0  # Total harga direset setelah pembayaran

    return choose_bank_and_confirm
