
def get_price(S):
    price = 700
    toppings = [0, 0, 0]
    for i, char in enumerate(S):
        if char == "o":
            toppings[i] = 1
    for i in range(len(toppings)):
        if toppings[i] == 1:
            price += 100
    return price

