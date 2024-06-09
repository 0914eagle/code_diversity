
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
    
    # Process the queries
    for query in queries:
        if query[0] == 1:
            # Query 1: Place a white stone on (1, x) and replace black stones below it
            x = query[1]
            for i in range(2, N):
                if grid[i][x] == 1:
                    grid[i][x] = 0
                else:
                    break
        elif query[0] == 2:
            # Query 2: Place a white stone on (x, 1) and replace black stones to the right of it
            x = query[1]
            for j in range(2, N):
                if grid[x][j] == 1:
                    grid[x][j] = 0
                else:
                    break
    
    # Count the number of black stones left on the grid
    count = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 1:
                count += 1
    
    return count

