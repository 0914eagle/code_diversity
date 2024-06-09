
def solve(ants1, ants2, T):
    # Initialize the order of the ants after T seconds as an empty string
    order = ""

    # Loop through each second of the simulation
    for second in range(T):
        # Loop through each ant in the first row
        for i in range(len(ants1)):
            # If the ant is not the first ant in the first row
            if i > 0:
                # Get the position of the ant in the second row that is behind the current ant in the first row
                j = len(ants2) - i
                # If the ant in the second row is moving in the opposite direction
                if ants2[j] in "ABC":
                    # Swap the positions of the two ants
                    ants1[i], ants1[i-1] = ants1[i-1], ants1[i]
                    ants2[j], ants2[j-1] = ants2[j-1], ants2[j]

    # Concatenate the orders of the ants in the first and second row
    order = "".join(ants1 + ants2)

    return order

