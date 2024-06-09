
def solve(N, Q, queries):
    # Initialize a 2D array to represent the grid
    grid = [[0] * N for _ in range(N)]
    
    # Place the black stones in the center of the grid
    for i in range(1, N-1):
        for j in range(1, N-1):
            grid[i][j] = 1
    
    # Process each query
    for query in queries:
        # Get the type and position of the query
        type, pos = query
        
        # If the query is of type 1, place a white stone on (1, x) and propagate it to the right
        if type == 1:
            grid[0][pos-1] = 2
            for i in range(pos, N):
                if grid[0][i] == 1:
                    grid[0][i] = 2
                    break
        
        # If the query is of type 2, place a white stone on (x, 1) and propagate it down
        else:
            grid[pos-1][0] = 2
            for i in range(pos, N):
                if grid[i][0] == 1:
                    grid[i][0] = 2
                    break
    
    # Count the number of black stones left on the grid
    count = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 1:
                count += 1
    
    return count

