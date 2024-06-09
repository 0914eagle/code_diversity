
def get_max_fruits(n, v, a, b):
    # Sort the trees by the day they ripen
    sorted_trees = sorted(zip(a, b), key=lambda x: x[0])

    # Initialize the variables
    total_fruits = 0
    current_day = 1

    # Loop through the trees
    for tree in sorted_trees:
        # Check if the tree can be collected on the current day
        if current_day == tree[0]:
            # Add the fruits from the current tree to the total
            total_fruits += tree[1]
            # Decrement the number of fruits Valera can collect
            v -= tree[1]
            # Increment the current day
            current_day += 1

        # Check if the tree can be collected on the next day
        elif current_day == tree[0] + 1:
            # Add the fruits from the current tree to the total
            total_fruits += tree[1]
            # Decrement the number of fruits Valera can collect
            v -= tree[1]
            # Increment the current day
            current_day += 1

        # Check if the tree cannot be collected
        else:
            # Do nothing
            pass

    # Return the total number of fruits
    return total_fruits

