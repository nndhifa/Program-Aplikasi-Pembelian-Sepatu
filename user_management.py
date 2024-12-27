from data_handler import load_data, save_data

AKUN_FILE = "akunfix.json"

def load_accounts():
    return load_data(AKUN_FILE)

def save_accounts(accounts):
    save_data(accounts, AKUN_FILE)

def login(username, password, accounts):
    if username in accounts and accounts[username] == password:
        return True
    return False

def register(username, password, accounts):
    if username in accounts:
        return False
    accounts[username] = password
    save_accounts(accounts)
    return True
