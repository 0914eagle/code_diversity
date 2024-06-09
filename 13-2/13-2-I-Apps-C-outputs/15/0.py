
def find_shortest_cycle(files):
    # Initialize a graph with the given files as nodes
    graph = {}
    for file in files:
        graph[file] = []

    # Add edges to the graph based on the import statements
    for file in files:
        imports = files[file]
        for import_file in imports:
            graph[file].append(import_file)

    # Find a shortest cycle in the graph
    cycle = []
    for file in files:
        if file not in cycle:
            cycle = find_cycle(graph, file, cycle)
            if len(cycle) > 0:
                break

    # Return the shortest cycle
    return cycle

def find_cycle(graph, node, cycle):
    # If the node is already in the cycle, we have found a cycle
    if node in cycle:
        return cycle

    # Add the node to the cycle
    cycle.append(node)

    # Recursively search for a cycle starting from the node's neighbors
    for neighbor in graph[node]:
        cycle = find_cycle(graph, neighbor, cycle)
        if len(cycle) > 0:
            break

    # Return the cycle
    return cycle

