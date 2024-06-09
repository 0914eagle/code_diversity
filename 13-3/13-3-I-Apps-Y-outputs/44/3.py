
def solve(N1, N2, row1, row2, T):
    # Initialize the order of the ants after T seconds
    order = ""

    # Loop through each second
    for second in range(T):
        # Loop through each ant in the first row
        for i in range(N1):
            # If the ant is not the first ant in the first row
            if i > 0:
                # Get the position of the ant in the second row
                j = N2 - i - 1
                # If the ant in the second row is moving in the opposite direction
                if row2[j] < row2[j-1]:
                    # Swap the positions of the two ants
                    row2[j], row2[j-1] = row2[j-1], row2[j]

    # Add the order of the ants in the first row to the order after T seconds
    order += "".join(row1)
    # Add the order of the ants in the second row to the order after T seconds
    order += "".join(row2)

    return order

