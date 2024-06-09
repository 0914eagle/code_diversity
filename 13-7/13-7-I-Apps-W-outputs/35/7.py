
def solve(N, Q, queries):
    # Initialize a 2D array to represent the grid
    grid = [[0] * N for _ in range(N)]

    # Place the black stones in the center of the grid
    for i in range(N - 2):
        for j in range(N - 2):
            grid[i + 1][j + 1] = 1

    # Place the white stones on the bottom and right sides of the grid
    for i in range(N):
        grid[N - 1][i] = 1
        grid[i][N - 1] = 1

    # Process each query
    for query in queries:
        type, x = query
        if type == 1:
            # Place a white stone on (1, x) and replace black stones with white stones as we go down
            grid[1][x] = 1
            for i in range(2, N):
                if grid[i][x] == 1:
                    grid[i][x] = 0
                else:
                    break
        else:
            # Place a white stone on (x, 1) and replace black stones with white stones as we go right
            grid[x][1] = 1
            for i in range(2, N):
                if grid[x][i] == 1:
                    grid[x][i] = 0
                else:
                    break

    # Count the number of black stones left on the grid
    count = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 1:
                count += 1

    return count

