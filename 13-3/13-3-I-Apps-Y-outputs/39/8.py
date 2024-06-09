
def solve(N, D):
    # Initialize the minimum number of inspectors to deploy
    min_inspectors = 0

    # Loop through each tree
    for i in range(1, N + 1):
        # Check if the tree is within the range of the current inspector
        if i - D <= N and i + D >= 1:
            # Increment the minimum number of inspectors
            min_inspectors += 1

    # Return the minimum number of inspectors
    return min_inspectors

