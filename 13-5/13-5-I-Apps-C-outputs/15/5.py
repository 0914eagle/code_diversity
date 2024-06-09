
def get_max_independent_set_size(n, m, edges):
    # Initialize a set to store the vertices in the independent set
    independent_set = set()
    # Iterate through the edges and add the vertices to the independent set
    for edge in edges:
        independent_set.add(edge[0])
        independent_set.add(edge[1])
    # Return the size of the independent set
    return len(independent_set)

