
def solve(a, b):
    for price in range(1, 101):
        tax_8 = int(price * 0.08)
        tax_10 = int(price * 0.1)
        if tax_8 == a and tax_10 == b:
            return price
    return -1

