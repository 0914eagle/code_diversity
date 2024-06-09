
def solve(N, Q, queries):
    # Initialize the grid with N rows and N columns
    grid = [[0] * N for _ in range(N)]

    # Place the black stones on the central (N-2) x (N-2) squares
    for i in range(1, N-1):
        for j in range(1, N-1):
            grid[i][j] = 1

    # Process each query
    for query in queries:
        # Get the type of query and the coordinate x
        type, x = query

        # If the query is of type 1, place a white stone on (1, x) and move down until we hit a white stone or the edge of the grid
        if type == 1:
            grid[1][x] = 2
            for i in range(2, N):
                if grid[i][x] == 1:
                    grid[i][x] = 2
                elif grid[i][x] == 0:
                    break

        # If the query is of type 2, place a white stone on (x, 1) and move right until we hit a white stone or the edge of the grid
        else:
            grid[x][1] = 2
            for j in range(2, N):
                if grid[x][j] == 1:
                    grid[x][j] = 2
                elif grid[x][j] == 0:
                    break

    # Count the number of black stones remaining on the grid
    count = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 1:
                count += 1

    return count

