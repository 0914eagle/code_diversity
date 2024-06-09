
def get_surviving_islands(N, T, K, S, V):
    # Initialize a list to keep track of the number of surviving islands
    surviving_islands = [1] * (N + 1)

    # Iterate through each island and its dependencies
    for i in range(2, N + 1):
        # If the island has no dependencies, skip it
        if K[i - 1] == 0:
            continue

        # If the island's threshold is not met, it will collapse
        if T[i - 1] > sum(V[i - 1] for i in S[i - 1]):
            surviving_islands[i] = 0

        # Iterate through the island's dependencies
        for j in range(K[i - 1]):
            # If the dependency is not surviving, the island will collapse
            if surviving_islands[S[i - 1][j] - 1] == 0:
                surviving_islands[i] = 0
                break

    # Return the number of surviving islands
    return sum(surviving_islands)

