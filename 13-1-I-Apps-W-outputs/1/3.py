
def solve(N, paths, permutation):
    # Initialize a graph with N nodes and 0 edges
    graph = [[] for _ in range(N)]

    # Add edges to the graph based on the given paths
    for path in paths:
        graph[path[0] - 1].append(path[1] - 1)
        graph[path[1] - 1].append(path[0] - 1)

    # Initialize a list to store the number of boring pairs before each destruction
    boring_pairs = [0]

    # Iterate through the permutation of paths
    for i in range(1, len(permutation)):
        # Get the current path and the previous path
        current_path = permutation[i] - 1
        previous_path = permutation[i - 1] - 1

        # Get the nodes connected by the current path
        current_nodes = graph[current_path]

        # Get the nodes connected by the previous path
        previous_nodes = graph[previous_path]

        # Iterate through the nodes connected by the current path
        for node in current_nodes:
            # If the node is not connected to the previous path, it is a boring pair
            if node not in previous_nodes:
                boring_pairs.append(boring_pairs[-1] + 1)
            else:
                boring_pairs.append(boring_pairs[-1])

    return boring_pairs

