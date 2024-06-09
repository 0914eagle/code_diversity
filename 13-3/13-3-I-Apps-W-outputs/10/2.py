
def solve(n, edges):
    # Initialize a dictionary to store the labels for each edge
    labels = {}
    # Initialize a set to store the used labels
    used_labels = set()
    # Iterate over the edges and assign labels
    for u, v in edges:
        # If the edge is not labeled yet, assign a label that is not used yet
        if (u, v) not in labels:
            labels[(u, v)] = next(x for x in range(n-1) if x not in used_labels)
            used_labels.add(labels[(u, v)])
        # If the edge is already labeled, use the same label
        else:
            labels[(u, v)] = labels[(v, u)]
    # Return the list of labels
    return [labels[(u, v)] for u, v in edges]

