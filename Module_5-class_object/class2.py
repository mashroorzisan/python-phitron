class Shop:
    shopping_mall = 'Jamuna'
    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = [] #instance attribute

    def add_to_cart(self, item):
        self.cart.append(item)
    
mehjabeen = Shop('mehjabeen')
mehjabeen.add_to_cart(12)
mehjabeen.add_to_cart("hannan o monnan")
