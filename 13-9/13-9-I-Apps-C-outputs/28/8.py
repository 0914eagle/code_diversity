
def get_largest_square_killer(matrix):
    # Initialize variables
    largest_killer_size = 0
    killer_size = 0
    current_row = 0
    current_col = 0
    max_row = len(matrix)
    max_col = len(matrix[0])

    # Loop through the matrix
    while current_row < max_row and current_col < max_col:
        # Check if the current position is a potential start of a square killer
        if matrix[current_row][current_col] == "1":
            # Check if the current position is the start of a square killer
            if is_square_killer_start(matrix, current_row, current_col):
                # Find the size of the square killer
                killer_size = find_square_killer_size(matrix, current_row, current_col)
                # Update the largest killer size
                largest_killer_size = max(largest_killer_size, killer_size)

        # Increment the current position
        current_col += 1
        if current_col == max_col:
            current_col = 0
            current_row += 1

    # Return the largest killer size
    return largest_killer_size

def is_square_killer_start(matrix, row, col):
    # Check if the current position is the start of a square killer
    if matrix[row][col] == "1" and matrix[row][col + 1] == "1" and matrix[row + 1][col] == "1" and matrix[row + 1][col + 1] == "1":
        return True
    else:
        return False

def find_square_killer_size(matrix, row, col):
    # Initialize variables
    killer_size = 0
    max_row = len(matrix)
    max_col = len(matrix[0])

    # Loop through the matrix
    while row < max_row and col < max_col:
        # Check if the current position is part of the square killer
        if matrix[row][col] == "1":
            # Increment the killer size
            killer_size += 1

        # Increment the current position
        col += 1
        if col == max_col:
            col = 0
            row += 1

    # Return the killer size
    return killer_size

# Test the function
matrix = [
    [1, 0, 1, 0, 1],
    [1, 1, 0, 0, 1],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1]
]
print(get_largest_square_killer(matrix))

# Test the function with no square killers
matrix = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]
print(get_largest_square_killer(matrix))

