
def solve(n, edges):
    # Initialize a dictionary to store the labels
    labels = {}
    # Initialize the maximum value of MEX(u, v)
    max_mex = n - 2
    # Loop through each edge and calculate the MEX(u, v)
    for u, v in edges:
        # If the edge is not already labeled, calculate the MEX(u, v)
        if u not in labels or v not in labels:
            # If the edge is not already labeled, calculate the MEX(u, v)
            if u not in labels:
                labels[u] = 0
            if v not in labels:
                labels[v] = 0
            # Calculate the MEX(u, v)
            mex = max(labels[u], labels[v]) + 1
            # Update the maximum value of MEX(u, v)
            max_mex = max(max_mex, mex)
        # If the edge is already labeled, update the label dictionary
        else:
            labels[u] = labels[v] = max(labels[u], labels[v]) + 1
    # Loop through the label dictionary and update the labels
    for node in labels:
        labels[node] = max_mex - labels[node]
    # Return the list of labels
    return [labels[node] for node in range(1, n + 1)]

