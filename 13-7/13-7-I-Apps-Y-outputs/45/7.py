
def get_tower_count(widths):
    # Initialize variables
    tower_count = 0
    current_tower_height = 0

    # Iterate through the widths of the bricks
    for width in widths:
        # If the width is greater than the current tower height, we have finished a tower
        if width > current_tower_height:
            tower_count += 1
            current_tower_height = width
        # Otherwise, we add the brick to the current tower
        else:
            current_tower_height += width

    return tower_count

def main():
    # Read the input
    num_bricks = int(input())
    brick_widths = [int(x) for x in input().split()]

    # Call the function to get the tower count
    tower_count = get_tower_count(brick_widths)

    # Print the output
    print(tower_count)

if __name__ == '__main__':
    main()

