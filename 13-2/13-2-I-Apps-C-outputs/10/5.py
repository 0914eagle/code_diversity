
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

                # Find the position in the reconstructed map where the current map piece can be placed
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
        piece = piece.T[::-1]
    elif rotation == 2:
        piece = piece[::-1]
    elif rotation == 3:
        piece = piece.T

    # Flip the piece as needed
    if flip:
        piece = piece[::-1]

    return piece

def find_position(reconstructed_map, piece):
    # Loop through the reconstructed map to find a matching position for the piece
    for i in range(len(reconstructed_map)):
        for j in range(len(reconstructed_map[0])):
            # If the piece matches the reconstructed map at the current position, return the position
            if reconstructed_map[i:i+len(piece), j:j+len(piece)] == piece:
                return i, j

    # If no matching position is found, return None
    return None

def update_map(reconstructed_map, piece, position):
    # Update the reconstructed map with the piece at the given position
    reconstructed_map[position[0]:position[0]+len(piece), position[1]:position[1]+len(piece)] = piece
    return reconstructed_map

