
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
                # Check if the cell can be reproduced by stamping a 3x3 square
                if can_reproduce_cell(art_array, reproduced_array, i, j):
                    # If it can be reproduced, stamp the 3x3 square with the corresponding color
                    stamp_cell(reproduced_array, i, j, art_array[i][j])
                else:
                    # If it cannot be reproduced, return "NO"
                    return "NO"

    # If all cells can be reproduced, return "YES"
    return "YES"

# Check if a cell can be reproduced by stamping a 3x3 square
def can_reproduce_cell(art_array, reproduced_array, i, j):
    # Check if the cell is not already stamped
    if reproduced_array[i][j] != 0:
        return False

    # Check if the cell is not outside the boundaries of the art piece
    if i < 0 or i >= len(art_array) or j < 0 or j >= len(art_array[0]):
        return False

    # Check if the cell is the same color as the surrounding 8 cells
    if art_array[i][j] != art_array[i-1][j] or art_array[i][j] != art_array[i+1][j] or art_array[i][j] != art_array[i][j-1] or art_array[i][j] != art_array[i][j+1]:
        return False

    # If all conditions are met, return True
    return True

# Stamp a 3x3 square with a color
def stamp_cell(reproduced_array, i, j, color):
    # Stamp the 3x3 square with the corresponding color
    for k in range(i, i+3):
        for l in range(j, j+3):
            reproduced_array[k][l] = color

