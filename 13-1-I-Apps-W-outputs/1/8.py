
def solve(N, paths, order):
    # Initialize a graph with N nodes and 0 edges
    graph = [[] for _ in range(N)]

    # Add edges to the graph based on the input paths
    for path in paths:
        graph[path[0] - 1].append(path[1] - 1)
        graph[path[1] - 1].append(path[0] - 1)

    # Initialize a list to store the number of boring pairs before each destruction
    boring_pairs = [0]

    # Iterate through the order of destruction
    for i in range(1, len(order)):
        # Find the path that was destroyed in the previous step
        prev_path = order[i - 1]

        # Find the nodes that are connected to the destroyed path
        nodes = [prev_path[0] - 1, prev_path[1] - 1]

        # Iterate through the remaining paths
        for j in range(i, len(order)):
            # Find the path that is being destroyed in this step
            curr_path = order[j]

            # Check if the current path is connected to any of the nodes from the previous step
            if curr_path[0] - 1 in nodes or curr_path[1] - 1 in nodes:
                # If the current path is connected to any of the nodes, it is also boring
                boring_pairs.append(boring_pairs[-1] + 1)
            else:
                # If the current path is not connected to any of the nodes, it is not boring
                boring_pairs.append(boring_pairs[-1])

    return boring_pairs

