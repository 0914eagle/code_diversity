
def is_wall_completed(h, w, n, x):
    # Initialize variables
    current_layer = 0
    current_row = 0
    total_bricks = 0

    # Iterate through the bricks
    for i in range(n):
        # Check if the current brick fits in the current layer
        if total_bricks + x[i] <= w:
            # Add the brick to the current layer
            total_bricks += x[i]
        else:
            # Move to the next layer
            current_layer += 1
            current_row = 0
            total_bricks = x[i]

        # Check if the current layer is complete
        if current_layer == h:
            # Check if the current brick fits in the last layer
            if total_bricks == w:
                return "YES"
            else:
                return "NO"

    # Check if the last layer is complete
    if total_bricks == w:
        return "YES"
    else:
        return "NO"

