
def find_price_before_tax(a, b):
    # Loop through possible prices and check if they satisfy the condition
    for price in range(1, 101):
        tax_8 = round(price * 0.08)
        tax_10 = round(price * 0.1)
        if tax_8 == a and tax_10 == b:
            return price
    
    # If no price satisfies the condition, return -1
    return -1

