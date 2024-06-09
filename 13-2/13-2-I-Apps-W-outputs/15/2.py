
def solve(n, edges):
    # Initialize a list to store the labels
    labels = [0] * (n - 1)
    # Initialize a set to keep track of the used labels
    used_labels = set()
    # Iterate through the edges
    for i, (u, v) in enumerate(edges):
        # Find the MEX of the edge
        mex = 0
        while mex in used_labels:
            mex += 1
        # Add the label to the list and set
        labels[i] = mex
        used_labels.add(mex)
    # Return the list of labels
    return labels

