
def solve(a, b):
    # Loop through possible prices
    for price in range(1, 101):
        # Calculate tax for 8% rate
        tax_8 = int(price * 0.08)
        # Calculate tax for 10% rate
        tax_10 = int(price * 0.1)
        # Check if tax amounts match the given values
        if tax_8 == a and tax_10 == b:
            return price
    # If no price satisfies the condition, return -1
    return -1

