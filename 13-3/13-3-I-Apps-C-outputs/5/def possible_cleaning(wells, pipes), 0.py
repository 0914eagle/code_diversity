
def possible_cleaning(wells, pipes):
    # Initialize a graph with the wells as nodes
    graph = {}
    for well in wells:
        graph[well] = []

    # Add edges to the graph based on the pipes
    for pipe in pipes:
        graph[pipe[0]].append(pipe[1:])

    # Check if the graph is connected
    visited = set()
    queue = [wells[0]]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            queue.extend(graph[node])

    # If the graph is connected, return "possible"
    if len(visited) == len(wells):
        return "possible"

    # If the graph is not connected, return "impossible"
    return "impossible"

