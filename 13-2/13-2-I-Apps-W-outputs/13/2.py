
def get_max_apples(n, x_a_pairs):
    # Sort the x_a_pairs based on the x coordinate
    x_a_pairs.sort(key=lambda x: x[0])

    # Initialize the maximum number of apples collected
    max_apples = 0

    # Initialize the current x coordinate
    current_x = 0

    # Initialize the current direction (left or right)
    direction = "right"

    # Iterate through the x_a_pairs
    for x, a in x_a_pairs:
        # If the current x coordinate is less than the x coordinate of the current apple tree
        if current_x < x:
            # Update the current direction to "right"
            direction = "right"
        # If the current x coordinate is greater than the x coordinate of the current apple tree
        elif current_x > x:
            # Update the current direction to "left"
            direction = "left"

        # Update the current x coordinate
        current_x = x

        # If the current direction is "right"
        if direction == "right":
            # Update the maximum number of apples collected
            max_apples += a
        # If the current direction is "left"
        elif direction == "left":
            # Update the maximum number of apples collected
            max_apples += a

    # Return the maximum number of apples collected
    return max_apples

