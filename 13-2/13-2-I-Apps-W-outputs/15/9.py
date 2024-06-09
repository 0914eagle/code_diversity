
def solve(n, edges):
    # Initialize a dictionary to store the labels
    labels = {}
    # Initialize the maximum value of MEX(u,v)
    max_mex = n - 2
    # Loop through the edges
    for u, v in edges:
        # If the edge is not labeled yet
        if u not in labels or v not in labels:
            # Assign the smallest available label to the edge
            if u not in labels:
                labels[u] = 0
            if v not in labels:
                labels[v] = 1
        # If both edges are labeled
        else:
            # Calculate the MEX value for the edge
            mex = max(labels[u], labels[v]) + 1
            # Update the maximum MEX value
            max_mex = min(max_mex, mex)
            # Assign the label to the edge
            labels[u] = mex
            labels[v] = mex
    # Return the labels in the order of the edges
    return [labels[u] for u, _ in edges]

