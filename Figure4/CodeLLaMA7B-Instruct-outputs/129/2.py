

def minPath(grid, k):
    
    # Initialize the distance array with infinite distance
    distance = [[float('inf') for _ in range(len(grid[0]))] for _ in range(len(grid))]

    # Initialize the previous array with -1
    previous = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]

    # Initialize the distance and previous for the starting cell
    distance[0][0] = 0
    previous[0][0] = -1

    # Loop through each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # If the current cell is not the starting cell, check if the distance and previous are already set
            if i > 0 and j > 0 and distance[i][j] == float('inf'):
                # If the distance and previous are not set, check if we can reach the current cell from the previous cell
                if distance[i - 1][j] != float('inf') and distance[i][j - 1] != float('inf'):
                    # If we can reach the current cell from the previous cell, set the distance and previous
                    distance[i][j] = distance[i - 1][j] + distance[i][j - 1]
                    previous[i][j] = max(previous[i - 1][j], previous[i][j - 1])

    # Loop through each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # If the current cell is not the starting cell, check if the distance and previous are already set
            if i > 0 and j > 0 and distance[i][j] == float('inf'):
                # If the distance and previous are not set, check if we can reach the current cell from the previous cell
                if distance[i - 1][j] != float('inf') and distance[i][j - 1] != float('inf'):
                    # If we can reach the current cell from the previous cell, set the distance and previous
                    distance[i][j] = distance[i - 1][j] + distance[
