
def solve(n, m, edges):
    # Initialize a list to store the permutation
    permutation = [0] * n
    # Initialize a set to keep track of the vertices that are already labeled
    labeled_vertices = set()
    # Initialize a queue to do a BFS traversal of the graph
    queue = []

    # Start with the first vertex as the source vertex
    source_vertex = 1

    # Label the source vertex with the smallest label (1)
    permutation[source_vertex-1] = 1
    labeled_vertices.add(source_vertex)

    # Add the source vertex to the queue
    queue.append(source_vertex)

    while queue:
        # Dequeue a vertex from the queue
        vertex = queue.pop(0)

        # Get the neighbors of the dequeued vertex
        neighbors = [edge[1] for edge in edges if edge[0] == vertex]

        # Label the unlabeled neighbors with the next available label
        for neighbor in neighbors:
            if neighbor not in labeled_vertices:
                label = permutation[vertex-1] + 1
                permutation[neighbor-1] = label
                labeled_vertices.add(neighbor)
                queue.append(neighbor)

    return permutation

