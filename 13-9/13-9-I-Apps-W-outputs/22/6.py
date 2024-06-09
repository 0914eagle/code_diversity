
def find_final_position(n, m, k, holes, swaps):
    # Initialize the position of the bone as 1
    bone_position = 1

    # Loop through each swapping operation
    for i in range(k):
        # Get the positions of the cups to be swapped
        cup1_position, cup2_position = swaps[i]

        # Check if either cup is in a hole
        if cup1_position in holes or cup2_position in holes:
            # If either cup is in a hole, the bone falls into the hole and is not affected by the swapping operation
            continue

        # Swap the positions of the cups
        bone_position = cup2_position if bone_position == cup1_position else cup1_position

    return bone_position

