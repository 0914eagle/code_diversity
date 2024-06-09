
def solve(grid):
    # Convert the grid to a list of lists
    grid = [list(row) for row in grid.split()]
    
    # Initialize the final state of the grid
    final_grid = []
    
    # While there is a row or column that consists only of white squares
    while any(all(cell == "." for cell in row) for row in grid) or any(all(cell == "." for cell in col) for col in zip(*grid)):
        # Find the row or column that consists only of white squares
        row_or_col = next((row for row in grid if all(cell == "." for cell in row)), None)
        if row_or_col is None:
            row_or_col = next((col for col in zip(*grid) if all(cell == "." for cell in col)), None)
        
        # Remove the row or column and delete the space between the rows or columns
        grid.remove(row_or_col)
        for row in grid:
            row.remove(row_or_col[0])
        
        # Add the row or column to the final state of the grid
        final_grid.append(row_or_col)
    
    # Return the final state of the grid
    return "\n".join("".join(row) for row in final_grid)

