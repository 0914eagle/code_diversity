
def find_min_time(n, m, volcanoes):
    # Initialize a matrix to store the distances from the starting cell
    distances = [[float("inf") for _ in range(n+1)] for _ in range(n+1)]
    distances[1][1] = 0
    
    # Loop through each cell in the matrix
    for i in range(1, n+1):
        for j in range(1, n+1):
            # If the current cell is a volcano, skip it
            if (i, j) in volcanoes:
                continue
            # If the current cell is not the destination cell, check if we can reach it from the starting cell
            if (i, j) != (n, n):
                # Check if we can reach the current cell from the left and bottom cells
                if i > 1 and distances[i-1][j] != float("inf"):
                    distances[i][j] = min(distances[i][j], distances[i-1][j] + 1)
                if j > 1 and distances[i][j-1] != float("inf"):
                    distances[i][j] = min(distances[i][j], distances[i][j-1] + 1)
    
    # Return the minimum time it takes to reach the destination cell
    return distances[n][n]

