
def reconstruct_painting(N, K, M, commands):
    # Initialize the canvas with a 2D array of ones
    canvas = [[1] * N for _ in range(N)]

    # Iterate through the commands
    for command in commands:
        # Split the command into its components
        op, x1, y1, x2, y2 = command.split()

        # Convert the coordinates to integers
        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2)

        # Check if the command is PAINT
        if op == "PAINT":
            # Get the colour from the command
            colour = int(x1)

            # Iterate through the cells in the rectangle
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    # Check if the cell is within the bounds of the canvas
                    if x >= 0 and x < N and y >= 0 and y < N:
                        # Set the cell to the chosen colour
                        canvas[x][y] = colour

        # Check if the command is SAVE
        elif op == "SAVE":
            # Save the current state of the canvas
            saved_states.append(canvas.copy())

        # Check if the command is LOAD
        elif op == "LOAD":
            # Load the saved state of the canvas
            canvas = saved_states[int(x1) - 1]

    # Return the reconstructed painting
    return canvas

