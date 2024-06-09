
def reconstruct_painting(N, K, M, commands):
    # Initialize the canvas with a 2D array of zeros
    canvas = [[0] * N for _ in range(N)]

    # Iterate through the commands
    for command in commands:
        # If the command is PAINT, update the canvas with the checkerboard pattern
        if command.startswith("PAINT"):
            color, x1, y1, x2, y2 = map(int, command.split())
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    if (x + y) % 2 == 0:
                        canvas[x][y] = color

        # If the command is SAVE, save the current state of the canvas
        elif command == "SAVE":
            saved_canvas = canvas.copy()

        # If the command is LOAD, load the saved state of the canvas
        elif command.startswith("LOAD"):
            x = int(command.split()[1])
            canvas = saved_canvas[x]

    # Return the final state of the canvas
    return canvas

