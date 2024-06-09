
def is_reproducible(art_piece):
    # Initialize a 2D array to store the colors of the art piece
    art_array = []
    for row in art_piece:
        art_array.append([])
        for col in row:
            art_array[-1].append(col)

    # Check if the art piece can be reproduced
    for i in range(len(art_array)):
        for j in range(len(art_array[0])):
            if art_array[i][j] != 'W' and not can_reproduce(art_array, i, j):
                return "NO"

    return "YES"

# Check if a given cell can be reproduced
def can_reproduce(art_array, i, j):
    # Check if the cell is on the boundary of the art piece
    if i < 1 or j < 1 or i > len(art_array) - 2 or j > len(art_array[0]) - 2:
        return False

    # Check if the cell has the same color as its neighbors
    if art_array[i][j] != art_array[i - 1][j] or art_array[i][j] != art_array[i + 1][j] or art_array[i][j] != art_array[i][j - 1] or art_array[i][j] != art_array[i][j + 1]:
        return False

    # Check if the cell has the same color as its diagonal neighbors
    if art_array[i][j] != art_array[i - 1][j - 1] or art_array[i][j] != art_array[i - 1][j + 1] or art_array[i][j] != art_array[i + 1][j - 1] or art_array[i][j] != art_array[i + 1][j + 1]:
        return False

    return True

