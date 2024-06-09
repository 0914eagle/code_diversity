
def largest_square_killer(matrix):
    # Initialize a list to store the sizes of the square killers
    killer_sizes = []
    
    # Loop through each row of the matrix
    for i in range(len(matrix)):
        # Loop through each column of the matrix
        for j in range(len(matrix[0])):
            # Check if the current element is part of a square killer
            if matrix[i][j] == "1":
                # Find the size of the square killer by checking the surrounding elements
                size = 1
                while i + size < len(matrix) and j + size < len(matrix[0]) and matrix[i + size][j + size] == "1":
                    size += 1
                # Add the size of the square killer to the list
                killer_sizes.append(size)
    
    # Return the largest square killer size or -1 if there are no square killers
    return max(killer_sizes) if killer_sizes else -1

