
def get_maximum_value_of_jewels(jewels, knapsack_sizes):
    # Initialize a dictionary to store the maximum value of jewels for each size of knapsack
    max_values = {}
    
    # Loop through each size of knapsack
    for knapsack_size in knapsack_sizes:
        # Initialize the maximum value for this size of knapsack to 0
        max_value = 0
        
        # Loop through each jewel
        for jewel in jewels:
            # Check if the jewel is smaller than or equal to the current size of the knapsack
            if jewel[0] <= knapsack_size:
                # Add the value of the jewel to the maximum value for this size of knapsack
                max_value += jewel[1]
        
        # Add the maximum value for this size of knapsack to the dictionary
        max_values[knapsack_size] = max_value
    
    # Return the dictionary of maximum values
    return max_values

