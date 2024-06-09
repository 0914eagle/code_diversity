
def linkoping_pipes(wells, pipes):
    # Initialize a graph with the wells as nodes
    graph = {}
    for well in wells:
        graph[well] = []

    # Add edges to the graph based on the pipes
    for pipe in pipes:
        graph[pipe[0]].append(pipe[1:])

    # Find all cycles in the graph
    cycles = []
    for well in graph:
        for pipe in graph[well]:
            if pipe[1] in graph and pipe[0] != pipe[1]:
                cycles.append([well, pipe[1]])

    # Check if there are any cycles with more than 2 edges
    for cycle in cycles:
        if len(cycle) > 2:
            return "impossible"

    # If all cycles have 2 edges, return "possible"
    return "possible"

