
def solve(N, D):
    # Initialize the minimum number of inspectors to deploy
    min_inspectors = 0

    # Loop through each tree and check if it is within the range of the inspector's inspection
    for i in range(1, N + 1):
        # Check if the tree is within the range of the inspector's inspection
        if i - D <= 0 or i + D >= N:
            # Increment the minimum number of inspectors if the tree is not within the range
            min_inspectors += 1

    # Return the minimum number of inspectors needed to deploy
    return min_inspectors

