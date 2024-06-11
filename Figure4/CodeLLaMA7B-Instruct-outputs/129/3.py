

def minPath(grid, k):
    
    # Initialize the distance array with infinite distance
    distance = [[float('inf') for _ in range(len(grid[0]))] for _ in range(len(grid))]
    # Initialize the previous array with -1
    previous = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]

    # Set the distance for the starting cell to 0
    distance[0][0] = 0
    previous[0][0] = -1

    # Loop through each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # If the current cell is not the starting cell
            if i > 0 or j > 0:
                # Get the distances from the previous cell
                left_distance = distance[i][j - 1] if j > 0 else float('inf')
                right_distance = distance[i][j + 1] if j < len(grid[0]) - 1 else float('inf')
                top_distance = distance[i - 1][j] if i > 0 else float('inf')
                bottom_distance = distance[i + 1][j] if i < len(grid) - 1 else float('inf')

                # Update the distance and previous array for the current cell
                distance[i][j] = min(left_distance, right_distance, top_distance, bottom_distance) + 1
                previous[i][j] = i - 1 if left_distance == distance[i][j] else (i + 1 if right_distance == distance[i][j] else (j - 1 if top_distance == distance[i][j] else j + 1))

    # Get the path
    path = []
    cell = (len(grid) - 1, len(grid[0]) - 1)
    while cell != (-1, -1):
        path.append(grid[cell[0]][cell[1]])
        cell = (previous[cell[0]][cell[1]], cell[1])

    # Reverse the path
    path.reverse()

    # Return the path
    return path
