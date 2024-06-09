
def get_maximum_value_of_jewels(jewels, knapsack_sizes):
    # Initialize a dictionary to store the maximum value of jewels for each knapsack size
    max_values = {i: 0 for i in knapsack_sizes}

    # Iterate over the jewels
    for jewel in jewels:
        # Get the size and value of the jewel
        size, value = jewel

        # Iterate over the knapsack sizes
        for knapsack_size in knapsack_sizes:
            # Check if the jewel fits in the current knapsack size
            if size <= knapsack_size:
                # Update the maximum value of jewels for the current knapsack size
                max_values[knapsack_size] = max(max_values[knapsack_size], value + max_values[knapsack_size - size])

    return max_values

