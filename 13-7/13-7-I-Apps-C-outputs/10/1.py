
def get_max_marked_nodes(n, d):
    # Initialize a list to store the marked nodes
    marked = []

    # Iterate through the tree nodes
    for i in range(1, n):
        # If the current node is not marked and is not closer than distance d to any of the marked nodes, mark it
        if i not in marked and all(abs(i - j) >= d for j in marked):
            marked.append(i)

    # Return the maximum number of marked nodes
    return len(marked)

