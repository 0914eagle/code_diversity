
def reconstruct_painting(N, K, commands):
    # Initialize the painting with a white canvas
    painting = [[1] * N for _ in range(N)]

    # Iterate through the commands and apply them to the painting
    for command in commands:
        if command.startswith("PAINT"):
            # Extract the colour and coordinates of the rectangle from the command
            colour, x1, y1, x2, y2 = map(int, command.split()[1:])

            # Iterate over the cells in the rectangle and paint them with the chosen colour
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    painting[x][y] = colour

        elif command.startswith("SAVE"):
            # Save the current painting to a list of lists
            saved_paintings.append(painting)

        elif command.startswith("LOAD"):
            # Load the saved painting with the given ordinal number
            painting = saved_paintings[int(command.split()[1]) - 1]

    # Return the reconstructed painting
    return painting

