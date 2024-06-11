

def minPath(grid, k):
    
    # Initialize the distance array with infinite distance
    distance = [[float('inf') for _ in range(len(grid[0]))] for _ in range(len(grid))]

    # Initialize the previous array with -1
    previous = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]

    # Initialize the distance and previous arrays for the starting cell
    distance[0][0] = 0
    previous[0][0] = -1

    # Loop through each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # If the current cell is not the starting cell, check if the distance and previous arrays have been initialized
            if i > 0 or j > 0:
                # Check if the current cell is a valid move
                if isValidMove(i, j, grid, k, distance, previous):
                    # Update the distance and previous arrays
                    distance[i][j] = distance[i - 1][j - 1] + grid[i][j]
                    previous[i][j] = (i - 1, j - 1)

    # Find the minimum distance and the corresponding cell
    min_distance = float('inf')
    min_cell = (-1, -1)

    # Loop through each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # If the current cell is a valid move and the distance is less than the minimum distance, update the minimum distance and the corresponding cell
            if isValidMove(i, j, grid, k, distance, previous) and distance[i][j] < min_distance:
                min_distance = distance[i][j]
                min_cell = (i, j)

    # Return the path
    path = []
    current_cell = min_cell
    while current_cell != (-1, -1):
        path.append(grid[current_cell[0]][current_cell[1]])
        current_cell = previous[current_cell[0]][current_cell[1]]
    return path[::
