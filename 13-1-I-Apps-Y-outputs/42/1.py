
def solve(n, m, map):
    # Initialize a 2D array to store the solution
    solution = [[0] * m for _ in range(n)]

    # Loop through each row of the map
    for i in range(n):
        # Loop through each column of the map
        for j in range(m):
            # If the current cell is land
            if map[i][j] == ".":
                # Check if the cell is directly adjacent to a coffee shop
                if any(solution[i-1][j] == "E" for i in range(max(0, i-1), i+2) for j in range(max(0, j-1), j+2) if i != i or j != j):
                    # If it is, place a coffee shop on it
                    solution[i][j] = "E"

    # Return the solution
    return solution

