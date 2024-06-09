
def count_worlds(n, m):
    # Initialize the graph with only the source and sink vertices
    graph = {(0, 0): set(), (0, 1): set(), (1, 0): set(), (1, 1): set()}

    # Iterate over the number of changes
    for i in range(n):
        # Add a new vertex and edges to the graph
        graph[(i, 0)] = set()
        graph[(i, 1)] = set()
        graph[(i - 1, 0)].add((i, 0))
        graph[(i - 1, 1)].add((i, 1))
        graph[(i, 0)].add((i - 1, 0))
        graph[(i, 1)].add((i - 1, 1))

    # Count the number of non-similar worlds
    count = 0
    for v in graph:
        # Check if the vertex is not the source or sink vertex
        if v != (0, 0) and v != (n, 0):
            # Check if the vertex has a minimum cut of size at least m
            if len(graph[v]) >= m:
                count += 1

    return count % 1000000007

