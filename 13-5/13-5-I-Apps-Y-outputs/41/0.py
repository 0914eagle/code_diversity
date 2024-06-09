
def equalize_prices(a, k):
    # Sort the prices in non-decreasing order
    a.sort()
    # Initialize the minimum difference between prices to infinity
    min_diff = float('inf')
    # Initialize the equal price to be returned
    equal_price = -1
    # Loop through the prices and find the minimum difference between them
    for i in range(len(a) - 1):
        diff = a[i + 1] - a[i]
        if diff <= k:
            min_diff = min(min_diff, diff)
        else:
            break
    # If the minimum difference is less than or equal to k, return the average of the two closest prices
    if min_diff <= k:
        equal_price = (a[0] + a[-1]) // 2
    return equal_price

