
def is_reproducible(art_piece):
    # Initialize a 2D array to store the colors of the art piece
    art_array = []
    for row in art_piece:
        art_array.append([])
        for col in row:
            art_array[-1].append(col)
    
    # Initialize a 2D array to store the colors of the reproduced art piece
    reproduced_array = [[0] * len(art_array[0]) for _ in range(len(art_array))]
    
    # Loop through the art piece and check if it is possible to reproduce it
    for i in range(len(art_array)):
        for j in range(len(art_array[0])):
            if art_array[i][j] != reproduced_array[i][j]:
                return "NO"
    
    return "YES"
