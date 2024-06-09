
def solve(grid):
    # Convert the grid to a set of rows and columns
    rows = set(grid)
    cols = set(map(tuple, zip(*grid)))
    
    # While there is a row or column that consists only of white squares, remove it and delete the space between the rows or columns
    while any(all(c == "." for c in row) for row in grid) or any(all(c == "." for c in col) for col in zip(*grid)):
        for row in grid:
            if all(c == "." for c in row):
                rows.remove(row)
                break
        for col in zip(*grid):
            if all(c == "." for c in col):
                cols.remove(col)
                break
        grid = [list(c) for c in zip(*grid) if c not in cols]
    
    # Return the final state of the grid
    return ["".join(row) for row in grid]

