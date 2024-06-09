
def solve(matrix, k):
    # Initialize the result string
    result = ""

    # Loop through each row of the matrix
    for i in range(len(matrix)):
        # Loop through each column of the matrix
        for j in range(len(matrix[i])):
            # If the current cell is not the last cell in the row
            if j < len(matrix[i]) - 1:
                # If the current cell and the next cell are not the same
                if matrix[i][j] != matrix[i][j + 1]:
                    # Add the smaller of the two letters to the result string
                    result += min(matrix[i][j], matrix[i][j + 1])
            # If the current cell is the last cell in the row
            else:
                # Add the current cell to the result string
                result += matrix[i][j]

    # Return the result string
    return result

