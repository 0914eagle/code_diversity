
def solve(n, k, a):
    # Sort the prices in ascending order
    a.sort()
    # Initialize the minimum difference between prices
    min_diff = k + 1
    # Initialize the maximum equal price
    max_price = -1
    # Iterate over the prices
    for i in range(n):
        # Calculate the difference between the current price and the previous price
        diff = a[i] - a[i - 1] if i > 0 else k + 1
        # If the difference is less than the minimum difference, update the minimum difference
        if diff < min_diff:
            min_diff = diff
        # If the difference is equal to the minimum difference, update the maximum equal price
        if diff == min_diff:
            max_price = a[i]
    # Return the maximum equal price
    return max_price

