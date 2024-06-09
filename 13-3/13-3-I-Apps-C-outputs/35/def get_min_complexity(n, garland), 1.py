
def get_min_complexity(n, garland):
    # Initialize the complexity to 0
    complexity = 0
    # Iterate through the garland and count the number of pairs with different parity
    for i in range(n - 1):
        if garland[i] != 0 and garland[i + 1] != 0 and garland[i] % 2 != garland[i + 1] % 2:
            complexity += 1
    # Return the complexity
    return complexity

