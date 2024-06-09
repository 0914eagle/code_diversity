
def get_min_complexity(n, garland):
    # Initialize the complexity to 0
    complexity = 0
    # Iterate through the garland and check if any adjacent bulbs have different parity
    for i in range(n - 1):
        if garland[i] % 2 != garland[i + 1] % 2:
            complexity += 1
    # Return the minimum complexity
    return complexity

