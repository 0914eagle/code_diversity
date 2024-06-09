
def get_bridges(n, m, edges):
    # Initialize a dictionary to store the edges and their weights
    edge_weights = {}
    for edge in edges:
        edge_weights[edge] = 1

    # Initialize a dictionary to store the vertices and their neighbors
    vertex_neighbors = {}
    for edge in edges:
        vertex1, vertex2 = edge
        if vertex1 not in vertex_neighbors:
            vertex_neighbors[vertex1] = set()
        vertex_neighbors[vertex1].add(vertex2)
        if vertex2 not in vertex_neighbors:
            vertex_neighbors[vertex2] = set()
        vertex_neighbors[vertex2].add(vertex1)

    # Initialize a set to store the bridges
    bridges = set()

    # Iterate over the edges and check if they are bridges
    for edge in edges:
        vertex1, vertex2 = edge
        if len(vertex_neighbors[vertex1]) == 1 and len(vertex_neighbors[vertex2]) == 1:
            # If both vertices have only one neighbor, then the edge is a bridge
            bridges.add(edge)
        elif vertex1 in vertex_neighbors[vertex2] and vertex2 in vertex_neighbors[vertex1]:
            # If both vertices are neighbors, then the edge is not a bridge
            continue
        else:
            # If one vertex is a neighbor of the other, then the edge is a bridge
            bridges.add(edge)

    return len(bridges)

