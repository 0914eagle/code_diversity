
def min_wolves_to_escape(graph, pigs):
    # Initialize a set to store the vertices of the graph that are leaves
    leaves = set()
    
    # Iterate over the graph and find all the leaves
    for vertex in graph:
        if len(graph[vertex]) == 1:
            leaves.add(vertex)
    
    # Initialize a set to store the vertices of the graph that are occupied by pigs
    pig_vertices = set(pigs)
    
    # Initialize a set to store the vertices of the graph that are occupied by wolves
    wolf_vertices = set(range(len(graph))) - pig_vertices
    
    # Initialize a variable to store the minimum number of wolves to remove
    min_wolves = 0
    
    # Iterate until there is at least one pig on each leaf vertex
    while len(leaves) > 0:
        # Find the leaf vertex that is closest to a pig
        closest_leaf = None
        min_distance = float('inf')
        for leaf in leaves:
            for pig in pig_vertices:
                distance = graph[pig][leaf]
                if distance < min_distance:
                    min_distance = distance
                    closest_leaf = leaf
                    break
        
        # Remove the wolf that is occupying the closest leaf vertex
        wolf_vertices.remove(closest_leaf)
        leaves.remove(closest_leaf)
        min_wolves += 1
    
    return min_wolves

