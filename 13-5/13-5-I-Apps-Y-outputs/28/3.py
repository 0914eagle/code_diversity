
def solve(S):
    price = 700
    toppings = 0
    for char in S:
        if char == 'o':
            toppings += 1
    price += toppings * 100
    return price

