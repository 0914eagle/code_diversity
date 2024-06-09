
def get_max_marked_nodes(n, d):
    # Initialize a list to store the marked nodes
    marked = []

    # Iterate through the input nodes
    for i in range(1, n):
        # If the current node is not closer to any of the marked nodes than the allowed distance, mark it
        if all(abs(i - j) > d for j in marked):
            marked.append(i)

    # Return the maximum number of marked nodes
    return len(marked)

