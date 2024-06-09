
def solve(N, Q, queries):
    # Initialize a 2D array to store the grid
    grid = [[0] * N for _ in range(N)]

    # Place the black stones in the central (N-2) x (N-2) square
    for i in range(1, N-1):
        for j in range(1, N-1):
            grid[i][j] = 1

    # Place the white stones on the bottom and right sides
    for i in range(N):
        grid[N-1][i] = 1
        grid[i][N-1] = 1

    # Process each query
    for query in queries:
        if query[0] == 1:
            # Query 1: Place a white stone on (1, x) and replace black stones below it
            x = query[1]
            for i in range(1, x+1):
                if grid[i+1][x] == 1:
                    grid[i+1][x] = 0
        else:
            # Query 2: Place a white stone on (x, 1) and replace black stones to the right of it
            x = query[1]
            for i in range(1, x+1):
                if grid[x][i+1] == 1:
                    grid[x][i+1] = 0

    # Count the number of black stones left on the grid
    count = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 1:
                count += 1

    return count

