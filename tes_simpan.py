from revisi import TokoSepatuApp
import tkinter as tk

# Membuat instance aplikasi
root = tk.Tk()
app = TokoSepatuApp(root)

# Tes penyimpanan manual
app.akun = {"test_user": "test_password"}
app.save_akun()
print("Tes penyimpanan selesai. Periksa akunfix.json.")
root.destroy()  # Menutup jendela tkinter
