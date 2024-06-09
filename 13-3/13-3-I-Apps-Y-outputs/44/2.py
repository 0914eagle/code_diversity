
def solve(N1, N2, row1, row2, T):
    # Initialize the order of the ants after T seconds
    order = []

    # Loop through each second
    for second in range(T):
        # Loop through each ant in the first row
        for i in range(N1):
            # If the ant is not the first ant in the first row
            if i > 0:
                # Get the ant in front of the current ant
                front_ant = row1[i-1]

                # If the ant in front of the current ant is in the second row and is moving in the opposite direction
                if front_ant in row2 and row2.index(front_ant) < i:
                    # Swap the positions of the current ant and the ant in front of it
                    row1[i-1] = row1[i]
                    row1[i] = front_ant

        # Loop through each ant in the second row
        for i in range(N2):
            # If the ant is not the first ant in the second row
            if i > 0:
                # Get the ant in front of the current ant
                front_ant = row2[i-1]

                # If the ant in front of the current ant is in the first row and is moving in the opposite direction
                if front_ant in row1 and row1.index(front_ant) < i:
                    # Swap the positions of the current ant and the ant in front of it
                    row2[i-1] = row2[i]
                    row2[i] = front_ant

    # Add the order of the ants after T seconds to the output
    order += row1 + row2

    return "".join(order)

