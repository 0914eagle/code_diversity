
def count_optimal_paths(n, roads):
    # Initialize a graph with n nodes and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for u, v in roads:
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)

    # Count the number of optimal paths of length 2
    count = 0
    for u in range(n):
        for v in graph[u]:
            if v not in graph[u]:
                continue
            count += 1

    return count

