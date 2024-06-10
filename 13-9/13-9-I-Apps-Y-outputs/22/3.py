
def can_complete_wall(height, width, bricks):
    
    # Initialize the current layer and the total height of the wall
    current_layer = 0
    total_height = 0
    
    # Iterate through the bricks
    for brick in bricks:
        # If the brick fits in the current layer, add it to the layer
        if brick <= width - current_layer:
            current_layer += brick
        # If the brick does not fit in the current layer, move to the next layer
        else:
            total_height += 1
            current_layer = brick
    
    # If the total height of the wall is less than or equal to the given height, return True
    return total_height <= height

def main():
    # Read the input
    height, width, n = map(int, input().split())
    bricks = list(map(int, input().split()))
    
    # Determine whether the construction worker can complete the wall
    if can_complete_wall(height, width, bricks):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

