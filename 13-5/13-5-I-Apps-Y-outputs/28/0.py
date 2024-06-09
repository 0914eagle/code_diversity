
def get_ramen_price(S):
    price = 700
    toppings = ["boiled egg", "sliced pork", "green onions"]
    for i, char in enumerate(S):
        if char == "o":
            price += 100
    return price

