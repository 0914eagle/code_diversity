
def reconstruct_painting(commands):
    # Initialize the canvas with a 2D array of ones
    canvas = [[1] * N for _ in range(N)]
    # Iterate through the commands
    for command in commands:
        # If the command is PAINT, update the canvas with the checkerboard pattern
        if command.startswith("PAINT"):
            c, x1, y1, x2, y2 = map(int, command.split())
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    if (x + y) % 2 == 0:
                        canvas[x][y] = c
        # If the command is SAVE, save the current state of the canvas
        elif command.startswith("SAVE"):
            pass
        # If the command is LOAD, load the saved state of the canvas
        elif command.startswith("LOAD"):
            pass
    # Return the reconstructed painting
    return canvas

