
def solve_treasure_hunt(map_pieces):
    # Initialize variables
    W, H = 0, 0
    grid = []
    pieces = []

    # Iterate over each map piece
    for i, piece in enumerate(map_pieces):
        # Get the width and height of the piece
        w, h = piece[0], piece[1]

        # Add the piece to the grid
        grid += [piece[2:]]

        # Add the piece to the list of pieces
        pieces.append([i+1, w, h])

        # Update the width and height of the grid
        W = max(W, w)
        H = max(H, h)

    # Initialize the reconstructed map
    reconstructed_map = [["-"] * W for _ in range(H)]

    # Iterate over each square in the grid
    for i in range(H):
        for j in range(W):
            # Get the value of the square
            value = grid[i][j]

            # Check if the value is not a digit
            if not value.isdigit():
                continue

            # Get the piece that contains the square
            piece = pieces[int(value) - 1]

            # Add the piece to the reconstructed map
            for x in range(piece[1]):
                for y in range(piece[2]):
                    reconstructed_map[i+y][j+x] = value

    # Return the reconstructed map
    return [W, H] + ["".join(row) for row in reconstructed_map]

