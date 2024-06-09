
def get_maximum_value_of_jewels(n, k, jewels):
    # Sort the jewels in descending order of value
    jewels.sort(key=lambda x: x[1], reverse=True)
    
    # Initialize the knapsack with zero value
    knapsack = [0] * (k + 1)
    
    # Loop through the jewels
    for jewel in jewels:
        # Get the size and value of the jewel
        size, value = jewel
        
        # Loop through the knapsack sizes
        for i in range(1, k + 1):
            # Check if the jewel fits in the current knapsack size
            if size <= i:
                # Update the knapsack value with the maximum of the current value and the value of the jewel
                knapsack[i] = max(knapsack[i], knapsack[i - size] + value)
    
    # Return the maximum value in the knapsack
    return knapsack[-1]

