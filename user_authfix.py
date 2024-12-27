from data_management import load_data, save_data

def load_akun():
    return load_data("akunfix.json")

def save_akun(akun):
    save_data(akun, "akunfix.json")
