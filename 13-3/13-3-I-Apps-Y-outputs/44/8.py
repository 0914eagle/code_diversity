
def solve(ants1, ants2, T):
    # Initialize the order of the ants after T seconds as an empty string
    order = ""

    # Loop through each second of the simulation
    for second in range(T):
        # Loop through each ant in the first row
        for i in range(len(ants1)):
            # If the ant is not the first ant in the row
            if i > 0:
                # Get the index of the ant in front of the current ant
                front_index = i - 1

                # If the ant in front of the current ant is in the second row
                if ants1[front_index] in ants2:
                    # Swap the positions of the two ants
                    ants1[i], ants1[front_index] = ants1[front_index], ants1[i]

        # Loop through each ant in the second row
        for i in range(len(ants2)):
            # If the ant is not the first ant in the row
            if i > 0:
                # Get the index of the ant in front of the current ant
                front_index = i - 1

                # If the ant in front of the current ant is in the first row
                if ants2[front_index] in ants1:
                    # Swap the positions of the two ants
                    ants2[i], ants2[front_index] = ants2[front_index], ants2[i]

    # Concatenate the orders of the ants in the two rows
    order = "".join(ants1 + ants2)

    return order

