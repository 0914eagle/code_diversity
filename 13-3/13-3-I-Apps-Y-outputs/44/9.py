
def solve(ants1, ants2, T):
    # Initialize the order of the ants after T seconds as an empty string
    order = ""

    # Loop through each second of the simulation
    for second in range(T):
        # Loop through each ant in the first row
        for ant in ants1:
            # If the ant is not the first ant in the first row
            if ant != ants1[0]:
                # Find the position of the ant in the second row
                pos = ants2.index(ant)
                # If the ant in the second row is moving in the opposite direction
                if pos < len(ants2) - 1 and ants2[pos + 1] == ant:
                    # Swap the positions of the two ants
                    ants2[pos], ants2[pos + 1] = ants2[pos + 1], ants2[pos]

        # Add the order of the ants in the second row to the order of the ants after T seconds
        order += "".join(ants2)

    return order
