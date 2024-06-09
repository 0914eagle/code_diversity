
def find_cycles(n, m, edges):
    # Initialize a dictionary to store the graph
    graph = {}
    for i in range(1, n+1):
        graph[i] = []

    # Add edges to the graph
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    # Initialize a set to store the connected components
    connected_components = set()

    # Iterate through the graph and find the connected components
    for node in graph:
        if node not in connected_components:
            # Initialize a queue to do BFS
            queue = [node]
            connected_components.add(node)

            while queue:
                node = queue.pop(0)
                for neighbor in graph[node]:
                    if neighbor not in connected_components:
                        queue.append(neighbor)
                        connected_components.add(neighbor)

    # Initialize a set to store the cycles
    cycles = set()

    # Iterate through the connected components and find the cycles
    for component in connected_components:
        if len(graph[component]) == 1:
            # If the connected component has only one edge, it is a cycle
            cycles.add(frozenset([component, graph[component][0]]))
        else:
            # If the connected component has more than one edge, it is not a cycle
            pass

    return len(cycles)

