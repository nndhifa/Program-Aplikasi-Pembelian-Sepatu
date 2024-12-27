class ShoppingCart:
    def __init__(self):
        self.cart = []
        self.total_price = 0

    def add_item(self, item):
        self.cart.append(item)
        self.total_price += item['harga']

    def remove_item(self, item):
        if item in self.cart:
            self.cart.remove(item)
            self.total_price -= item['harga']

    def clear_cart(self):
        self.cart.clear()
        self.total_price = 0

    def get_items(self):
        return self.cart

    def get_total_price(self):
        return self.total_price
