
def get_min_complexity(n, garland):
    # Sort the garland in ascending order
    garland.sort()
    # Initialize the complexity and the number of pairs
    complexity = 0
    num_pairs = 0
    # Iterate through the garland
    for i in range(n - 1):
        # If the current bulb and the next bulb have different parity, increment the number of pairs
        if garland[i] % 2 != garland[i + 1] % 2:
            num_pairs += 1
    # Return the minimum complexity
    return num_pairs

