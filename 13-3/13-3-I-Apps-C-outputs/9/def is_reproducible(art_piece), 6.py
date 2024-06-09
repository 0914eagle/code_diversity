
def is_reproducible(art_piece):
    # Initialize a 2D array to store the colors of the art piece
    art_array = []
    for row in art_piece:
        art_array.append([])
        for col in row:
            art_array[-1].append(col)

    # Initialize a 2D array to store the colors of the reproduced art piece
    reproduced_array = [[0] * len(art_array[0]) for _ in range(len(art_array))]

    # Iterate through the art piece and reproduce it in the reproduced array
    for i in range(len(art_array)):
        for j in range(len(art_array[0])):
            if art_array[i][j] == 'R':
                reproduced_array[i][j] = 1
            elif art_array[i][j] == 'G':
                reproduced_array[i][j] = 2
            elif art_array[i][j] == 'B':
                reproduced_array[i][j] = 3
            else:
                reproduced_array[i][j] = 0

    # Check if the reproduced art piece is the same as the original art piece
    for i in range(len(art_array)):
        for j in range(len(art_array[0])):
            if art_array[i][j] != reproduced_array[i][j]:
                return "NO"

    return "YES"

