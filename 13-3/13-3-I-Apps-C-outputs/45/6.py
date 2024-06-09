
def solve(n, m, s, edges):
    # Initialize the graph as an adjacency list
    graph = [[] for _ in range(n + 1)]
    for edge in edges:
        u, v = edge[1], edge[2]
        graph[u].append(v)
        graph[v].append(u)

    # Find all reachable vertices from vertex s
    reachable = set([s])
    queue = [s]
    while queue:
        vertex = queue.pop(0)
        for neighbor in graph[vertex]:
            if neighbor not in reachable:
                reachable.add(neighbor)
                queue.append(neighbor)

    # Find the maximum number of reachable vertices by orienting all undirected edges in one direction
    max_reachable = len(reachable)
    max_edges = []
    for edge in edges:
        if edge[0] == 2 and edge[1] != edge[2]:
            max_edges.append(edge)

    # Find the minimum number of reachable vertices by orienting all undirected edges in the opposite direction
    min_reachable = 0
    min_edges = []
    for edge in edges:
        if edge[0] == 2 and edge[1] != edge[2]:
            min_edges.append(edge)

    return max_reachable, max_edges, min_reachable, min_edges

