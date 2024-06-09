
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
    mst = find_mst(graph)
    added_edges = []
    for i in range(n):
        for j in range(i + 1, n):
            if i not in mst[j] and j not in mst[i]:
                added_edges.append([i, j])

    return diameter, added_edges

def find_diameter(graph):
    diameter = 0
    for i in graph:
        for j in graph[i]:
            if j not in graph[i]:
                diameter = max(diameter, 1)
            else:
                diameter = max(diameter, len(graph[i]) + len(graph[j]) - 1)
    return diameter

def find_mst(graph):
    mst = {i: set() for i in graph}
    visited = set()
    queue = [(0, 0)]
    while queue:
        dist, node = heapq.heappop(queue)
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    mst[node].add(neighbor)
                    heapq.heappush(queue, (dist + 1, neighbor))
    return mst


