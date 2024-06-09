
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
        return [diameter]

    # Otherwise, find the minimum spanning tree and return the added edges
    mst = kruskal(graph)
    added_edges = []
    for edge in mst:
        if edge not in edges:
            added_edges.append(edge)
    return [diameter] + added_edges

def find_diameter(graph):
    diameter = 0
    for vertex in graph:
        for neighbor in graph[vertex]:
            if neighbor not in graph[vertex]:
                continue
            diameter = max(diameter, len(find_path(graph, vertex, neighbor)))
    return diameter

def find_path(graph, start, end):
    path = []
    visited = set()
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        if vertex == end:
            path.append(vertex)
            break
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                path.append(neighbor)
    return path[::-1]

def kruskal(graph):
    mst = []
    edges = [(weight, vertex1, vertex2) for vertex1 in graph for vertex2 in graph[vertex1] if vertex1 < vertex2]
    edges.sort(key=lambda x: x[0])
    for edge in edges:
        if find_set(graph, edge[1]) != find_set(graph, edge[2]):
            mst.append(edge[1:])
            union_sets(graph, edge[1], edge[2])
    return mst

def find_set(graph, vertex):
    if vertex not in graph:
        return vertex
    return find_set(graph, graph[vertex])

def union_sets(graph, vertex1, vertex2):
    root1 = find_set(graph, vertex1)
    root2 = find_set(graph, vertex2)
    if root1 < root2:
        graph[vertex2] = root1
    else:
        graph[vertex1] = root2

