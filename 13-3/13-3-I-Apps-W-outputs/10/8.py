
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
        # Assign the MEX as the label for the edge
        labels[i] = mex
        # Add the label to the set of used labels
        used_labels.add(mex)
    # Return the labels
    return labels

