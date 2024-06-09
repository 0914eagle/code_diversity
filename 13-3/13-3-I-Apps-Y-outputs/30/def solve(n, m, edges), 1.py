
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

    # Add the edges that are not in the minimum spanning tree to the graph
    added_edges = []
    for edge in edges:
        if edge not in mst:
            added_edges.append(edge)
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])

    # Find the diameter of the resulting tree
    diameter = 0
    for edge in mst:
        diameter = max(diameter, graph[edge[0]].intersection(graph[edge[1]]).__len__())

    return diameter, added_edges


def dfs(graph, vertex, visited, component):
    if vertex in visited:
        return
    visited.add(vertex)
    component.append(vertex)
    for neighbor in graph[vertex]:
        dfs(graph, neighbor, visited, component)


def prim(graph, start):
    visited = set()
    mst = []
    pq = [(0, start)]
    while pq:
        weight, vertex = heapq.heappop(pq)
        if vertex in visited:
            continue
        visited.add(vertex)
        mst.append((vertex, vertex))
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                heapq.heappush(pq, (weight + 1, neighbor))
    return mst


def main():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        edges.append(list(map(int, input().split())))
    diameter, added_edges = solve(n, m, edges)
    print(diameter)
    for edge in added_edges:
        print(*edge)


if __name__ == '__main__':
    main()

