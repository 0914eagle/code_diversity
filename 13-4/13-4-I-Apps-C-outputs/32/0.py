
def knapsack(jewels, knapsacks):
    # Initialize a dictionary to store the maximum value of jewels for each size of knapsack
    max_values = {}

    # Loop through each jewel and its size
    for jewel, size in jewels:
        # Loop through each size of knapsack
        for i in range(1, knapsacks + 1):
            # If the current size of knapsack is greater than or equal to the current jewel's size
            if i >= size:
                # Update the maximum value of jewels for the current size of knapsack
                max_values[i] = max(max_values.get(i, 0) + jewel, max_values.get(i, 0))

    # Return the maximum value of jewels for each size of knapsack
    return [max_values.get(i, 0) for i in range(1, knapsacks + 1)]

