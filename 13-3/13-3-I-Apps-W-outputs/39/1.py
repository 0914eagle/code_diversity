
def count_valid_pairs(n, edges):
    # Initialize a dictionary to store the neighbors of each vertex
    neighbors = {i: set() for i in range(1, n + 1)}

    # Add edges to the dictionary
    for edge in edges:
        neighbors[edge[0]].add(edge[1])
        neighbors[edge[1]].add(edge[0])

    # Initialize a set to store the valid pairs
    valid_pairs = set()

    # Iterate over all pairs of vertices
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            # If i and j are not neighbors, they are not valid
            if j not in neighbors[i]:
                continue

            # If the edge between i and j has a weight of 0, they are not valid
            if edges[i - 1][j - 1] == 0:
                continue

            # If we have already found a valid path from i to j, they are not valid
            if (j, i) in valid_pairs:
                continue

            # Mark the pair as valid and add it to the set
            valid_pairs.add((i, j))

    return len(valid_pairs)

