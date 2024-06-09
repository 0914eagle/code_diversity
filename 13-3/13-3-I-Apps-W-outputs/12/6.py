
def get_max_fruits(n, v, trees):
    # Sort the trees by the day they ripen
    trees.sort(key=lambda x: x[0])

    # Initialize the variables
    total_fruits = 0
    current_day = 1

    # Loop through the trees
    for tree in trees:
        # Check if the current day is less than or equal to the day the fruit ripens
        if current_day <= tree[0]:
            # Add the number of fruits to the total
            total_fruits += tree[1]
            # Increment the current day
            current_day += 1
        # If the current day is greater than the day the fruit ripens, break the loop
        else:
            break

    # Return the total fruits
    return total_fruits

