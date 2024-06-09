
def count_valid_pairs(n, edges):
    # Initialize a dictionary to store the neighbors of each vertex
    neighbors = {i: set() for i in range(1, n + 1)}

    # Add edges to the dictionary
    for edge in edges:
        x, y, c = edge
        neighbors[x].add(y)
        neighbors[y].add(x)

    # Initialize a set to store the valid pairs
    valid_pairs = set()

    # Iterate over all pairs of vertices
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            # If i and j are neighbors, they are not valid
            if j in neighbors[i]:
                continue
            # If the path from i to j contains a 0-edge after a 1-edge, they are not valid
            if any(neighbors[i][k] == j and neighbors[i][k - 1] == j for k in range(len(neighbors[i]))):
                continue
            # If the path from j to i contains a 0-edge after a 1-edge, they are not valid
            if any(neighbors[j][k] == i and neighbors[j][k - 1] == i for k in range(len(neighbors[j]))):
                continue
            # If i and j are valid, add them to the set of valid pairs
            valid_pairs.add((i, j))

    return len(valid_pairs)

