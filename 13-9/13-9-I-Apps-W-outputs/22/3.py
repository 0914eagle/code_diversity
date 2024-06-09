
def find_final_position(n, m, k, holes, swaps):
    # Initialize the position of the bone as 1
    bone = 1

    # Loop through each swapping operation
    for i in range(k):
        # Get the positions of the cups to be swapped
        cup1, cup2 = swaps[i]

        # If either cup is in a hole, skip this operation
        if cup1 in holes or cup2 in holes:
            continue

        # Swap the positions of the cups
        bone = cup1 if bone == cup2 else cup2

    # Return the final position of the bone
    return bone

