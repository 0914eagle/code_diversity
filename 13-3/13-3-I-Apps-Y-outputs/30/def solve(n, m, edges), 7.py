
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

    # Otherwise, find the minimum spanning tree and return the edges that connect the components
    mst = kruskal(graph)
    components = find_components(mst)
    edges_to_add = []
    for i in range(len(components) - 1):
        for j in range(i + 1, len(components)):
            edges_to_add.append((components[i], components[j]))

    return [diameter] + edges_to_add

def find_diameter(graph):
    diameter = 0
    for vertex in graph:
        for neighbor in graph[vertex]:
            if graph[neighbor]:
                diameter = max(diameter, len(graph[neighbor]) + 1)
    return diameter

def kruskal(graph):
    mst = {}
    for vertex in graph:
        mst[vertex] = set()
    edges = [(weight, edge[0], edge[1]) for edge in graph.items() for weight in graph[edge[0]]]
    edges.sort()
    for edge in edges:
        if find_set(mst, edge[1]) != find_set(mst, edge[2]):
            union_sets(mst, edge[1], edge[2])
            mst[edge[1]].add(edge[2])
            mst[edge[2]].add(edge[1])
    return mst

def find_components(graph):
    components = []
    for vertex in graph:
        if vertex not in components:
            dfs(graph, vertex, components)
    return components

def dfs(graph, vertex, components):
    if vertex in components:
        return
    components.append(vertex)
    for neighbor in graph[vertex]:
        dfs(graph, neighbor, components)

def find_set(mst, vertex):
    if vertex not in mst:
        return vertex
    return find_set(mst, mst[vertex].pop())

def union_sets(mst, vertex1, vertex2):
    mst[vertex1].update(mst[vertex2])
    mst[vertex2] = mst[vertex1]

