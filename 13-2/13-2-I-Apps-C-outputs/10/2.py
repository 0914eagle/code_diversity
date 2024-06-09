
def solve(map_pieces):
    # Initialize the reconstructed map with the first map piece
    reconstructed_map = map_pieces[0]
    used_map_pieces = [0]

    # Loop through the remaining map pieces
    for i in range(1, len(map_pieces)):
        # Try rotating the map piece and see if it fits
        for rotation in range(4):
            rotated_map_piece = rotate_map_piece(map_pieces[i], rotation)
            if fits_in_map(reconstructed_map, rotated_map_piece):
                # If it fits, add it to the reconstructed map and mark it as used
                reconstructed_map = add_map_piece_to_map(reconstructed_map, rotated_map_piece)
                used_map_pieces.append(i + 1)
                break

    # Return the reconstructed map and the used map pieces
    return reconstructed_map, used_map_pieces

def rotate_map_piece(map_piece, rotation):
    # Rotate the map piece by 90 degrees clockwise
    return list(map(list, zip(*map_piece[::-1])))[::rotation]

def fits_in_map(reconstructed_map, map_piece):
    # Check if the map piece fits in the reconstructed map
    for i in range(len(map_piece)):
        for j in range(len(map_piece[0])):
            if map_piece[i][j] != 0 and reconstructed_map[i + 1][j + 1] != 0:
                return False
    return True

def add_map_piece_to_map(reconstructed_map, map_piece):
    # Add the map piece to the reconstructed map
    for i in range(len(map_piece)):
        for j in range(len(map_piece[0])):
            if map_piece[i][j] != 0:
                reconstructed_map[i + 1][j + 1] = map_piece[i][j]
    return reconstructed_map

