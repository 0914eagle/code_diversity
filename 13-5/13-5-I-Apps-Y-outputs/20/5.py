
def solve(grid):
    # Find the number of rows and columns in the grid
    H, W = len(grid), len(grid[0])
    
    # Initialize a matrix to store the final state of the grid
    final_grid = [[0] * W for _ in range(H)]
    
    # Iterate through each row and column
    for i in range(H):
        for j in range(W):
            # If the current square is black, set it to 1 in the final grid
            if grid[i][j] == '#':
                final_grid[i][j] = 1
    
    # Remove rows and columns that consist only of white squares
    while True:
        # Find the rows and columns that consist only of white squares
        rows, cols = [], []
        for i in range(H):
            for j in range(W):
                if final_grid[i][j] == 0:
                    rows.append(i)
                    cols.append(j)
                    break
        if not rows or not cols:
            break
        
        # Remove the rows and columns and update the final grid
        for i in rows:
            final_grid.pop(i)
        for j in cols:
            for row in final_grid:
                row.pop(j)
    
    # Return the final grid
    return final_grid

