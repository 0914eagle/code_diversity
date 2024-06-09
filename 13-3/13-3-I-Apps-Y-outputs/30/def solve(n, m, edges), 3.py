
def solve(n, m, edges):
    # Create a graph with the given edges
    graph = {i: set() for i in range(1, n + 1)}
    for v, u in edges:
        graph[v].add(u)
        graph[u].add(v)

    # Find the connected components of the graph
    components = []
    visited = set()
    for node in graph:
        if node not in visited:
            component = []
            dfs(graph, node, visited, component)
            components.append(component)

    # Find the minimum spanning tree of the graph
    mst = []
    for component in components:
        mst.extend(prim(graph, component[0]))

    # Add the missing edges to the MST to form a tree
    tree = []
    for node in graph:
        for neighbor in graph[node]:
            if (node, neighbor) not in mst and (neighbor, node) not in mst:
                tree.append((node, neighbor))

    # Return the diameter of the tree and the added edges
    return len(mst) + len(tree), tree

def dfs(graph, node, visited, component):
    if node in visited:
        return
    visited.add(node)
    component.append(node)
    for neighbor in graph[node]:
        dfs(graph, neighbor, visited, component)

def prim(graph, start):
    visited = set()
    queue = [(0, start)]
    mst = []
    while queue:
        dist, node = heapq.heappop(queue)
        if node in visited:
            continue
        visited.add(node)
        mst.append((node, dist))
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(queue, (weight, neighbor))
    return mst

def add_edges(n, m, edges):
    graph = {i: set() for i in range(1, n + 1)}
    for v, u in edges:
        graph[v].add(u)
        graph[u].add(v)
    return graph

def get_diameter(graph):
    diameter = 0
    for node in graph:
        for neighbor in graph[node]:
            diameter = max(diameter, len(graph[node]) + len(graph[neighbor]))
    return diameter

def get_connected_components(graph):
    visited = set()
    components = []
    for node in graph:
        if node not in visited:
            component = []
            dfs(graph, node, visited, component)
            components.append(component)
    return components

def get_minimum_spanning_tree(graph):
    visited = set()
    queue = [(0, graph[0])]
    mst = []
    while queue:
        dist, node = heapq.heappop(queue)
        if node in visited:
            continue
        visited.add(node)
        mst.append((node, dist))
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(queue, (weight, neighbor))
    return mst

def get_tree_edges(graph):
    tree_edges = []
    for node in graph:
        for neighbor in graph[node]:
            if (node, neighbor) not in tree_edges and (neighbor, node) not in tree_edges:
                tree_edges.append((node, neighbor))
    return tree_edges

