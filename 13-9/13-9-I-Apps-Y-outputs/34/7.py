
def get_price_before_tax(A, B):
    for price in range(1, 101):
        tax_8 = round(price * 0.08)
        tax_10 = round(price * 0.1)
        if tax_8 == A and tax_10 == B:
            return price
    return -1

