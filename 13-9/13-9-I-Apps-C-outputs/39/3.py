
def solve(n, targets):
    # Check if the number of targets is valid
    if sum(targets) > 2 * n:
        return -1
    
    # Initialize the grid with no targets
    grid = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Add targets to the grid
    for i, target in enumerate(targets):
        if target == 0:
            continue
        for j in range(target):
            # Find a valid position for the target
            while True:
                row = i + 1
                col = j + 1
                if grid[row][col] == 0:
                    break
                row += 1
            # Add the target to the grid
            grid[row][col] = 1
    
    # Check if the configuration is valid
    for i in range(1, n + 1):
        if sum(grid[i]) > 2:
            return -1
    
    # Return the configuration of targets
    result = []
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if grid[i][j] == 1:
                result.append([i, j])
    return result

