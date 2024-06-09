
def num_cycles(n, m, edges):
    # Initialize a dictionary to store the connected components
    connected_components = {}

    # Iterate over the edges
    for edge in edges:
        # Add the vertices to the dictionary if they are not already present
        if edge[0] not in connected_components:
            connected_components[edge[0]] = set()
        if edge[1] not in connected_components:
            connected_components[edge[1]] = set()

        # Add the edge to the dictionary
        connected_components[edge[0]].add(edge[1])
        connected_components[edge[1]].add(edge[0])

    # Initialize a counter for the number of cycles
    num_cycles = 0

    # Iterate over the connected components
    for component in connected_components.values():
        # Check if the component is a cycle
        if len(component) > 2 and len(component) == len(set(component)):
            num_cycles += 1

    return num_cycles

