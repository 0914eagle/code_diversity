
def largest_square_killer(matrix):
    # Initialize variables
    max_size = -1
    current_size = 0
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    
    # Loop through each element in the matrix
    for row in range(num_rows):
        for col in range(num_cols):
            # If the current element is a 1, check if it forms a square killer
            if matrix[row][col] == "1":
                # Check if the current element is the top-left corner of a square killer
                if row > 0 and col > 0 and matrix[row-1][col-1] == "1":
                    # Check if the current element is the top-right corner of a square killer
                    if col < num_cols-1 and matrix[row-1][col+1] == "1":
                        # Check if the current element is the bottom-left corner of a square killer
                        if row < num_rows-1 and matrix[row+1][col-1] == "1":
                            # Check if the current element is the bottom-right corner of a square killer
                            if col < num_cols-1 and matrix[row+1][col+1] == "1":
                                # If all corners are 1s, increment the current size
                                current_size += 1
                            else:
                                # If not all corners are 1s, break out of the loops
                                break
                        else:
                            # If not all corners are 1s, break out of the loops
                            break
                    else:
                        # If not all corners are 1s, break out of the loops
                        break
                else:
                    # If not all corners are 1s, break out of the loops
                    break
    
    # Return the largest size found
    return max_size

