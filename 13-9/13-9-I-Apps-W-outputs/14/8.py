
def get_shortest_path(graph, start, end):
    visited = set()
    queue = [(start, 0)]
    while queue:
        (node, distance) = queue.pop(0)
        if node not in visited:
            visited.add(node)
            if node == end:
                return distance
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, distance + 1))
    return -1

def build_graph(edges):
    graph = {}
    for (a, b, _) in edges:
        if a not in graph:
            graph[a] = set()
        if b not in graph:
            graph[b] = set()
        graph[a].add(b)
        graph[b].add(a)
    return graph

def solve(n, m, edges):
    graph = build_graph(edges)
    for i in range(n):
        if get_shortest_path(graph, i, 1) == -1:
            return "impossible"
    return "possible"

if __name__ == '__main__':
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        a, b, d = map(int, input().split())
        edges.append((a, b, d))
    print(solve(n, m, edges))

