
def solve(grid):
    # Convert the grid to a list of rows
    rows = grid.split('\n')
    # Initialize the rating variable
    rating = 0
    # Iterate through the rows
    for row in rows:
        # Check if the row is blank
        if row.strip() == '':
            # Increment the rating
            rating += 1
    # Return the rating
    return rating

