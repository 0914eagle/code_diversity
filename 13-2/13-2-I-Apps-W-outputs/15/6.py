
def solve(n, edges):
    # Initialize a dictionary to store the labels for each edge
    labels = {}
    # Initialize a set to store the used labels
    used_labels = set()
    # Iterate over the edges and assign labels
    for edge in edges:
        # If the edge has not been labeled yet, assign a label that is not used yet
        if edge not in labels:
            # Find the smallest available label that is not used yet
            for label in range(n-2):
                if label not in used_labels:
                    break
            # Assign the label to the edge
            labels[edge] = label
            # Add the label to the set of used labels
            used_labels.add(label)
    # Return the list of labels
    return [labels[edge] for edge in edges]

