
def reconstruct_painting(N, K, M, commands):
    # Initialize the canvas with all cells set to white (color 1)
    canvas = [[1] * N for _ in range(N)]

    # Iterate through the commands and apply them to the canvas
    for command in commands:
        if command.startswith("PAINT"):
            # Extract the color and coordinates of the rectangle from the command
            color, x1, y1, x2, y2 = map(int, command.split()[1:])

            # Check if the coordinates are valid
            if x1 < 0 or x1 >= N or x2 < 0 or x2 >= N or y1 < 0 or y1 >= N or y2 < 0 or y2 >= N:
                continue

            # Apply the checkerboard pattern to the rectangle
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    if (x + y) % 2 == 0:
                        canvas[x][y] = color

        elif command.startswith("SAVE"):
            # Save the current state of the canvas
            saved_canvas = canvas.copy()

        elif command.startswith("LOAD"):
            # Load the saved state of the canvas
            canvas = saved_canvas.copy()

    # Return the reconstructed painting
    return canvas

