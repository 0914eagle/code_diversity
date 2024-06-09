
def runeology(matrix):
    # Initialize a set to store the unique columns
    unique_cols = set()
    # Iterate through the matrix and add each column to the set
    for col in matrix:
        unique_cols.add(tuple(col))
    # Return the number of rows that can be deleted
    return len(matrix) - len(unique_cols)

