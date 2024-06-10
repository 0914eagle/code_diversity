
def get_wall_completion_status(h, w, n, x):
    # Initialize variables
    layer_height = 1
    layer_width = w
    num_layers = h
    num_bricks = n
    brick_lengths = x

    # Check if the number of bricks is less than the number of layers
    if num_bricks < num_layers:
        return "NO"

    # Check if the total length of the bricks is less than the width of the wall
    if sum(brick_lengths) < layer_width:
        return "NO"

    # Initialize a list to store the bricks for each layer
    layer_bricks = []

    # Iterate through the layers
    for i in range(num_layers):
        # Initialize a list to store the bricks for the current layer
        current_layer_bricks = []

        # Iterate through the bricks
        for j in range(num_bricks):
            # Check if the current brick can be placed in the current layer
            if brick_lengths[j] <= layer_width:
                # Add the brick to the current layer
                current_layer_bricks.append(brick_lengths[j])
                # Decrease the width of the layer by the length of the brick
                layer_width -= brick_lengths[j]

        # Add the current layer to the list of layers
        layer_bricks.append(current_layer_bricks)

        # Check if the current layer is incomplete
        if len(current_layer_bricks) == 0:
            return "NO"

        # Reset the width of the layer to the width of the wall
        layer_width = w

    # Check if all the layers are complete
    if len(layer_bricks) == num_layers:
        return "YES"
    else:
        return "NO"

def main():
    h, w, n = map(int, input().split())
    x = list(map(int, input().split()))
    print(get_wall_completion_status(h, w, n, x))

if __name__ == '__main__':
    main()

