
def get_min_diff(n, k, batteries):
    # Sort the batteries in non-decreasing order
    batteries.sort()
    # Initialize the minimum difference to a large value
    min_diff = 10**9 + 1
    # Loop through all possible combinations of batteries
    for i in range(len(batteries) - k + 1):
        # Get the power output of the first chip
        chip1_power = batteries[i]
        # Get the power output of the second chip
        chip2_power = batteries[i + k - 1]
        # Calculate the difference between the two chips
        diff = abs(chip1_power - chip2_power)
        # If the difference is smaller than the minimum difference, update the minimum difference
        if diff < min_diff:
            min_diff = diff
    # Return the minimum difference
    return min_diff

