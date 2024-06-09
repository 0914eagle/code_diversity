
def is_wall_completable(height, width, bricks):
    # Initialize variables
    current_layer = 0
    current_row = 0
    layers = []

    # Iterate through the bricks
    for brick in bricks:
        # If the current layer is full, move to the next layer
        if current_row == width:
            current_layer += 1
            current_row = 0

        # If the current layer is not full, add the brick to the layer
        if current_layer < height:
            layers.append(brick)
            current_row += 1

    # Check if the last layer is full
    if current_row == width:
        return "YES"
    else:
        return "NO"

