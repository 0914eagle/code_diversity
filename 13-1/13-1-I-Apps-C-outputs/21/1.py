
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
            # If the current cell is not the destination cell, check the neighbors
            if (i, j) != (n, n):
                # Check the neighbor to the right
                if j < n and distances[i][j+1] > distances[i][j] + 1:
                    distances[i][j+1] = distances[i][j] + 1
                # Check the neighbor below
                if i < n and distances[i+1][j] > distances[i][j] + 1:
                    distances[i+1][j] = distances[i][j] + 1
    
    # Return the minimum distance from the starting cell to the destination cell
    return distances[n][n]

