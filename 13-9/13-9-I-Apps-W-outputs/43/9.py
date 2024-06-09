
def paint_cube(k):
    # Initialize a kxkxk matrix with all units as white
    matrix = [[0] * k for _ in range(k)]

    # Iterate over each layer
    for layer in range(k):
        # Iterate over each row
        for row in range(k):
            # Iterate over each column
            for col in range(k):
                # Check if the current unit is white
                if matrix[layer][row][col] == 0:
                    # Check if the current unit has at least one white neighbor in the same layer
                    if any(matrix[layer][row][:col] + matrix[layer][row][col + 1:]):
                        # Check if the current unit has at least one black neighbor in the same layer
                        if any(matrix[layer][:row] + matrix[layer][row + 1:]):
                            # Mark the current unit as black
                            matrix[layer][row][col] = 1

    # Check if all units have been marked
    if all(map(sum, matrix)):
        # Return the matrix
        return matrix

    # If no solution is found, return -1
    return -1

