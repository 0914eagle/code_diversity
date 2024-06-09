
def find_final_position(n, m, k, holes, swaps):
    # Initialize the position of the bone as 1
    position = 1

    # Loop through each swap operation
    for i in range(k):
        # Get the positions of the cups to be swapped
        cup1, cup2 = swaps[i]

        # If the bone is inside either of the cups, move it to the other cup
        if position in [cup1, cup2]:
            position = cup2 if position == cup1 else cup1

        # If the bone is not inside either of the cups, move it to the other cup
        else:
            position = cup2

        # If the position of the bone is inside a hole, move it to the next cup
        if position in holes:
            position += 1

    return position

