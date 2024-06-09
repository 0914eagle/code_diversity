
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
            if art_array[i][j] != "W":
                # Check if the cell can be reproduced by stamping a 3x3 square
                if can_reproduce_cell(i, j, art_array, reproduced_array):
                    # If it can be reproduced, stamp the 3x3 square with the corresponding color
                    stamp_cell(i, j, art_array[i][j], reproduced_array)
                else:
                    # If it cannot be reproduced, return "NO"
                    return "NO"

    # If all cells can be reproduced, return "YES"
    return "YES"

# Check if a cell can be reproduced by stamping a 3x3 square
def can_reproduce_cell(i, j, art_array, reproduced_array):
    # Check if the cell is within the boundaries of the art piece
    if i < 0 or i >= len(art_array) or j < 0 or j >= len(art_array[0]):
        return False

    # Check if the cell has already been stamped
    if reproduced_array[i][j] != 0:
        return False

    # Check if the cell can be reproduced by stamping a 3x3 square
    for row in range(i, i + 3):
        for col in range(j, j + 3):
            # If the cell is not within the boundaries of the art piece, return False
            if row < 0 or row >= len(art_array) or col < 0 or col >= len(art_array[0]):
                return False
            # If the cell has already been stamped, return False
            if reproduced_array[row][col] != 0:
                return False
            # If the cell has a different color than the current cell, return False
            if art_array[row][col] != art_array[i][j]:
                return False

    return True

# Stamp a 3x3 square with a color
def stamp_cell(i, j, color, reproduced_array):
    for row in range(i, i + 3):
        for col in range(j, j + 3):
            reproduced_array[row][col] = color

