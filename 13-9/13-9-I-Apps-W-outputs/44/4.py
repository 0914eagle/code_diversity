
def find_labels(n, m, edges):
    # Initialize a list to store the labels
    labels = [0] * n
    # Initialize a set to keep track of the vertices that have been labeled
    labeled = set()
    # Initialize a queue to store the vertices to be labeled
    queue = []

    # Add the first vertex to the queue
    queue.append(1)

    while queue:
        # Get the vertex to be labeled from the queue
        vertex = queue.pop(0)
        # Label the vertex with the next available label
        labels[vertex - 1] = vertex
        # Add the vertex to the set of labeled vertices
        labeled.add(vertex)
        # Find all the neighbors of the vertex that have not been labeled yet
        neighbors = [edge[1] for edge in edges if edge[0] == vertex and edge[1] not in labeled]
        # Add the neighbors to the queue
        queue += neighbors

    return labels

