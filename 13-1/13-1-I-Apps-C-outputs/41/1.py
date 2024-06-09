
def get_max_heap_size(n, values):
    # Initialize a list to store the heap property for each node
    heap_property = [False] * (n + 1)
    # Set the heap property for the root node to True
    heap_property[1] = True
    # Iterate through the nodes in reverse order
    for i in range(n, 0, -1):
        # If the current node has a parent and the parent node has the heap property, set the current node's heap property to True
        if values[i][1] != 0 and heap_property[values[i][1]]:
            heap_property[i] = True
    # Return the number of nodes with the heap property
    return sum(heap_property)

