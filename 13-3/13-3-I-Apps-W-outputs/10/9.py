
def solve(n, edges):
    # Initialize a list to store the labels
    labels = [0] * (n - 1)
    # Initialize a set to keep track of the used labels
    used_labels = set()
    # Iterate through the edges
    for i in range(n - 1):
        # Get the current edge
        edge = edges[i]
        # Find the minimum excludant of the current edge
        mex = find_mex(edge, used_labels)
        # Add the minimum excludant to the list of labels
        labels[i] = mex
        # Add the minimum excludant to the set of used labels
        used_labels.add(mex)
    # Return the list of labels
    return labels

def find_mex(edge, used_labels):
    # Initialize the minimum excludant as 0
    mex = 0
    # Iterate through the possible labels
    for label in range(len(used_labels)):
        # If the current label is not in the set of used labels, return it
        if label not in used_labels:
            return label
        # Otherwise, increment the minimum excludant
        mex += 1
    # If all labels are used, return the minimum excludant
    return mex

