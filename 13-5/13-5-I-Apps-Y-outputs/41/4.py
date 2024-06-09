
def solve(a, k):
    # Sort the prices in ascending order
    a.sort()
    # Initialize the minimum difference between prices as k
    min_diff = k
    # Initialize the equal price as the first price
    equal_price = a[0]
    # Iterate through the prices
    for i in range(1, len(a)):
        # Calculate the difference between the current price and the equal price
        diff = abs(a[i] - equal_price)
        # If the difference is less than the minimum difference, update the minimum difference and the equal price
        if diff < min_diff:
            min_diff = diff
            equal_price = a[i]
    # Return the equal price
    return equal_price

