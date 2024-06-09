
def get_max_heap_size(n, values):
    # Initialize a list to store the heap property for each node
    heap_property = [False] * (n + 1)
    # Set the root node as the largest node
    heap_property[1] = True
    # Iterate through the nodes in reverse order
    for i in range(n, 0, -1):
        # If the current node is not the root node
        if i != 1:
            # Get the parent node and its value
            parent = values[i][1]
            parent_value = values[parent][0]
            # If the current node is larger than its parent node
            if values[i][0] > parent_value:
                # Set the heap property for the current node to True
                heap_property[i] = True
                # Set the heap property for the parent node to False
                heap_property[parent] = False
    # Return the number of nodes with the heap property set to True
    return sum(heap_property)

n = int(input())
values = []
for i in range(n):
    values.append(list(map(int, input().split())))
print(get_max_heap_size(n, values))

