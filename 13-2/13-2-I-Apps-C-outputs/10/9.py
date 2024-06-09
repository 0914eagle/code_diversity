
def solve(map_pieces):
    # Initialize the reconstructed map with the first map piece
    reconstructed_map = map_pieces[0]
    used_pieces = [0]

    # Loop through the remaining map pieces
    for i in range(1, len(map_pieces)):
        # Try rotating and flipping the current map piece to find a matching position in the reconstructed map
        for rotation in range(4):
            for flip in [False, True]:
                # Rotate and flip the current map piece as needed
                rotated_piece = rotate_piece(map_pieces[i], rotation, flip)

                # Find the position in the reconstructed map where the current map piece fits
                position = find_position(reconstructed_map, rotated_piece)

                # If a matching position is found, update the reconstructed map and used pieces
                if position is not None:
                    reconstructed_map = update_map(reconstructed_map, rotated_piece, position)
                    used_pieces.append(i)
                    break

    # Find the width and height of the reconstructed map
    width = len(reconstructed_map[0])
    height = len(reconstructed_map)

    # Return the width, height, and used pieces
    return width, height, used_pieces

def rotate_piece(piece, rotation, flip):
    # Rotate the piece as needed
    if rotation == 1:
        piece = list(map(list, zip(*piece[::-1])))
    elif rotation == 2:
        piece = list(map(list, zip(*piece)))[::-1]
    elif rotation == 3:
        piece = list(map(list, zip(*piece)))[::-1][::-1]

    # Flip the piece as needed
    if flip:
        piece = list(map(list, zip(*piece)))[::-1]

    return piece

def find_position(reconstructed_map, piece):
    # Find the position in the reconstructed map where the piece fits
    for i in range(len(reconstructed_map)):
        for j in range(len(reconstructed_map[0])):
            if reconstructed_map[i][j] == '0' and piece_fits(reconstructed_map, piece, i, j):
                return (i, j)
    return None

def piece_fits(reconstructed_map, piece, i, j):
    # Check if the piece fits in the reconstructed map at the given position
    for x in range(len(piece)):
        for y in range(len(piece[0])):
            if piece[x][y] != '0' and reconstructed_map[i+x][j+y] != '0':
                return False
    return True

def update_map(reconstructed_map, piece, position):
    # Update the reconstructed map with the piece at the given position
    i, j = position
    for x in range(len(piece)):
        for y in range(len(piece[0])):
            if piece[x][y] != '0':
                reconstructed_map[i+x][j+y] = piece[x][y]
    return reconstructed_map

