
def get_max_marked_nodes(n, d, edges):
    # Initialize a set to store the marked nodes
    marked = set()
    # Loop through each edge and mark the nodes
    for i, j in edges:
        # If the distance between the nodes is less than or equal to d, mark them
        if j - i <= d:
            marked.add(i)
            marked.add(j)
    # Return the length of the marked set, which is the maximum number of nodes that can be marked
    return len(marked)

