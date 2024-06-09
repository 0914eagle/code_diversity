
def count_ways(n, m, p):
    # Initialize a 2D array to store the number of obstacles in each subgrid
    obstacles = [[0] * (m // 2) for _ in range(n // 2)]

    # Initialize a variable to store the number of ways to place obstacles
    ways = 0

    # Loop through each subgrid in the grid
    for i in range(n // 2):
        for j in range(m // 2):
            # If the subgrid contains no obstacles, we can place an obstacle in this subgrid
            if obstacles[i][j] == 0:
                # Increment the number of ways to place obstacles
                ways += 1
                # Place an obstacle in this subgrid
                obstacles[i][j] = 1
                # If the subgrid is on the edge of the grid, we can place obstacles in the adjacent subgrids as well
                if i == 0 or j == 0 or i == n // 2 - 1 or j == m // 2 - 1:
                    # Loop through the adjacent subgrids
                    for k in range(i, min(i + 2, n // 2)):
                        for l in range(j, min(j + 2, m // 2)):
                            # If the subgrid contains no obstacles, we can place an obstacle in this subgrid
                            if obstacles[k][l] == 0:
                                # Increment the number of ways to place obstacles
                                ways += 1
                                # Place an obstacle in this subgrid
                                obstacles[k][l] = 1

    # Return the number of ways to place obstacles modulo p
    return ways % p

