
def max_value_jewels(jewels, knapsack_size):
    # Initialize a dictionary to store the maximum value of jewels that can be taken from each knapsack
    max_values = {}

    # Loop through each jewel and its value
    for s, v in jewels:
        # Check if the current knapsack size is already full
        if sum(max_values.values()) + s > knapsack_size:
            # If the current knapsack size is full, break the loop
            break
        # If the current knapsack size is not full, add the value of the current jewel to the maximum value for that knapsack size
        max_values[s] = max_values.get(s, 0) + v

    # Return the maximum value of jewels that can be taken from each knapsack
    return list(max_values.values())

