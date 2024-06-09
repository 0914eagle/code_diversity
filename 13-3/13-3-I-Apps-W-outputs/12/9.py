
def get_max_fruits(n, v, a, b):
    # Sort the trees by the day they ripen
    sorted_trees = sorted(zip(a, b), key=lambda x: x[0])

    # Initialize the variables
    total_fruits = 0
    current_day = 1

    # Loop through the trees and collect fruits
    for tree in sorted_trees:
        # Check if the tree ripens today
        if tree[0] == current_day:
            # Check if Valera can collect all the fruits from this tree
            if tree[1] <= v:
                # Add the fruits to the total and move on to the next tree
                total_fruits += tree[1]
            else:
                # Add the maximum number of fruits Valera can collect and move on to the next tree
                total_fruits += v
        # Check if the tree ripens tomorrow
        elif tree[0] == current_day + 1:
            # Check if Valera can collect all the fruits from this tree
            if tree[1] <= v:
                # Add the fruits to the total and move on to the next tree
                total_fruits += tree[1]
            else:
                # Add the maximum number of fruits Valera can collect and move on to the next tree
                total_fruits += v
        # The tree does not ripen today or tomorrow, skip it
        else:
            continue

        # Increment the current day
        current_day += 1

    # Return the total number of fruits collected
    return total_fruits

