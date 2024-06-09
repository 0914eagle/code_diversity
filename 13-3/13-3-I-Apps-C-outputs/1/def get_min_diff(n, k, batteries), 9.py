
def get_min_diff(n, k, batteries):
    # Sort the batteries in non-decreasing order
    batteries.sort()
    # Initialize the minimum difference to a large value
    min_diff = float('inf')
    # Loop through all possible combinations of batteries for each chip
    for i in range(len(batteries) - k + 1):
        chip_1 = batteries[i:i+k]
        chip_2 = batteries[i+k:i+2*k]
        # Calculate the difference between the power outputs of the two chips
        diff = abs(min(chip_1) - min(chip_2))
        # Update the minimum difference if necessary
        min_diff = min(min_diff, diff)
    # Return the minimum difference
    return min_diff

