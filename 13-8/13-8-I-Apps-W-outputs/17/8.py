
def get_maximum_clique(A):
    # Initialize a dictionary to store the clique sizes for each vertex
    clique_sizes = {}
    
    # Iterate over the vertices in the graph
    for vertex in A:
        # Initialize the clique size for the current vertex to 1
        clique_sizes[vertex] = 1
        # Iterate over the remaining vertices in the graph
        for other_vertex in A:
            # If the current vertex is divisible by the other vertex, or vice versa, add 1 to the clique size for the current vertex
            if vertex % other_vertex == 0 or other_vertex % vertex == 0:
                clique_sizes[vertex] += 1
    
    # Return the maximum clique size among all vertices
    return max(clique_sizes.values())

