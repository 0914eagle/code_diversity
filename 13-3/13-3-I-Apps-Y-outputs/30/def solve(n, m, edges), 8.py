
def solve(n, m, edges):
    # Initialize the graph as a dictionary with each vertex as a key and its neighbors as values
    graph = {i: set() for i in range(1, n + 1)}
    for edge in edges:
        graph[edge[0]].add(edge[1])
        graph[edge[1]].add(edge[0])

    # Find the connected components in the graph
    components = []
    visited = set()
    for vertex in graph:
        if vertex not in visited:
            component = []
            dfs(graph, vertex, visited, component)
            components.append(component)

    # Find the minimum spanning tree for each connected component
    mst = []
    for component in components:
        mst.extend(prim(graph, component[0]))

    # Add the edges from the minimum spanning tree to the graph
    for edge in mst:
        graph[edge[0]].add(edge[1])
        graph[edge[1]].add(edge[0])

    # Find the diameter of the resulting tree
    diameter = 0
    for edge in mst:
        diameter = max(diameter, graph[edge[0]].intersection(graph[edge[1]]).__len__())

    # Return the diameter and the added edges
    return diameter, mst


def dfs(graph, vertex, visited, component):
    if vertex in visited:
        return
    visited.add(vertex)
    component.append(vertex)
    for neighbor in graph[vertex]:
        dfs(graph, neighbor, visited, component)


def prim(graph, start):
    visited = set()
    queue = [(0, start)]
    mst = []
    while queue:
        distance, vertex = heapq.heappop(queue)
        if vertex in visited:
            continue
        visited.add(vertex)
        mst.append((start, vertex))
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                heapq.heappush(queue, (distance + 1, neighbor))
    return mst


# Test the function with a sample input
n = 4
m = 2
edges = [(1, 2), (2, 3)]
print(solve(n, m, edges))

