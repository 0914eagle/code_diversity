
def get_max_fruits(n, v, a, b):
    # Sort the trees by the day they ripen
    sorted_trees = sorted(zip(a, b), key=lambda x: x[0])

    # Initialize the variables
    total_fruits = 0
    current_day = 1

    # Loop through the trees
    for i in range(n):
        # Check if the current day is before or after the day the tree ripens
        if current_day <= sorted_trees[i][0]:
            # Add the fruits that can be collected on the current day
            total_fruits += min(v, sorted_trees[i][1])
        elif current_day == sorted_trees[i][0] + 1:
            # Add the fruits that can be collected on the next day
            total_fruits += min(v, sorted_trees[i][1] - v)
        current_day += 1

    return total_fruits

