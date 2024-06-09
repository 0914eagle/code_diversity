
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

# Rotate a map piece by a given number of rotations and flip it if needed
def rotate_piece(piece, rotations, flip):
    # Rotate the piece the given number of times
    for _ in range(rotations):
        piece = rotate_piece_once(piece)

    # Flip the piece if needed
    if flip:
        piece = flip_piece(piece)

    return piece

# Rotate a map piece by 90 degrees clockwise
def rotate_piece_once(piece):
    return [list(row) for row in zip(*piece[::-1])]

# Flip a map piece horizontally
def flip_piece(piece):
    return [row[::-1] for row in piece]

# Find the position in the reconstructed map where a given map piece fits
def find_position(reconstructed_map, piece):
    for i in range(len(reconstructed_map)):
        for j in range(len(reconstructed_map[0])):
            # Check if the current position in the reconstructed map is empty
            if reconstructed_map[i][j] == 0:
                # Check if the map piece fits at the current position
                if fits(reconstructed_map, piece, i, j):
                    return (i, j)

    return None

# Check if a map piece fits at a given position in the reconstructed map
def fits(reconstructed_map, piece, i, j):
    for x in range(len(piece)):
        for y in range(len(piece[0])):
            # Check if the current position in the map piece is empty
            if piece[x][y] == 0:
                continue

            # Check if the current position in the reconstructed map is empty or matches the current position in the map piece
            if reconstructed_map[i+x][j+y] != piece[x][y] and reconstructed_map[i+x][j+y] != 0:
                return False

    return True

# Update the reconstructed map with a given map piece at a given position
def update_map(reconstructed_map, piece, position):
    i, j = position

    for x in range(len(piece)):
        for y in range(len(piece[0])):
            # Update the current position in the reconstructed map with the current position in the map piece
            reconstructed_map[i+x][j+y] = piece[x][y]

    return reconstructed_map

