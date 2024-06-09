
def max_value_jewels(jewels, knapsack_size):
    # Initialize a dictionary to store the maximum value of jewels for each size of knapsack
    max_values = {i: 0 for i in range(1, knapsack_size + 1)}

    # Iterate over the jewels
    for jewel in jewels:
        # Get the size and value of the jewel
        size, value = jewel

        # Iterate over the sizes of knapsacks
        for i in range(1, knapsack_size + 1):
            # Check if the jewel fits in the current knapsack
            if size <= i:
                # Update the maximum value of jewels for the current knapsack
                max_values[i] = max(max_values[i], max_values[i - size] + value)

    return max_values

