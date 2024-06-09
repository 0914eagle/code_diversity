
def is_balanced(grid):
    # Initialize variables to keep track of the leftmost and rightmost points
    leftmost, rightmost = float('inf'), -float('inf')

    # Iterate through the grid and find the leftmost and rightmost points
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != '.':
                leftmost = min(leftmost, j)
                rightmost = max(rightmost, j)

    # Calculate the center of gravity
    center_x = (leftmost + rightmost) / 2

    # Check if the structure is balanced or falls to the left or right
    if center_x < leftmost:
        return 'left'
    elif center_x > rightmost:
        return 'right'
    else:
        return 'balanced'

