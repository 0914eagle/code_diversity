
def can_clean_intersections(wells, pipes):
    # Initialize a graph with the wells as nodes
    graph = {}
    for well in wells:
        graph[well] = []

    # Add edges to the graph based on the pipes
    for pipe in pipes:
        graph[pipe[0]].append(pipe[1:])

    # Iterate through the graph and check if there are any cycles
    for well in graph:
        visited = set()
        queue = [well]
        while queue:
            node = queue.pop(0)
            if node in visited:
                continue
            visited.add(node)
            queue.extend(graph[node])
            if node in visited:
                return "impossible"
    return "possible"

