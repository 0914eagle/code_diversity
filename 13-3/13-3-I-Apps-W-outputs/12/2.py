
def get_max_fruits(n, v, a, b):
    # Sort the trees by the day they ripen
    sorted_trees = sorted(zip(a, b), key=lambda x: x[0])

    # Initialize the variables
    total_fruits = 0
    current_day = 1

    # Loop through the trees
    for i in range(n):
        # Check if the current day is before or equal to the day the tree ripens
        if current_day <= sorted_trees[i][0]:
            # Add the number of fruits that can be collected on the current day
            total_fruits += min(v, sorted_trees[i][1])
            # Increment the current day
            current_day += 1

    # Return the total number of fruits collected
    return total_fruits

