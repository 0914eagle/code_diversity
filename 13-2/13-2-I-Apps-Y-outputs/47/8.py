
def is_wall_completable(height, width, bricks):
    # Initialize variables
    current_layer = 0
    current_row = 0
    num_rows = 0
    num_bricks = len(bricks)

    # Iterate through the bricks
    for i in range(num_bricks):
        # Check if the current brick fits in the current layer
        if current_row + bricks[i] <= width:
            # If it fits, add it to the current layer
            current_row += bricks[i]
        else:
            # If it doesn't fit, move to the next layer
            current_layer += 1
            current_row = bricks[i]
            num_rows += 1

    # Check if the last layer is complete
    if current_layer < height - 1 or current_row < width:
        return "NO"
    else:
        return "YES"

