
def solve(matrix, k):
    # Initialize the result string
    result = ""

    # Loop through each row of the matrix
    for i in range(len(matrix)):
        # Loop through each column of the matrix
        for j in range(len(matrix[0])):
            # If the current cell is not part of the path, skip it
            if matrix[i][j] == "x":
                continue
            # If the current cell is the starting cell, add it to the result string
            if i == 0 and j == 0:
                result += matrix[i][j]
            # If the current cell is not the starting cell, check if it is connected to the previous cell
            else:
                # If the previous cell is not part of the path, skip it
                if matrix[i-1][j] == "x":
                    continue
                # If the previous cell is part of the path, check if the current cell is connected to it
                if matrix[i][j-1] == "x":
                    continue
                # If the current cell is connected to the previous cell, add it to the result string
                result += matrix[i][j]

    # Return the result string
    return result

