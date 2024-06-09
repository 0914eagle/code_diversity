
def solve(ants1, ants2, T):
    # Initialize the order of the ants after T seconds
    order = ""

    # Loop through each second
    for second in range(T):
        # Loop through each ant in the first row
        for i in range(len(ants1)):
            # If the ant is not the first ant in the first row
            if i > 0:
                # Get the position of the ant in the second row that is behind the current ant in the first row
                pos = (i - 1) % len(ants2)

                # If the ant in the second row is moving in the opposite direction
                if ants2[pos] in "ACEGIKMOQSUWY":
                    # Swap the positions of the two ants
                    ants1[i], ants1[i-1] = ants1[i-1], ants1[i]

    # Add the order of the ants to the output
    order += "".join(ants1) + "".join(ants2)

    return order

