
def purify_cells(grid):
    # Initialize the number of purification spells to be cast
    num_spells = 0
    
    # Initialize a list to store the rows and columns that have been purified
    purified_rows = []
    purified_cols = []
    
    # Loop through each row and column in the grid
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            # If the current cell is evil and has not been purified, cast a purification spell
            if grid[row][col] == "E" and (row not in purified_rows or col not in purified_cols):
                num_spells += 1
                purified_rows.append(row)
                purified_cols.append(col)
    
    # Return the minimum number of purification spells needed to purify all cells
    return num_spells

