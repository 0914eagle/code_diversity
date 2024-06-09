
def f1(n, m, p):
    # Initialize a 2D array to store the number of obstacles in each subgrid
    obstacles = [[0] * (m // 2) for _ in range(n // 2)]

    # Initialize a set to store the possible positions of the obstacles
    positions = set()

    # Loop through each subgrid and count the number of obstacles in each subgrid
    for i in range(n // 2):
        for j in range(m // 2):
            obstacles[i][j] = sum(obstacles[i][j:]) + sum(obstacles[i:][j])
            positions.add((i, j))

    # Initialize a variable to store the minimum number of obstacles
    min_obstacles = float('inf')

    # Loop through each possible position of the obstacles and calculate the number of obstacles in each subgrid
    for i, j in positions:
        obstacles[i][j] += 1
        min_obstacles = min(min_obstacles, sum(map(sum, obstacles)))
        obstacles[i][j] -= 1

    # Return the number of ways Bob can place the minimum number of obstacles modulo p
    return min_obstacles % p

