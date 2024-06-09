
def equalize_prices(a, k):
    # Sort the prices in non-decreasing order
    a.sort()
    # Initialize the minimum difference between prices to be the maximum possible value
    min_diff = float('inf')
    # Initialize the equal price to be the minimum possible value
    equal_price = 0
    # Loop through the prices and find the minimum difference between any two prices
    for i in range(len(a) - 1):
        diff = a[i + 1] - a[i]
        if diff < min_diff:
            min_diff = diff
            equal_price = (a[i] + a[i + 1]) // 2
    # Check if the minimum difference is less than or equal to the given threshold k
    if min_diff <= k:
        return equal_price
    else:
        return -1

