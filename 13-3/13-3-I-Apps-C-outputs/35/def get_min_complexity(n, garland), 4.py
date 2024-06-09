
def get_min_complexity(n, garland):
    # Initialize the complexity to 0
    complexity = 0
    # Iterate through the garland
    for i in range(n):
        # Check if the current bulb is not removed
        if garland[i] != 0:
            # Get the number of the current bulb
            curr_num = garland[i]
            # Get the number of the next bulb
            next_num = garland[(i + 1) % n]
            # Check if the current and next bulbs have different parity
            if curr_num % 2 != next_num % 2:
                # Increment the complexity
                complexity += 1
    # Return the minimum complexity
    return complexity

