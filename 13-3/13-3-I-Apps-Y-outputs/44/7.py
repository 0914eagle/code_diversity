
def solve(ants1, ants2, T):
    # Initialize the order of the ants after T seconds as an empty string
    order = ""

    # Loop through each second
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
                    ants2 = ants2[:j] + ants1[i] + ants2[j+1:]

        # Add the order of the ants in the second row to the order of the ants after T seconds
        order += "".join(ants2)

    # Return the order of the ants after T seconds
    return order

