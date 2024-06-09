
def solve(N, Q, queries):
    # Initialize a 2D array to represent the grid
    grid = [[0] * N for _ in range(N)]
    
    # Place the black stones on the central (N-2) \times (N-2) squares
    for i in range(1, N-1):
        for j in range(1, N-1):
            grid[i][j] = 1
    
    # Place the white stones on the bottom and right sides
    for i in range(N):
        grid[N-1][i] = 1
        grid[i][N-1] = 1
    
    # Process each query
    for query in queries:
        type, x = query
        if type == 1:
            # Move down from (1, x) and replace black stones with white stones
            for i in range(1, N):
                if grid[i][x] == 1:
                    grid[i][x] = 0
                else:
                    break
        elif type == 2:
            # Move right from (x, 1) and replace black stones with white stones
            for j in range(1, N):
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

