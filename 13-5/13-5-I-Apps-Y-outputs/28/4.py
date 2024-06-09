
def solve(S):
    price = 700
    for char in S:
        if char == 'o':
            price += 100
    return price

