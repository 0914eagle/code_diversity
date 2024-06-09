
def find_final_position(n, m, k, holes, swaps):
    # Initialize the position of the bone as 1
    bone = 1
    # Loop through each swap operation
    for i in range(k):
        # Get the positions of the cups to be swapped
        cup1, cup2 = swaps[i]
        # If the bone is inside one of the cups, move it to the other cup
        if bone in [cup1, cup2]:
            bone = cup2 if bone == cup1 else cup1
        # If the bone falls into a hole, return -1
        if bone in holes:
            return -1
        # Swap the positions of the cups
        cup1, cup2 = cup2, cup1
    # Return the final position of the bone
    return bone

