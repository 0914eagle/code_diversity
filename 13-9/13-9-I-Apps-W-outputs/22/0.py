
def solve(n, m, k, holes, swaps):
    # Initialize the position of the bone as 1
    bone = 1
    # Loop through each swapping operation
    for i in range(k):
        # Get the positions of the cups to be swapped
        cup1, cup2 = swaps[i]
        # If the bone is inside one of the cups, move it to the other cup
        if bone in [cup1, cup2]:
            bone = cup2 if bone == cup1 else cup1
        # If the bone is not inside any of the cups, move it to the position of the other cup
        else:
            bone = cup2
    # Return the final position of the bone
    return bone

