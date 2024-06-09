
def get_minimal_bdd_size(n, function_values):
    # Initialize a dictionary to store the BDD nodes
    bdd_nodes = {}

    # Initialize the root node with the function values
    root_node = (0, function_values)
    bdd_nodes[0] = root_node

    # Loop until all the nodes are processed
    while len(bdd_nodes) > 0:
        # Get the next node to process
        node_id, node_values = bdd_nodes.popitem()

        # Check if the node is a leaf node
        if len(node_values) == 1:
            # If the node is a leaf node, return the size of the BDD
            return len(bdd_nodes) + 1

        # Split the node values into two subsets
        subset1 = node_values[:len(node_values) // 2]
        subset2 = node_values[len(node_values) // 2:]

        # Create two new nodes for the subsets
        node1 = (node_id * 2, subset1)
        node2 = (node_id * 2 + 1, subset2)

        # Add the new nodes to the dictionary
        bdd_nodes[node1[0]] = node1
        bdd_nodes[node2[0]] = node2

    # If all the nodes are processed and no leaf node is found, return -1
    return -1

