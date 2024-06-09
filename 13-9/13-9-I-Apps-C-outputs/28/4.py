
def find_largest_square_killer(matrix):
    # Initialize variables
    largest_killer = 0
    killer_sizes = []

    # Loop through each row of the matrix
    for i in range(len(matrix)):
        # Loop through each column of the matrix
        for j in range(len(matrix[i])):
            # If the current element is a 1, check if it is part of a square killer
            if matrix[i][j] == "1":
                # Check if the current element is part of a square killer by checking the elements above, below, and to the left and right
                if (i > 0 and matrix[i - 1][j] == "1") and (j > 0 and matrix[i][j - 1] == "1"):
                    # If the current element is part of a square killer, find the size of the killer by checking the elements around it
                    killer_size = 1
                    for k in range(i - 1, -1, -1):
                        if matrix[k][j] == "1":
                            killer_size += 1
                        else:
                            break
                    for l in range(j - 1, -1, -1):
                        if matrix[i][l] == "1":
                            killer_size += 1
                        else:
                            break
                    for m in range(i + 1, len(matrix)):
                        if matrix[m][j] == "1":
                            killer_size += 1
                        else:
                            break
                    for n in range(j + 1, len(matrix[i])):
                        if matrix[i][n] == "1":
                            killer_size += 1
                        else:
                            break
                    # Add the size of the killer to the list of killer sizes
                    killer_sizes.append(killer_size)

    # Return the largest killer size
    if len(killer_sizes) > 0:
        return max(killer_sizes)
    else:
        return -1

