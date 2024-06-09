
def solve(n, m, grid):
    # Initialize a 2D array to store the solution
    solution = [[0] * m for _ in range(n)]

    # Loop through each row of the grid
    for i in range(n):
        # Loop through each column of the grid
        for j in range(m):
            # If the current cell is land and has no adjacent coffee shops, place a coffee shop on it
            if grid[i][j] == "." and not any(solution[i-1][j], solution[i+1][j], solution[i][j-1], solution[i][j+1]):
                solution[i][j] = "E"

    # Return the solution
    return ["".join(row) for row in solution]

