
def find_labels(n, m, edges):
    # Initialize a list to store the labels
    labels = [0] * n
    # Initialize a set to keep track of the vertices that are already labeled
    labeled_vertices = set()
    # Iterate through the edges and assign labels based on the following criteria:
    # * Labels form a valid permutation of length n
    # * Labels are lexicographically smallest
    # * If there exists an edge from vertex v to vertex u, then label_v should be smaller than label_u
    for edge in edges:
        v, u = edge
        if v not in labeled_vertices:
            labels[v] = v
            labeled_vertices.add(v)
        if u not in labeled_vertices:
            labels[u] = v + 1
            labeled_vertices.add(u)
    return labels

