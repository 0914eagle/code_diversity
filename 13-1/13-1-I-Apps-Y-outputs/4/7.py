
def solve(ants1, ants2, T):
    # Initialize the order of the ants after T seconds as an empty string
    order = ""

    # Loop through each second
    for second in range(T):
        # Loop through each ant in the first row
        for ant in ants1:
            # If the ant is not the first ant in the first row
            if ant != ants1[0]:
                # Find the ant in the second row that is behind the current ant in the first row
                behind_ant = ants2[ants1.index(ant) - 1]

                # If the behind ant is moving in the opposite direction
                if behind_ant != ants2[0] and behind_ant != ants2[-1]:
                    # Swap the positions of the current ant and the behind ant
                    ants1[ants1.index(ant)] = behind_ant
                    ants2[ants2.index(behind_ant)] = ant

    # Add the order of the ants in the first row to the order string
    order += "".join(ants1)

    # Add the order of the ants in the second row to the order string
    order += "".join(ants2)

    return order

