
def is_possible(height, width, bricks):
    
    # Initialize the current layer height to 0
    current_layer_height = 0
    # Initialize the number of bricks used to 0
    num_bricks_used = 0

    # Iterate through the bricks
    for brick in bricks:
        # If the current layer height plus the height of the current brick is less than or equal to the wall height
        if current_layer_height + brick <= height:
            # Add the height of the current brick to the current layer height
            current_layer_height += brick
            # Increment the number of bricks used
            num_bricks_used += 1
        # If the current layer height plus the height of the current brick is greater than the wall height
        else:
            # Break out of the loop
            break

    # If the number of bricks used is equal to the number of bricks available
    if num_bricks_used == len(bricks):
        # Return True
        return True
    else:
        # Return False
        return False

def main():
    # Read the height, width, and number of bricks from stdin
    height, width, num_bricks = map(int, input().split())
    # Read the brick lengths from stdin
    bricks = list(map(int, input().split()))

    # Determine if it is possible to build the wall
    if is_possible(height, width, bricks):
        # If it is possible, print YES
        print("YES")
    else:
        # If it is not possible, print NO
        print("NO")

if __name__ == '__main__':
    main()

