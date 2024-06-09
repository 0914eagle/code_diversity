
def solve(n, k, batteries):
    # Sort the batteries in non-decreasing order
    batteries.sort()
    # Initialize the minimum difference to a large value
    min_diff = 10**9 + 1
    # Iterate over all possible combinations of batteries
    for i in range(len(batteries) - k + 1):
        # Calculate the power output of the first chip
        chip1_power = sum(batteries[i:i+k])
        # Calculate the power output of the second chip
        chip2_power = sum(batteries[i+k:i+2*k])
        # Calculate the difference in power outputs
        diff = abs(chip1_power - chip2_power)
        # Update the minimum difference if necessary
        min_diff = min(min_diff, diff)
    # Return the minimum difference
    return min_diff

