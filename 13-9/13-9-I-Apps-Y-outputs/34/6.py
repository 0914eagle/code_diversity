
def solve(a, b):
    # Loop through possible prices
    for price in range(1, 101):
        # Calculate the consumption tax for 8% and 10% tax rates
        tax_8 = int(price * 0.08)
        tax_10 = int(price * 0.1)
        # Check if the consumption tax is equal to A or B
        if tax_8 == a or tax_10 == b:
            return price
    # If no price satisfies the condition, return -1
    return -1

