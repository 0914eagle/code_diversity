
def solve(n, m, edges):
    # Create a graph with the given edges
    graph = {i: set() for i in range(1, n + 1)}
    for v, u in edges:
        graph[v].add(u)
        graph[u].add(v)

    # Find the connected components of the graph
    components = []
    visited = set()
    for i in range(1, n + 1):
        if i not in visited:
            component = []
            dfs(graph, i, visited, component)
            components.append(component)

    # Find the minimum spanning tree of the graph
    mst = []
    for component in components:
        mst.extend(prim(graph, component[0]))

    # Add the edges that are not in the MST to the graph
    added_edges = []
    for v, u in edges:
        if (v, u) not in mst:
            added_edges.append((v, u))
            graph[v].add(u)
            graph[u].add(v)

    # Return the diameter of the resulting tree and the added edges
    return len(mst) + len(added_edges), added_edges

def dfs(graph, start, visited, component):
    visited.add(start)
    component.append(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, component)

def prim(graph, start):
    mst = []
    visited = set()
    pq = [(0, start)]
    while pq:
        weight, node = heapq.heappop(pq)
        if node not in visited:
            visited.add(node)
            mst.append((node, weight))
            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(pq, (weight, neighbor))
    return mst

def main():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        v, u = map(int, input().split())
        edges.append((v, u))
    print(solve(n, m, edges))

if __name__ == '__main__':
    main()

