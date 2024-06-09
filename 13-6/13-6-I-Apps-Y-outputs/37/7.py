
def number_of_paths(n, m, edges):
    # Initialize a matrix to store the number of paths from vertex i to vertex j
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # Initialize the number of paths from vertex 1 to vertex 1 as 1
    dp[1][1] = 1

    # Iterate over the edges
    for i in range(m):
        # Get the endpoints of the current edge
        a, b = edges[i]

        # Iterate over the possible starting vertices
        for j in range(1, n + 1):
            # If the current edge is not a self-loop and the starting vertex is not the same as the ending vertex
            if a != b and j != a:
                # Add the number of paths from vertex j to vertex a to the number of paths from vertex j to vertex b
                dp[j][b] += dp[j][a]

    # Return the number of paths from vertex 1 to vertex n
    return dp[1][n]

