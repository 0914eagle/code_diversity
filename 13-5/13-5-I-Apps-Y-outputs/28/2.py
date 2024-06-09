
def solve(S):
    price = 700
    for c in S:
        if c == 'o':
            price += 100
    return price

