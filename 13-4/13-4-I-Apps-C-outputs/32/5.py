
def max_value_knapsack(jewels, knapsacks):
    # Initialize a dictionary to store the maximum value for each knapsack size
    max_values = {}

    # Loop through each jewel
    for jewel in jewels:
        # Get the size and value of the jewel
        size, value = jewel

        # Loop through each knapsack size
        for knapsack in range(1, knapsacks + 1):
            # Check if the jewel fits in the knapsack
            if size <= knapsack:
                # Update the maximum value for the knapsack size
                max_values[knapsack] = max(max_values.get(knapsack, 0) + value, max_values.get(knapsack, 0))

    # Return the maximum value for each knapsack size
    return [max_values.get(i, 0) for i in range(1, knapsacks + 1)]

