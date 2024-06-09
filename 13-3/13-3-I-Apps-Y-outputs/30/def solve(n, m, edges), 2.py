
def solve(n, m, edges):
    # Initialize the graph as a dictionary with each vertex as a key and its neighbors as values
    graph = {i: set() for i in range(1, n + 1)}
    for edge in edges:
        graph[edge[0]].add(edge[1])
        graph[edge[1]].add(edge[0])

    # Find the diameter of the given graph
    diameter = find_diameter(graph)

    # If the graph is already a tree, return the diameter
    if m == n - 1:
        return diameter

    # Otherwise, find the minimum spanning tree and add the missing edges
    mst = kruskal(graph)
    added_edges = []
    for edge in mst:
        if edge not in edges:
            added_edges.append(edge)

    return diameter, added_edges

def find_diameter(graph):
    diameter = 0
    for vertex in graph:
        for neighbor in graph[vertex]:
            if neighbor not in graph[vertex]:
                continue
            diameter = max(diameter, len(graph[vertex]) + len(graph[neighbor]) - 1)
    return diameter

def kruskal(graph):
    mst = []
    edges = [(len(graph[u]) + len(graph[v]), (u, v)) for u in graph for v in graph[u] if v > u]
    edges.sort()
    for _, (u, v) in edges:
        if find_set(u, graph) != find_set(v, graph):
            mst.append((u, v))
            union_sets(u, v, graph)
    return mst

def find_set(vertex, graph):
    if vertex != graph[vertex]:
        graph[vertex] = find_set(graph[vertex], graph)
    return graph[vertex]

def union_sets(vertex1, vertex2, graph):
    root1 = find_set(vertex1, graph)
    root2 = find_set(vertex2, graph)
    if root1 < root2:
        graph[root2] = root1
    else:
        graph[root1] = root2

