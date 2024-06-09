
def get_maximum_independent_set(n, m, edges):
    # Initialize a set to store the independent set
    independent_set = set()
    # Iterate through the edges
    for edge in edges:
        # If the edge is not in the independent set, add it
        if edge[0] not in independent_set and edge[1] not in independent_set:
            independent_set.add(edge[0])
            independent_set.add(edge[1])
    # Return the size of the independent set
    return len(independent_set)

