
def get_min_complexity(n, garland):
    # Sort the garland in ascending order
    garland.sort()
    # Initialize the complexity to 0
    complexity = 0
    # Iterate through the garland and check for adjacent bulbs with different parity
    for i in range(n - 1):
        if garland[i] % 2 != garland[i + 1] % 2:
            complexity += 1
    return complexity

