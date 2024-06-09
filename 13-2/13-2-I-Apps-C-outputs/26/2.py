
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
            if coloring & (1 << i):
                colors.append(1)
            else:
                colors.append(0)

        # Calculate the niceness of the current coloring
        niceness = 0
        for i in range(N):
            # Find the distance between the current vertex and all its neighbors
            distances = [abs(i - j) for j in graph[i + 1]]

            # Find the maximum distance between white and black vertices
            max_white = max(distances[colors[i] == 0])
            max_black = max(distances[colors[i] == 1])

            # Calculate the niceness of the current coloring
            niceness = max(niceness, max_white, max_black)

        # Add the niceness of the current coloring to the sum
        niceness_sum += niceness

    # Return the sum of nicenesses modulo (10^9 + 7)
    return niceness_sum % (10 ** 9 + 7)

