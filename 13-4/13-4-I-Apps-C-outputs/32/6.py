
def get_maximum_value_of_jewels(jewels, knapsack_size):
    # Initialize a dictionary to store the maximum value of jewels that can be taken from each size of knapsack
    max_value_per_knapsack = {}

    # Loop through each jewel and its size
    for jewel, size in jewels:
        # If the size of the jewel is less than or equal to the size of the knapsack, add the value of the jewel to the maximum value for that size of knapsack
        if size <= knapsack_size:
            max_value_per_knapsack[size] = max_value_per_knapsack.get(size, 0) + jewel
        # Otherwise, add the value of the jewel to the maximum value for the next larger size of knapsack
        else:
            max_value_per_knapsack[size + 1] = max_value_per_knapsack.get(size + 1, 0) + jewel

    # Return the maximum value of jewels that can be taken from each size of knapsack
    return [max_value_per_knapsack.get(i, 0) for i in range(1, knapsack_size + 1)]

