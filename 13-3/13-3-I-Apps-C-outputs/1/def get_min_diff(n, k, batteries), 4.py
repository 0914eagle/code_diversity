
def get_min_diff(n, k, batteries):
    # Sort the batteries in non-decreasing order
    batteries.sort()
    # Initialize the minimum difference to a large value
    min_diff = float('inf')
    # Loop through all possible combinations of batteries for each chip
    for i in range(len(batteries) - k + 1):
        # Get the power output of the first chip
        chip1_power = batteries[i]
        # Get the power output of the second chip
        chip2_power = batteries[i + k - 1]
        # Calculate the difference in power outputs
        diff = abs(chip1_power - chip2_power)
        # Update the minimum difference if necessary
        min_diff = min(min_diff, diff)
    # Return the minimum difference
    return min_diff

