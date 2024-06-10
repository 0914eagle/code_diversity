
def is_wall_complete(height, width, lengths):
    # Initialize variables
    current_height = 0
    current_width = 0
    layers = []

    # Iterate through the lengths of the bricks
    for length in lengths:
        # If the current layer is not full
        if current_width + length <= width:
            # Add the brick to the current layer
            current_width += length
        # If the current layer is full
        else:
            # Add the current layer to the list of layers
            layers.append(current_width)
            # Start a new layer
            current_width = length
            current_height += 1

    # If the last layer is not empty
    if current_width > 0:
        # Add the last layer to the list of layers
        layers.append(current_width)

    # Check if the total height of the layers is greater than or equal to the height of the wall
    return current_height >= height

def main():
    height, width, n = map(int, input().split())
    lengths = list(map(int, input().split()))
    print("YES") if is_wall_complete(height, width, lengths) else print("NO")

if __name__ == '__main__':
    main()

