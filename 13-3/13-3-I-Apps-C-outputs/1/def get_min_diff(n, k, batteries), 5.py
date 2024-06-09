
def get_min_diff(n, k, batteries):
    # Sort the batteries in non-decreasing order
    batteries.sort()
    # Initialize the minimum difference to a large value
    min_diff = float('inf')
    # Loop through all possible combinations of batteries for each chip
    for i in range(len(batteries) - k + 1):
        chip1_power = batteries[i]
        chip2_power = batteries[i + k - 1]
        diff = abs(chip1_power - chip2_power)
        if diff < min_diff:
            min_diff = diff
    return min_diff

