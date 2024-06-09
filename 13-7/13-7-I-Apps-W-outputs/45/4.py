
def solve(matrix, k):
    # Initialize the result string
    result = ""

    # Loop through each row of the matrix
    for i in range(len(matrix)):
        # Loop through each column of the matrix
        for j in range(len(matrix[i])):
            # If the current cell is not part of the result string, add it to the result
            if matrix[i][j] not in result:
                result += matrix[i][j]

    # Return the result string
    return result

