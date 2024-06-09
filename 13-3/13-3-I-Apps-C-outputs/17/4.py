
def f1(n, m, p):
    # Initialize a 2D array to store the number of obstacles in each subgrid
    obstacles = [[0] * (m // 2) for _ in range(n // 2)]

    # Initialize a set to store the positions of the obstacles
    positions = set()

    # Loop through each subgrid and count the number of obstacles in it
    for i in range(n // 2):
        for j in range(m // 2):
            # If the subgrid has no obstacles, add it to the set of positions
            if obstacles[i][j] == 0:
                positions.add((i, j))

    # Initialize a variable to store the number of ways to place obstacles
    ways = 0

    # Loop through each position and count the number of ways to place obstacles in it
    for i, j in positions:
        # If the position is on the edge of the grid, only one way to place obstacles
        if i == 0 or j == 0 or i == n // 2 - 1 or j == m // 2 - 1:
            ways += 1
        # If the position is not on the edge of the grid, count the number of ways to place obstacles
        else:
            ways += 4

    # Return the number of ways to place obstacles modulo p
    return ways % p

