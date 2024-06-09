
def get_maximum_marked_nodes(n, d, tree):
    # Initialize a set to store the marked nodes
    marked_nodes = set()

    # Iterate through the tree in reverse order (starting from the last node)
    for i in range(n-1, -1, -1):
        # If the current node is not marked and is not closer than d to any marked node, mark it
        if i not in marked_nodes and all(i-j not in marked_nodes for j in range(i-d, i)):
            marked_nodes.add(i)

    # Return the number of marked nodes
    return len(marked_nodes)

