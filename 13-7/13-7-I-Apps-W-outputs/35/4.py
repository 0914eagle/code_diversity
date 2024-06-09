
def solve(N, Q, queries):
    # Initialize a 2D array to represent the grid
    grid = [[0] * N for _ in range(N)]

    # Place the black stones on the central (N-2) x (N-2) squares
    for i in range(1, N-1):
        for j in range(1, N-1):
            grid[i][j] = 1

    # Place the white stones on the bottom and right sides
    for i in range(N):
        grid[N-1][i] = 1
        grid[i][N-1] = 1

    # Process each query
    for query in queries:
        # Query type 1: Place a white stone on (1, x) and flip all black stones between (1, x) and the first white stone you hit if you go down
        if query[0] == 1:
            x = query[1]
            for i in range(1, x+1):
                if grid[1][i] == 1:
                    break
                grid[1][i] = 1

        # Query type 2: Place a white stone on (x, 1) and flip all black stones between (x, 1) and the first white stone you hit if you go right
        elif query[0] == 2:
            x = query[1]
            for i in range(1, x+1):
                if grid[i][1] == 1:
                    break
                grid[i][1] = 1

    # Count the number of black stones remaining on the grid
    count = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 1:
                count += 1

    return count

