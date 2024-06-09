
def runeology(matrix):
    # Initialize a set to store the unique columns
    unique_cols = set()
    # Iterate through the matrix and add each column to the set
    for col in matrix:
        unique_cols.add(tuple(col))
    # Initialize a variable to store the maximum number of rows that can be deleted
    max_rows = 0
    # Iterate through the matrix and check if deleting a row will break the no-equal-column rule
    for row in matrix:
        # If the current row is not in the set of unique columns, it can be deleted
        if tuple(row) not in unique_cols:
            # Add the current row to the set of unique columns
            unique_cols.add(tuple(row))
            # Increment the maximum number of rows that can be deleted
            max_rows += 1
    # Return the maximum number of rows that can be deleted
    return max_rows

