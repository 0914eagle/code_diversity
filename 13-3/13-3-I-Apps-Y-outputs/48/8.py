
def get_spanning_tree(n, m, edges):
    # Initialize a graph with n vertices and m edges
    graph = [[] for _ in range(n)]
    for edge in edges:
        graph[edge[0] - 1].append(edge[1] - 1)
        graph[edge[1] - 1].append(edge[0] - 1)

    # Find a vertex with the maximum degree
    max_degree = 0
    max_vertex = 0
    for i in range(n):
        degree = len(graph[i])
        if degree > max_degree:
            max_degree = degree
            max_vertex = i

    # Create a spanning tree with the maximum degree vertex as the root
    tree = []
    visited = [False] * n
    queue = [max_vertex]
    visited[max_vertex] = True
    while queue:
        vertex = queue.pop(0)
        tree.append([vertex + 1, graph[vertex].pop(0) + 1])
        visited[graph[vertex][0]] = True
        queue.append(graph[vertex][0])

    # Add the remaining edges to the spanning tree
    for i in range(n):
        for j in graph[i]:
            if not visited[j]:
                tree.append([i + 1, j + 1])
                visited[j] = True

    return tree

