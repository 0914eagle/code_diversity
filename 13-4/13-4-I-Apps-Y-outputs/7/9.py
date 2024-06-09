
def num_cycles(n, m, edges):
    # Initialize a dictionary to store the connected components
    connected_components = {}

    # Iterate over the edges
    for edge in edges:
        # Add the vertices to the connected component dictionary
        connected_components[edge[0]] = edge[0]
        connected_components[edge[1]] = edge[0]

        # Check if the vertices are already in the same connected component
        if connected_components[edge[0]] == connected_components[edge[1]]:
            # If they are, merge the components
            connected_components[edge[1]] = connected_components[edge[0]]

    # Initialize a counter for the number of cycles
    num_cycles = 0

    # Iterate over the connected components
    for component in connected_components.values():
        # Check if the component is a cycle
        if len(component) > 2:
            # If it is, increment the number of cycles
            num_cycles += 1

    return num_cycles

