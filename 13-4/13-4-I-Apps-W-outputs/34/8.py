
def runeology(matrix):
    # Initialize a set to store the unique columns
    unique_cols = set()
    # Iterate through the rows of the matrix
    for row in matrix:
        # Convert the row to a set to remove duplicates
        row_set = set(row)
        # If the set is not already in the unique columns set, add it
        if row_set not in unique_cols:
            unique_cols.add(row_set)
        # If the set is already in the unique columns set, return the current number of rows deleted
        else:
            return len(matrix) - matrix.index(row)
    # If all rows are unique, return 0
    return 0

