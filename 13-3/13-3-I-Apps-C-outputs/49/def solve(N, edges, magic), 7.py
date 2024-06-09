
def solve(N, edges, magic):
    # Initialize a dictionary to store the magic of each node
    node_magic = {i: magic[i-1] for i in range(1, N+1)}
    
    # Iterate through the edges and update the magic of the nodes
    for edge in edges:
        node1, node2 = edge[0], edge[1]
        node_magic[node1] *= node_magic[node2]
        node_magic[node2] = node_magic[node1]
    
    # Find the node with the minimum magic
    min_magic = min(node_magic.values())
    
    # Find the node with the minimum magic that is not a leaf node
    non_leaf_nodes = [node for node in node_magic if node_magic[node] == min_magic and node != 1]
    if len(non_leaf_nodes) == 0:
        return str(min_magic) + "/1"
    else:
        node = non_leaf_nodes[0]
    
    # Find the path from the root node to the minimum magic node
    path = [node]
    while node != 1:
        for edge in edges:
            if edge[1] == node:
                node = edge[0]
                path.append(node)
                break
    
    # Calculate the magic of the path
    magic_path = 1
    for i in range(len(path)-1):
        magic_path *= node_magic[path[i]]
    
    # Return the magic of the path in the form of a reduced fraction
    gcd = math.gcd(magic_path, min_magic)
    return str(magic_path//gcd) + "/" + str(min_magic//gcd)

