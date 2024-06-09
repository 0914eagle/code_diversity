
def find_final_position(n, m, k, holes, swaps):
    # Initialize the position of the bone as 1
    bone = 1

    # Loop through each swapping operation
    for i in range(k):
        # Get the positions of the cups to be swapped
        cup1, cup2 = swaps[i]

        # If the bone is inside one of the cups, move it to the other cup
        if bone in [cup1, cup2]:
            bone = cup2 if bone == cup1 else cup1

        # If the bone falls into a hole, set its position to -1
        if bone in holes:
            bone = -1
            break

    # Return the final position of the bone
    return bone

