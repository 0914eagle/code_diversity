
def solve(n, a):
    # Check if the number of targets is valid
    if sum(a) > 2 * n:
        return -1
    
    # Initialize the grid with zeros
    grid = [[0] * n for _ in range(n)]
    
    # Fill the grid with targets based on the hits
    for i, hits in enumerate(a):
        for j in range(hits):
            # Find the first empty cell in the current column
            for row in range(n):
                if grid[row][i] == 0:
                    break
            # Place the target in the empty cell
            grid[row][i] = 1
    
    # Check if the grid is valid
    for row in grid:
        if sum(row) > 2:
            return -1
    
    # Return the grid as the solution
    return grid

