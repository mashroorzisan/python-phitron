class Shop:
    cart = [] #class attribute
    def __init__(self, buyer):
        self.buyer = buyer

    def add_to_cart(self, item):
        self.cart.append(item)

mehzabeen = Shop("mehzabeen")
mehzabeen.add_to_cart("shoes")
mehzabeen.add_to_cart(12)
mehzabeen.add_to_cart("bangi")
print(mehzabeen.cart)
