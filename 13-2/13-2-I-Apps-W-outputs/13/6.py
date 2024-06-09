
def get_max_apples(n, apple_trees):
    # Sort the apple trees by their position
    apple_trees.sort(key=lambda x: x[0])

    # Initialize the maximum number of apples collected
    max_apples = 0

    # Initialize the current position
    current_position = 0

    # Initialize the current direction (0 for left, 1 for right)
    current_direction = 0

    # Loop through the apple trees
    for tree in apple_trees:
        # If the current position is not the same as the position of the current apple tree
        if current_position != tree[0]:
            # Update the current position
            current_position = tree[0]

            # Update the current direction
            current_direction = 1 - current_direction

        # Add the number of apples on the current apple tree to the maximum number of apples collected
        max_apples += tree[1]

    # Return the maximum number of apples collected
    return max_apples

