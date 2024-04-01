balance = 3200


def buy_things(item, price):
    global balance
    balance = balance - price
    print(f"{item} pulu pulu {price} til til")
    print(f"balance inside the function,", balance)


buy_things(23, 200)
