

def minPath(grid, k):
    
    # Initialize the distance matrix with infinite distance
    distance = [[float('inf') for _ in range(len(grid[0]))] for _ in range(len(grid))]
    # Initialize the previous matrix with -1
    previous = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]

    # Set the distance for the starting cell to 0
    distance[0][0] = 0
    previous[0][0] = -1

    # Loop through each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # If the cell is not the starting cell, check if the distance is less than the current distance
            if i > 0 and j > 0 and distance[i-1][j] + grid[i][j] < distance[i][j]:
                distance[i][j] = distance[i-1][j] + grid[i][j]
                previous[i][j] = i-1
            # If the cell is not the starting cell, check if the distance is less than the current distance
            if j > 0 and distance[i][j-1] + grid[i][j] < distance[i][j]:
                distance[i][j] = distance[i][j-1] + grid[i][j]
                previous[i][j] = j-1

    # Find the minimum distance
    min_distance = float('inf')
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if distance[i][j] < min_distance:
                min_distance = distance[i][j]

    # If the minimum distance is greater than k, return -1
    if min_distance > k:
        return -1

    # Initialize the path with the starting cell
    path = [grid[0][0]]

    # Loop through each cell in the previous matrix
    i = len(grid) - 1
    j = len(grid[0]) - 1
    while i != -1 and j != -1:
        # If the current cell is not the starting cell
