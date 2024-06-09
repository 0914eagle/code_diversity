
def solve(grid):
    # Convert the grid to a set of rows and columns
    rows = set(grid)
    cols = set([c for row in grid for c in row])
    
    # While there are rows or columns that only contain white squares
    while '.' in rows or '.' in cols:
        # Remove any rows or columns that only contain white squares
        rows.discard('.')
        cols.discard('.')
        
        # Remove the spaces between the remaining rows and columns
        grid = [row for row in grid if row not in rows]
        grid = [''.join(row) for row in grid]
    
    # Return the final state of the grid
    return grid

