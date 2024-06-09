
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
    non_leaf_nodes = [node for node in node_magic if node_magic[node] == min_magic and node != 1 and node != N]
    if len(non_leaf_nodes) == 0:
        return str(min_magic)
    else:
        node = non_leaf_nodes[0]
    
    # Find the path from the root node to the minimum magic node
    path = []
    while node != 1:
        path.append(node)
        node = find_parent(node, edges)
    
    # Find the gcd of the magic of the nodes in the path
    gcd = find_gcd(path, node_magic)
    
    # Return the reduced fraction of the path magic
    return f"{min_magic//gcd}/{node_magic[path[0]]//gcd}"

def find_parent(node, edges):
    for edge in edges:
        if edge[1] == node:
            return edge[0]

def find_gcd(path, node_magic):
    gcd = node_magic[path[0]]
    for node in path[1:]:
        gcd = gcd(gcd, node_magic[node])
    return gcd

