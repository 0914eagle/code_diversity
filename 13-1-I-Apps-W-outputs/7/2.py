
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
    # Iterate over the edges and check if the condition is met
    for edge in edge_set:
        u, v = edge
        if abs(labels[u] - labels[v]) != 1:
            return "NO"
    # If all conditions are met, return a valid labeling
    labeling = [0] * n
    for i in range(1, n1+1):
        labeling[i-1] = 1
    for i in range(n1, n1+n2):
        labeling[i-1] = 2
    for i in range(n1+n2, n1+n2+n3):
        labeling[i-1] = 3
    return "YES\n" + "".join(str(label) for label in labeling)

