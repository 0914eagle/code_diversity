
def find_price(a, b):
    # Loop through possible prices
    for price in range(1, 101):
        # Calculate the amount of tax at 8% and 10%
        tax_8 = int(price * 0.08)
        tax_10 = int(price * 0.1)
        # Check if the tax amounts are equal to A and B respectively
        if tax_8 == a and tax_10 == b:
            return price
    # If no price satisfies the condition, return -1
    return -1

