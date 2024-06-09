
def solve(N, edges):
    # Initialize the graph as a dictionary of sets
    graph = {i: set() for i in range(1, N + 1)}

    # Add edges to the graph
    for edge in edges:
        graph[edge[0]].add(edge[1])
        graph[edge[1]].add(edge[0])

    # Initialize the niceness sum
    niceness_sum = 0

    # Iterate over all possible colorings of the graph
    for coloring in range(2 ** N):
        # Convert the binary representation of the coloring to a list of colors
        colors = []
        for i in range(N):
            colors.append(coloring >> i & 1)

        # Initialize the maximum distance between white and black vertices
        max_white_distance = 0
        max_black_distance = 0

        # Iterate over all edges in the graph
        for i in range(N - 1):
            # Get the vertices connected by the current edge
            u, v = edges[i]

            # If the current edge is between two vertices of the same color, skip it
            if colors[u - 1] == colors[v - 1]:
                continue

            # If the current edge is between a white and a black vertex, update the maximum distance
            if colors[u - 1] == 0 and colors[v - 1] == 1:
                max_white_distance = max(max_white_distance, graph[u].index(v))
            elif colors[u - 1] == 1 and colors[v - 1] == 0:
                max_black_distance = max(max_black_distance, graph[u].index(v))

        # Add the niceness of the current coloring to the sum
        niceness_sum += max(max_white_distance, max_black_distance)

    # Return the sum of the nicenesses modulo (10^9 + 7)
    return niceness_sum % (10 ** 9 + 7)

