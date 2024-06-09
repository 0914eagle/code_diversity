
def solve(grid):
    # Convert the grid to a set of rows and columns
    rows = set(grid)
    cols = set(map(tuple, zip(*grid)))
    
    # While there is a row or column that consists only of white squares, remove it and delete the space between the rows or columns
    while any(row == "." * len(grid[0]) for row in rows) or any(col == "." * len(grid) for col in cols):
        if any(row == "." * len(grid[0]) for row in rows):
            rows.remove(next(row for row in rows if row == "." * len(grid[0])))
        if any(col == "." * len(grid) for col in cols):
            cols.remove(next(col for col in cols if col == "." * len(grid)))
    
    # Return the final state of the grid
    return ["".join(row) for row in grid]

