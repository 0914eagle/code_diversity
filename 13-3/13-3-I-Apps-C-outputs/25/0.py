
def is_permutation_possible(n):
    # Initialize a list to store the positions of the swaps
    swaps = []

    # Iterate through each pair of positions (i, j) where i < j
    for i in range(n):
        for j in range(i+1, n):
            # If the swap (i, j) has not been performed yet, perform it
            if (i, j) not in swaps:
                swaps.append((i, j))

    # If the number of swaps is equal to the number of positions, return "YES" and the swaps
    if len(swaps) == n:
        return "YES\n" + "\n".join([f"{i} {j}" for i, j in swaps])

    # Otherwise, return "NO"
    return "NO"

