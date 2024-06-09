
def reconstruct_painting(commands):
    # Initialize the canvas with a 2D array of ones
    canvas = [[1] * N for _ in range(N)]
    # Initialize the current color to 1
    current_color = 1
    # Iterate through the commands
    for command in commands:
        # If the command is PAINT, update the canvas with the checkerboard pattern
        if command.startswith("PAINT"):
            # Extract the color and coordinates of the rectangle
            color, x1, y1, x2, y2 = map(int, command.split()[1:])
            # Update the canvas with the checkerboard pattern
            for i in range(x1, x2 + 1):
                for j in range(y1, y2 + 1):
                    if (i + j) % 2 == 0:
                        canvas[i][j] = color
        # If the command is SAVE, save the current state of the canvas
        elif command.startswith("SAVE"):
            # Save the current state of the canvas
            saved_state = canvas.copy()
        # If the command is LOAD, load the saved state of the canvas
        elif command.startswith("LOAD"):
            # Extract the ordinal number of the save
            save_number = int(command.split()[1])
            # Load the saved state of the canvas
            canvas = saved_state[save_number - 1]
        # If the command is UNDO, undo the last change to the canvas
        elif command.startswith("UNDO"):
            # Undo the last change to the canvas
            canvas = canvas[:-1]
    # Return the reconstructed painting
    return canvas

