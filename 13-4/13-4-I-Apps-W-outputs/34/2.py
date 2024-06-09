
def solve(matrix):
    # Initialize a set to store the unique columns
    unique_cols = set()
    # Initialize a variable to store the maximum number of rows that can be deleted
    max_rows = 0
    # Iterate over the rows of the matrix
    for row in matrix:
        # Check if the current row is already in the set of unique columns
        if row not in unique_cols:
            # If not, add it to the set and increment the maximum number of rows that can be deleted
            unique_cols.add(row)
            max_rows += 1
        else:
            # If the current row is already in the set, break the loop
            break
    return max_rows

