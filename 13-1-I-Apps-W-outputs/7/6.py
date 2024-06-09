
def solve(n, m, n1, n2, n3, edges):
    # Initialize a dictionary to store the number of vertices with each label
    labels = {1: 0, 2: 0, 3: 0}
    # Initialize a set to store the edges
    edge_set = set()
    # Iterate over the edges and update the dictionary and set
    for edge in edges:
        u, v = edge
        labels[u] += 1
        labels[v] += 1
        edge_set.add((u, v))
    # Check if the number of vertices with each label is correct
    if labels[1] != n1 or labels[2] != n2 or labels[3] != n3:
        return "NO"
    # Iterate over the edges and check if the difference between the labels of the vertices is 1
    for edge in edge_set:
        u, v = edge
        if abs(labels[u] - labels[v]) != 1:
            return "NO"
    # If all conditions are met, return a valid labeling
    labeling = "".join(str(labels[i]) for i in range(1, n + 1))
    return "YES\n" + labeling

