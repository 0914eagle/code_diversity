
def solve(matrix):
    # Initialize a set to store the unique columns
    unique_cols = set()
    # Iterate through the rows of the matrix
    for row in matrix:
        # If the current row is not in the set of unique columns, add it to the set
        if row not in unique_cols:
            unique_cols.add(row)
        # If the set of unique columns has more than one element, return the size of the set - 1 (since we don't want to delete the last row)
        if len(unique_cols) > 1:
            return len(unique_cols) - 1
    # If the set of unique columns has only one element, return 0 (since we can't delete any rows)
    return 0

