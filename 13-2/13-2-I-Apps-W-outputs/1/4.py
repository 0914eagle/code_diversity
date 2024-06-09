
def is_good_matrix(matrix):
    # Check if the matrix is empty
    if not matrix:
        return True

    # Get the dimensions of the matrix
    num_rows, num_cols = len(matrix), len(matrix[0])

    # Iterate over each sub-matrix of even length
    for row1 in range(num_rows):
        for col1 in range(num_cols):
            for row2 in range(row1, num_rows):
                for col2 in range(col1, num_cols):
                    # Check if the sub-matrix is of even length
                    if (row2 - row1) % 2 == 0 or (col2 - col1) % 2 == 0:
                        continue

                    # Count the number of ones in the sub-matrix
                    count = 0
                    for i in range(row1, row2 + 1):
                        for j in range(col1, col2 + 1):
                            if matrix[i][j] == 1:
                                count += 1

                    # Check if the number of ones is odd
                    if count % 2 == 1:
                        return False

    # If all sub-matrices are good, return True
    return True

