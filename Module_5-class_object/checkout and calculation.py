class Shopping:
    cart = []
    def __init__(self, name):
        self.name = name
        self.cart = []
    def add_to_cart(self, item, price, quantity):
        product = {
            "item": item,
            "price": price,
            "quantity": quantity
        }
        self.cart.append(product)

    def checkout(self):
        totalPrice = 0
        totalQuantity = 0 
        totalProducts = len(self.cart)
        for item in self.cart:
            totalQuantity += item["quantity"]
            totalPrice += item["price"] * item["quantity"]
        print("No. of products: ",totalProducts)
        print("No. of items: ", totalQuantity)
        print("Total Price: ",totalPrice)

        
zisanCart = Shopping("zisan")
zisanCart.add_to_cart('alu', 30, 3)
zisanCart.add_to_cart('pepsodent', 50, 2)
zisanCart.add_to_cart('cycle', 5000, 6)
zisanCart.checkout()