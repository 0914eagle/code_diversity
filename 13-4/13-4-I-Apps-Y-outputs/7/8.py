
def find_cycles(n, m, edges):
    # Initialize a dictionary to store the graph
    graph = {i: set() for i in range(1, n + 1)}

    # Add edges to the graph
    for edge in edges:
        u, v = edge
        graph[u].add(v)
        graph[v].add(u)

    # Initialize a set to store the cycles
    cycles = set()

    # Iterate over the vertices
    for vertex in graph:
        # If the vertex is not visited, do a DFS to find all the cycles that start from this vertex
        if vertex not in cycles:
            cycle = []
            dfs(graph, vertex, cycle)
            # If the cycle is not empty, add it to the set of cycles
            if cycle:
                cycles.add(tuple(cycle))

    # Return the number of cycles
    return len(cycles)

# DFS function to find all the cycles that start from a given vertex
def dfs(graph, vertex, cycle):
    # Mark the current vertex as visited
    cycle.append(vertex)

    # If the vertex has unvisited neighbors, recurse on them
    for neighbor in graph[vertex] - set(cycle):
        dfs(graph, neighbor, cycle)

    # If the vertex is the starting vertex of the cycle, add it to the cycle
    if cycle[0] == vertex:
        cycle.append(vertex)

