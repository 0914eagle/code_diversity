
def solve(matrix):
    # Initialize a set to store the unique columns
    unique_cols = set()
    # Initialize a variable to store the maximum number of rows that can be deleted
    max_rows = 0
    # Iterate over the rows of the matrix
    for i in range(len(matrix)):
        # Check if the current row is already in the set of unique columns
        if matrix[i] in unique_cols:
            # If it is, break the loop and return the maximum number of rows that can be deleted
            return max_rows
        # Add the current row to the set of unique columns
        unique_cols.add(matrix[i])
        # Increment the maximum number of rows that can be deleted
        max_rows += 1
    # If all rows are unique, return the maximum number of rows that can be deleted
    return max_rows

