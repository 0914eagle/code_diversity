
def num_cycles(n, m, edges):
    # Initialize a dictionary to store the connected components
    connected_components = {}

    # Iterate over the edges
    for edge in edges:
        # Add the vertices to the connected component if they are not already present
        connected_components[edge[0]] = connected_components.get(edge[0], set()) | {edge[0]}
        connected_components[edge[1]] = connected_components.get(edge[1], set()) | {edge[1]}

        # If the vertices are already present in the connected component, merge the sets
        if edge[0] in connected_components and edge[1] in connected_components:
            connected_components[edge[0]] |= connected_components[edge[1]]
            connected_components[edge[1]] = connected_components[edge[0]]

    # Initialize a counter for the number of cycles
    num_cycles = 0

    # Iterate over the connected components
    for component in connected_components.values():
        # If the component is a cycle, increment the counter
        if len(component) > 2 and all(edge[0] in component and edge[1] in component for edge in edges if edge[0] in component and edge[1] in component):
            num_cycles += 1

    return num_cycles

