
def solve(n, m, map):
    # Initialize a 2D array to store the solution
    solution = [[0] * m for _ in range(n)]

    # Loop through each row of the map
    for i in range(n):
        # Loop through each column of the map
        for j in range(m):
            # If the current cell is land
            if map[i][j] == ".":
                # Check if the cell is adjacent to any other coffee shop
                adjacent_coffee_shops = 0
                for k in range(i-1, i+2):
                    for l in range(j-1, j+2):
                        if 0 <= k < n and 0 <= l < m and map[k][l] == "E":
                            adjacent_coffee_shops += 1
                # If the cell is not adjacent to any other coffee shop, place a coffee shop on it
                if adjacent_coffee_shops == 0:
                    solution[i][j] = "E"

    return solution

