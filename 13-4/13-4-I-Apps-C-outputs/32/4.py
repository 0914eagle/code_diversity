
def knapsack(jewels, knapsacks):
    # Initialize a dictionary to store the maximum value of jewels for each size of knapsack
    max_values = {}

    # Loop through each jewel and its size and value
    for s, v in jewels:
        # Loop through each size of knapsack and calculate the maximum value of jewels that can be taken
        for k in range(1, knapsacks + 1):
            # If the current size of knapsack is greater than the current jewel size, add the jewel value to the maximum value for that size of knapsack
            if k >= s:
                max_values[k] = max(max_values.get(k, 0) + v, max_values.get(k, 0))

    # Return the maximum value of jewels for each size of knapsack
    return [max_values.get(i, 0) for i in range(1, knapsacks + 1)]

