
def solve(s):
    price = 700
    toppings = {'o': 100, 'x': 0}
    for char in s:
        price += toppings[char]
    return price

