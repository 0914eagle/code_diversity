
def is_wall_completed(height, width, bricks):
    # Initialize variables
    current_layer = 0
    current_row = 0
    layers = []

    # Iterate through the bricks
    for brick in bricks:
        # If the current layer is not full, add the brick to the current layer
        if current_row < width:
            layers[current_layer].append(brick)
            current_row += brick
        # If the current layer is full, move to the next layer
        else:
            current_layer += 1
            current_row = brick
            layers.append([brick])

    # Check if the last layer is full
    if current_row == width:
        return "YES"
    else:
        return "NO"

