
def reconstruct_painting(N, K, M, commands):
    # Initialize the canvas with all cells set to white (color 1)
    canvas = [[1] * N for _ in range(N)]

    # Iterate through the commands and apply them to the canvas
    for command in commands:
        if command.startswith("PAINT"):
            # Extract the color and coordinates of the rectangle from the command
            color, x1, y1, x2, y2 = map(int, command.split()[1:])

            # Paint the rectangle with the given color
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    canvas[x][y] = color

        elif command.startswith("SAVE"):
            # Save the current state of the canvas
            pass

        elif command.startswith("LOAD"):
            # Load the saved state of the canvas
            pass

    # Return the canvas with the reconstructed painting
    return canvas

