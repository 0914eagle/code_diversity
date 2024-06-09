
def solve(matrix, k):
    # Initialize the result string
    result = ""

    # Loop through each row of the matrix
    for i in range(len(matrix)):
        # Loop through each column of the matrix
        for j in range(len(matrix[i])):
            # If the cell is not blocked by a previous change
            if matrix[i][j] != "-":
                # Add the letter to the result string
                result += matrix[i][j]
                # Block the cell so that it cannot be used again
                matrix[i][j] = "-"
                # Decrement the number of available changes
                k -= 1
                # If all changes have been used, break the loop
                if k == 0:
                    break
            # If the cell is blocked by a previous change, skip it
            else:
                continue
        # If all changes have been used, break the loop
        if k == 0:
            break

    # Return the result string
    return result

