
def reconstruct_painting(commands):
    # Initialize the canvas with a 2D array of ones
    canvas = [[1] * N for _ in range(N)]

    # Iterate through the commands and apply them to the canvas
    for command in commands:
        if command.startswith("PAINT"):
            # Extract the colour and coordinates of the rectangle from the command
            colour, x1, y1, x2, y2 = map(int, command.split()[1:])

            # Iterate over the cells in the rectangle and paint them with the chosen colour
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    canvas[x][y] = colour

        elif command.startswith("SAVE"):
            # Save the current state of the canvas
            saved_state = canvas.copy()

        elif command.startswith("LOAD"):
            # Load the saved state of the canvas
            canvas = saved_state.copy()

    # Return the final state of the canvas
    return canvas

