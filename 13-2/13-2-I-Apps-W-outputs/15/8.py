
def solve(n, edges):
    # Initialize a dictionary to store the labels for each edge
    labels = {}
    # Initialize a set to store the used labels
    used_labels = set()
    # Iterate over the edges and assign labels
    for edge in edges:
        # If the edge has not been labeled yet, assign a label that is not already used
        if edge not in labels:
            for label in range(n-2):
                if label not in used_labels:
                    labels[edge] = label
                    used_labels.add(label)
                    break
        # If the edge has already been labeled, add the label to the set of used labels
        else:
            used_labels.add(labels[edge])
    # Return the list of labels
    return [labels[edge] for edge in edges]

