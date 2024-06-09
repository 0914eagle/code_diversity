
def solve(grid):
    # Convert the grid to a list of lists
    grid = [list(row) for row in grid.split()]
    
    # Find the number of rows and columns
    H, W = len(grid), len(grid[0])
    
    # Initialize the final state of the grid
    final_grid = [[' ' for _ in range(W)] for _ in range(H)]
    
    # Iterate until there are no more rows or columns to remove
    while True:
        # Find the indices of the rows and columns that consist only of white squares
        row_indices, col_indices = [], []
        for i in range(H):
            for j in range(W):
                if grid[i][j] == '.':
                    row_indices.append(i)
                    col_indices.append(j)
        
        # If there are no more rows or columns to remove, break the loop
        if not row_indices or not col_indices:
            break
        
        # Remove the rows and columns and update the final state of the grid
        for i in row_indices:
            for j in range(W):
                final_grid[i][j] = grid[i][j]
        for j in col_indices:
            for i in range(H):
                final_grid[i][j] = grid[i][j]
        
        # Update the grid and remove the removed rows and columns
        grid = [row for i, row in enumerate(grid) if i not in row_indices]
        grid = [[' ' if j not in col_indices else row[j] for j in range(W)] for row in grid]
    
    # Return the final state of the grid
    return [''.join(row) for row in final_grid]

