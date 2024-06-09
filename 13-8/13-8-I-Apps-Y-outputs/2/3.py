
def solve(grid):
    # Convert the grid to a list of rows
    rows = grid.split('\n')
    # Initialize the rating variable
    rating = 0
    # Iterate over the rows
    for row in rows:
        # Check if the row is not empty
        if row.strip():
            # Increment the rating by 1 for each non-blank column
            rating += len(row.strip())
    # Return the rating
    return rating

