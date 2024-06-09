
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

    # Add the edges to form a tree
    tree = set(mst)
    for edge in edges:
        if edge not in tree:
            tree.add(edge)

    # Find the diameter of the tree
    diameter = 0
    for edge in tree:
        diameter = max(diameter, graph[edge[0]][edge[1]])

    return diameter, list(tree - set(edges))

def dfs(graph, vertex, visited, component):
    if vertex in visited:
        return
    visited.add(vertex)
    component.append(vertex)
    for neighbor in graph[vertex]:
        dfs(graph, neighbor, visited, component)

def prim(graph, start):
    visited = set()
    priority_queue = [(0, start)]
    while priority_queue:
        distance, vertex = heapq.heappop(priority_queue)
        if vertex in visited:
            continue
        visited.add(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (graph[vertex][neighbor], neighbor))
        yield (vertex, neighbor)

