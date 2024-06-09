
def solve(n, m, map):
    # Initialize a 2D array to store the solution
    solution = [[0] * m for _ in range(n)]

    # Loop through each row of the map
    for i in range(n):
        # Loop through each column of the map
        for j in range(m):
            # If the current cell is land and has no coffee shop adjacent to it, place a coffee shop on it
            if map[i][j] == "." and (i > 0 and solution[i - 1][j] == 1 or j > 0 and solution[i][j - 1] == 1 or i < n - 1 and solution[i + 1][j] == 1 or j < m - 1 and solution[i][j + 1] == 1):
                solution[i][j] = 1

    # Return the solution
    return solution

