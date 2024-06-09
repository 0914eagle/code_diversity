
def get_max_marked_nodes(n, d):
    # Initialize a list to store the marked nodes
    marked = []

    # Iterate through the tree nodes
    for i in range(1, n):
        # Check if the current node is closer to any of the marked nodes than the allowed distance
        for j in marked:
            if abs(i - j) <= d:
                break
        else:
            # If the current node is not closer to any of the marked nodes, mark it
            marked.append(i)

    # Return the maximum number of marked nodes
    return len(marked)

