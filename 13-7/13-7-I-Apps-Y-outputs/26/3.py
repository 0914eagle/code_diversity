
def find_price_before_tax(a, b):
    # Initialize the lowest price that satisfies the condition as -1
    lowest_price = -1

    # Iterate through possible prices
    for price in range(1, 101):
        # Calculate the amount of consumption tax levied on the price
        tax_8 = int(price * 0.08)
        tax_10 = int(price * 0.1)

        # Check if the amount of consumption tax is within the given range
        if a <= tax_8 <= b and a <= tax_10 <= b:
            # If the price satisfies the condition, update the lowest price
            lowest_price = price

    # Return the lowest price that satisfies the condition
    return lowest_price

