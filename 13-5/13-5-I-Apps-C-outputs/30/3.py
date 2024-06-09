
def reconstruct_painting(N, K, M, commands):
    # Initialize the canvas with white cells
    canvas = [[1] * N for _ in range(N)]

    # Iterate through the commands
    for command in commands:
        # Extract the command type and parameters
        command_type, *params = command.split()
        params = [int(x) for x in params]

        # Handle the PAINT command
        if command_type == "PAINT":
            # Extract the colour and coordinates of the rectangle
            colour, x1, y1, x2, y2 = params

            # Paint the rectangle with the chosen colour
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    canvas[x][y] = colour

        # Handle the SAVE command
        elif command_type == "SAVE":
            # Save the current state of the canvas
            saved_canvas = canvas.copy()

        # Handle the LOAD command
        elif command_type == "LOAD":
            # Load the saved state of the canvas
            canvas = saved_canvas.copy()

    # Return the reconstructed painting
    return canvas

