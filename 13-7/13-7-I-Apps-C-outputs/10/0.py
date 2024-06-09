
def get_max_marked_nodes(n, d):
    # Initialize a list to store the marked nodes
    marked = []
    # Iterate through the tree nodes
    for i in range(1, n):
        # Check if the current node is closer than the distance d to any of the marked nodes
        if any(abs(i - j) <= d for j in marked):
            # If it is, skip it
            continue
        # If it's not, mark it and add it to the list of marked nodes
        marked.append(i)
    # Return the length of the list of marked nodes, which is the maximum number of nodes that can be marked
    return len(marked)

