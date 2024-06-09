
def solve(n, m, k, holes, swaps):
    # Initialize the position of the bone as 1
    bone = 1
    # Loop through each swap operation
    for i in range(k):
        # Get the positions of the cups to be swapped
        cup1, cup2 = swaps[i]
        # Check if either cup is in a hole
        if cup1 in holes or cup2 in holes:
            # If either cup is in a hole, the bone falls into the hole and we can return the final position as None
            return None
        # Swap the positions of the cups
        bone = cup2 if bone == cup1 else cup1
    # Return the final position of the bone
    return bone

