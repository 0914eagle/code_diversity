
def equalize_prices(prices, k):
    # Sort the prices in non-decreasing order
    prices.sort()
    # Initialize the minimum difference between prices
    min_diff = float('inf')
    # Initialize the equal price
    equal_price = 0
    # Iterate over the prices
    for i in range(len(prices)):
        # Calculate the difference between the current price and the equal price
        diff = abs(prices[i] - equal_price)
        # If the difference is less than or equal to k, update the minimum difference and equal price
        if diff <= k:
            min_diff = min(min_diff, diff)
            equal_price = prices[i]
        # If the difference is greater than k, break the loop
        else:
            break
    # Return the equal price if the minimum difference is 0, otherwise return -1
    return equal_price if min_diff == 0 else -1

