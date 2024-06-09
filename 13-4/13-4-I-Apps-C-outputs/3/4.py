
def reconstruct_painting(N, K, M, commands):
    # Initialize the canvas with all cells set to white (1)
    canvas = [[1] * N for _ in range(N)]

    # Iterate through the commands and apply them to the canvas
    for command in commands:
        if command.startswith("PAINT"):
            # Extract the color and coordinates of the rectangle from the command
            color, x1, y1, x2, y2 = map(int, command.split()[1:])

            # Iterate over the cells in the rectangle and paint them with the chosen color
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    canvas[x][y] = color

        elif command.startswith("SAVE"):
            # Save the current state of the canvas
            saved_canvas = canvas.copy()

        elif command.startswith("LOAD"):
            # Load the saved state of the canvas
            canvas = saved_canvas.copy()

    # Return the final state of the canvas
    return canvas

