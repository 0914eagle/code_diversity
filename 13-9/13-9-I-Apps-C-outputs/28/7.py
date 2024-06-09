
def get_largest_square_killer(matrix):
    # Initialize variables
    largest_killer_size = 0
    current_killer_size = 0
    rows = len(matrix)
    cols = len(matrix[0])

    # Iterate over each element in the matrix
    for i in range(rows):
        for j in range(cols):
            # Check if the current element is part of a square killer
            if matrix[i][j] == "1":
                current_killer_size += 1
                # Check if the current killer size is larger than the largest killer size
                if current_killer_size > largest_killer_size:
                    largest_killer_size = current_killer_size
            else:
                current_killer_size = 0

    return largest_killer_size

