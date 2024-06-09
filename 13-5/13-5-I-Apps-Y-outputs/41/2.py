
def equalize_prices(a, k):
    # Sort the prices in non-decreasing order
    a.sort()
    # Initialize the minimum difference between prices to k + 1
    min_diff = k + 1
    # Initialize the equal price to be returned
    equal_price = 0
    # Loop through the prices and find the minimum difference
    for i in range(len(a) - 1):
        diff = a[i + 1] - a[i]
        if diff < min_diff:
            min_diff = diff
            equal_price = a[i] + diff // 2
    # Check if the minimum difference is less than or equal to k
    if min_diff <= k:
        return equal_price
    else:
        return -1

