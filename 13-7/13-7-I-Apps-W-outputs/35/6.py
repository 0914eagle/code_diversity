
def solve(N, Q, queries):
    # Initialize a 2D array to represent the grid
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
        # Query type (1 for horizontal, 2 for vertical)
        qtype = query[0]
        # Coordinate of the white stone to be placed
        x = query[1]

        # Check if the query is valid
        if not (1 <= x <= N-1):
            continue

        # Place the white stone
        if qtype == 1:
            grid[N-1][x] = 1
        else:
            grid[x][N-1] = 1

        # Replace the black stones with white stones
        if qtype == 1:
            for i in range(N-1, x-1, -1):
                if grid[N-1][i] == 1:
                    grid[N-1][i] = 0
                else:
                    break
        else:
            for i in range(N-1, x-1, -1):
                if grid[i][N-1] == 1:
                    grid[i][N-1] = 0
                else:
                    break

    # Count the number of black stones left on the grid
    count = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 1:
                count += 1

    return count

