
def is_reproducible(art_piece):
    # Initialize a 2D array to store the colors of the art piece
    art_array = []
    for row in art_piece:
        art_array.append([])
        for col in row:
            art_array[-1].append(col)

    # Initialize a 2D array to store the colors of the reproduced art piece
    reproduced_array = [[0] * len(art_array[0]) for _ in range(len(art_array))]

    # Loop through each cell in the art piece and check if it can be reproduced
    for i in range(len(art_array)):
        for j in range(len(art_array[0])):
            # If the cell is not white, check if it can be reproduced
            if art_array[i][j] != 'W':
                # Check if the cell can be reproduced by stamping a 3x3 square with the current color
                if can_reproduce(art_array, reproduced_array, i, j):
                    # If it can be reproduced, stamp the 3x3 square with the current color
                    stamp_square(reproduced_array, i, j, art_array[i][j])
                else:
                    # If it cannot be reproduced, return "NO"
                    return "NO"

    # If all cells can be reproduced, return "YES"
    return "YES"

# Check if a 3x3 square can be reproduced at a given position
def can_reproduce(art_array, reproduced_array, i, j):
    # Check if the square is within the boundaries of the art piece
    if i < 0 or i + 2 >= len(art_array) or j < 0 or j + 2 >= len(art_array[0]):
        return False

    # Check if the colors of the 3x3 square match the colors of the art piece
    for row in range(i, i + 3):
        for col in range(j, j + 3):
            if art_array[row][col] != reproduced_array[row][col]:
                return False

    return True

# Stamp a 3x3 square with a given color
def stamp_square(reproduced_array, i, j, color):
    for row in range(i, i + 3):
        for col in range(j, j + 3):
            reproduced_array[row][col] = color

