
def solve(R, C, matrix):
    # Initialize a set to store the unique columns
    unique_cols = set()
    # Iterate through the rows of the matrix
    for i in range(R):
        # Get the current row
        row = matrix[i]
        # Check if the current row is already in the set of unique columns
        if row in unique_cols:
            # If it is, return the current number of rows that can be deleted
            return i
        # Add the current row to the set of unique columns
        unique_cols.add(row)
    # If all rows are unique, return 0
    return 0

