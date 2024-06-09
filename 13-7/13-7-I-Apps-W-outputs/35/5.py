
def solve(N, Q, queries):
    # Initialize the grid with N rows and N columns
    grid = [[0] * N for _ in range(N)]

    # Place the black stones on the central (N-2) \times (N-2) squares
    for i in range(1, N-1):
        for j in range(1, N-1):
            grid[i][j] = 1

    # Process each query
    for query in queries:
        # Get the type of query and the coordinate x
        type, x = query

        # If the query is of type 1, place a white stone on (1, x) and replace the black stones between (1, x) and the first white stone you hit if you go down from (1, x)
        if type == 1:
            for i in range(1, x+1):
                if grid[1][i] == 1:
                    grid[1][i] = 0
                if grid[1][i] == 0:
                    break

        # If the query is of type 2, place a white stone on (x, 1) and replace the black stones between (x, 1) and the first white stone you hit if you go right from (x, 1)
        if type == 2:
            for j in range(1, x+1):
                if grid[j][1] == 1:
                    grid[j][1] = 0
                if grid[j][1] == 0:
                    break

    # Count the number of black stones on the grid
    count = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 1:
                count += 1

    return count

