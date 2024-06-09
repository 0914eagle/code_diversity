
def get_min_complexity(n, garland):
    # Sort the garland in ascending order
    garland.sort()
    # Initialize the complexity to 0
    complexity = 0
    # Iterate through the garland
    for i in range(n-1):
        # If the current bulb and the next bulb have different parity, increment the complexity
        if garland[i] % 2 != garland[i+1] % 2:
            complexity += 1
    return complexity

