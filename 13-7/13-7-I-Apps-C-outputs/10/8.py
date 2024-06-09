
def get_max_marked_nodes(n, d, tree):
    # Initialize a set to store the marked nodes
    marked_nodes = set()
    # Loop through each node in the tree
    for i in range(1, n + 1):
        # If the node is not marked, try to mark it
        if i not in marked_nodes:
            # Check if marking this node will violate the distance constraint
            if any(abs(i - x) <= d for x in marked_nodes):
                continue
            # If not, mark the node and add it to the set
            marked_nodes.add(i)
    # Return the number of marked nodes
    return len(marked_nodes)

