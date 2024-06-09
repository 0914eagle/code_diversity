
def get_max_marked_nodes(n, d, tree):
    # Initialize a set to store the marked nodes
    marked = set()
    # Loop through each node in the tree
    for i in range(1, n + 1):
        # If the node is not marked, try to mark it
        if i not in marked:
            # Check if marking the node would violate the distance constraint
            if any(abs(i - j) <= d for j in marked):
                continue
            # If not, mark the node and add it to the set
            marked.add(i)
    # Return the number of marked nodes
    return len(marked)

