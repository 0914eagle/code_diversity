
def can_reproduce_art(art):
    # Initialize a 2D array to store the colors of the art piece
    art_array = []
    for row in art:
        art_array.append([])
        for col in row:
            art_array[-1].append(col)

    # Initialize a 2D array to store the colors of the reproduced art piece
    reproduced_array = [[None for _ in range(len(art_array[0]))] for _ in range(len(art_array))]

    # Iterate through the art piece and check if it is possible to reproduce it
    for i in range(len(art_array)):
        for j in range(len(art_array[0])):
            # If the current cell is not white, check if it is possible to reproduce it
            if art_array[i][j] != "W":
                # Check if the current cell is a corner cell
                if i == 0 or j == 0 or i == len(art_array) - 1 or j == len(art_array[0]) - 1:
                    # If the current cell is a corner cell, it is not possible to reproduce it
                    return "NO"
                # Check if the current cell has the same color as its adjacent cells
                if (art_array[i - 1][j] == art_array[i][j] and
                        art_array[i + 1][j] == art_array[i][j] and
                        art_array[i][j - 1] == art_array[i][j] and
                        art_array[i][j + 1] == art_array[i][j]):
                    # If the current cell has the same color as its adjacent cells, it is possible to reproduce it
                    reproduced_array[i][j] = art_array[i][j]
                else:
                    # If the current cell does not have the same color as its adjacent cells, it is not possible to reproduce it
                    return "NO"
            # If the current cell is white, it is possible to reproduce it
            else:
                reproduced_array[i][j] = "W"

    # If all cells of the reproduced art piece have been colored, it is possible to reproduce the art piece
    if all(all(cell is not None for cell in row) for row in reproduced_array):
        return "YES"
    else:
        return "NO"

