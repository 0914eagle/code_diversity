
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
            # Find the distance between the current vertex and all other vertices of the same color
            distance = 0
            for j in range(N):
                if colors[i] == colors[j] and i != j:
                    distance = max(distance, abs(i - j))

            # Add the distance to the niceness sum
            niceness += distance

        # Add the niceness of the current coloring to the total niceness sum
        niceness_sum += niceness

    # Return the total niceness sum modulo (10^9 + 7)
    return niceness_sum % (10 ** 9 + 7)

