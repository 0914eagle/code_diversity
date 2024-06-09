
def is_balanced(grid):
    # Initialize variables to keep track of the leftmost and rightmost points
    leftmost = float('inf')
    rightmost = -float('inf')

    # Iterate through the grid and find the leftmost and rightmost points
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != '.':
                leftmost = min(leftmost, j)
                rightmost = max(rightmost, j)

    # Check if the center of gravity is within the range of the leftmost and rightmost points
    if leftmost < rightmost:
        return 'balanced'
    elif leftmost > rightmost:
        return 'right'
    else:
        return 'left'

