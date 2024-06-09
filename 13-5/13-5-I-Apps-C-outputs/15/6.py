
def get_max_independent_set(n, m, edges):
    # Initialize a set to store the independent set
    independent_set = set()
    # Iterate through the edges
    for edge in edges:
        # If the edge connects two vertices that are already in the independent set, remove them
        if edge[0] in independent_set and edge[1] in independent_set:
            independent_set.remove(edge[0])
            independent_set.remove(edge[1])
    # Return the size of the independent set
    return len(independent_set)

