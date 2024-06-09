
def find_price_before_tax(a, b):
    for price in range(1, 101):
        tax_8 = round(price * 0.08)
        tax_10 = round(price * 0.10)
        if tax_8 == a and tax_10 == b:
            return price
    return -1

