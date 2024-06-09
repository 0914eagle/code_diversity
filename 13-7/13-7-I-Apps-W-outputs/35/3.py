
def solve(N, Q, queries):
    # Initialize the grid with N rows and N columns
    grid = [[0] * N for _ in range(N)]

    # Place the black stones in the central (N-2) x (N-2) square
    for i in range(1, N-1):
        for j in range(1, N-1):
            grid[i][j] = 1

    # Process each query
    for query in queries:
        # Get the type of query and the position of the white stone
        type, pos = query

        # If the query is to place a white stone on the bottom side, process it accordingly
        if type == 1:
            # Place the white stone on the bottom side
            grid[N-1][pos-1] = 1

            # Replace the black stones with white stones as we move down from the white stone
            for i in range(pos-1, N-1):
                if grid[N-1][i] == 1:
                    grid[N-1][i] = 0
                else:
                    break

        # If the query is to place a white stone on the right side, process it accordingly
        elif type == 2:
            # Place the white stone on the right side
            grid[pos-1][N-1] = 1

            # Replace the black stones with white stones as we move right from the white stone
            for j in range(pos-1, N-1):
                if grid[j][N-1] == 1:
                    grid[j][N-1] = 0
                else:
                    break

    # Count the number of black stones on the grid
    count = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 1:
                count += 1

    return count

