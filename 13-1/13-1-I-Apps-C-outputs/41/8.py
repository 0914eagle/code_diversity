
def get_max_heap_size(n, values):
    # Initialize a list to store the heap property for each node
    heap_property = [False] * (n + 1)
    # Set the root node as the largest value
    heap_property[1] = True
    # Iterate through the nodes in reverse order
    for i in range(n, 0, -1):
        # If the current node is not the root and its value is greater than its parent's value
        if i != 1 and values[i] > values[i // 2]:
            # Set the heap property for the current node to True
            heap_property[i] = True
        # If the current node is the root or its value is less than or equal to its parent's value
        else:
            # Set the heap property for the current node to False
            heap_property[i] = False
    # Return the number of nodes with the heap property set to True
    return sum(heap_property)

