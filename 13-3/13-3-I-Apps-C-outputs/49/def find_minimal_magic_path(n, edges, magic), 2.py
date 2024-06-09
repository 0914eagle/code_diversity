
def find_minimal_magic_path(n, edges, magic):
    # Initialize a dictionary to store the magic of each node
    node_magic = {i: magic[i-1] for i in range(1, n+1)}
    
    # Iterate over the edges and update the magic of the nodes
    for edge in edges:
        node1, node2 = edge[0], edge[1]
        node_magic[node1] *= node_magic[node2]
        node_magic[node2] = node_magic[node1]
    
    # Find the node with the minimum magic
    min_magic = min(node_magic.values())
    
    # Find the path with the minimum magic
    min_path = [k for k, v in node_magic.items() if v == min_magic]
    
    # Return the magic of the path in the form of a reduced fraction
    gcd = math.gcd(min_magic, len(min_path))
    return f"{min_magic//gcd}/{len(min_path)//gcd}"

