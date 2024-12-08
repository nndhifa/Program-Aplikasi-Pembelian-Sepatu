class CartManagement:
    def __init__(self):
        self.keranjang = []
        self.total_harga = 0

    def add_to_cart(self, item):
        """Menambahkan item ke keranjang."""
        self.keranjang.append(item)
        self.total_harga += item['harga']

    def clear_cart(self):
        """Mengosongkan keranjang."""
        self.keranjang = []
        self.total_harga = 0

    def get_total(self):
        """Mengembalikan total harga keranjang."""
        return self.total_harga
