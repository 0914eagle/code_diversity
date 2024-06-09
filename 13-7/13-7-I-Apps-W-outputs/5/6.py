
def solve(N, T, K, V):
    # Initialize a list to store the number of surviving islands
    surviving_islands = []

    # Loop through each island
    for i in range(N):
        # Check if the current island has enough goods to survive
        if T[i] <= sum(V[i]):
            # Add the current island to the list of surviving islands
            surviving_islands.append(i)

    # Return the number of surviving islands
    return len(surviving_islands)

