
def find_minimal_magic_path(nodes, edges, magic):
    # Initialize a dictionary to store the magic of each node
    node_magic = {node: magic[node - 1] for node in nodes}
    
    # Iterate through the edges and update the magic of the nodes
    for edge in edges:
        node1, node2 = edge
        node_magic[node1] *= node_magic[node2]
        node_magic[node2] = node_magic[node1]
    
    # Find the node with the minimum magic
    min_magic = min(node_magic.values())
    
    # Find the node with the minimum magic that is not a leaf node
    non_leaf_nodes = [node for node in nodes if node_magic[node] == min_magic and node != 1]
    if not non_leaf_nodes:
        return f"{min_magic}/1"
    node = non_leaf_nodes[0]
    
    # Find the path from the root node to the minimum magic node
    path = []
    while node != 1:
        path.append(node)
        node = find_parent(node, edges)
    
    # Calculate the magic of the path
    path_magic = 1
    for node in path:
        path_magic *= node_magic[node]
    
    # Find the greatest common divisor of the path magic and the number of nodes in the path
    gcd = find_gcd(path_magic, len(path))
    
    # Return the reduced fraction of the path magic
    return f"{path_magic // gcd}/{len(path) // gcd}"

def find_parent(node, edges):
    for edge in edges:
        if edge[1] == node:
            return edge[0]
    return None

def find_gcd(a, b):
    if b == 0:
        return a
    return find_gcd(b, a % b)

