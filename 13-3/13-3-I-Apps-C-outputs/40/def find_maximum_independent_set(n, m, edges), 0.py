
def find_maximum_independent_set(n, m, edges):
    # Initialize a set to store the independent set
    independent_set = set()

    # Iterate through the edges and add them to the independent set
    for edge in edges:
        independent_set.add(edge[0])
        independent_set.add(edge[1])

    # Return the size of the independent set
    return len(independent_set)
