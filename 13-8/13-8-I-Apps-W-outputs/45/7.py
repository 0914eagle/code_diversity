
def solve(n, k, rows):
    # Initialize the minimum number of neighbors to infinity
    min_neighbors = float('inf')
    # Initialize the solution matrix
    solution = [[0] * n for _ in range(n)]
    # Loop through each row
    for i in range(n):
        # Loop through each column
        for j in range(n):
            # If the current cell is empty
            if rows[i][j] == '.':
                # Check if the cell has at least k empty cells around it
                neighbors = 0
                for row in range(i-1, i+2):
                    for col in range(j-1, j+2):
                        if 0 <= row < n and 0 <= col < n and rows[row][col] == '.':
                            neighbors += 1
                # If the cell has at least k empty cells around it, add it to the solution
                if neighbors >= k:
                    solution[i][j] = 1
                    # Update the minimum number of neighbors
                    min_neighbors = min(min_neighbors, neighbors)
    # Return the solution matrix and the minimum number of neighbors
    return solution, min_neighbors

