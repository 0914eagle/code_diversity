
def solve(grid):
    # Convert the grid to a list of lists
    grid = [list(row) for row in grid.split('\n')]
    
    # Remove all the rows and columns that are all white
    while True:
        rows_to_remove = []
        cols_to_remove = []
        for i in range(len(grid)):
            if all(cell == '.' for cell in grid[i]):
                rows_to_remove.append(i)
        for j in range(len(grid[0])):
            if all(row[j] == '.' for row in grid):
                cols_to_remove.append(j)
        if not rows_to_remove and not cols_to_remove:
            break
        for i in rows_to_remove:
            grid.pop(i)
        for j in cols_to_remove:
            for row in grid:
                row.pop(j)
    
    # Return the final state of the grid
    return '\n'.join(''.join(row) for row in grid)

