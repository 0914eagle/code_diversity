
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
        nodes = set()
        queue = [prev_path]
        while queue:
            node = queue.pop(0)
            if node not in nodes:
                nodes.add(node)
                queue.extend(graph[node])

        # Update the number of boring pairs after the destruction
        boring_pairs.append(boring_pairs[-1] - len(nodes))

    return boring_pairs

