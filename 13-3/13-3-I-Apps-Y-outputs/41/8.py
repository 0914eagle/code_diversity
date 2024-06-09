
def get_bridges(n, m, edges):
    # Initialize a dictionary to store the degree of each vertex
    degrees = {}
    for i in range(1, n+1):
        degrees[i] = 0
    
    # Initialize a list to store the bridges
    bridges = []
    
    # Iterate over the edges and update the degree of the vertices
    for edge in edges:
        a, b = edge[0], edge[1]
        degrees[a] += 1
        degrees[b] += 1
    
    # Iterate over the edges again and check if they are bridges
    for edge in edges:
        a, b = edge[0], edge[1]
        if degrees[a] == 1 or degrees[b] == 1:
            bridges.append(edge)
    
    return len(bridges)

