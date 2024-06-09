
def equalize_prices(prices, k):
    # Sort the prices in non-decreasing order
    prices.sort()
    # Initialize the minimum difference between prices as k
    min_diff = k
    # Initialize the equal price as the first price
    equal_price = prices[0]
    # Iterate over the prices
    for i in range(1, len(prices)):
        # Calculate the difference between the current price and the equal price
        diff = abs(prices[i] - equal_price)
        # If the difference is less than the minimum difference, update the minimum difference and the equal price
        if diff < min_diff:
            min_diff = diff
            equal_price = prices[i]
    # Return the equal price
    return equal_price

