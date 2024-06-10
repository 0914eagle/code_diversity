
def is_possible(height, width, bricks):
    # Initialize variables
    current_height = 0
    current_width = 0
    layers = 0

    # Iterate through the bricks
    for brick in bricks:
        # Check if the brick fits in the current layer
        if current_width + brick <= width:
            # Add the brick to the current layer
            current_width += brick
        else:
            # Move to the next layer
            layers += 1
            current_width = brick

        # Check if the brick fits in the current layer
        if current_height + 1 <= height:
            # Add the brick to the current layer
            current_height += 1
        else:
            # Move to the next layer
            layers += 1
            current_height = 1

    # Check if the last layer is complete
    if current_height == height and current_width == width:
        return True
    else:
        return False

def main():
    # Read the input
    height, width, n = map(int, input().split())
    bricks = list(map(int, input().split()))

    # Check if the construction worker can complete the wall
    if is_possible(height, width, bricks):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

