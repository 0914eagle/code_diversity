
def reconstruct_map(map_pieces):
    # Initialize an empty grid to store the reconstructed map
    grid = []

    # Iterate through the map pieces
    for piece in map_pieces:
        # Get the width and height of the current piece
        width, height = piece[0], piece[1]

        # Iterate through the squares in the current piece
        for i in range(height):
            for j in range(width):
                # Get the value of the current square
                value = piece[i + 2][j]

                # If the grid is not large enough to fit the current piece, extend it
                if len(grid) < height:
                    grid.append([])
                if len(grid[i]) < width:
                    grid[i].append(value)
                else:
                    grid[i].append(value)

    # Return the reconstructed map
    return grid

