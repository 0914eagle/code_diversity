
def solve_treasure_map(map_pieces):
    # Initialize a dictionary to store the map pieces and their dimensions
    piece_dimensions = {}
    for i, piece in enumerate(map_pieces):
        piece_dimensions[i] = (len(piece[0]), len(piece))

    # Initialize a set to store the used map pieces
    used_pieces = set()

    # Initialize the reconstructed map with an empty string
    reconstructed_map = ""

    # Loop through the map pieces and add them to the reconstructed map
    for i, piece in enumerate(map_pieces):
        # Check if the piece has already been used
        if i in used_pieces:
            continue

        # Add the piece to the reconstructed map
        reconstructed_map += piece

        # Add the piece to the used set
        used_pieces.add(i)

        # Check if the reconstructed map is complete
        if len(reconstructed_map) == sum(piece_dimensions[i] for i in piece_dimensions):
            break

    # Rotate the reconstructed map if necessary
    if len(reconstructed_map) != sum(piece_dimensions[i] for i in piece_dimensions):
        reconstructed_map = rotate_map(reconstructed_map, piece_dimensions)

    # Split the reconstructed map into a list of lines
    reconstructed_map = reconstructed_map.split("\n")

    # Get the dimensions of the reconstructed map
    width = len(reconstructed_map[0])
    height = len(reconstructed_map)

    # Create a list to store the indices of the map pieces
    piece_indices = []

    # Loop through the reconstructed map and add the indices of the map pieces
    for i in range(width):
        for j in range(height):
            piece_indices.append(map_pieces.index(reconstructed_map[j][i]))

    # Return the dimensions and the indices of the map pieces
    return f"{width} {height}\n{'-' * width}\n{'\n'.join(reconstructed_map)}\n{'\n'.join(str(piece_indices[i * width:(i + 1) * width]) for i in range(height))}"

# Function to rotate a map piece
def rotate_map(map_piece, piece_dimensions):
    # Get the dimensions of the map piece
    width, height = piece_dimensions[map_pieces.index(map_piece)]

    # Initialize a new map piece with the rotated dimensions
    rotated_map_piece = [""] * height
    for i in range(width):
        for j in range(height):
            rotated_map_piece[j] += map_piece[width - i - 1][j]

    # Return the rotated map piece
    return "\n".join(rotated_map_piece)

