
def solve(S):
    price = 700
    toppings = {"o": 100, "x": 0}
    for char in S:
        price += toppings[char]
    return price

