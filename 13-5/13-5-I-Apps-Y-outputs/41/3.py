
def equalize_prices(prices, k):
    # Sort the prices in non-decreasing order
    sorted_prices = sorted(prices)
    # Initialize the minimum difference between prices as k
    min_diff = k
    # Initialize the equal price as the first price
    equal_price = sorted_prices[0]
    # Iterate through the prices
    for i in range(1, len(sorted_prices)):
        # Calculate the difference between the current price and the equal price
        diff = sorted_prices[i] - equal_price
        # If the difference is less than the minimum difference, update the minimum difference and the equal price
        if diff < min_diff:
            min_diff = diff
            equal_price = sorted_prices[i]
    # Return the equal price
    return equal_price

