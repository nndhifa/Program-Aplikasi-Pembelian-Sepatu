import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

# Data for shoes and other products
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

# User credentials database
user_credentials = {}

# Functions for SignUp and Login
def sign_up():
    username = simpledialog.askstring("Sign Up", "Enter username:")
    if username in user_credentials:
        messagebox.showwarning("Warning", "Username already exists.")
        return
    password = simpledialog.askstring("Sign Up", "Enter password:", show="*")
    user_credentials[username] = password
    messagebox.showinfo("Success", "Account created successfully! You can now log in.")

def login():
    username = simpledialog.askstring("Login", "Enter username:")
    password = simpledialog.askstring("Login", "Enter password:", show="*")
    if username in user_credentials and user_credentials[username] == password:
        messagebox.showinfo("Success", "Login successful!")
        root.withdraw()  # Hide the login window
        show_main_page()  # Show the main page
    else:
        messagebox.showwarning("Login Failed", "Invalid username or password.")

# Main page after login
def show_main_page():
    main_window = tk.Toplevel(root)
    main_window.title("Main Shopping Page")
    main_window.geometry("800x600")

    # Main shopping page UI components here (as shown in your provided code)
    # Example:
    main_label = tk.Label(main_window, text="Welcome to the Shopping App", font=("Arial", 16))
    main_label.pack(pady=20)

    # Add further shopping-related components (product display, cart, etc.)

    # Option to logout and go back to login
    logout_button = ttk.Button(main_window, text="Logout", command=main_window.destroy)
    logout_button.pack(pady=10)

# Setup initial root window for login/signup
root = tk.Tk()
root.title("User Login / Signup")
root.geometry("400x300")

# Buttons for Sign Up and Login
sign_up_button = ttk.Button(root, text="Sign Up", command=sign_up)
sign_up_button.pack(pady=10)

login_button = ttk.Button(root, text="Login", command=login)
login_button.pack(pady=10)

# Start the application with login/signup screen
root.mainloop()
