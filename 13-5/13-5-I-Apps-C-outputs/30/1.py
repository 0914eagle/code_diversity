
def reconstruct_painting(N, K, M, commands):
    # Initialize the painting with a white canvas
    painting = [[1] * N for _ in range(N)]

    # Iterate through the commands
    for command in commands:
        # If the command is PAINT, paint the rectangle
        if command.startswith("PAINT"):
            # Parse the command
            color, x1, y1, x2, y2 = map(int, command.split())

            # Paint the rectangle
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    painting[x][y] = color

        # If the command is SAVE, save the painting
        elif command.startswith("SAVE"):
            # Save the painting
            saved_painting = painting.copy()

        # If the command is LOAD, load the saved painting
        elif command.startswith("LOAD"):
            # Parse the command
            save_id = int(command.split()[1])

            # Load the saved painting
            painting = saved_painting[save_id]

    # Return the painting
    return painting

