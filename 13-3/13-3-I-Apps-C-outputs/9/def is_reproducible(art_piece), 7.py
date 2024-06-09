
def is_reproducible(art_piece):
    # Initialize a 2D array to store the colors of the art piece
    art_array = []
    for row in art_piece:
        art_array.append([])
        for col in row:
            art_array[-1].append(col)

    # Initialize a 2D array to store the colors of the reproduced art piece
    reproduced_array = [[0] * len(art_array[0]) for _ in range(len(art_array))]

    # Loop through each row of the art piece
    for i in range(len(art_array)):
        # Loop through each column of the art piece
        for j in range(len(art_array[0])):
            # If the current cell is not white, skip it
            if art_array[i][j] != 'W':
                continue
            # If the current cell is white, check if it is possible to reproduce it
            if not is_white_cell_reproducible(art_array, reproduced_array, i, j):
                return "NO"

    return "YES"

def is_white_cell_reproducible(art_array, reproduced_array, i, j):
    # If the current cell is not white, return True
    if art_array[i][j] != 'W':
        return True
    # If the current cell is white and it has already been reproduced, return True
    if reproduced_array[i][j] != 0:
        return True
    # If the current cell is white and it has not been reproduced, check if it is possible to reproduce it
    if is_white_cell_reproducible(art_array, reproduced_array, i-1, j-1) and \
       is_white_cell_reproducible(art_array, reproduced_array, i-1, j) and \
       is_white_cell_reproducible(art_array, reproduced_array, i-1, j+1) and \
       is_white_cell_reproducible(art_array, reproduced_array, i, j-1) and \
       is_white_cell_reproducible(art_array, reproduced_array, i, j+1) and \
       is_white_cell_reproducible(art_array, reproduced_array, i+1, j-1) and \
       is_white_cell_reproducible(art_array, reproduced_array, i+1, j) and \
       is_white_cell_reproducible(art_array, reproduced_array, i+1, j+1):
        reproduced_array[i][j] = 1
        return True
    return False

