
def solve(N, T, K, S, V):
    # Initialize a list to keep track of the number of surviving islands
    surviving_islands = []

    # Loop through each island and check if it has enough goods to survive
    for i in range(N):
        # If the island has enough goods to survive, add it to the list of surviving islands
        if T[i] <= sum(V[i] for i in S[i]):
            surviving_islands.append(i)

    # Return the number of surviving islands
    return len(surviving_islands)

