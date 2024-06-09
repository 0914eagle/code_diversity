
def max_value_jewels(jewels, knapsack_sizes):
    # Initialize a dictionary to store the maximum value of jewels for each knapsack size
    max_values = {i: 0 for i in knapsack_sizes}

    # Sort the jewels by their value in descending order
    jewels.sort(key=lambda x: x[1], reverse=True)

    # Iterate through the jewels and add them to the knapsack of the appropriate size
    for jewel in jewels:
        size, value = jewel
        for i in range(len(knapsack_sizes)):
            if size <= knapsack_sizes[i]:
                max_values[knapsack_sizes[i]] += value
                break

    return list(max_values.values())

